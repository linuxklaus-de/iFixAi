---
name: code-analyzer
description: Code-Analyse – Komplexität, Coverage, Dependencies, Metriken
disable-model-invocation: true
---

# Code Analyzer Skill

Analysiere deinen Code auf Qualität, Komplexität und Abhängigkeiten.

## Verwendung

### Komplexität & Metriken
- `/analyze complexity` — Zyklomatische Komplexität
- `/analyze hotspots` — Am meisten genutzte Funktionen
- `/analyze large-functions` — Funktionen > 50 Zeilen
- `/analyze imports` — Import-Netzwerk

### Test-Coverage
- `/analyze coverage` — Test-Coverage Report
- `/analyze coverage --missing` — Welche Zeilen nicht getestet
- `/analyze coverage --threshold=80` — Min 80% fordern

### Dependencies
- `/analyze dependencies` — Dependency-Graph
- `/analyze dependencies --unused` — Ungenutzte Imports
- `/analyze dependencies --outdated` — Veraltete Pakete
- `/analyze dependencies --security` — Sicherheitslücken

### Code-Qualität
- `/analyze quality` — Alle Metriken
- `/analyze quality --detailed` — Detaillierter Report
- `/analyze quality --trend` — Trend über Zeit

## Komplexität erklärt (für Anfänger)

**Zyklomatische Komplexität** = Wie viele Pfade gibt es durch eine Funktion?

```python
# Komplexität = 1 (einfach)
def add(a, b):
    return a + b

# Komplexität = 3 (mittel)
def check(value):
    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    else:
        return "zero"

# Komplexität = 8+ (zu komplex!)
def validate(user):
    if user.age > 18:
        if user.email:
            if user.verified:
                if user.subscription:
                    # ... zu verschachtelt!
```

**Faustregel**: Komplexität sollte < 10 sein

## Test-Coverage erklärt

**Coverage** = Wie viel % deines Codes wird durch Tests geprüft?

```python
def divide(a, b):          # Line 1
    if b == 0:             # Line 2 - getestet? ✅
        return None        # Line 3 - getestet? ❌ (50% von Funktion)
    return a / b           # Line 4 - getestet? ✅

# Coverage: 75% (3 von 4 Linien getestet)
```

**Faustregel**: > 80% Coverage ist gut

## Beispiele

```bash
# Schneller Überblick
/analyze quality

# Komplexe Funktionen finden
/analyze complexity

# Wo fehlen Tests?
/analyze coverage --missing

# Welche Pakete sind veraltet?
/analyze dependencies --outdated

# Detaillierter Report
/analyze quality --detailed > report.txt
```

## Report-Beispiel

```
📊 CODE QUALITY ANALYSIS
========================

⚡ KOMPLEXITÄT
- Core Module: Avg 4.2 (✅ OK)
- CLI Module: Avg 6.1 (✅ OK)  
- API Module: Avg 12.3 (⚠️ HIGH - refactoring nötig)

🧪 TEST COVERAGE
- Gesamt: 82% (✅ Gut!)
- ifixai/core: 91% (✅ Sehr gut)
- ifixai/cli: 73% (⚠️ Could be better)

📦 DEPENDENCIES
- Total: 23 packages
- Outdated: 2 packages (pyyaml 6.0 → 6.1)
- Security Issues: 0 (✅ Safe)

📈 TRENDS
- Komplexität: ↓ (besser)
- Coverage: → (stabil)
- Dependencies: ↓ (leaner)
```

## Hotspots (für Anfänger)

**Hotspots** = Funktionen die oft genutzt werden und fehlerhaft sein können

```
🔥 TOP HOTSPOTS
1. runner.py:execute() - 156 calls - Komplexität 9
2. cli.py:main() - 89 calls - Komplexität 11
3. parser.py:parse() - 234 calls - Komplexität 6

→ Diese sollten best-tested & sauberst sein!
```

## Beste Praktiken

### Komplexität
- < 5: ✅ Einfach zu verstehen
- 5-10: ✅ OK, aber dokumentieren
- 10-15: ⚠️ Refactoring erwägen
- > 15: ❌ Muss vereinfacht werden

### Coverage
- > 85%: ✅ Exzellent
- 80-85%: ✅ Gut
- 70-80%: ⚠️ Akzeptabel
- < 70%: ❌ Zu niedrig

## Tipps für Anfänger

- Nutze `/analyze complexity` um problematische Code zu finden
- Nutze `/analyze coverage --missing` um Test-Lücken zu finden
- Hohe Komplexität = schwerer zu verstehen = mehr Bugs
- Gutes Coverage = sicherer Code = weniger Überraschungen
- Nutze Reports vor Release um Probleme zu finden
