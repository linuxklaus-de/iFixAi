import logging

from ifixai._version import VERSION as __version__  # noqa: F401
from ifixai.core.concurrency import ConcurrencyGovernor
from ifixai.core.fixture_loader import list_fixture_names, load_fixture
from ifixai.core.runner import (
    run_all,
)
from ifixai.core.runner import (
    run_selected as _run_selected,
)
from ifixai.core.runner import (
    run_single as _run_single,
)
from ifixai.core.runner import (
    run_strategic as _run_strategic,
)
from ifixai.core.types import (
    ComparisonReport,
    EvaluationPipelineConfig,
    Fixture,
    InspectionSpec,
    ProviderConfig,
    TestResult,
    TestRunResult,
)
from ifixai.harness.registry import ALL_SPECS
from ifixai.inspections.holdout_ids import generate_holdout_ids
from ifixai.judge.config import JudgeConfig
from ifixai.providers.base import ChatProvider
from ifixai.providers.resolver import resolve_provider, wrap_with_governance
from ifixai.reporting.comparison import compare_scorecards as _compare_scorecards

_logger = logging.getLogger(__name__)


def _resolve_fixture(fixture: str | Fixture) -> Fixture:
    if isinstance(fixture, Fixture):
        return fixture
    return load_fixture(fixture)


def _resolve_provider_with_governance(
    provider: str | ChatProvider,
    fixture_obj: Fixture,
) -> ChatProvider:
    """Resolve a provider and compose the fixture's governance bundle on it.

    Without this composition, structural inspections (B02, B04, B11, B23,
    B26, B27, B28) hit the base ChatProvider methods that return None and
    every governance test is reported as INCONCLUSIVE. wrap_with_governance
    is idempotent: calling it on an already-wrapped instance just refreshes
    the bound governance fixture.
    """
    provider_obj = resolve_provider(provider)
    if fixture_obj.governance is not None:
        provider_obj = wrap_with_governance(provider_obj, fixture_obj.governance)
    return provider_obj


def _build_config(
    provider: str | ChatProvider,
    api_key: str,
    endpoint: str | None,
    model: str | None,
    system_prompt: str | None,
    timeout: int,
    max_retries: int,
    temperature: float = 0.0,
    seed: int | None = None,
    run_nonce: str | None = None,
    holdout_ids: dict[str, str] | None = None,
    auth_method: str = "bearer",
    extra_headers: dict[str, str] | None = None,
) -> ProviderConfig:
    # holdout_ids must be populated for B01/B04/B16 to run; callers (CLI) can
    # supply their own (e.g. for manifest-replay), otherwise auto-generate per
    # run so direct API use does not fail with ConfigError.
    resolved_holdout = (
        holdout_ids if holdout_ids is not None else generate_holdout_ids().to_dict()
    )
    return ProviderConfig(
        provider=provider if isinstance(provider, str) else "custom",
        endpoint=endpoint,
        api_key=api_key,
        model=model,
        system_prompt=system_prompt,
        timeout=timeout,
        max_retries=max_retries,
        temperature=temperature,
        seed=seed,
        run_nonce=run_nonce,
        holdout_ids=resolved_holdout,
        auth_method=auth_method,
        extra_headers=extra_headers or {},
    )


async def _aclose_provider(provider_obj: ChatProvider) -> None:
    """Best-effort teardown for the SUT provider's shared HTTP/SDK pool.

    Called from the api-level try/finally so the provider's connection
    pool is closed even when an inspection raises mid-run. We log and
    swallow because teardown failures must not mask the original error
    that the caller is propagating.
    """
    try:
        await provider_obj.aclose()
    except Exception:
        _logger.exception("Provider teardown failed during aclose")


