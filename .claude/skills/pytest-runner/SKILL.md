---
name: pytest-runner
description: Erweiterte pytest-Tests mit Debug, Coverage, Watch
disable-model-invocation: true
---

# Pytest Runner Skill (Erweitert)

Führe Tests aus mit vielen Optionen – perfekt für schnelles Debugging.

## Verwendung

### Basis
- `/test` — Schnelle Unit-Tests
- `/test integration` — Integration-Tests
- `/test acceptance` — Langsame Tests
- `/test all` — Alle Tests

### Debugging
- `/test debug` — Mit Debug-Output (verbose)
- `/test debug <name>` — Einzelner Test mit Debug
- `/test pdb` — Mit Python Debugger stoppen

### Coverage & Metriken
- `/test coverage` — Mit Coverage-Report
- `/test coverage --html` — HTML-Report öffnen
- `/test coverage --fail-under=80` — Min. 80% fordern

### Watch & Develop
- `/test watch` — Auto-Run bei Datei-Änderungen
- `/test watch <pattern>` — Nur bestimmte Tests

## Beispiele

```bash
# Schneller Check
/test unit

# Debug einen fehlgeschlagenen Test
/test debug test_core

# Coverage vor Commit
/test coverage --fail-under=85

# Watch während du entwickelst
/test watch
```

## Interne Befehle

```bash
pytest -m unit                          # Unit-Tests
pytest -m integration                   # Integration
pytest --cov=ifixai --cov-report=html  # Coverage
pytest -vv -s                           # Verbose + Print
pytest --pdb                            # Debugger
pytest-watch                            # Watch mode
```

## Tipps für Anfänger

- Nutze `/test debug` wenn Tests fehlschlagen
- Nutze `/test coverage` vor größeren Changes
- Nutze `/test watch` während du Code schreibst
- Coverage sollte > 80% sein für sauberen Code
