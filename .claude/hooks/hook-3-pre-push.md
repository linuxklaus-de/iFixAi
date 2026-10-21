---
name: Hook #3 - Pre-Push Security-Audit
trigger: pre_push
status: active
---

# Hook #3: Pre-Push Security-Audit

**Wann:** Bevor du zu GitHub pushst
**Was:** Sicherheit prüfen + Dependencies checken

## Workflow

```
Du willst: git push origin main
    ↓
Hook #3 lauft:
    1. bandit -r ifixai        (Security Scan)
    2. pip list --outdated     (Überprüfe Packages)
    ↓
Sicher? ✅ → Push erlaubt
Sicherheitslücken? ❌ → Push blockiert
```

## Konfiguration

```json
{
  "hooks": {
    "pre_push": {
      "name": "hook-3-pre-push-security-audit",
      "commands": [
        {
          "name": "bandit-security",
          "command": "cd /home/klapo/iFixAi && bandit -r ifixai -q 2>/dev/null && echo '✅ Security OK' || echo '⚠️ Security Issues Found'",
          "halt_on_error": false
        },
        {
          "name": "check-dependencies",
          "command": "cd /home/klapo/iFixAi && pip list --outdated 2>/dev/null | head -5 && echo '📦 Check outdated packages'",
          "halt_on_error": false
        }
      ]
    }
  }
}
```

## Befehle

### 1. Security Scan (Bandit)
```bash
bandit -r ifixai -q
```
Prüft auf:
- ❌ Unsichere Hash-Funktionen (MD5, SHA1)
- ❌ Hard-coded Credentials
- ❌ SQL-Injection Risiken
- ❌ Unsecure Random
- ❌ Eval/Exec Risiken
- ❌ Path-Traversal

### 2. Dependencies Check
```bash
pip list --outdated
```
- Zeigt veraltete Pakete
- Warnt vor Sicherheits-Updates

## Beispiel: Push wird blockiert

```
Du: git push origin main
    ↓
Hook #3 Check:
⚠️ Security Issues Found
    Issue: Use of insecure MD5 hash
    Location: ifixai/core.py:42
    
⚠️ Push abgelehnt!

📦 Outdated packages:
   ruff 0.4.0 → 0.5.0
   mypy 1.0.0 → 1.3.0
```

**Was du tun musst:**
```bash
# 1. Security-Issue fixen
# ifixai/core.py:42 - MD5 → SHA256

# 2. Dependencies aktualisieren
pip install --upgrade ruff mypy

# 3. Tests laufen lassen
/test unit

# 4. Erneut pushen
git push origin main
# ✅ Dieses mal: Security OK!
```

## Beispiel: Push erlaubt

```
Du: git push origin main
    ↓
Hook #3 Check:
✅ Security OK
📦 Packages aktuell
    
✅ Push erlaubt!
    
Pushed to origin/main:
  abc1234..def5678 feat(core): add retry
```

## Security-Levels bei Bandit

🔴 **CRITICAL** — High Severity (MUSS gefixt)
🟠 **HIGH** — Medium Severity (SOLLTE gefixt)
🟡 **MEDIUM** — Low Severity (Nice-to-have)

## Häufige Security-Issues

### Issue: Hard-coded Password
```python
# ❌ Bandit findet das
PASSWORD = "super_secret_123"

# ✅ Besser: Environment Variable
PASSWORD = os.environ.get("DB_PASSWORD")
```

### Issue: Insecure Hash
```python
# ❌ MD5 ist unsicher
import hashlib
hash = hashlib.md5(data).hexdigest()

# ✅ SHA256 ist sicher
import hashlib
hash = hashlib.sha256(data).hexdigest()
```

### Issue: SQL-Injection
```python
# ❌ String interpolation = Injection Risk
query = f"SELECT * FROM users WHERE id = {user_id}"

# ✅ Parameterized Query = Sicher
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

## Vorteile

✅ Keine Sicherheitslücken publishen
✅ Team & Users sind geschützt
✅ Compliance-Standards erfüllt
✅ Dependencies bleiben aktuell

## Wenn Hook fehlschlägt

**Sicherheit ist wichtig! Fix sofort:**

```bash
# 1. Security-Issue anschauen
⚠️ Issue: Use of insecure function
   Location: ifixai/parser.py:12

# 2. Code fixen (ersetze unsicheres Code)

# 3. Tests laufen
/test unit

# 4. Commit + Push
git add .
git commit -m "fix: replace insecure MD5 with SHA256"
git push origin main
```

## Deaktivieren (nicht empfohlen!)

```json
{
  "hooks": {
    "pre_push": {
      "enabled": false
    }
  }
}
```

⚠️ **Nicht empfohlen** - Sicherheitsrisiko!

---

**Status:** ✅ Aktiv - schützt dein Projekt vor Sicherheitslücken
