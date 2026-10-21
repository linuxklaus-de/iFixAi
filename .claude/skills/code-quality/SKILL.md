---
name: code-quality
description: Code-Qualitätschecks – Ruff, mypy, bandit
disable-model-invocation: true
---

# Code Quality Skill

Überprüfe und verbessere die Codequalität mit iFixAi's Tools.

## Verwendung

- `/code-quality check` — Alle Checks laufen
- `/code-quality ruff` — Nur Linting mit Ruff
- `/code-quality mypy` — Nur Type-Checking
- `/code-quality bandit` — Nur Security-Check
- `/code-quality fix` — Versuche, automatisch zu fixen

## Was wird geprüft

### Ruff (Linting)
- Code-Stil (E, F)
- Import-Reihenfolge (I)
- Type-Hints (UP)
- Best Practices (RUF)

### mypy (Type-Checking)
- Alle Type-Annotationen überprüfen
- Strikte Mode für höchste Sicherheit

### bandit (Security)
- Sicherheitslücken finden
- SQL-Injection, unsichere Hash-Funktionen, etc.

## Beispiele

```bash
# Kompletter Check
/code-quality check

# Auto-Fix Linting-Fehler
/code-quality fix
```
