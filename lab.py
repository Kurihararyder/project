import sqlite3
import health

def main():
    while True:
        print("歡迎來到檢驗科資訊管理系統")
        print("=======================")
        print("1. 新增病患資料")
        print("2. 修改病患資料")
        print("3. 查詢病患資料")
        print("4. 新增檢驗資料")
        print("5. 修改檢驗資料")
        print("6. 刪除檢驗資料")
        print("7. 查詢檢驗資料")
        print("8. 檢驗報告健康風險評估系統")
        print("9. 離開系統")
        choice = input("請選擇操作：")
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            update_patient()
        elif choice == "3":
            see_patient()    
        elif choice == "4":
            add_test()
        elif choice == "5":
            update_test()
        elif choice == "6":
            delete_test()
        elif choice == "7":
            see_test()
        elif choice == "8":
            health.run()            
        elif choice == "9":
            print("感謝使用，再見！")
            break
        else:
            print("無效選項，請重新選擇。")

def Hospital_db():
    conn = sqlite3.connect("Hospital.db")
    cursor = conn.cursor()
    
    # 病患資料表
    cursor.execute("""CREATE TABLE IF NOT EXISTS patients (
        patient_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        birthday TEXT NOT NULL
    )""")
    
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

# 新增病患基本資料
def add_patient():
    print("新增病人資料")
    patient_id = input("病患身分證字號: ")
    
