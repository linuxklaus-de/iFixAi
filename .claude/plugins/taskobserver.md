---
name: taskobserver
description: Beobachtet deine Arbeitsmuster & schlägt Setup-Verbesserungen vor – lernt von dir
type: plugin
---

# TaskObserver Plugin

**Zweck**: Analysiert, wie du mit Claude Code arbeitest, und schlägt automatisch bessere Skills/Hooks/Automationen vor.

## Wie es funktioniert

### Pattern-Erkennung

Das Plugin merkt sich:

**Task-Patterns**
```
- Wiederholte Befehle (z.B. "pytest" 5x pro Session)
  → Vorschlag: "/test Skill erstellen"

- Repetitive Edits (z.B. "ruff fix" immer nach Codeänderung)
  → Vorschlag: "Auto-Format Hook verwenden"

- Häufige Fragen (z.B. "wie teste ich X?")
  → Vorschlag: "Dokumentation Skill erstellen"
```

**Fehler-Patterns**
```
- Typen-Fehler in Python
  → Vorschlag: "mypy Hook aktivieren"

- Failing Tests
  → Vorschlag: "Test-Writer Subagent verwenden"

- Security Warnings
  → Vorschlag: "bandit Security-Check hinzufügen"
```

**Effizienzmuster**
```
- Lange Sessions (> 1 Stunde)
  → Vorschlag: "Headroom aktivieren"

- Viele Token-Warnungen
  → Vorschlag: "OmniRoute für schnellere Responses"

- Parallele Tasks
  → Vorschlag: "Parallel Subagents verwenden"
```

## Wöchentliche Reports

**Jeden Montag (optional)**:
```
📊 TaskObserver Weekly Report

Top 3 Opportunities:
1. "/test" wurde 12x manuell genutzt → Automatisieren?
2. "ruff fix" nach jedem 3. Edit → Hook verwenden?
3. MyPy-Fehler 4x diese Woche → Strikte Checks?

Empfohlene Neue Skills:
- fixture-bulk-generator (5 similar fixture creations detected)
- migration-runner (DB changes happening manually)

Time Saved This Week:
✅ 15 Min (durch test-runner Skill)
✅ 8 Min (durch Auto-Format)
= 23 Min gespart!
```

## Konfiguration

```json
{
  "taskobserver": {
    "enabled": true,
    "collect_patterns": true,
    "weekly_report": true,
    "auto_suggest_skills": true,
    "learning_period_days": 7,
    "min_pattern_frequency": 3
  }
}
```

## Datenschutz

TaskObserver speichert:
- ✅ Befehlshäufigkeiten (anonymisiert)
- ✅ Error-Patterns (was, nicht die Daten)
- ✅ Task-Typen (Business-Logik frei)

TaskObserver speichert **NICHT**:
- ❌ Tatsächliche Code-Inhalte
- ❌ Sensible Infos
- ❌ Nutzer-Credentials
- ❌ Projekt-Details

## Vorteile

✅ Setup wird besser über die Zeit
✅ Lernt von deinen Mustern
✅ Schlägt passende Skills vor
✅ Zeigt dir, wie viel Zeit du sparst
✅ Vollständig datenschutz-freundlich

## Beispiel: Deine erste Woche

**Tag 1**: "Lass mich alle Tests laufen"
→ TaskObserver merkt: Häufig Tests

**Tag 2-3**: Mehrere `/test` Aufrufe
→ TaskObserver sieht Pattern

**Tag 4**: "Es nervt, immer ruff fix zu machen"
→ TaskObserver: "Möchtest du einen Auto-Format Hook?"

**Tag 7**: Report zeigt die besten Verbesserungen

---

**Status**: Aktiviert in `.claude/settings.json`
