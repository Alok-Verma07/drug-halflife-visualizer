# 🔧 Backend — Flask API Server

This folder contains the Python Flask backend for the Drug Half-Life Visualizer.

---

## 📁 File Structure
backend/
├── app.py            ← Flask server with API routes
├── database.py       ← SQLite setup and drug data (51 drugs)
├── requirements.txt  ← Python dependencies
├── run.py            ← Entry point to start server
└── .gitignore        ← Ignores drugs.db and pycache

---

## ⚙️ Setup Instructions

**1. Install dependencies:**
```bash
pip install -r requirements.txt
```

**2. Start the server:**
```bash
python app.py
```

Server runs at `http://localhost:5000`

> On first run, `drugs.db` is automatically created and seeded with 51 drugs.

---

## 📡 API Routes

### `GET /api/drugs`
Returns a JSON list of all 51 drug names.
```json
["Amoxicillin", "Aspirin", "Atenolol", "Caffeine", ...]
```

---

### `GET /api/drug?name=Paracetamol`
Returns full pharmacokinetic data for one drug.
```json
{
  "name": "Paracetamol",
  "category": "Painkillers / NSAIDs",
  "route": "Oral",
  "description": "Fever and mild to moderate pain relief",
  "half_life": 2.5,
  "vd": 0.9,
  "cmax": 20.0,
  "t_min": 4.0,
  "t_max": 20.0,
  "toxic_level": 25.0
}
```

---

### `GET /api/drugs/category?name=Antibiotics`
Returns all drug names in a given category.
```json
["Amoxicillin", "Azithromycin", "Ciprofloxacin", ...]
```

**Available categories:**
- Painkillers / NSAIDs
- Antibiotics
- Diabetes / Metabolic
- Heart / Blood Pressure
- Respiratory
- Gastrointestinal
- Hormones / Steroids
- Neurological / Psych

---

## 🗄️ Database Schema

Table name: `drugs` — auto-generated as `drugs.db` on first run.

| Column | Type | Description |
|--------|------|-------------|
| name | TEXT | Drug name (primary key) |
| category | TEXT | Drug category group |
| route | TEXT | Administration route (Oral, IV, Inhalation) |
| description | TEXT | What the drug treats |
| half_life | REAL | Hours for concentration to halve |
| vd | REAL | Volume of distribution (L/kg) |
| cmax | REAL | Max concentration after standard dose |
| t_min | REAL | Minimum therapeutic concentration (mg/L) |
| t_max | REAL | Maximum therapeutic concentration (mg/L) |
| toxic_level | REAL | Concentration above which drug is dangerous |

---

## 🧪 Testing the API

Once the server is running, test these in your browser:
http://localhost:5000/api/drugs
http://localhost:5000/api/drug?name=Paracetamol
http://localhost:5000/api/drugs/category?name=Antibiotics

---

## 📦 Dependencies
flask
flask-cors