#檢查病患是否存在
    conn = sqlite3.connect("Hospital.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    if cursor.fetchone():
        print("此病患資料已存在。")
        conn.close()
        return
    else:
        name = input("病患姓名 : ")
        birthday = input("病患生日(YYYY-MM-DD) : ")

        cursor.execute("""INSERT INTO patients (patient_id, name , birthday)
        VALUES (?, ? ,?)""", (patient_id, name, birthday))
        
        conn.commit()
        conn.close()
        print("病患資料已新增！")

#修改病患基本資料
def update_patient():
    print("修改病患資料")
    patient_id = input("請輸入病患身分證字號: ")

    conn = sqlite3.connect("Hospital.db")
    cursor = conn.cursor()



    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    row = cursor.fetchone()

    if not row:
        print("查無此病患資料。")
    else:
        print(f"原本的姓名: {row[1]}，生日: {row[2]}")
        name = input("請輸入新的姓名: ")
        birthday = input("請輸入新的生日 (YYYY-MM-DD): ")
        cursor.execute("UPDATE patients SET name = ?, birthday = ? WHERE patient_id = ?", (name, birthday, patient_id))
        conn.commit()
        print("病患資料已修改！")
    
    conn.close()



#查看病患    
def see_patient():
    print("查詢病患資料")
    patient_id = input("請輸入病患身分證字號: ")

    conn = sqlite3.connect("Hospital.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    row = cursor.fetchone()

    if not row:
        print("查無此病人資料。")
    else:
        print(f"身分證字號: {row[0]}")
        print(f"姓名: {row[1]}")
        print(f"生日: {row[2]}")

    conn.close()

# 新增檢驗資料
def add_test():
    print("新增檢驗資料")
    patient_id = input("病患身份證字號 : ")

#檢查病患是否存在
    conn = sqlite3.connect("Hospital.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))

    if not cursor.fetchone():
        print("查無此病患，請先新增病患資料。")
        conn.close()
        return
    
    else:
        print("新增檢驗資料")
    patient_id = input("病患身分證字號: ")
    test_id = input("檢驗ID: ")

    # 輸入各項檢驗結果
    Glucose = float(input("請輸入空腹血糖 : "))
    HbA1c = float(input("請輸入糖化血色素 : "))
    Glupc = float(input("請輸入飯後血糖 : "))
    Alb = float(input("請輸入白蛋白 : "))
    TP = float(input("請輸入血清蛋白總量 : "))
    ASTGOT = float(input("請輸入天門冬胺酸轉胺酶 : "))
    ASTGPT = float(input("請輸入丙胺酸轉胺酶 : "))
    DBil = float(input("請輸入直接膽紅素 : "))
    ALP = float(input("請輸入鹼性磷酸酶 : "))
    TBil = float(input("請輸入總膽紅素 : "))
    UN = float(input("請輸入尿素氮 : "))
    CRE = float(input("請輸入肌酸酐 : "))
    UA = float(input("請輸入尿酸 : "))
    TCHO = float(input("請輸入總膽固醇 : "))
    LDLC = float(input("請輸入低密度脂蛋白 : "))
    HDLC = float(input("請輸入高密度脂蛋白 : "))
    TG = float(input("請輸入三酸甘油酯 : "))
    Hb = float(input("請輸入血色素 : "))
    Hct = float(input("請輸入血比容 : "))
    PLT = float(input("請輸入血小板 : "))
    WBC = float(input("請輸入白血球 : "))
    RBC = float(input("請輸入紅血球 : "))
    hsCRP = float(input("請輸入高敏感度C反應性蛋白 : "))
    Alpha = float(input("請輸入甲型胎兒蛋白 : "))
    CEA = float(input("請輸入癌胚胎抗原 : "))
    CA125 = float(input("請輸入癌症抗原125 : "))
    CA199 = float(input("請輸入癌症抗原19-9 : "))

    # 將資料寫入資料庫
    cursor.execute("""
        INSERT INTO test (patient_id, Glucose, HbA1c, Glupc, Alb, TP, ASTGOT, ASTGPT,DBil, ALP, TBil, UN, CRE, UA, TCHO, LDLC, HDLC, TG,Hb, Hct, PLT, WBC, RBC, hsCRP, Alpha, CEA, CA125, CA199,test_id) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, 
    (patient_id, Glucose, HbA1c, Glupc, Alb, TP, ASTGOT, ASTGPT,DBil, ALP, TBil, UN, CRE, UA, TCHO, LDLC, HDLC, TG,Hb, Hct, PLT, WBC, RBC, hsCRP, Alpha, CEA, CA125, CA199,test_id)

    )

    conn.commit()
    print("檢驗資料新增成功!!!")

# 查詢病患的檢驗資料
def see_test():
    print("查詢檢驗資料")
    test_id = input("請輸入檢驗ID : ")

    import sqlite3
    conn = sqlite3.connect("Hospital.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM test WHERE test_id = ?", (test_id,))

    if not cursor.fetchone():
        print("查無檢驗資料。")
        conn.close()
        return
    
    else:
        print("查詢檢驗資料")
    patient_id = input("病患ID: ")
    test_id = input("檢驗ID: ")
    cursor.execute("SELECT * FROM test WHERE test_id = ?", (test_id,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print("=" * 30)
            print(f"檢驗ID: {row[29]}")  # 檢驗ID
            print(f"空腹血糖 (Glucose): {row[2]}")
            print(f"糖化血色素 (HbA1c): {row[3]}")
            print(f"飯後血糖 (Glupc): {row[4]}")
            print(f"白蛋白 (Alb): {row[5]}")
            print(f"血清蛋白總量 (TP): {row[6]}")
            print(f"天門冬胺酸轉胺酶 (ASTGOT): {row[7]}")
            print(f"丙胺酸轉胺酶 (ASTGPT): {row[8]}")
            print(f"直接膽紅素 (DBil): {row[9]}")
            print(f"鹼性磷酸酶 (ALP): {row[10]}")
            print(f"總膽紅素 (TBil): {row[11]}")
            print(f"尿素氮 (UN): {row[12]}")
            print(f"肌酸酐 (CRE): {row[13]}")
            print(f"尿酸 (UA): {row[14]}")
            print(f"總膽固醇 (TCHO): {row[15]}")
            print(f"低密度脂蛋白 (LDLC): {row[16]}")
            print(f"高密度脂蛋白 (HDLC): {row[17]}")
            print(f"三酸甘油酯 (TG): {row[18]}")
            print(f"血色素 (Hb): {row[19]}")
            print(f"血比容 (Hct): {row[20]}")
            print(f"血小板 (PLT): {row[21]}")
            print(f"白血球 (WBC): {row[22]}")
            print(f"紅血球 (RBC): {row[23]}")
            print(f"高敏感度C反應性蛋白 (hsCRP): {row[24]}")
            print(f"甲型胎兒蛋白 (Alpha): {row[25]}")
            print(f"癌胚胎抗原 (CEA): {row[26]}")
            print(f"癌症抗原125 (CA125): {row[27]}")
            print(f"癌症抗原19-9 (CA199): {row[28]}")
    else:
        print("查無此病患檢驗資料。")

    conn.close()
   
    
# 修改檢驗資料
def update_test():
    print("修改檢驗資料")
    test_id = input("請輸入要修改的檢驗ID: ")

#檢查檢驗ID是否存在
    import sqlite3
    conn = sqlite3.connect("Hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test WHERE test_id = ?", (test_id,))
    row = cursor.fetchone()
    if not row:
        print("查無此檢驗資料。")
        conn.close()
        return
    else:
        # 修改檢驗資料

        print("請重新輸入此筆檢驗的所有資料：")
        patient_id = input("病患患ID: ")
        Glucose = float(input("請輸入空腹血糖 : "))
        HbA1c = float(input("請輸入糖化血色素 : "))
        Glupc = float(input("請輸入飯後血糖 : "))
        Alb = float(input("請輸入白蛋白 : "))
        TP = float(input("請輸入血清蛋白總量 : "))
        ASTGOT = float(input("請輸入天門冬胺酸轉胺酶 : "))
        ASTGPT = float(input("請輸入丙胺酸轉胺酶 : "))
        DBil = float(input("請輸入直接膽紅素 : "))
        ALP = float(input("請輸入鹼性磷酸酶 : "))
        TBil = float(input("請輸入總膽紅素 : "))
        UN = float(input("請輸入尿素氮 : "))
        CRE = float(input("請輸入肌酸酐 : "))
        UA = float(input("請輸入尿酸 : "))
        TCHO = float(input("請輸入總膽固醇 : "))
        LDLC = float(input("請輸入低密度脂蛋白 : "))
        HDLC = float(input("請輸入高密度脂蛋白 : "))
        TG = float(input("請輸入三酸甘油酯 : "))
        Hb = float(input("請輸入血色素 : "))
        Hct = float(input("請輸入血比容 : "))
        PLT = float(input("請輸入血小板 : "))
        WBC = float(input("請輸入白血球 : "))
        RBC = float(input("請輸入紅血球 : "))
        hsCRP = float(input("請輸入高敏感度C反應性蛋白 : "))
        Alpha = float(input("請輸入甲型胎兒蛋白 : "))
        CEA = float(input("請輸入癌胚胎抗原 : "))
        CA125 = float(input("請輸入癌症抗原125 : "))
        CA199 = float(input("請輸入癌症抗原19-9 : "))

        cursor.execute("""
            UPDATE test SET
                patient_id=?, Glucose=?, HbA1c=?, Glupc=?, Alb=?, TP=?, ASTGOT=?, ASTGPT=?,
                DBil=?, ALP=?, TBil=?, UN=?, CRE=?, UA=?, TCHO=?, LDLC=?, HDLC=?, TG=?,
                Hb=?, Hct=?, PLT=?, WBC=?, RBC=?, hsCRP=?, Alpha=?, CEA=?, CA125=?, CA199=?
            WHERE test_id = ?
        """, (
            patient_id, Glucose, HbA1c, Glupc, Alb, TP, ASTGOT, ASTGPT,DBil, ALP, TBil, UN, CRE, UA, TCHO, LDLC, HDLC, TG,Hb, Hct, PLT, WBC, RBC, hsCRP, Alpha, CEA, CA125, CA199,test_id
            )
        )

        conn.commit()
        print("檢驗資料修改成功！")






# 刪除檢驗資料
def delete_test():
    print("刪除檢驗資料")
    patient_id = input("請輸入病患身分證字號 : ")

    conn = sqlite3.connect("Hospital.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM test WHERE patient_id = ?", (patient_id,))
    rows = cursor.fetchall()
    
    if not rows:
        print("查無此病患檢驗資料。")
        conn.close()
        return

    test_id = input("請輸入檢驗ID : ")

    cursor.execute("SELECT * FROM test WHERE patient_id = ? AND test_id = ?", (patient_id, test_id))
    row = cursor.fetchone()

    if not row:
        print("此檢驗ID不存在。")
        conn.close()
        return

    cursor.execute("DELETE FROM test WHERE patient_id = ? AND test_id = ?", (patient_id, test_id))
    conn.commit()
    conn.close()
    print("檢驗資料已刪除！")

#啟動程式
if __name__ == "__main__":
    Hospital_db()
    main()
