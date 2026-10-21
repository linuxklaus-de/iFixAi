---
name: omniroute
description: Intelligentes Modell-Switching bei großem Kontext – schneller bei Limits
type: plugin
---

# OmniRoute Plugin

**Zweck**: Automatisch zwischen AI-Modellen wechseln, wenn der Kontext groß wird oder Nutzungs-Limits nahe sind.

## Wie es funktioniert

### Kontext-Größe Monitoring
- **Klein** (< 50K tokens): Normales Modell (Opus für tiefe Analysen)
- **Mittel** (50K-100K tokens): Balanciertes Modell (Sonnet für schnelle Lösungen)
- **Groß** (> 100K tokens): Schnelles Modell (Haiku für Edits)

### Token-Limits Beobachten
Wenn Token-Budget:
- **> 80%**: Wechsel zu Haiku (schneller, effizienter)
- **> 90%**: Nur noch Edits/Schreib-Operationen
- **> 95%**: Frage den Nutzer, ob Zusammenfassung nötig ist

## Konfiguration

```json
{
  "omniroute": {
    "enabled": true,
    "model_strategy": "adaptive",
    "token_thresholds": {
      "small": 50000,
      "medium": 100000,
      "large": 150000
    },
    "token_warning": 0.8,
    "token_critical": 0.95
  }
}
```

## Vorteile

✅ Schnellere Responses bei großen Projekten
✅ Sparsamer mit Token-Budget
✅ Automatisch – keine manuellen Einstellungen
✅ Perfekt für lange Sessions

## Verwendung

Einfach aktiviert – du merkst nur schnellere Responses! 🚀

---

**Status**: Aktiviert in `.claude/settings.json`
