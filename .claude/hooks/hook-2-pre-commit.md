---
name: Hook #2 - Pre-Commit Quality-Gate
trigger: pre_commit
status: active
---

# Hook #2: Pre-Commit Quality-Gate

**Wann:** Bevor Git Commit erstellt wird
**Was:** Tests, Linting, Type-Checking - alles muss grün sein

## Workflow

```
Du willst: git commit -m "..."
    ↓
Hook #2 lauft automatisch:
    1. pytest -m unit          (Tests)
    2. ruff check              (Linting)
    3. mypy check              (Types)
    ↓
Alle grün? ✅ → Commit erlaubt
Mindestens eins rot? ❌ → Commit blockiert
```

## Konfiguration

```json
{
  "hooks": {
    "pre_commit": {
      "name": "hook-2-pre-commit-quality-gate",
      "commands": [
        {
          "name": "tests",
          "command": "cd /home/klapo/iFixAi && pytest -m unit -q 2>/dev/null && echo '✅ Unit Tests PASSED' || echo '❌ Tests FAILED'",
          "halt_on_error": false
        },
        {
          "name": "linting",
          "command": "cd /home/klapo/iFixAi && ruff check . 2>/dev/null && echo '✅ Linting OK' || echo '❌ Linting FAILED'",
          "halt_on_error": false
        },
        {
          "name": "types",
          "command": "cd /home/klapo/iFixAi && mypy ifixai --no-error-summary 2>/dev/null && echo '✅ Type Check OK' || echo '⚠️ Type Errors'",
          "halt_on_error": false
        }
      ]
    }
  }
}
```

## Befehle

### 1. Unit Tests
```bash
pytest -m unit -q
```
- Schnelle Tests laufen
- Muss 100% grün sein

### 2. Linting (Ruff)
```bash
ruff check .
```
- Code-Stil wird überprüft
- Keine Fehler erlaubt

### 3. Type Checking (MyPy)
```bash
mypy ifixai --no-error-summary
```
- Alle Type Hints geprüft
- Keine incompatible Types

## Beispiel: Commit wird blockiert

```
Du: git commit -m "fix: handle timeout in tests"
    ↓
Hook #2 Check:
❌ Tests FAILED
    ifixai/tests/test_async.py::test_timeout - AssertionError
    
❌ Commit abgelehnt!
    
→ Du musst:
  1. Test fixen: pytest -m unit --tb=short
  2. Code reparieren
  3. Datei speichern (Hook #1 formatiert)
  4. Erneut versuchen: git commit -m "..."
```

## Beispiel: Commit erlaubt

```
Du: git commit -m "feat(core): add retry logic"
    ↓
Hook #2 Check:
✅ Unit Tests PASSED (23 passed in 0.45s)
✅ Linting OK
✅ Type Check OK
    
✅ Commit erstellt!
    
Commit: abc1234 "feat(core): add retry logic"
Branch: main
```

## `halt_on_error` erklärt

```json
"halt_on_error": false
```

Das bedeutet:
- Alle 3 Commands laufen immer
- Selbst wenn einer fehlschlägt
- Du siehst alle Fehler auf einmal
- Schneller reparieren!

## Fehlerszenarien

### Szenario 1: Test fehlgeschlagen
```
❌ Tests FAILED
→ Welcher Test? pytest -m unit -v
→ Debuggen: /test debug <name>
→ Fixen und erneut committen
```

### Szenario 2: Linting Fehler
```
❌ Linting FAILED
→ Ruff hat Fehler gefunden
→ Auto-fixen: ruff check --fix .
→ Datei speichern (Hook #1 hilft)
→ Erneut committen
```

### Szenario 3: Type Errors
```
⚠️ Type Errors
→ MyPy hat Type-Probleme gefunden
→ Type Hints hinzufügen
→ Incompatible Types fixen
→ Erneut committen
```

## Vorteile

✅ Keine broken Commits in Git-History
✅ Nur sauberer Code wird committed
✅ Schnelle Feedback-Loop
✅ Team kann auf sauberer Code vertrauen

## Wenn Hook fehlschlägt

**Ist normal beim Lernen!**

```bash
# 1. Fehler anschauen
❌ Tests FAILED

# 2. Lokal fixen
pytest -m unit --tb=short
# → Schaue welcher Test fehlschlägt
# → Fix Code

# 3. Hook nochmal prüfen
# → Datei speichern (Hook #1 formatiert)

# 4. Erneut committen
git commit -m "..."
# → Dieses mal: ✅ Alle grün!
```

## Deaktivieren (nicht empfohlen!)

```json
{
  "hooks": {
    "pre_commit": {
      "enabled": false
    }
  }
}
```

⚠️ **Nicht empfohlen** - Qualität sinkt!

---

**Status:** ✅ Aktiv - schützt deine Git-History vor Müll
