# 💊 Drug Half-Life & Dosage Visualizer

A Biology + IT project that visualizes how drugs move through the human body over time using real pharmacokinetic equations.

---

## 🔬 What It Does

Users select a medicine, enter a dose (mg) and body weight (kg). The app calculates and animates how drug concentration rises and falls in the bloodstream over 48 hours.

The graph shows:
- 🟢 **Green band** → Therapeutic window (safe & effective range)
- 🔴 **Red line** → Toxic threshold (dangerous level)
- 🔵 **Blue curve** → Single dose concentration over time
- 🟠 **Orange dashed curve** → Multi-dose accumulation simulation

---

## 🧬 The Biology Behind It

Drugs are eliminated from the body following **first-order kinetics** — concentration drops exponentially over time. The rate depends on the drug's **half-life**.

**Core Formula:**
C(t) = (Dose / Vd) × e^(−0.693 × t / half_life)

| Term | Meaning |
|------|---------|
| C(t) | Drug concentration at time t (mg/L) |
| Dose | Amount taken in mg |
| Vd | Volume of distribution (L/kg × body weight) |
| half_life | Drug-specific constant in hours |
| t | Time in hours |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript |
| Charts | Chart.js |
| Backend | Python + Flask |
| Database | SQLite (51 drugs) |

---

## 🚀 How To Run

**1. Clone the repo:**
```bash
git clone https://github.com/Alok-Verma07/drug-halflife-visualizer.git
cd drug-halflife-visualizer
```

**2. Install dependencies:**
```bash
cd backend
pip install -r requirements.txt
```

**3. Start the server:**
```bash
python app.py
```

**4. Open the app:**

Open `templates/index.html` in your browser.

---

## 📡 API Routes

| Route | Description |
|-------|-------------|
| `GET /api/drugs` | Returns all 51 drug names |
| `GET /api/drug?name=Paracetamol` | Returns full PK data for one drug |
| `GET /api/drugs/category?name=Antibiotics` | Returns drugs by category |

---

## 👥 Team — BIT Biology Project

| Person | Role |
|--------|------|
| Person 1A | Database & Drug Data |
| Person 1B | Flask API Server |
| Person 2 | Pharmacokinetic Graph & Math |
| Person 3 | Frontend UI & Dashboard |
| Person 4 | Presentation, Biology Content & GitHub |
