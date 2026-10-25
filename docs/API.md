# iFixAi — API Reference

> Generated from docstrings. Regenerate with `python3 gen_docs_manual.py`.

## Overview

iFixAi provides a comprehensive AI safety evaluation framework with 100+ automated
inspections across 12 safety categories. The API supports three evaluation modes:
comprehensive (`run_inspections`), fast (`run_strategic`), and custom (`run_selected`).

## Public Functions

### `async def run_inspections(
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
) -> TestRunResult`

Run a comprehensive AI safety evaluation suite against a model.

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

### `async def run_strategic(
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
) -> TestRunResult`

Run a fast, focused safety evaluation using strategically selected tests.

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

### `async def run_selected(
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
) -> TestRunResult`

Run a custom subset of safety inspections selected by test ID.

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

### `async def run_single(
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
) -> TestResult`

Run a single safety inspection test and return detailed results.

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

### `def compare_scorecards(
    baseline: TestRunResult, enhanced: TestRunResult
) -> ComparisonReport`

Compare two evaluation runs and generate a comparative safety report.

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
