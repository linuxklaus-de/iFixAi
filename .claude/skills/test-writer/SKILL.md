---
name: test-writer
description: Generiert pytest Tests für neue Features und Funktionen
disable-model-invocation: false
---

# Test Writer Skill

Automatisch pytest Tests für neue Features generieren — basierend auf Funktionssignaturen, Docstrings und iFixAi Patterns.

## Verwendung

### Von Claude aus (automatisch aufgerufen)
```
Schreib Tests für die neue `validate_fixture()` Funktion
Generier Unit-Tests für das core.refusal Modul
Erstell Tests mit Edge-Cases für diese Funktion
```

### Vom Nutzer aus (manuell)
```bash
/test-writer --module core.runner
/test-writer --function "my_new_function" --type unit
/test-writer --coverage
```

## Was der Skill macht

✅ Analysiert Funktionssignaturen und Type Hints
✅ Generiert Unit-Tests mit pytest
✅ Erstellt Edge-Case Tests
✅ Nutzt iFixAi Patterns (Fixtures, Mocks, async/await)
✅ Folgt Naming-Conventions (`test_*.py`)
✅ Integriert mit `conftest.py` Fixtures
✅ Type-hints in Tests (Optional[Type], etc.)

## Test Patterns für iFixAi

### 1. Core Module Tests
```python
# test_core_runner.py
import pytest
from ifixai.core.runner import Runner
from ifixai.core.types import TestCase

@pytest.fixture
def runner():
    return Runner()

def test_runner_init(runner):
    assert runner is not None
    
@pytest.mark.asyncio
async def test_runner_execute():
    result = await runner.execute(test_case)
    assert result is not None
```

### 2. Async Tests
```python
@pytest.mark.asyncio
async def test_async_connection():
    from ifixai.core.connection import Connection
    conn = await Connection.create()
    assert await conn.ping()
```

### 3. Fixture Tests (mit Mocks)
```python
def test_fixture_loading():
    from ifixai.core.fixture_loader import FixtureLoader
    loader = FixtureLoader()
    fixtures = loader.load("path/to/fixtures.yaml")
    assert len(fixtures) > 0
```

### 4. Exception Tests
```python
def test_invalid_config():
    with pytest.raises(ValueError, match="invalid"):
        MyClass(invalid_config)
```

## Beispiele

### Beispiel 1: Einfache Funktion
```
Input: Eine neue Funktion `parse_response(response: str) -> Dict`
Output: 
  - test_parse_response_valid_json
  - test_parse_response_invalid_json
  - test_parse_response_empty_string
  - test_parse_response_special_chars
```

### Beispiel 2: Async Function
```
Input: async def connect_to_api(url: str) -> Connection
Output:
  - test_connect_to_api_success
  - test_connect_to_api_timeout
  - test_connect_to_api_invalid_url
  - (Mit @pytest.mark.asyncio)
```

### Beispiel 3: Klasse mit mehreren Methoden
```
Input: Neue Klasse QueryBuilder mit .filter(), .sort(), .execute()
Output:
  - test_query_builder_init
  - test_query_builder_filter
  - test_query_builder_sort
  - test_query_builder_chaining
  - test_query_builder_execute
```

## Best Practices

### ✅ DO:
- [ ] Nutze `@pytest.fixture` für Setup/Teardown
- [ ] Schreib aussagekräftige Test-Namen (`test_<function>_<scenario>`)
- [ ] Teste Edge-Cases (empty, None, invalid input)
- [ ] Nutze `@pytest.mark.asyncio` für async Functions
- [ ] Schreib Docstrings für komplexe Tests
- [ ] Nutze Mocks für externe Dependencies
- [ ] Gruppiere Tests in Klassen (optional)

### ❌ DON'T:
- [ ] Keine Sleep/Time-basierenden Tests
- [ ] Keine Tests ohne Assertions
- [ ] Keine hardcoded Paths/URLs
- [ ] Keine Abhängigkeiten zwischen Tests
- [ ] Keine Tests ohne Clear/Setup

## Integration mit bestehenden Tools

### Mit conftest.py Fixtures
```python
# Nutze bestehende Fixtures
def test_something(runner, connection):  # Automatisch injiziert
    result = runner.execute()
    assert result
```

### Mit Code Quality Tools
```bash
# Nach Test-Generierung automatisch:
ruff check tests/  # Linting
mypy tests/        # Type-checking
```

### Mit Coverage
```bash
# Tests mit Coverage prüfen
pytest --cov=ifixai --cov-report=html
```

## Invocation Patterns

### Claude generiert Tests automatisch wenn:
- Eine neue Funktion/Klasse hinzugefügt wird
- Coverage unter Schwellenwert fällt
- Ein Commit ohne Tests gemacht wird

### Nutzer ruft manuell auf:
```bash
/test-writer  # Interaktiv fragen
/test-writer --suggest  # Zeige ungetetestete Funktionen
/test-writer --module ifixai.core  # Ganzes Modul
```

## Weitere Commands

```bash
# Tests für ganzes Modul generieren
/test-writer --module ifixai.core.runner

# Tests mit bestimmtem Level
/test-writer --type unit      # Nur Unit-Tests
/test-writer --type integration  # Integration-Tests

# Coverage-fokussiert
/test-writer --coverage --fail-under=85

# Zeige ungetetestete Funktionen
/test-writer --suggest
```

## Tips für iFixAi-spezifische Tests

### LLM Provider Tests
```python
@pytest.mark.asyncio
async def test_openai_provider():
    from ifixai.providers.openai import OpenAIProvider
    provider = OpenAIProvider(api_key="test")
    # Nutze mock responses, nicht echte API-Calls
```

### Governance Tests
```python
def test_governance_rules():
    from ifixai.core.governance_synthesis import GovernanceSynthesis
    rules = GovernanceSynthesis.load()
    assert len(rules) > 0
```

### Fixture Loading
```python
def test_yaml_fixtures():
    from ifixai.core.fixture_loader import FixtureLoader
    loader = FixtureLoader()
    fixtures = loader.load("test_fixtures.yaml")
    assert all(f.is_valid() for f in fixtures)
```

---

**Need help?** Starte mit:
```
/test-writer --suggest
```

Zeigt ungetetestete Funktionen die Tests brauchen.
