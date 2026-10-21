# 🪝 iFixAi Custom Hooks

Automatische Qualitätschecks & Prozesse - läuft im Hintergrund!

---

## **Hook #1: Post-Edit Auto-Format & Type-Check**

### Wann triggered?
```
→ Jedes mal wenn ich Code speichere (Edit/Write)
```

### Was passiert?
```
1. ruff check --fix  (Auto-Format Code)
2. mypy check        (Prüfe Typen)
```

### Output
```
✅ Ruff Format OK
✅ MyPy OK
```

### Nutzen
- ✅ Code wird automatisch formatiert
- ✅ Typen werden geprüft
- ✅ Keine manualen `ruff fix` Befehle nötig
- ✅ Fehler werden sofort sichtbar

### Beispiel

**Vorher**: Du schreibst messy Code
```python
def calculate(x,y  ):
    result=x+y
    return result
```

**Nachher**: Hook formatiert automatisch
```python
def calculate(x, y):
    result = x + y
    return result
```

---

## **Hook #2: Pre-Commit Quality-Gate**

### Wann triggered?
```
→ Bevor du `git commit` erstellst
```

### Was passiert?
```
1. pytest -m unit    (Tests laufen)
2. ruff check        (Linting)
3. mypy check        (Type-Checking)
```

### Output
```
✅ Unit Tests PASSED
✅ Linting OK
✅ Type Check OK
→ Commit erlaubt!
```

oder

```
❌ Tests FAILED
→ Commit blockiert!
```

### Nutzen
- ✅ Nur sauberer Code in Git
- ✅ Tests müssen grün sein
- ✅ Verhindert broken commits
- ✅ Keine Überraschungen später

### Workflow

```
Du schreibst Code
    ↓
Du speicherst (Hook #1: Format & Type-Check)
    ↓
Du willst committen
    ↓
Hook #2: Laufen alle Tests?
    → Ja? ✅ Commit erlaubt
    → Nein? ❌ Commit blockiert, Fix nötig
```

---

## **Hook #3: Pre-Push Security-Audit**

### Wann triggered?
```
→ Bevor du zu GitHub pushst (git push)
```

### Was passiert?
```
1. bandit -r ifixai  (Security-Scan)
2. pip list          (Überprüfe Dependencies)
```

### Output
```
✅ Security OK
📦 Check outdated packages
→ Push erlaubt!
```

### Nutzen
- ✅ Keine Sicherheitslücken publishen
- ✅ Dependencies sind aktuell
- ✅ Team ist sicher
- ✅ Compliance-freundlich

### Beispiel

Hook findet:
```
⚠️ SQL-Injection risk in line 42
⚠️ Hard-coded password in config
```

→ Du musst fixen bevor Push möglich ist!

---

## **Hook #4: Watch-Mode Auto-Test**

### Wann triggered?
```
→ Jedes mal wenn sich Python-Datei ändert
```

### Was passiert?
```
pytest -m unit --tb=short  (Tests laufen automatisch)
```

### Output
```
✅ 23 passed in 0.45s
```

oder

```
❌ 2 failed, 21 passed
→ Hier ist das Problem: ...
```

### Nutzen
- ✅ Instant Feedback beim Entwickeln
- ✅ Spar Zeit bei manuellen Test-Runs
- ✅ Bugs werden sofort sichtbar
- ✅ Schnellere Entwicklung

### Beispiel Workflow

```
Du änderst ifixai/core.py
    ↓ (Auto-trigger)
Tests laufen (0.5 Sekunden)
    ↓
Output: "✅ 23 passed"
    ↓
Du weißt sofort: Deine Änderung ist gut!
```

---

## **Hook #5: Commit-Message Validator**

### Wann triggered?
```
→ Wenn du eine Commit-Message schreibst
```

### Was wird geprüft?

#### Rule #1: Conventional Commits Format
```
✅ feat(core): add async support
❌ Added new feature
```

#### Rule #2: Erste Zeile < 50 Zeichen
```
✅ fix(tests): handle timeout errors
❌ This is a very long commit message that exceeds the recommended length of 50 characters
```

#### Rule #3: Keine WIP/DEBUG Flags
```
✅ feat(cli): new command parser
❌ WIP: new feature
❌ DEBUG: testing something
```

### Output

**Gute Message:**
```
✅ Conventional Commits format OK
✅ First line < 50 chars
✅ No WIP/TEMP flags
→ Message ist perfect!
```

**Schlechte Message:**
```
❌ Use Conventional Commits: feat(scope): description
↑ Deine Message "Added stuff" folgt nicht dem Format
```

### Nutzen
- ✅ Konsistente Git-Historie
- ✅ Bessere Code-Reviews
- ✅ Automatische Changelog-Generierung möglich
- ✅ Team-Standard

---

## 📊 **Alle Hooks im Überblick**

| Hook | Trigger | Aktion | Nutzen |
|------|---------|--------|--------|
| **#1** | Nach Edit/Write | Format + Type-Check | Sauberer Code |
| **#2** | Vor Commit | Tests + Linting | Nur guter Code in Git |
| **#3** | Vor Push | Security + Dependencies | Keine Bugs publishen |
| **#4** | File Changes | Auto-Test | Instant Feedback |
| **#5** | Commit-Message | Format-Prüfung | Konsistente Historia |

---

## 🚀 **Dein Workflow mit Hooks**

```
1️⃣ Du schreibst Code
        ↓
   Hook #1 (Auto-Format)
   "Code ist formatiert! ✅"
        ↓
2️⃣ Datei änder sich
        ↓
   Hook #4 (Auto-Test)
   "Tests: ✅ 23 passed"
        ↓
3️⃣ Du willst Commit
        ↓
   Hook #5 (Message-Check)
   "Message: ✅ Valid"
        ↓
   Hook #2 (Quality-Gate)
   "Tests: ✅ All green"
        ↓
4️⃣ Git Commit erstellt ✅
        ↓
5️⃣ Du willst Push zu GitHub
        ↓
   Hook #3 (Security-Audit)
   "Security: ✅ Safe"
        ↓
6️⃣ Push zu GitHub ✅
```

**Resultat**: Sauberer, sicherer Code! 🎉

---

## ⚙️ **Konfiguration**

Alle Hooks sind in `.claude/settings.json` konfiguriert:
```json
{
  "hooks": {
    "post_tool_use": { ... },      // Hook #1
    "pre_commit": { ... },          // Hook #2
    "pre_push": { ... },            // Hook #3
    "file_watch": { ... },          // Hook #4
    "commit_message_validation": {}  // Hook #5
  }
}
```

---

## 🎓 **Für Anfänger: FAQ**

**Q: Werden die Hooks automatisch laufen?**
A: Ja! Aktiviert in settings.json. Du merkst es nur durch bessere Code-Qualität.

**Q: Was wenn ein Hook fehlschlägt?**
A: z.B. Hook #2: Commit wird blockiert. Du musst Tests fixen, dann erneut committen.

**Q: Kann ich einen Hook ausschalten?**
A: Ja, in settings.json: `"enabled": false`

**Q: Sind Hooks schnell?**
A: Ja! Meist < 1 Sekunde. Hook #4 (Tests) dauert länger aber läuft im Hintergrund.

**Q: Was ist "halt_on_error"?**
A: Wenn `true` → Prozess stoppt bei Fehler. Wenn `false` → Zeigt Fehler aber stoppt nicht.

---

## ✅ **Status: ALLE HOOKS AKTIV!**

Dein iFixAi Projekt ist jetzt **vollständig automatisiert**! 🚀
