---
name: fixture-generator
description: Generiere Test-Fixtures für iFixAi Tests
disable-model-invocation: true
---

# Fixture Generator Skill

iFixAi hat viele Test-Fixtures in YAML/JSON. Dieses Skill hilft, neue Fixtures zu erstellen.

## Verwendung

- `/fixture` — Neues Fixture interaktiv erstellen
- `/fixture <name>` — Fixture mit bestimmtem Namen
- `/fixture list` — Alle existierenden Fixtures anzeigen

## Fixture-Typen

iFixAi nutzt Fixtures in:
- `ifixai/fixtures/` — Test-Daten
- `ifixai/inspections/` — Inspection-Configs
- `ifixai/schemas/` — JSON Schemas

## Beispiel

```yaml
# Neues Fixture
name: "test_custom_inspection"
provider: "openai"
model: "gpt-4"
temperature: 0.7
```

## Best Practice

- Halte Fixtures klein und fokussiert
- Nutze bestehende Schemas als Vorlage
- Dokumentiere ungewöhnliche Werte
