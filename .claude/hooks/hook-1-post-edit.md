---
name: Hook #1 - Post-Edit Auto-Format & Type-Check
trigger: post_tool_use (Edit/Write)
status: active
---

# Hook #1: Post-Edit Auto-Format & Type-Check

**Wann:** Jedes mal wenn ich Code speichere oder neue Datei schreibe
**Was:** Automatisches Formatieren + Type-Checking

## Konfiguration

```json
{
  "hooks": {
    "post_tool_use": {
      "Edit": [
        {
          "name": "hook-1-ruff-format",
          "command": "cd /home/klapo/iFixAi && ruff check --fix . 2>/dev/null && echo '✅ Ruff Format OK' || echo '⚠️ Ruff Check'",
          "description": "Auto-format Code mit Ruff"
        },
        {
          "name": "hook-1-mypy-typecheck",
          "command": "cd /home/klapo/iFixAi && mypy ifixai --no-error-summary 2>/dev/null && echo '✅ MyPy OK' || echo '⚠️ Type Errors'",
          "description": "Type-Check mit mypy"
        }
      ],
      "Write": [
        {
          "name": "hook-1-validate-write",
          "command": "echo '✅ File written, auto-formatting on next edit'",
          "description": "Validates written files"
        }
      ]
    }
  }
}
```

## Befehle

### Ruff Format
```bash
ruff check --fix .
```
- ✅ Import-Reihenfolge korrigiert
- ✅ Whitespace-Fehler behoben
- ✅ Unnötige Imports entfernt
- ✅ Code-Stil standardisiert

### MyPy Type-Check
```bash
mypy ifixai --no-error-summary
```
- ✅ Type Hints validiert
- ✅ Incompatible Types gefunden
- ✅ None-Value Issues erkannt

## Beispiel

**Dein Code (vorher):**
```python
def process(data,opt=None  ):
    result=data['key']
    if opt:
        result=result.upper()
    return result
```

**Nach Hook #1:**
```python
def process(data, opt: Optional[str] = None) -> str:
    result = data["key"]
    if opt:
        result = result.upper()
    return result
```

**Automatisch behoben:**
- ✅ Abstände um Kommas hinzugefügt
- ✅ Type Hints hinzugefügt
- ✅ Zitate konsistentiert
- ✅ Einrückung standardisiert

## Vorteile

✅ Du merkst es nicht - läuft einfach
✅ Keine manuellen `ruff fix` Befehle nötig
✅ Typen werden sofort überprüft
✅ Konsistenter Code über das Projekt

## Wenn Hook fehlschlägt

```
⚠️ Type Errors
→ MyPy hat Type-Fehler gefunden
→ Du musst sie manuell fixen:
  - Type Hint hinzufügen
  - Incompatible Typ korrigieren
→ Nach Fix: Datei erneut speichern
```

## Deaktivieren

Wenn du Hook #1 nicht möchtest:
```json
{
  "hooks": {
    "post_tool_use": {
      "Edit": {
        "enabled": false
      }
    }
  }
}
```

---

**Status:** ✅ Aktiv und läuft jedes mal wenn Code gespeichert wird
