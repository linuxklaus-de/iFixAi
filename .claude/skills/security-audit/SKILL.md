---
name: security-audit
description: Sicherheit prüfen – Bandit, Mypy, Dependencies, AI-Safety
disable-model-invocation: true
---

# Security Audit Skill

Prüfe deinen Code auf Sicherheitslücken & AI-Safety Standards.

## Verwendung

### Schnelle Audits
- `/audit` — Alle Audits laufen
- `/audit quick` — Nur bandit (1 Min)
- `/audit deep` — Alle Checks (5 Min)

### Spezifische Audits
- `/audit security` — Sicherheitslücken (bandit)
- `/audit types` — Type-Safety (mypy --strict)
- `/audit dependencies` — Veraltete Pakete
- `/audit compliance` — AI-Safety Standards
- `/audit secrets` — Nach Secrets scannen

### Reports
- `/audit report` — Kompletten Report
- `/audit report --json` — Als JSON (für CI)
- `/audit report --html` — Als HTML-Bericht

## Was wird geprüft

### Sicherheit (Bandit)
❌ Unsichere Hash-Funktionen
❌ SQL-Injection Risiken
❌ Unsichere Pickle/Shelve
❌ Hard-coded Credentials
❌ Unsecure Random
❌ Path-Traversal Risiken

### Type-Safety (mypy)
❌ Missing Type Hints
❌ Incompatible Types
❌ None-Value Issues
❌ Callable Type Errors

### Dependencies
❌ Veraltete Pakete
❌ Bekannte Vulnerabilities
❌ Incompatible Versionen

### AI-Safety Standards (iFixAi specific)
❌ Unsichere Provider-Configs
❌ Fehlende Error-Handling
❌ Logging von Secrets
❌ Unsafe Model Calls

## Beispiele

```bash
# Schneller Check vor Commit
/audit quick

# Deep-Audit vor Release
/audit deep --report

# Nur Security
/audit security

# JSON für CI/CD Pipeline
/audit report --json > security.json
```

## Severity Levels

🔴 **CRITICAL** — Muss sofort behoben werden
🟠 **HIGH** — Sollte vor Release behoben werden
🟡 **MEDIUM** — Sollte bald behoben werden
🟢 **LOW** — Nice-to-Have Verbesserungen

## Vor Release

Checklist vor Release:
```bash
/audit deep --report
# Alle CRITICAL/HIGH müssen grün sein!
```

## Tipps für Anfänger

- Nutze `/audit quick` oft (ist schnell)
- Nutze `/audit deep` vor Commits (sauberer Code)
- Nutze `/audit report` vor Releases
- Sicherheit = Qualität!
