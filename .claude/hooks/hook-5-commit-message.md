---
name: Hook #5 - Commit-Message Validator
trigger: commit_message_validation
status: active
---

# Hook #5: Commit-Message Validator

**Wann:** Wenn du eine Git Commit-Message schreibst
**Was:** Validiert dass Message dem Conventional Commits Format folgt

## Workflow

```
Du schreibst Commit-Message:
"Added new feature"
    ↓
Hook #5 prüft:
    1. Conventional Commits Format?
    2. Erste Zeile < 50 Zeichen?
    3. Keine WIP/DEBUG Flags?
    ↓
Alle OK? ✅ → Commit erlaubt
Fehler? ❌ → Commit blockiert
```

## Konfiguration

```json
{
  "hooks": {
    "commit_message_validation": {
      "name": "hook-5-commit-message-validator",
      "rules": [
        {
          "pattern": "^(feat|fix|docs|style|refactor|perf|test|chore)(\\(.+\\))?:.+",
          "message": "✅ Conventional Commits format OK",
          "error_message": "❌ Use Conventional Commits: feat(scope): description"
        },
        {
          "pattern": "^.{1,50}$",
          "message": "✅ First line < 50 chars",
          "error_message": "❌ First line must be < 50 characters"
        },
        {
          "not_pattern": "^.*(WIP|TEMP|DEBUG).*$",
          "message": "✅ No WIP/TEMP flags",
          "error_message": "⚠️ Remove WIP/TEMP flags before committing"
        }
      ]
    }
  }
}
```

## Rule #1: Conventional Commits Format

### Format
```
<type>(<scope>): <subject>
```

### Types
- `feat` — Neues Feature
- `fix` — Bug-Fix
- `docs` — Dokumentation
- `style` — Code-Stil (keine Logik-Änderung)
- `refactor` — Code umstrukturiert
- `perf` — Performance
- `test` — Tests
- `chore` — Build, Dependencies, etc.

### Scope (Optional)
```
fix(tests): handle timeout error
    ↑
 Bereich (optional)
```

### Gültige Messages ✅
```
feat: add new feature
fix: handle async error
docs: update README
feat(core): add retry logic
fix(tests): improve timeout
chore(deps): update ruff
```

### Ungültige Messages ❌
```
Added new feature          (kein Type)
add feature                (kein Type)
feat: ADD FEATURE          (Großbuchstaben)
feat add feature           (kein Doppelpunkt)
```

## Rule #2: Erste Zeile < 50 Zeichen

### Warum 50?
- ✅ GitHub truncates nach ~50 chars in Log
- ✅ Leichter zu lesen in `git log`
- ✅ Standard in Industrie

### Zählen
```
feat(core): add retry logic
↑         ↑                 ↑
0        10                 30 chars ✅
```

```
fix(tests): handle async timeout errors properly
↑         ↑                                      ↑
0        10                                     50 chars ✅
```

```
feat(core): add support for async operations with proper error handling
↑         ↑                                                           ↑
0        10                                                          75 chars ❌
```

## Rule #3: Keine WIP/DEBUG Flags

### Ungültig ❌
```
WIP: new feature
TEMP: testing something
DEBUG: trying this approach
[WIP] Add retry logic
```

### Gültig ✅
```
feat(core): add retry logic
fix(tests): handle timeout
docs: update configuration
```

## Vollständige Commit-Message Struktur

```
feat(core): add retry logic
           ↑
        Max 50 Zeichen (Hook #5 prüft)

Implement exponential backoff for failed requests.
The retry mechanism now supports:
- Configurable max attempts
- Exponential delay between retries
- Custom backoff strategy

Fixes #123
           ↑
        (Optional: Issue Reference)
```

## Beispiele: Hook-Validierung

### Beispiel 1: Message erfolgreich ✅
```
Input: "feat(core): add async support"

Hook #5 Validierung:
✅ Conventional Commits format OK
   - Type: "feat" ✓
   - Scope: "core" ✓
   - Message: "add async support" ✓
   
✅ First line < 50 chars
   - Length: 31 ✓
   
✅ No WIP/TEMP flags
   - "WIP" nicht vorhanden ✓

✅ Message ist valid!
→ Commit erstellt
```

### Beispiel 2: Format ungültig ❌
```
Input: "Added async support"

Hook #5 Validierung:
❌ Conventional Commits format OK
   - Missing type (feat/fix/docs/...)
   - Message muss sein: "feat: Added async support"
   
Error: "Use Conventional Commits: feat(scope): description"

→ Commit blockiert!
→ Du musst Message ändern
```

### Beispiel 3: Zu lang ❌
```
Input: "feat(core): add comprehensive async support with error handling"

Hook #5 Validierung:
✅ Conventional Commits format OK

❌ First line < 50 chars
   - Length: 65 (zu lang!)
   
Error: "First line must be < 50 characters"

→ Commit blockiert!
→ Kurzer fassen: "feat(core): add async support"
```

### Beispiel 4: WIP Flag ❌
```
Input: "WIP: new async feature"

Hook #5 Validierung:
✅ Conventional Commits format OK (hat Type: "WIP")

❌ No WIP/TEMP flags
   - Message enthält "WIP"
   
Error: "Remove WIP/TEMP flags before committing"

→ Commit blockiert!
→ "feat(core): add async support" (ohne WIP)
```

## Workflow mit Hook #5

```
1. Du schreibst Code
   ↓
2. Commit vorbereiten
   git add .
   ↓
3. Commit-Message schreiben
   git commit -m "Added new feature"
   ↓
4. Hook #5 prüft
   ❌ Missing type (feat/fix/...)
   ↓
5. Du änderst Message
   git commit --amend -m "feat: add new feature"
   ↓
6. Hook #5 prüft nochmal
   ✅ Conventional Commits format OK
   ✅ First line < 50 chars
   ✅ No WIP/TEMP flags
   ↓
7. Commit erstellt ✅
```

## Vorteile

✅ Konsistente Git-Historie
✅ Bessere Code-Reviews
✅ Automatische Changelog-Generierung möglich
✅ Team-Standard
✅ Leichte zu lesen mit `git log`

## Deaktivieren

```json
{
  "hooks": {
    "commit_message_validation": {
      "enabled": false
    }
  }
}
```

Nicht empfohlen - Clean History ist wichtig!

## Best Practices

✅ Imperativ verwenden: "Add" nicht "Added"
✅ Kurz bleiben: < 50 Zeichen
✅ Type immer angeben: feat/fix/docs/...
✅ Scope optional: (core), (tests), (cli)
✅ Details in Body erklären

---

**Status:** ✅ Aktiv - garantiert saubere Git-Historie
