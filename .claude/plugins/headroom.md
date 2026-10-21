---
name: headroom
description: Context-Reduktion – entfernt unnötige alte Messages, fokussiert auf aktuelle Aufgabe
type: plugin
---

# Headroom Plugin

**Zweck**: Reduziert Context-Größe automatisch, indem alte/irrelevante Messages entfernt werden. Macht Claude schneller & effizienter.

## Wie es funktioniert

### Automatische Context-Verwaltung

**Phase 1: Summarize (bei 70% Context)**
- Fasse letzte 10 Messages zusammen
- Behalte nur Kern-Informationen
- Entferne repetitive Fragen

**Phase 2: Archive (bei 85% Context)**
- Speichere alte Messages in Memory
- Behalte nur aktuelle Task
- Reduziert Größe um ~50%

**Phase 3: Reset (bei 95% Context)**
- Frage den Nutzer, ob neue Session nötig ist
- Gibt dir die Option zu speichern/archivieren

### Smart Filtering
Entfernt **nicht** automatisch:
- Aufgaben-Definitionen
- User Instructions (CLAUDE.md)
- Wichtige Kontexte (Memory)

Entfernt **automatisch**:
- Abgeschlossene Tasks
- Debug-Output (git logs, Bash output)
- Bestätigte Lösungen
- Wiederholte Fragen

## Konfiguration

```json
{
  "headroom": {
    "enabled": true,
    "auto_summarize_at": 0.70,
    "auto_archive_at": 0.85,
    "keep_latest_messages": 5,
    "archive_location": "memory"
  }
}
```

## Vorteile

✅ Längere Sessions möglich
✅ Schnellere Responses (weniger zu lesen)
✅ Fokus bleibt auf aktuelle Aufgabe
✅ Wichtiges bleibt gespeichert (Memory)

## Beispiel

**Vorher**: 150K Tokens (voll)
```
- Plugins Setup (abgeschlossen)
- Git Commit Fehler (gelöst)
- Test Failures (behoben)
- Test Erfolg (bestätigt)
- Neue Aufgabe (aktiv) ← AKTUELL
```

**Nachher**: 45K Tokens (geräumt)
```
[ARCHIVED: Setup & Commits (2 messages summarized)]

- Neue Aufgabe (aktiv) ← AKTUELL
```

## Nutzer-Kontrolle

Du kannst jederzeit sagen:
- "Keine Auto-Summary" – deaktiviert für diese Session
- "Archive Everything" – räumt sofort auf
- "Reset Context" – neue Session mit nur der aktuellen Aufgabe

---

**Status**: Aktiviert in `.claude/settings.json`
