---
name: commit-message-helper
description: Bessere Commit-Messages – Conventional Commits, automatisch
disable-model-invocation: true
---

# Commit Message Helper Skill

Schreibe bessere Git-Commits mit Struktur und Best Practices.

## Verwendung

### Assisted Mode
- `/commit` — Interaktiv Commit schreiben
- `/commit --type=fix` — Fix-Commit
- `/commit --type=feat` — Feature-Commit
- `/commit --type=docs` — Dokumentation
- `/commit --type=refactor` — Refactoring

### Conventional Commits
- `/commit conventional` — CC Format
- `/commit cc` — Shorthand für CC

### Automatisch
- `/commit auto` — Aus Diff generieren
- `/commit auto --ai` — Mit AI-Vorschlag

### Changelog
- `/commit changelog` — Changelog-Entry erstellen
- `/commit changelog --for=v4.2.0` — Für bestimmte Version

## Conventional Commits Format

```
<type>(<scope>): <subject>
<blank line>
<body>
<blank line>
<footer>
```

### Types
- **feat** — Neues Feature
- **fix** — Bug-Fix
- **docs** — Dokumentation
- **style** — Code-Stil (keine Logik-Änderung)
- **refactor** — Code umstrukturiert (keine Features)
- **perf** — Performance verbessert
- **test** — Tests hinzugefügt
- **chore** — Build, Dependencies, etc.

### Scope (Optional)
```
fix(core): handle async errors correctly
       ↑
    Bereich
```

Beispiele: `core`, `cli`, `tests`, `fixtures`

## Beispiele

### Gut ❌
```
Fixed bug in test runner
```

### Besser ✅
```
fix(tests): handle async fixtures with timeout

Previously, fixtures would hang indefinitely if
the provider was slow. Now we use a 5-second
timeout and proper error handling.

Fixes #123
```

### Struktur für Anfänger
```bash
# Interactive Mode
/commit

# Was hast du geändert?
Fix bug in test runner

# Welcher Bereich?
tests

# Detaillierte Beschreibung?
Handle async fixtures with proper timeout
Added 5-second timeout for slow providers
Improved error messages

# Fertig!
```

## Best Practices

✅ Imperativ verwenden: "Add" nicht "Added"
✅ Kurz bleiben: Erste Zeile < 50 Zeichen
✅ Details in Body erklären
✅ Referenziere Issues: "Fixes #123"
✅ Eine logische Änderung pro Commit

❌ Keine Großbuchstaben am Anfang (außer Names)
❌ Keine Punkte am Ende
❌ Nicht "Misc updates" schreiben

## Changelog Generieren

```bash
# Changelog für aktuelle Version
/commit changelog

# Output:
## [4.2.0] - 2026-10-21
### Added
- New test runner with watch mode
- Security audit skill

### Fixed
- Async fixture handling
- Type errors in CLI

### Changed
- Updated documentation
```

## Tipps für Anfänger

- Nutze `/commit conventional` um saubere Historie zu bauen
- Nutze `/commit` wenn du unsicher bist
- Gute Commits = leichte Code-Review!
- Nutze `/commit changelog` vor Releases
