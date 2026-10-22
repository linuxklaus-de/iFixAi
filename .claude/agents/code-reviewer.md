# Code Reviewer Agent

Ein spezialisierter Agent für gründliche Code-Reviews vor Merges und Releases.

## Zweck

Automatische Code-Reviews für:
- Sicherheitsprobleme (Security Issues)
- Performance-Probleme
- Code-Quality (Type-Safety, Best Practices)
- Test-Coverage
- iFixAi-spezifische Patterns

## Invocation

```bash
# Manuell aufrufen
claude -p "Review the changes in this PR for security, performance, and quality"

# Oder in Claude Code
/code-review

# Mit ultra-detail
/code-review ultra
```

## Was dieser Agent prüft

### 🔒 Security
- [ ] Keine hardcoded Secrets/API-Keys
- [ ] Keine SQL/Command Injection Risiken
- [ ] Sichere Authentifizierung
- [ ] Dependency-Vulnerabilities
- [ ] OWASP Top 10 Compliance

### ⚡ Performance
- [ ] Keine N+1 Queries
- [ ] Effiziente Datenstrukturen
- [ ] Async/await Patterns korrekt
- [ ] Memory Leaks vermieden
- [ ] Timeout-Handling vorhanden

### 📊 Code Quality
- [ ] Type Hints vollständig
- [ ] Naming Conventions
- [ ] DRY Principle (Don't Repeat Yourself)
- [ ] SOLID Principles
- [ ] Fehlerbehandlung

### 🧪 Test Coverage
- [ ] Tests für neue Features
- [ ] Edge-Cases getestet
- [ ] Mock/Patch korrekt genutzt
- [ ] Coverage nicht gesunken
- [ ] Integration-Tests vorhanden

### 🎯 iFixAi-spezifisch
- [ ] Fixture-Loading korrekt
- [ ] Governance Rules beachtet
- [ ] LLM-Provider Integration korrekt
- [ ] Telemetry/Logging vorhanden
- [ ] Type-Safe für pydantic Models

## Review Kategorien

Der Agent gibt Feedback in diesen Kategorien:

```
🔴 CRITICAL - Muss vor Merge gefixt werden
🟠 MAJOR - Sollte gefixt werden
🟡 MINOR - Nice-to-have Improvements
🟢 INFO - Informationen/Best-Practices
```

## Beispiel Review Output

```
## Code Review Summary

✅ Security: PASS
✅ Performance: PASS
⚠️  Coverage: 78% (Target: 85%)
🔴 Type Safety: 2 issues found

### Issues

🔴 CRITICAL: Type annotation missing
File: ifixai/core/runner.py:45
Issue: Function returns Any but should return TestResult
Fix: Add type hint `-> TestResult`

🟡 MINOR: Inefficient loop
File: ifixai/core/fixture_loader.py:120
Issue: Loading fixtures one-by-one, could batch
Suggestion: Use batch_load() method
```

## Integration mit Git Workflow

### Pre-Push Hook
```bash
# Automatisch aufrufen vor Push
/code-review --fail-on-critical
```

### Pre-Commit Hook
```bash
# Schneller Review vor Commit
/code-review --quick
```

### Pull Request
```bash
# Detaillierter Review für PR
/code-review --detailed
# Oder
/code-review ultra  # Cloud-basierter Multi-Agent Review
```

## Review Modes

### Quick (2-3 min)
```bash
/code-review
```
- Basic security & performance checks
- Type annotations
- Obvious code smells

### Detailed (5-10 min)
```bash
/code-review --detailed
```
- Alle Quick-Checks
- Test Coverage Analyse
- Performance Profile
- iFixAi Best Practices

### Ultra (10-20 min, Cloud)
```bash
/code-review ultra
```
- Multi-agent parallel review
- Deep security analysis
- Architecture review
- Compliance check
- Database/API impact analysis

## Configuration

```bash
# Nur Security-Issues
/code-review --focus security

# Nur Performance
/code-review --focus performance

# Nur Coverage
/code-review --focus coverage

# Fail bei Critical Issues
/code-review --fail-on-critical

# Mit Suggestions für Fixes
/code-review --suggest-fixes
```

## Best Practices für Reviews

### ✅ DO:
- [ ] Review vor jedem Merge in main
- [ ] Nutze `--suggest-fixes` für Auto-Patches
- [ ] Prüfe externe Dependency-Changes extra
- [ ] Security-Review bei Secrets/Auth-Code
- [ ] Performance-Review bei Data-Heavy Code

### ❌ DON'T:
- [ ] Nicht skipped critical issues
- [ ] Nicht Tests überspringen
- [ ] Nicht Type-Hints ignorieren
- [ ] Nicht Coverage-Drops akzeptieren

## iFixAi-spezifische Review-Punkte

### Fixture Loading
```python
# ✅ GOOD
from ifixai.core.fixture_loader import FixtureLoader
loader = FixtureLoader()
fixtures = await loader.load_async("path/to/fixtures.yaml")

# ❌ BAD
fixtures = json.load(open("fixtures.json"))  # No validation!
```

### Governance Integration
```python
# ✅ GOOD
from ifixai.core.governance_synthesis import apply_rules
result = apply_rules(test_case, governance_rules)

# ❌ BAD
result = test_case  # Governance ignored!
```

### Error Handling
```python
# ✅ GOOD
try:
    result = await execute_test()
except TimeoutError:
    logger.error("Test timeout", extra={"test_id": test_id})
    # Telemetry sent

# ❌ BAD
result = await execute_test()  # Crashes on timeout
```

## Example Workflow

```bash
# 1. Entwickle Feature mit Tests
git commit -m "feat(core): Add new validation"

# 2. Vor Push: Review
/code-review

# 3. Falls Issues:
# - Fix sie
# - Review wieder
/code-review

# 4. After fix: Push
git push origin feature-branch
```

## Commands Übersicht

| Command | Effekt |
|---------|--------|
| `/code-review` | Quick review |
| `/code-review --detailed` | Detaillierter review |
| `/code-review ultra` | Cloud-basierter deep review |
| `/code-review --focus security` | Nur Security |
| `/code-review --focus coverage` | Nur Test-Coverage |
| `/code-review --suggest-fixes` | Mit Auto-Fix Suggestions |
| `/code-review --fail-on-critical` | Exit code 1 bei critical issues |

---

**Nutze diesen Agent vor jedem Merge für höhere Code-Quality!** 🎯
