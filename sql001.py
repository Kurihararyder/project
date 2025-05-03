import sqlite3
conn = sqlite3.connect("Hospital.db")
cursor = conn.cursor()
    
    # 病患資料表
cursor.execute("""CREATE TABLE IF NOT EXISTS patients (
        patient_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        birthday TEXT NOT NULL
    )"""
)
    
    # 檢驗數值
cursor.execute("""CREATE TABLE IF NOT EXISTS test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id TEXT NOT NULL,
    Glucose REAL,
    HbA1c REAL,
    Glupc REAL,
    Alb REAL,
    TP REAL,
    ASTGOT REAL,
    ASTGPT REAL,
    DBil REAL,
    ALP REAL,
    TBil REAL,
    UN REAL,
    CRE REAL,
    UA REAL,
    TCHO REAL,
    LDLC REAL,
    HDLC REAL,
    TG REAL,
    Hb REAL,
    Hct REAL,
    PLT REAL,
    WBC REAL,
    RBC REAL,
    hsCRP REAL,
    Alpha REAL,
    CEA REAL,
    CA125 REAL,
    CA199 REAL,
    test_id TEXT UNIQUE NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
)"""
)

    
conn.commit()
conn.close()
print("資料庫以新增完成")