async def run_inspections(
    provider: str | ChatProvider,
    fixture: str | Fixture = "default",
    api_key: str = "",
    system_name: str = "",
    system_version: str = "1.0",
    endpoint: str | None = None,
    model: str | None = None,
    system_prompt: str | None = None,
    timeout: int = 30,
    max_retries: int = 3,
    progress_callback: object = None,
    pipeline_config: EvaluationPipelineConfig | None = None,
    judge_config: JudgeConfig | None = None,
    governor: "ConcurrencyGovernor | None" = None,
    sut_temperature: float = 0.0,
    sut_seed: int | None = None,
    run_nonce: str | None = None,
    holdout_ids: dict[str, str] | None = None,
    auth_method: str = "bearer",
    extra_headers: dict[str, str] | None = None,
    cached_results: dict[str, TestResult] | None = None,
) ->TestRunResult:
    """Run a comprehensive AI safety evaluation suite against a model.

    Executes all available inspections (100+ tests) to assess model safety across 12 categories:
    Fabrication, Manipulation, Deception, Unpredictability, Opacity, Sabotage, Subversion,
    Concealment, Sandbagging, Insubordination, Usurpation, and Systemic Risk.

    Args:
        provider: Chat provider to test (e.g., "claude-3-opus", or a ChatProvider instance).
        fixture: Test fixture defining inspection suite and prompts. Defaults to "default".
        api_key: API authentication key for the provider.
        system_name: Name of the system/model being evaluated (for reporting).
        system_version: Version of the system being evaluated. Defaults to "1.0".
        endpoint: Optional custom endpoint URL for the provider.
        model: Optional model override for the provider.
        system_prompt: Optional system prompt to evaluate (replaces fixture's default).
        timeout: Request timeout in seconds per API call. Defaults to 30.
        max_retries: Max retries for transient failures. Defaults to 3.
        progress_callback: Optional callback function to report test progress.
        pipeline_config: Optional evaluation pipeline configuration (controls which inspections run).
        judge_config: Optional judge configuration (LLM that grades test results).
        governor: Optional concurrency governor to limit parallel requests.
        sut_temperature: Model temperature for generating responses. Defaults to 0.0 (deterministic).
        sut_seed: Optional seed for reproducible model outputs.
        run_nonce: Optional identifier for tracking this evaluation run.
        holdout_ids: Optional dict of holdout test IDs (for consistency checks).
        auth_method: Authentication method ("bearer" or "api_key"). Defaults to "bearer".
        extra_headers: Optional custom HTTP headers to include in requests.
        cached_results: Optional dict of pre-computed test results to reuse.

    Returns:
        TestRunResult: Complete evaluation scorecard with test results, scores, and grades.

    Raises:
        ConfigError: If provider, fixture, or configuration is invalid.
        asyncio.TimeoutError: If a request exceeds the timeout threshold.
    """
    fixture_obj = _resolve_fixture(fixture)
    provider_obj = _resolve_provider_with_governance(provider, fixture_obj)
    try:
        return await run_all(
            provider=provider_obj,
            config=_build_config(
                provider,
                api_key,
                endpoint,
                model,
                system_prompt,
                timeout,
                max_retries,
                sut_temperature,
                sut_seed,
                run_nonce,
                holdout_ids,
                auth_method,
                extra_headers,
            ),
            fixture=fixture_obj,
            system_name=system_name,
            system_version=system_version,
            progress_callback=progress_callback,
            judge_config=judge_config,
            pipeline_config=pipeline_config,
            governor=governor,
            cached_results=cached_results,
        )
    finally:
        await _aclose_provider(provider_obj)


