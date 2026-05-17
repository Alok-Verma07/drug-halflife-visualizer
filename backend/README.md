# 🔧 Backend — Flask API Server

This folder contains the Python Flask backend for the Drug Half-Life Visualizer.

---

## 📁 File Structure
backend/
├── app.py            ← Flask server with API routes
├── database.py       ← SQLite setup and drug data
├── requirements.txt  ← Python dependencies
├── run.py            ← Entry point
└── .gitignore        ← Ignores drugs.db and cache

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

The server runs at `http://localhost:5000`

On first run, `drugs.db` is automatically created and seeded with 51 drugs.

---

## 📡 API Routes

### GET `/api/drugs`
Returns a list of all drug names.

**Example response:**
```json
["Amoxicillin", "Aspirin", "Atenolol", "Caffeine", ...]
```

---

### GET `/api/drug?name=Paracetamol`
Returns full pharmacokinetic data for one drug.

**Example response:**
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

### GET `/api/drugs/category?name=Antibiotics`
Returns all drug names in a given category.

**Available categories:**
- Painkillers / NSAIDs
- Antibiotics
- Diabetes / Metabolic
- Heart / Blood Pressure
- Respiratory
- Gastrointestinal
- Hormones / Steroids
- Neurological / Psych

**Example response:**
```json
["Amoxicillin", "Azithromycin", "Ciprofloxacin", ...]
```

---

## 🗄️ Database

The SQLite database (`drugs.db`) is auto-generated on first run from `database.py`.

**Table: `drugs`**

| Column | Type | Description |
|--------|------|-------------|
| name | TEXT | Drug name (primary key) |
| category | TEXT | Drug category |
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
