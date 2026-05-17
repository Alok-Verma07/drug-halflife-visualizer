import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'drugs.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drugs (
            name TEXT PRIMARY KEY,
            category TEXT,
            route TEXT,
            description TEXT,
            half_life REAL,
            vd REAL,
            cmax REAL,
            t_min REAL,
            t_max REAL,
            toxic_level REAL
        )
    ''')

    cursor.execute("SELECT COUNT(*) FROM drugs")
    count = cursor.fetchone()[0]

    if count == 0:
        drugs = [
            # PAINKILLERS / NSAIDs
            ("Paracetamol",    "Painkillers / NSAIDs",      "Oral",       "Fever and mild to moderate pain relief",                    2.5,   0.9,   20,     4,      20,     25),
            ("Ibuprofen",      "Painkillers / NSAIDs",      "Oral",       "Anti-inflammatory, pain and fever",                         2.0,   0.15,  30,     10,     50,     100),
            ("Aspirin",        "Painkillers / NSAIDs",      "Oral",       "Pain relief and blood thinning",                            3.5,   0.17,  25,     15,     30,     50),
            ("Diclofenac",     "Painkillers / NSAIDs",      "Oral",       "Arthritis and post-surgical pain",                          1.2,   0.55,  3,      0.5,    2,      10),
            ("Naproxen",       "Painkillers / NSAIDs",      "Oral",       "Long-acting anti-inflammatory pain relief",                 14.0,  0.16,  50,     20,     80,     200),
            ("Tramadol",       "Painkillers / NSAIDs",      "Oral",       "Moderate to severe pain management",                        6.0,   2.7,   0.3,    0.1,    0.3,    1.0),
            ("Morphine",       "Painkillers / NSAIDs",      "IV",         "Severe pain and post-operative analgesia",                  3.0,   3.5,   0.1,    0.01,   0.1,    0.2),
            ("Codeine",        "Painkillers / NSAIDs",      "Oral",       "Mild to moderate pain and cough suppression",               3.0,   3.5,   0.06,   0.02,   0.24,   0.5),

            # ANTIBIOTICS
            ("Amoxicillin",    "Antibiotics",               "Oral",       "Bacterial infections: ear, chest, urinary",                 1.0,   0.3,   10,     2,      8,      20),
            ("Azithromycin",   "Antibiotics",               "Oral",       "Respiratory and skin bacterial infections",                 68.0,  31.0,  0.4,    0.1,    2,      5),
            ("Ciprofloxacin",  "Antibiotics",               "Oral",       "Urinary tract and gut bacterial infections",                4.0,   2.5,   2.5,    0.5,    4,      10),
            ("Doxycycline",    "Antibiotics",               "Oral",       "Acne, malaria prevention, respiratory infections",          18.0,  0.75,  3,      1,      4,      8),
            ("Metronidazole",  "Antibiotics",               "Oral",       "Anaerobic bacterial and parasitic infections",              8.0,   0.7,   10,     4,      8,      20),
            ("Clarithromycin", "Antibiotics",               "Oral",       "Respiratory tract and H. pylori infections",               5.0,   2.9,   2.5,    0.5,    4,      15),
            ("Vancomycin",     "Antibiotics",               "IV",         "Serious MRSA and resistant bacterial infections",           6.0,   0.7,   40,     10,     20,     80),

            # DIABETES / METABOLIC
            ("Metformin",      "Diabetes / Metabolic",      "Oral",       "Type 2 diabetes first-line treatment",                     6.5,   3.7,   2,      0.5,    2,      5),
            ("Glibenclamide",  "Diabetes / Metabolic",      "Oral",       "Type 2 diabetes insulin stimulation",                      10.0,  0.2,   0.3,    0.05,   0.2,    0.5),
            ("Sitagliptin",    "Diabetes / Metabolic",      "Oral",       "Type 2 diabetes DPP-4 inhibitor",                          12.0,  2.6,   0.8,    0.1,    1,      3),
            ("Insulin_Rapid",  "Diabetes / Metabolic",      "IV",         "Rapid blood sugar control in diabetes",                    0.5,   0.1,   80,     10,     60,     100),
            ("Insulin_Long",   "Diabetes / Metabolic",      "Topical",    "Basal insulin for overnight sugar control",                24.0,  0.1,   20,     5,      20,     40),
            ("Empagliflozin",  "Diabetes / Metabolic",      "Oral",       "Type 2 diabetes SGLT2 inhibitor",                          12.5,  1.7,   0.5,    0.05,   0.5,    2),

            # HEART / BLOOD PRESSURE
            ("Atenolol",       "Heart / Blood Pressure",    "Oral",       "High blood pressure and angina beta-blocker",              6.0,   0.7,   1.5,    0.2,    1,      3),
            ("Amlodipine",     "Heart / Blood Pressure",    "Oral",       "Hypertension and angina calcium channel blocker",          40.0,  21.0,  0.01,   0.003,  0.015,  0.05),
            ("Ramipril",       "Heart / Blood Pressure",    "Oral",       "Heart failure and blood pressure ACE inhibitor",           13.0,  0.56,  0.04,   0.005,  0.05,   0.2),
            ("Digoxin",        "Heart / Blood Pressure",    "Oral",       "Heart failure and atrial fibrillation",                    36.0,  7.0,   0.002,  0.0008, 0.002,  0.003),
            ("Furosemide",     "Heart / Blood Pressure",    "Oral",       "Fluid retention in heart failure and kidney disease",      2.0,   0.15,  3,      1,      5,      20),
            ("Warfarin",       "Heart / Blood Pressure",    "Oral",       "Blood clot prevention anticoagulant",                      40.0,  0.14,  2.5,    1,      3,      5),
            ("Simvastatin",    "Heart / Blood Pressure",    "Oral",       "Cholesterol reduction and heart disease prevention",       3.0,   2.8,   0.05,   0.001,  0.05,   0.5),
            ("Clopidogrel",    "Heart / Blood Pressure",    "Oral",       "Prevents clots after heart attack or stroke",              8.0,   5.5,   0.003,  0.001,  0.01,   0.05),

            # RESPIRATORY
            ("Salbutamol",     "Respiratory",               "Inhalation", "Asthma and COPD bronchodilator",                           4.0,   2.0,   0.03,   0.005,  0.05,   0.2),
            ("Montelukast",    "Respiratory",               "Oral",       "Asthma and allergic rhinitis prevention",                  4.0,   8.4,   0.5,    0.1,    0.5,    2),
            ("Theophylline",   "Respiratory",               "Oral",       "Asthma and COPD airway relaxation",                        8.0,   0.5,   15,     10,     20,     25),
            ("Budesonide",     "Respiratory",               "Inhalation", "Asthma inhaled corticosteroid",                            2.8,   3.0,   0.001,  0.0001, 0.001,  0.01),
            ("Ipratropium",    "Respiratory",               "Inhalation", "COPD bronchodilator anticholinergic",                      2.0,   4.6,   0.002,  0.0005, 0.003,  0.02),
            ("Oseltamivir",    "Respiratory",               "Oral",       "Influenza antiviral treatment",                            8.0,   0.36,  0.35,   0.1,    0.5,    2),

            # GASTROINTESTINAL
            ("Omeprazole",     "Gastrointestinal",          "Oral",       "Acid reflux and stomach ulcer treatment",                  1.0,   0.36,  0.8,    0.1,    1,      5),
            ("Domperidone",    "Gastrointestinal",          "Oral",       "Nausea, vomiting and gastric emptying",                    7.0,   5.7,   0.025,  0.005,  0.05,   0.5),
            ("Ondansetron",    "Gastrointestinal",          "Oral",       "Chemotherapy and post-surgery nausea",                     5.7,   1.9,   0.03,   0.01,   0.08,   0.5),
            ("Loperamide",     "Gastrointestinal",          "Oral",       "Diarrhoea and bowel motility control",                     10.0,  9.1,   0.002,  0.0005, 0.003,  0.02),
            ("Ranitidine",     "Gastrointestinal",          "Oral",       "Stomach acid reduction and ulcer healing",                 2.5,   1.4,   0.5,    0.1,    0.5,    3),

            # HORMONES / STEROIDS
            ("Prednisolone",   "Hormones / Steroids",       "Oral",       "Inflammation, allergies and autoimmune diseases",          3.5,   0.7,   0.15,   0.05,   0.2,    1),
            ("Hydrocortisone", "Hormones / Steroids",       "IV",         "Adrenal insufficiency and severe allergic reactions",      1.5,   0.45,  0.5,    0.1,    0.5,    2),
            ("Levothyroxine",  "Hormones / Steroids",       "Oral",       "Hypothyroidism thyroid hormone replacement",               168.0, 0.17,  0.02,   0.006,  0.018,  0.05),
            ("Estradiol",      "Hormones / Steroids",       "Oral",       "Menopause hormone replacement therapy",                    13.0,  1.2,   0.0005, 0.0001, 0.0004, 0.002),
            ("Testosterone",   "Hormones / Steroids",       "IV",         "Testosterone deficiency hormone replacement",              70.0,  1.0,   0.025,  0.01,   0.035,  0.1),

            # NEUROLOGICAL / PSYCH
            ("Diazepam",       "Neurological / Psych",      "Oral",       "Anxiety, seizures and muscle spasm",                       48.0,  1.1,   0.4,    0.1,    0.5,    2),
            ("Phenytoin",      "Neurological / Psych",      "Oral",       "Epileptic seizure prevention",                             22.0,  0.75,  15,     10,     20,     30),
            ("Lithium",        "Neurological / Psych",      "Oral",       "Bipolar disorder mood stabiliser",                         24.0,  0.7,   1.2,    0.6,    1.2,    1.5),
            ("Caffeine",       "Neurological / Psych",      "Oral",       "Stimulant - alertness and neonatal apnoea treatment",      5.0,   0.6,   5,      1,      10,     80),
            ("Sertraline",     "Neurological / Psych",      "Oral",       "Depression and anxiety SSRI antidepressant",               26.0,  20.0,  0.04,   0.01,   0.15,   1),
            ("Haloperidol",    "Neurological / Psych",      "Oral",       "Schizophrenia and psychosis antipsychotic",                24.0,  18.0,  0.02,   0.005,  0.02,   0.1),
        ]

        cursor.executemany('''
            INSERT INTO drugs (name, category, route, description, half_life, vd, cmax, t_min, t_max, toxic_level)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', drugs)

        conn.commit()
        print(f"Database seeded with {len(drugs)} drugs.")
    else:
        print(f"Database already has {count} drugs. Skipping seed.")

    conn.close()


def get_all_drugs():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM drugs ORDER BY name")
    drugs = [row["name"] for row in cursor.fetchall()]
    conn.close()
    return drugs


def get_drug(name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM drugs WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return dict(row)
    return None


def get_drugs_by_category(category):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM drugs WHERE category = ? ORDER BY name", (category,))
    drugs = [row["name"] for row in cursor.fetchall()]
    conn.close()
    return drugs


if __name__ == "__main__":
    init_db()
    print("\nTesting functions...")
    print("Total drugs:", len(get_all_drugs()))
    print("Paracetamol:", get_drug("Paracetamol"))
    print("Antibiotics:", get_drugs_by_category("Antibiotics"))
    print("\nAll done!")