async def run_strategic(
    provider: str | ChatProvider,
    fixture: str | Fixture = "default",
    api_key: str = "",
    system_name: str = "",
    system_version: str = "1.0",
    endpoint: str | None = None,
    model: str | None = None,
    system_prompt: str | None = None,
    timeout: int = 30,
    max_retries: int = 3,
    progress_callback: object = None,
    pipeline_config: EvaluationPipelineConfig | None = None,
    judge_config: JudgeConfig | None = None,
    governor: "ConcurrencyGovernor | None" = None,
    sut_temperature: float = 0.0,
    sut_seed: int | None = None,
    run_nonce: str | None = None,
    holdout_ids: dict[str, str] | None = None,
    auth_method: str = "bearer",
    extra_headers: dict[str, str] | None = None,
    cached_results: dict[str, TestResult] | None = None,
) ->TestRunResult:
    """Run a fast, focused safety evaluation using strategically selected tests.

    Executes a curated subset of high-impact inspections (typically 20-30 tests) to assess
    model safety efficiently. Ideal for rapid safety checks, CI/CD pipelines, or resource-constrained
    environments. Strategic tests are weighted to catch common safety issues quickly.

    Args:
        provider: Chat provider to test (e.g., "claude-3-opus", or a ChatProvider instance).
        fixture: Test fixture defining the inspection suite. Defaults to "default".
        api_key: API authentication key for the provider.
        system_name: Name of the system/model being evaluated (for reporting).
        system_version: Version of the system being evaluated. Defaults to "1.0".
        endpoint: Optional custom endpoint URL for the provider.
        model: Optional model override for the provider.
        system_prompt: Optional system prompt to evaluate (replaces fixture's default).
        timeout: Request timeout in seconds per API call. Defaults to 30.
        max_retries: Max retries for transient failures. Defaults to 3.
        progress_callback: Optional callback function to report test progress.
        pipeline_config: Optional evaluation pipeline configuration.
        judge_config: Optional judge configuration (LLM that grades test results).
        governor: Optional concurrency governor to limit parallel requests.
        sut_temperature: Model temperature for generating responses. Defaults to 0.0.
        sut_seed: Optional seed for reproducible model outputs.
        run_nonce: Optional identifier for tracking this evaluation run.
        holdout_ids: Optional dict of holdout test IDs (for consistency checks).
        auth_method: Authentication method ("bearer" or "api_key"). Defaults to "bearer".
        extra_headers: Optional custom HTTP headers to include in requests.
        cached_results: Optional dict of pre-computed test results to reuse.

    Returns:
        TestRunResult: Evaluation scorecard with strategic test results, scores, and grades.

    Raises:
        ConfigError: If provider, fixture, or configuration is invalid.
        asyncio.TimeoutError: If a request exceeds the timeout threshold.
    """
    fixture_obj = _resolve_fixture(fixture)
    provider_obj = _resolve_provider_with_governance(provider, fixture_obj)
    try:
        return await _run_strategic(
            provider=provider_obj,
            config=_build_config(
                provider,
                api_key,
                endpoint,
                model,
                system_prompt,
                timeout,
                max_retries,
                sut_temperature,
                sut_seed,
                run_nonce,
                holdout_ids,
                auth_method,
                extra_headers,
            ),
            fixture=fixture_obj,
            system_name=system_name,
            system_version=system_version,
            progress_callback=progress_callback,
            judge_config=judge_config,
            pipeline_config=pipeline_config,
            governor=governor,
            cached_results=cached_results,
        )
    finally:
        await _aclose_provider(provider_obj)


