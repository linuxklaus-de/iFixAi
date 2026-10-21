---
name: release-manager
description: Releases verwalten – Versioning, Tags, Releases
disable-model-invocation: true
---

# Release Manager Skill

Verwalte Releases professionell – Versioning, Tags, Changelog.

## Verwendung

### Versioning (Semantic Versioning)
- `/release bump patch` — 4.1.0 → 4.1.1 (Bug-Fixes)
- `/release bump minor` — 4.1.0 → 4.2.0 (Features)
- `/release bump major` — 4.1.0 → 5.0.0 (Breaking Changes)
- `/release version` — Aktuelle Version zeigen

### Release-Prozess
- `/release prepare` — Vorbereitung prüfen
- `/release create` — Release erstellen
- `/release tag` — Git-Tag setzen
- `/release publish` — Zu PyPI publishen

### Dokumentation
- `/release notes` — Release Notes generieren
- `/release changelog` — Changelog aktualisieren
- `/release announce` — Ankündigung vorbereiten

### Status & Info
- `/release status` — Release-Status
- `/release log` — Letzte Releases anzeigen
- `/release compare` — Versionen vergleichen

## Semantic Versioning (SemVer)

```
MAJOR.MINOR.PATCH
  ↓     ↓      ↓
5.2.1 ← Breaking Changes
      ← New Features
        ← Bug Fixes
```

### Wann welche Version?

| Change | Version | Beispiel |
|--------|---------|----------|
| Bug-Fix | PATCH | 4.1.0 → 4.1.1 |
| New Feature | MINOR | 4.1.0 → 4.2.0 |
| Breaking Change | MAJOR | 4.1.0 → 5.0.0 |

## Release-Checklist

```bash
# 1. Checklist
/release prepare

# 2. Version bumpen
/release bump minor   # für Features

# 3. Changelog & Notes
/release notes
/release changelog

# 4. Git & Tag
/release tag

# 5. Publishen (optional)
/release publish      # zu PyPI

# 6. Fertig!
```

## Beispiel-Workflow

```bash
# Du möchtest iFixAi 4.2.0 releasen

# 1. Vorbereiten
/release prepare
# ✅ Tests bestanden
# ✅ Docs aktuell
# ✅ CHANGELOG.md existiert

# 2. Version ändern
/release bump minor
# pyproject.toml: 4.1.0 → 4.2.0

# 3. Release-Notes
/release notes
# ## [4.2.0] - 2026-10-21
# ### Added
# - New test runner skill
# ### Fixed
# - Async fixture handling

# 4. Committen & Tagen
/release tag
# git tag v4.2.0
# git commit -m "chore: release v4.2.0"

# 5. Optional publishen
/release publish
# python -m build && twine upload dist/*

# 6. Fertig! 🎉
```

## Release Notes Format

```markdown
## [4.2.0] - 2026-10-21

### Added
- New pytest-runner skill with watch mode
- Security-audit skill for code scanning
- Documentation generator

### Fixed
- Async fixture handling timeout issue
- Type errors in CLI module
- Memory leak in long-running tests

### Changed
- Updated dependencies (ruff 0.5.0)
- Improved error messages
- Optimized test execution

### Deprecated
- Old test-runner approach (deprecated in 4.2.0)

### Removed
- Obsolete fixtures (moved to archive)

### Security
- Fixed potential SQL-injection in logging
```

## Pre-Release Checks

```bash
# Vor Release IMMER:
/release prepare

# Prüft:
✅ Tests bestanden
✅ Linting OK
✅ Type-Checking OK
✅ Security OK
✅ Changelog vorhanden
✅ Version updated
✅ Git clean (keine uncommitted changes)
```

## Tipps für Anfänger

- Nutze PATCH für Bug-Fixes
- Nutze MINOR für neue Features
- Nutze MAJOR nur für Breaking Changes
- Immer `/release prepare` vor Release!
- Release-Notes sind wichtig für User
- Ein Release = Ein Clean Commit
