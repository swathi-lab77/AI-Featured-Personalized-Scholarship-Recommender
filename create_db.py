import sqlite3

DATABASE = 'scholarships.db'

def add_columns():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    try:
        c.execute("ALTER TABLE scholarships ADD COLUMN age TEXT")
    except sqlite3.OperationalError:
        pass
    try:
        c.execute("ALTER TABLE scholarships ADD COLUMN class TEXT")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()

def create_and_populate_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS scholarships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            gender TEXT,
            stream TEXT,
            age TEXT,
            class TEXT,
            eligibility TEXT,
            documents TEXT,
            registration_link TEXT,
            last_date TEXT
        )
        ''')
        c.execute('DELETE FROM scholarships')
        data = [
            # Central & State scholarships (Merit-based/standard)
            ('National Scholarship Portal', 'OC', 'Boys', 'All', '16', 'Class 12', '10+2 or above', 'Aadhaar, Bank Passbook', 'https://scholarships.gov.in', '2025-12-31'),
            ('National Scholarship Portal', 'OC', 'Girls', 'All', '16', 'Class 12', '10+2 or above', 'Aadhaar, Bank Passbook', 'https://scholarships.gov.in', '2025-12-31'),
            ('National Scholarship Portal', 'OC', 'Boys', 'All', '>=17', 'Class 12 /PG/UG', '10+2 or above', 'Aadhaar, Bank Passbook', 'https://scholarships.gov.in', '2025-12-31'),
            ('National Scholarship Portal', 'OC', 'Girls', 'All', '>=17', 'Class 12/PG/UG', '10+2 or above', 'Aadhaar, Bank Passbook', 'https://scholarships.gov.in', '2025-12-31'),
            ( 'National Scholarship Portal', 'OC', 'Girls', 'Engineering', '>=18', 'PG/UG', '10+2 or above', 'Aadhaar, Bank Passbook', 'https://scholarships.gov.in', '2025-12-31'),
            ('National Scholarship Portal', 'OC', 'Boys', 'Engineering', '>=18', 'PG/UG', '10+2 or above', 'Aadhaar, Bank Passbook', 'https://scholarships.gov.in', '2025-12-31'),
             ('National Scholarship Portal', 'OC', 'Girls', 'Medical', '>=18', 'PG/UG', '10+2 or above', 'Aadhaar, Bank Passbook', 'https://scholarships.gov.in', '2025-12-31'),
              ('National Scholarship Portal', 'OC', 'Boys', 'Medical', '>=18', 'PG/UG', '10+2 or above', 'Aadhaar, Bank Passbook', 'https://scholarships.gov.in', '2025-12-31'),
            ('Post Matric SC Scholarship', 'SC', 'Boys', 'All', '<=17', 'Class 9/10/11/12', 'Belonging to SC category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric SC Scholarship', 'SC', 'Boys', 'Engineering', '>=18', 'UG/PG', 'Belonging to SC category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric SC Scholarship', 'SC', 'Boys', 'Medical', '>=18', 'UG/PG', 'Belonging to SC category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric SC Scholarship', 'SC', 'Girls', 'All', '<=17', 'Class 9/10/11/12', 'Belonging to SC category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric SC Scholarship', 'SC', 'Girls', 'Medical', '>=18', 'UG/PG', 'Belonging to SC category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric SC Scholarship', 'SC', 'Girls', 'Engineering', '>=18', 'UG/PG', 'Belonging to SC category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric ST Scholarship', 'ST', 'Boys', 'All', '<=17', 'Class 9/10/11/12', 'Belonging to ST category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
             ('Post Matric ST Scholarship', 'ST', 'Boys', 'Engineering', '>=18', 'UG/PG', 'Belonging to ST category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric ST Scholarship', 'ST', 'Boys', 'Medical', '>=18', 'UG/PG', 'Belonging to ST category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric ST Scholarship', 'ST', 'Girls', 'All', '<=17', 'Class 9/10/11/12', 'Belonging to ST category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric ST Scholarship', 'ST', 'Girls', 'Engineering', '>17', 'UG/PG', 'Belonging to ST category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Post Matric ST Scholarship', 'ST', 'Girls', 'Medical', '>17', 'UG/PG', 'Belonging to ST category', 'Caste Certificate, Income Certificate', 'https://scholarships.gov.in', '2025-12-15'),
            ('Merit-cum-Means Scholarship', 'MINOR', 'Boys', 'Professional', '20', 'Professional', 'Minority students with >50% marks', 'Income proof, ID', 'https://scholarships.gov.in', '2025-10-31'),
            ('Merit-cum-Means Scholarship', 'MINOR', 'Girls', 'Professional', '20', 'Professional', 'Minority students with >50% marks', 'Income proof, ID', 'https://scholarships.gov.in', '2025-10-31'),
            ('BC Scholarship', 'BC', 'Boys', 'All', '<=17', 'Class 11/12', 'Belonging to BC category', 'Caste Certificate, Income Proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('BC Scholarship', 'BC', 'Boys', 'Engineering', '>17', 'UG/PG', 'Belonging to BC category', 'Caste Certificate, Income Proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('BC Scholarship', 'BC', 'Boys', 'Medical', '>17', 'UG/PG', 'Belonging to BC category', 'Caste Certificate, Income Proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('BC Scholarship', 'BC', 'Girls', 'All', '<=17', 'Class 11/12', 'Belonging to BC category', 'Caste Certificate, Income Proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('BC Scholarship', 'BC', 'Girls', 'Engineering', '>17', 'UG/PG', 'Belonging to BC category', 'Caste Certificate, Income Proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('BC Scholarship', 'BC', 'Girls', 'Medical', '>17', 'UG/PG', 'Belonging to BC category', 'Caste Certificate, Income Proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('OC Scholarship', 'OC', 'Boys', 'All', '16', 'Class 12', 'Open category', 'ID proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('OC Scholarship', 'OC', 'Girls', 'All', '16', 'Class 12', 'Open category', 'ID proof', 'https://scholarships.gov.in', '2025-12-31'),
            # HDFC Parivartan ECSS Scholarship
            ('HDFC Parivartan ECSS Scholarship', 'MINOR', 'Boys', 'All', '15', 'Class 11', '>=55% in previous exam, family income <=2.5 lakh', 'Marksheet, ID proof, income proof, admission letter', 'https://www.parivartanecss.com', '2025-10-31'),
            ('HDFC Parivartan ECSS Scholarship', 'MINOR', 'Girls', 'All', '15', 'Class 11', '>=55% in previous exam, family income <=2.5 lakh', 'Marksheet, ID proof, income proof, admission letter', 'https://www.parivartanecss.com', '2025-10-31'),
            # SBI Platinum Jubilee Asha Scholarship
            ('SBI Asha Scholarship', 'OC', 'Boys', 'All', '18', 'Undergraduate', '>=75% marks or 7 CGPA, family income <=6 lakh', 'Marksheet, ID proof, income proof', 'https://www.sbiashascholarship.co.in', '2025-11-15'),
            ('SBI Asha Scholarship', 'OC', 'Girls', 'All', '18', 'Undergraduate', '>=75% marks or 7 CGPA, family income <=6 lakh', 'Marksheet, ID proof, income proof', 'https://www.sbiashascholarship.co.in', '2025-11-15'),
            # ePASS (example: Telangana and other state portals)
            ('ePASS Scholarship (Telangana)', 'BC', 'Boys', 'All', '18', 'UG/PG', 'Resident of Telangana, eligible caste, family income limits', 'Caste & income proof, Aadhaar, college admission letter', 'https://telanganaepass.cgg.gov.in/', '2025-12-31'),
            ('ePASS Scholarship (Telangana)', 'BC', 'Girls', 'All', '18', 'UG/PG', 'Resident of Telangana, eligible caste, family income limits', 'Caste & income proof, Aadhaar, college admission letter', 'https://telanganaepass.cgg.gov.in/', '2025-12-31'),
            # Sample merit-based state central government scholarships
            ('Central Merit Scholarship', 'OC', 'Boys', 'All', '17', 'Class 12', 'Merit based on board marks', 'Marksheet, ID proof, admission proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('Central Merit Scholarship', 'OC', 'Girls', 'All', '17', 'Class 12', 'Merit based on board marks', 'Marksheet, ID proof, admission proof', 'https://scholarships.gov.in', '2025-12-31'),
            ('State Merit Scholarship (Karnataka)', 'OC', 'Boys', 'All', '16', 'Class 10', 'Merit based, Karnataka resident', 'Marksheet, residence proof', 'https://ssp.postmatric.karnataka.gov.in', '2025-12-15'),
            ('State Merit Scholarship (Karnataka)', 'OC', 'Girls', 'All', '16', 'Class 10', 'Merit based, Karnataka resident', 'Marksheet, residence proof', 'https://ssp.postmatric.karnataka.gov.in', '2025-12-15')
        ]
        c.executemany('''
        INSERT INTO scholarships (name, category, gender, stream, age, class, eligibility, documents, registration_link, last_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()

if __name__ == '__main__':
    add_columns()
    create_and_populate_db()