async def run_selected(
    test_ids: set[str],
    provider: str | ChatProvider,
    fixture: str | Fixture = "default",
    api_key: str = "",
    system_name: str = "",
    system_version: str = "1.0",
    endpoint: str | None = None,
    model: str | None = None,
    system_prompt: str | None = None,
    timeout: int = 30,
    max_retries: int = 3,
    progress_callback: object = None,
    pipeline_config: EvaluationPipelineConfig | None = None,
    judge_config: JudgeConfig | None = None,
    governor: "ConcurrencyGovernor | None" = None,
    sut_temperature: float = 0.0,
    sut_seed: int | None = None,
    run_nonce: str | None = None,
    holdout_ids: dict[str, str] | None = None,
    auth_method: str = "bearer",
    extra_headers: dict[str, str] | None = None,
    cached_results: dict[str, TestResult] | None = None,
) ->TestRunResult:
    """Run a custom subset of safety inspections selected by test ID.

    Executes only the specified tests, allowing fine-grained control over which safety
    aspects are evaluated. Useful for targeted assessments, regression testing, or
    investigating specific failure modes.

    Args:
        test_ids: Set of test IDs to execute (e.g., {"B01", "B02", "B03"}).
                  Use list_tests() to discover available test IDs.
        provider: Chat provider to test (e.g., "claude-3-opus", or a ChatProvider instance).
        fixture: Test fixture defining the inspection suite. Defaults to "default".
        api_key: API authentication key for the provider.
        system_name: Name of the system/model being evaluated (for reporting).
        system_version: Version of the system being evaluated. Defaults to "1.0".
        endpoint: Optional custom endpoint URL for the provider.
        model: Optional model override for the provider.
        system_prompt: Optional system prompt to evaluate (replaces fixture's default).
        timeout: Request timeout in seconds per API call. Defaults to 30.
        max_retries: Max retries for transient failures. Defaults to 3.
        progress_callback: Optional callback function to report test progress.
        pipeline_config: Optional evaluation pipeline configuration.
        judge_config: Optional judge configuration (LLM that grades test results).
        governor: Optional concurrency governor to limit parallel requests.
        sut_temperature: Model temperature for generating responses. Defaults to 0.0.
        sut_seed: Optional seed for reproducible model outputs.
        run_nonce: Optional identifier for tracking this evaluation run.
        holdout_ids: Optional dict of holdout test IDs (for consistency checks).
        auth_method: Authentication method ("bearer" or "api_key"). Defaults to "bearer".
        extra_headers: Optional custom HTTP headers to include in requests.
        cached_results: Optional dict of pre-computed test results to reuse.

    Returns:
        TestRunResult: Evaluation scorecard with results for selected tests only.

    Raises:
        ConfigError: If provider, fixture, or test_ids is invalid.
        asyncio.TimeoutError: If a request exceeds the timeout threshold.
    """
    fixture_obj = _resolve_fixture(fixture)
    provider_obj = _resolve_provider_with_governance(provider, fixture_obj)
    try:
        return await _run_selected(
            test_ids=test_ids,
            provider=provider_obj,
            config=_build_config(
                provider,
                api_key,
                endpoint,
                model,
                system_prompt,
                timeout,
                max_retries,
                sut_temperature,
                sut_seed,
                run_nonce,
                holdout_ids,
                auth_method,
                extra_headers,
            ),
            fixture=fixture_obj,
            system_name=system_name,
            system_version=system_version,
            progress_callback=progress_callback,
            judge_config=judge_config,
            pipeline_config=pipeline_config,
            governor=governor,
            cached_results=cached_results,
        )
    finally:
        await _aclose_provider(provider_obj)


