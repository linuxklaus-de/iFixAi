---
name: test-runner
description: Führe pytest-Tests mit Filtern aus (unit, integration, acceptance)
disable-model-invocation: true
---

# Test Runner Skill

Hiermit kannst du Tests in iFixAi einfach ausführen – mit verschiedenen Filtern.

## Verwendung

- `/test unit` — Schnelle Unit-Tests (keine externen Dependencies)
- `/test integration` — Integration-Tests (mit Mock-Provider)
- `/test acceptance` — Langsame Tests mit echten Dependencies
- `/test all` — Alle Tests
- `/test <test-name>` — Spezifischer Test nach Name

## Beispiele

```bash
# Nur Unit-Tests laufen
/test unit

# Tests mit Coverage
/test unit --cov

# Spezifischer Test
/test test_core
```

## Was passiert

Das Skill führt pytest mit den richtigen Markern aus:
- `pytest -m unit` → nur schnelle Tests
- `pytest -m integration` → mit Mock-Provider
- `pytest -m acceptance` → schwere Tests
