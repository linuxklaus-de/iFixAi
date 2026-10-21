---
name: documentation-generator
description: Dokumentation automatisch aus Code generieren & aktualisieren
disable-model-invocation: true
---

# Documentation Generator Skill

Erstelle und aktualisiere Dokumentation automatisch aus deinem Code.

## Verwendung

### API-Dokumentation
- `/docs api` — Aus Funktionen/Klassen generieren
- `/docs api --module=ifixai.core` — Nur bestimmtes Modul
- `/docs api --format=markdown` — Als Markdown ausgeben
- `/docs api --format=html` — Als HTML generieren

### README & Überblick
- `/docs readme` — README aktualisieren/neu schreiben
- `/docs overview` — Projekt-Überblick erstellen
- `/docs architecture` — Architektur dokumentieren

### Changelog & Releases
- `/docs changelog` — Changelog aus Commits generieren
- `/docs changelog --since=v4.0.0` — Seit bestimmter Version
- `/docs whatsnew` — "Was ist neu?" für Release

### Code-Kommentare
- `/docs from-code` — Docstrings aus Code generieren
- `/docs check-docs` — Fehlende Dokumentation finden
- `/docs examples` — Usage-Beispiele erstellen

## Beispiele

```bash
# API-Doku generieren
/docs api

# README aktualisieren
/docs readme

# Changelog für neue Version
/docs changelog --since=v4.0.0

# Docstrings prüfen
/docs check-docs
```

## Was wird dokumentiert

✅ Funktionen (Argumente, Return, Docstrings)
✅ Klassen (Methoden, Attribute, Beispiele)
✅ Module (Überblick, Submodule)
✅ CLI-Commands (Alle `/` Befehle)
✅ Konfiguration (settings.json, pyproject.toml)

## Output-Formate

- **Markdown** — Für GitHub/Docs
- **HTML** — Für Browser
- **ReStructuredText** — Für Sphinx
- **Plain Text** — Für einfache Lesbarkeit

## Tipps für Anfänger

- Nutze `/docs api` um deine Arbeit zu zeigen
- Nutze `/docs readme` für Projekt-Überblick
- Nutze `/docs changelog` vor Release
- Gute Docs = bessere Zusammenarbeit!
