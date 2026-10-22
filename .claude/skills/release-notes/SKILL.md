---
name: release-notes
description: Generiert Release-Notes aus Conventional Commits
disable-model-invocation: false
---

# Release Notes Skill

Automatisch Release-Notes aus deinen Conventional Commits generieren — perfekt für Releases und Changelogs.

## Verwendung

### Von Claude aus
```
Generier Release-Notes für Version 4.2.0
Erstell Changelog aus den letzten 10 Commits
```

### Manuell aufrufen
```bash
/release-notes --version 4.2.0
/release-notes --since v4.1.0
/release-notes --count 20
/release-notes --format markdown
```

## Was der Skill macht

✅ Parst Conventional Commits (feat:, fix:, docs:, etc.)
✅ Gruppiert nach Kategorien (Features, Fixes, Breaking Changes, etc.)
✅ Erstellt schöne Markdown-Changelogs
✅ Nutzt Commit-Nachrichten und Body
✅ Verlinkt GitHub Issues (#123)
✅ Generiert Zusammenfassungen für jede Version

## Commit Format (Conventional Commits)

Der Skill funktioniert am besten mit Conventional Commits:

```
feat(scope): description          # Neue Feature
fix(scope): description           # Bug-Fix
docs(scope): description          # Dokumentation
style(scope): description         # Code-Style
refactor(scope): description      # Refactoring
perf(scope): description          # Performance
test(scope): description          # Tests
chore(scope): description         # Wartung
```

### Mit Breaking Changes
```
feat!: Breaking change description

BREAKING CHANGE: Details der Breaking Change
```

## Release Notes Struktur

```markdown
# Version 4.2.0 (2025-10-22)

## ✨ Features
- **core**: Neue API für Fixture Loading (#145)
- **observability**: Erweiterte Logging-Optionen (#142)

## 🐛 Bug Fixes
- **runner**: Fehler bei async Execution behoben (#139)
- **connection**: Memory Leak in Connection Pool (#138)

## 📚 Documentation
- API Documentation aktualisiert
- Neue Guides für Governance

## 🔄 Breaking Changes
- Entfernt: Deprecated `old_api()` Funktion
- Geändert: `Config` Schema (siehe Migration Guide)

## 🙏 Contributors
- @contributor1
- @contributor2
```

## Beispiele

### Beispiel 1: Nach Version Tag
```bash
/release-notes --since v4.1.0 --until v4.2.0
```

### Beispiel 2: Letzte N Commits
```bash
/release-notes --count 50
```

### Beispiel 3: Mit Custom Template
```bash
/release-notes --template detailed
# vs
/release-notes --template summary
```

### Beispiel 4: Für GitHub Release
```bash
/release-notes --format github-release --version 4.2.0
# Gibt Format für GitHub Release-Seite aus
```

## Best Practices

### ✅ DO:
- [ ] Nutze Conventional Commits konsistent
- [ ] Nutze Scopes (feat(core), fix(api), etc.)
- [ ] Verlinke Issues (#123)
- [ ] Schreib aussagekräftige Commit-Bodies
- [ ] Gruppiere zusammenhängende Changes

### ❌ DON'T:
- [ ] Verwende keine aussagekräftigen Commit-Nachrichten
- [ ] Nutze nicht verschiedene Formate durcheinander
- [ ] Keine sehr lange Commit-Zeilen (>72 Zeichen)

## Integration mit iFixAi

### Feature Commits
```
feat(core): Add new test execution strategy for governance validation

- Implements parallel execution with timeout handling
- Adds metrics collection for performance analysis
- Includes telemetry integration

Fixes #245
```

### Fix Commits
```
fix(runner): Handle async timeout in connection pool

Previously connection timeouts were not properly propagated.
Now they're captured and reported with retry logic.

Fixes #238
```

### Breaking Changes
```
feat!: Refactor Configuration API for better type safety

BREAKING CHANGE: The Config class API has been completely redesigned.
See docs/migration-v4-to-v5.md for upgrade guide.

Fixes #200
```

## Commands

```bash
# Basis Release-Notes
/release-notes

# Mit spezifischer Version
/release-notes --version 4.2.0

# Letzte Commits seit Tag
/release-notes --since v4.1.0

# Detailliert
/release-notes --format detailed

# Für GitHub Release
/release-notes --github

# Template-Vorschau
/release-notes --template
```

## Workflow Beispiel

```bash
# 1. Features entwickeln mit Conventional Commits
git commit -m "feat(core): Add new validation rules"

# 2. Vor Release generieren
/release-notes --count 30

# 3. Reviewen und anpassen
# (Falls nötig: Manual edits)

# 4. Als GitHub Release veröffentlichen
# (Copy-Paste oder direkt hochladen)
```

## Output Beispiele

### Markdown Format (Standard)
```markdown
## Version 4.2.0

### Features
- New API for test discovery
- Improved error handling

### Fixes
- Memory leak in connection pool
```

### GitHub Release Format
```
Release v4.2.0

## What's New
- New API for test discovery
- Improved error handling

## Fixes
- Memory leak in connection pool
```

---

**Tipp**: Nutze `/release-notes --help` für alle Optionen!
