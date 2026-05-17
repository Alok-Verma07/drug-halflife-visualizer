# 🧬 Pharmacokinetics — Biology Concepts

This document explains the key biology concepts behind the Drug Half-Life & Dosage Visualizer.

---

## 1. What is Pharmacokinetics?

Pharmacokinetics (PK) is the study of how a drug moves through the body over time — how it is absorbed, distributed, metabolised, and eliminated. It answers the question: **"What does the body do to the drug?"**

---

## 2. Half-Life (t½)

**Definition:** The time it takes for the concentration of a drug in the bloodstream to reduce by half.

**Example:** Paracetamol has a half-life of 2.5 hours. If your blood concentration is 20 mg/L at time zero, it will be:
- 10 mg/L after 2.5 hours
- 5 mg/L after 5 hours
- 2.5 mg/L after 7.5 hours

**Why it matters:** A drug with a short half-life (e.g. Amoxicillin = 1 hour) needs to be taken more frequently than one with a long half-life (e.g. Diazepam = 48 hours).

---

## 3. First-Order Elimination Kinetics

Most drugs are eliminated from the body following **first-order kinetics** — meaning the rate of elimination is proportional to the current concentration.

This produces an **exponential decay curve:** C(t) = C₀ × e^(−0.693 × t / t½)
The higher the concentration, the faster the drug is eliminated — but the shape of the curve always remains exponential.

---

## 4. Volume of Distribution (Vd)

**Definition:** A theoretical measure of how widely a drug spreads throughout the body's tissues relative to blood plasma.

- **Low Vd** (e.g. 0.15 L/kg for Ibuprofen) → drug stays mostly in the bloodstream
- **High Vd** (e.g. 31 L/kg for Azithromycin) → drug spreads widely into body tissues

**Formula:** Vd = Dose / Initial Concentration
**Why it matters:** Vd directly affects the peak concentration after a dose. A higher Vd means lower peak blood concentration.

---

## 5. Therapeutic Window

**Definition:** The range of drug concentration in the blood that is both effective and safe.

| Zone | Meaning |
|------|---------|
| Below therapeutic minimum | Drug has no effect |
| Within therapeutic window | Drug works safely |
| Above toxic level | Drug causes harm |

**Example for Paracetamol:**
- Therapeutic minimum: 4 mg/L
- Therapeutic maximum: 20 mg/L
- Toxic level: 25 mg/L

---

## 6. Drug Accumulation (Multi-Dose Simulation)

When a drug is taken repeatedly before the previous dose is fully eliminated, concentrations **accumulate** in the bloodstream over time.

This is calculated by summing the contribution of each dose: C_total(t) = Σ (Dose / Vd) × e^(−0.693 × (t − i×interval) / t½)
**Why it matters:** Accumulation can push concentration above the toxic threshold — which is why dosing intervals matter clinically.

---

## 7. Key Drug Comparisons

| Drug | Half-life | Clinical Implication |
|------|-----------|---------------------|
| Paracetamol | 2.5 hours | Clears quickly, safe for frequent use |
| Diazepam | 48 hours | Stays in system for days, risk of accumulation |
| Amoxicillin | 1 hour | Must be taken every 8 hours to stay effective |
| Azithromycin | 68 hours | Once-daily dosing sufficient |
| Warfarin | 40 hours | Long-acting, careful monitoring needed |

---

## 8. Glossary

| Term | Definition |
|------|-----------|
| Pharmacokinetics | Study of drug movement through the body |
| Half-life (t½) | Time for blood concentration to halve |
| First-order kinetics | Elimination rate proportional to concentration |
| Volume of distribution (Vd) | How widely drug spreads in body tissues |
| Therapeutic window | Safe and effective concentration range |
| Toxic threshold | Concentration above which drug causes harm |
| Drug accumulation | Rise in baseline concentration with repeated doses |
| Cmax | Maximum concentration reached after a dose |
