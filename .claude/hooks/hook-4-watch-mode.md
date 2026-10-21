---
name: Hook #4 - Watch-Mode Auto-Test
trigger: file_watch
status: active
---

# Hook #4: Watch-Mode Auto-Test

**Wann:** Jedes mal wenn sich eine Python-Datei ändert
**Was:** Tests laufen automatisch im Hintergrund

## Workflow

```
Du änderst ifixai/core.py
    ↓
Hook #4 triggered (auto)
    ↓
pytest -m unit lauft (schnell, ~0.5s)
    ↓
Output: "✅ 23 passed" oder "❌ 2 failed"
    ↓
Du siehst sofort: Änderu ist OK oder kaputt
```

## Konfiguration

```json
{
  "hooks": {
    "file_watch": {
      "name": "hook-4-watch-mode-auto-test",
      "patterns": [
        {
          "glob": "ifixai/**/*.py",
          "command": "cd /home/klapo/iFixAi && pytest -m unit -q --tb=short 2>/dev/null || true",
          "description": "Auto-test on Python file changes"
        }
      ]
    }
  }
}
```

## Was wird überwacht

```
ifixai/**/*.py
    ↓
Alle Python-Dateien im ifixai-Verzeichnis
    ↓
Wenn eine ändert: Tests laufen automatisch
```

## Beispiel

```
Du schreibst:
def add(a, b):
    return a + b + 1  # ← Fehler! Sollte nur a+b sein

(Datei speichern)
    ↓
Hook #4:
❌ 1 failed, 22 passed
   test_core.py::test_add - AssertionError: 3 != 2
    
Du siehst sofort: Das ist falsch!
    
Du fixst:
def add(a, b):
    return a + b  # ← Richtig

(Datei speichern)
    ↓
Hook #4:
✅ 23 passed

Du siehst sofort: Jetzt ist es richtig!
```

## Vorteile

✅ Instant Feedback (< 1 Sekunde)
✅ Bugs werden sofort sichtbar
✅ Keine manuellen Test-Runs nötig
✅ Schnellere Entwicklung

## Output-Formate

### Kurz (mit -q flag)
```
✅ 23 passed in 0.45s
```

### Mit Fehlern
```
❌ 2 failed, 21 passed
test_core.py::test_async - TimeoutError
test_fixtures.py::test_yaml - ValueError
```

### Detailliert (mit -v flag)
```
test_core.py::test_add PASSED
test_core.py::test_subtract PASSED
...
23 passed in 0.45s
```

## Integration mit Workflow

```
1. Du öffnest ifixai/core.py
2. Du schreibst neue Funktion
3. Hook #1 (speichern)
   → Auto-Format + Type-Check
4. Hook #4 (auto)
   → Tests laufen
5. Output: Tests grün? ✅
   → Du kannst weiterentwickeln
6. Tests rot? ❌
   → Du weißt sofort: Fehler finden & fixen
```

## Konfigurieren

### Nur bestimmte Test-Dateien
```json
{
  "glob": "ifixai/tests/test_core.py",
  "command": "pytest ifixai/tests/test_core.py -q"
}
```

### Mit Coverage
```json
{
  "command": "pytest -m unit -q --cov=ifixai"
}
```

### Mit Verbose Output
```json
{
  "command": "pytest -m unit -v --tb=short"
}
```

## Deaktivieren

```json
{
  "hooks": {
    "file_watch": {
      "enabled": false
    }
  }
}
```

Oder: Nur bestimmte Dateien überwachen:
```json
{
  "glob": "ifixai/tests/**/*.py",  // Nur Tests
}
```

## Performance

### Timing
- Test-Lauf: ~0.5 Sekunden (nur Unit-Tests)
- File-Watch: < 10ms (sehr schnell)
- Total: ~0.5s nach Speichern

### CPU-Last
- Minimal (Tests laufen schnell)
- Nur wenn sich Datei ändert
- Nicht beim Tippen, nur beim Speichern

## Best Practices

✅ Nutze nur Unit-Tests (schnell)
✅ Watch-Mode während du entwickelst
✅ Schalte aus wenn CPU-Last zu hoch
✅ Integration-Tests manuell vor Commit

---

**Status:** ✅ Aktiv - gibt dir Instant Feedback beim Entwickeln