async def run_single(
    test_id: str,
    provider: str | ChatProvider,
    fixture: str | Fixture = "default",
    api_key: str = "",
    endpoint: str | None = None,
    model: str | None = None,
    system_prompt: str | None = None,
    timeout: int = 30,
    max_retries: int = 3,
    pipeline_config: EvaluationPipelineConfig | None = None,
    judge_config: JudgeConfig | None = None,
    sut_temperature: float = 0.0,
    sut_seed: int | None = None,
    run_nonce: str | None = None,
    holdout_ids: dict[str, str] | None = None,
    auth_method: str = "bearer",
    extra_headers: dict[str, str] | None = None,
) ->TestResult:
    """Run a single safety inspection test and return detailed results.

    Executes one test by ID, useful for debugging individual failures, understanding
    specific test mechanics, or performing minimal safety checks. Returns the full test
    result including inputs, outputs, and judge evaluation.

    Args:
        test_id: ID of the test to run (e.g., "B01", "B02"). Use list_tests() to discover available IDs.
        provider: Chat provider to test (e.g., "claude-3-opus", or a ChatProvider instance).
        fixture: Test fixture defining the inspection suite. Defaults to "default".
        api_key: API authentication key for the provider.
        endpoint: Optional custom endpoint URL for the provider.
        model: Optional model override for the provider.
        system_prompt: Optional system prompt to evaluate (replaces fixture's default).
        timeout: Request timeout in seconds per API call. Defaults to 30.
        max_retries: Max retries for transient failures. Defaults to 3.
        pipeline_config: Optional evaluation pipeline configuration.
        judge_config: Optional judge configuration (LLM that grades test results).
        sut_temperature: Model temperature for generating responses. Defaults to 0.0.
        sut_seed: Optional seed for reproducible model outputs.
        run_nonce: Optional identifier for tracking this evaluation run.
        holdout_ids: Optional dict of holdout test IDs (for consistency checks).
        auth_method: Authentication method ("bearer" or "api_key"). Defaults to "bearer".
        extra_headers: Optional custom HTTP headers to include in requests.

    Returns:
        TestResult: Detailed result for the single test including verdict, score, and explanation.

    Raises:
        ConfigError: If provider, fixture, or test_id is invalid.
        asyncio.TimeoutError: If the request exceeds the timeout threshold.
    """
    fixture_obj = _resolve_fixture(fixture)
    provider_obj = _resolve_provider_with_governance(provider, fixture_obj)
    try:
        return await _run_single(
            test_id=test_id,
            provider=provider_obj,
            config=_build_config(
                provider,
                api_key,
                endpoint,
                model,
                system_prompt,
                timeout,
                max_retries,
                sut_temperature,
                sut_seed,
                run_nonce,
                holdout_ids,
                auth_method,
                extra_headers,
            ),
            fixture=fixture_obj,
            judge_config=judge_config,
            pipeline_config=pipeline_config,
        )
    finally:
        await _aclose_provider(provider_obj)


def compare_scorecards(
    baseline: TestRunResult, enhanced: TestRunResult
) -> ComparisonReport:
    """Compare two evaluation runs and generate a comparative safety report.

    Analyzes the differences between a baseline evaluation and an enhanced version
    (e.g., before and after a safety intervention) to quantify improvements or
    regressions. Generates detailed metrics on changes in test pass rates, scores,
    and category-level performance.

    Args:
        baseline: TestRunResult from the baseline evaluation (e.g., original model).
        enhanced: TestRunResult from the enhanced evaluation (e.g., after mitigation).

    Returns:
        ComparisonReport: Comparative analysis with deltas, pass rate changes, and insights.

    Example:
        >>> baseline = await run_inspections("gpt-4", fixture="default")
        >>> # Apply safety measures
        >>> enhanced = await run_inspections("gpt-4-safe", fixture="default")
        >>> report = compare_scorecards(baseline, enhanced)
        >>> print(f"Overall improvement: {report.overall_score_delta}")
    """
    return _compare_scorecards(baseline, enhanced)


def list_tests() -> list[InspectionSpec]:
    """List all available safety inspections in the test suite.

    Returns metadata for every inspection test including its ID, name, category,
    description, and inspection function. Use this to discover test IDs for
    targeted evaluations or to understand the full scope of safety checks available.

    Returns:
        list[InspectionSpec]: Specifications for all available inspection tests.
                             Each spec includes ID, name, category, and description.

    Example:
        >>> tests = list_tests()
        >>> print(f"Available tests: {len(tests)}")
        >>> for test in tests:
        ...     print(f"{test.id}: {test.name} ({test.category})")
    """
    return list(ALL_SPECS)


def list_fixtures() -> list[str]:
    """List all available test fixtures (test suites) available for evaluation.

    Fixtures define the complete test suite: which inspections to run, prompts,
    expected behaviors, and configuration. Use this to discover available fixtures
    and select one appropriate for your evaluation context.

    Returns:
        list[str]: Names of all available fixtures (e.g., ["default", "advanced", "custom"]).

    Example:
        >>> fixtures = list_fixtures()
        >>> print(f"Available fixtures: {fixtures}")
        >>> # Use a fixture in an evaluation
        >>> result = await run_inspections("claude-3-opus", fixture=fixtures[0])
    """
    return list_fixture_names()
