def run():

    print("檢驗報告健康風險評估系統")    
    print("")
    print("1. 糖尿病檢查")
    print("2. 一般檢驗檢查(男性)")
    print("3. 一般檢驗檢查(女性)")
    print("4. 甲狀腺功能檢查")
    print("5. 心臟血管與血脂肪檢查")
    print("6. 一般檢查(從資料庫取得)")

    choice = int(input("請輸入要健康風險評估的項目"))

    if choice ==1:
        Glucose = float(input("請輸入空腹血糖 : "))
        Glucose2 = float(input("請輸入空腹後2小時候的空腹血糖 : "))
        HbA1c = float(input("請輸入糖化血色素 : "))
        insulin = float(input("請輸入胰島素數值 : "))
        Cpeptide0 = float(input("請輸入胰島素連結胜肽(0分鐘)的數值 : "))


        if Glucose == -1:
            print("空腹血糖：未檢查")
        elif 70 <= Glucose <= 100:
            print("空腹血糖：正常")
        elif Glucose < 70:
            print("空腹血糖：可能有低血糖風險")
        else:
            print("空腹血糖：可能有糖尿病風險")

        if Glucose2 == -1:
            print("飯後兩小時血糖：未檢查")
        elif Glucose2 < 140:
            print("飯後兩小時血糖：正常")
        else:
            print("飯後兩小時血糖：可能有糖尿病風險")
        
        if HbA1c == -1:
            print("糖化血色素：未檢查")
        elif 4.0 <= HbA1c <= 6.0:
            print("糖化血色素：正常")
        else:
            print("糖化血色素：異常值需注意糖尿病風險")

        if insulin == -1:
            print("胰島素：未檢查")
        elif insulin < 28.8:
            print("胰島素：正常")
        else:
            print("胰島素：異常，可能有胰島素阻抗")

        if Cpeptide0 == -1:
            print("胰島素連結胜肽(0分鐘)：未檢查")
        elif 0.78 <= Cpeptide0 <= 5.19:
            print("胰島素連結胜肽(0分鐘)：正常")
        else:
            print("胰島素連結胜肽(0分鐘)：異常，可能有胰島功能異常")
        
        print("（提醒：目前的數值分析只是標準值判定，醫生診斷為準）")

    elif choice == 2:
        print("請依序輸入以下檢驗數值(男性) : ")

        Glucose = float(input("請輸入空腹血糖 : "))
        HbA1c = float(input("請輸入糖化血色素 : "))
        Glupc = float(input("請輸入飯後血糖 : "))
        Alb = float(input("請輸入白蛋白 : "))
        TP = float(input("請輸入血清蛋白總量 : "))
        ASTGOT = float(input("請輸入天門冬胺酸轉胺酶 : "))
        ASTGPT = float(input("請輸入丙胺酸轉胺酶 : "))
        DBil = float(input("請輸入直接膽紅素 : "))
        ALP = float(input("請輸入鹼性磷酸酶 :"))
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

        if Glucose == -1 :
            print("空腹血糖：未檢查")
        elif 70 <= Glucose <= 100 :
            print("空腹血糖：正常")
        else:
            print("空腹血糖：異常")

        if HbA1c == -1 :
            print("糖化血色素：未檢查")
        elif 4.0 <= HbA1c <= 6.0 :
            print("糖化血色素：正常")
        else:
            print("糖化血色素：異常")

        if Glupc == -1 :
            print("飯後血糖：未檢查")
        elif Glupc < 140  :
            print("飯後血糖：正常")
        else:
            print("飯後血糖：異常")

        if Alb == -1 :
            print("白蛋白：未檢查")
        elif 3.5 <= Alb <= 5.7 :
            print("白蛋白：正常")
        else:
            print("白蛋白：異常")

        if TP == -1 :
            print("血清蛋白總量：未檢查")
        elif 6.4 <= TP <= 8.9:
            print("血清蛋白總量：正常")
        else:
            print("血清蛋白總量：異常")

        if ASTGOT == -1:
            print("天門冬胺酸轉胺酶(肝功能指數）：未檢查")
        elif 8 <= ASTGOT <= 31:
            print("天門冬胺酸轉胺酶(肝功能指數）：正常")
        else:
            print("天門冬胺酸轉胺酶(肝功能指數）：異常")

        if ASTGPT == -1:
            print("丙胺酸轉胺酶(肝功能指數)：未檢查")
        elif 0 <= ASTGPT <= 41:
            print("丙胺酸轉胺酶(肝功能指數)：正常")
        else:
            print("丙胺酸轉胺酶(肝功能指數)：異常")

        if DBil == -1 :
            print("直接膽紅素：未檢查")
        elif 0.03 <= DBil <= 0.18 :
            print("直接膽紅素：正常")
        else:
            print("直接膽紅素：異常")

        if ALP == -1:
            print("鹼性磷酸酶：未檢查")
        elif 34 <= ALP <= 104:
            print("鹼性磷酸酶：正常")
        else:
            print("鹼性磷酸酶：異常")

        if TBil == -1:
            print("總膽紅素：未檢查")
        elif 0.3 <= TBil <= 1.0:
            print("總膽紅素：正常")
        else:
            print("總膽紅素：異常")

        if UN == -1:
            print("尿素氮：未檢查")
        elif 7 <= UN <= 25:
            print("尿素氮：正常")
        else:
            print("尿素氮：異常")

        if CRE == -1:
            print("肌酸酐：未檢查")
        elif 0.6 <= CRE <= 1.3:
            print("肌酸酐：正常")
        else:
            print("肌酸酐：異常")

        if UA == -1:
            print("尿酸：未檢查")
        elif 4.4 <= UA <= 7.6:
            print("尿酸：正常")
        else:
            print("尿酸：異常")

        if TCHO == -1:
            print("總膽固醇：未檢查")
        elif TCHO < 200:
            print("總膽固醇：正常")
        else:
            print("總膽固醇：異常")

        if LDLC == -1:
            print("低密度脂蛋白：未檢查")
        elif LDLC < 130:
            print("低密度脂蛋白：正常")
        else:
            print("低密度脂蛋白：異常")

        if HDLC == -1:
            print("高密度脂蛋白：未檢查")
        elif HDLC > 40:
            print("高密度脂蛋白：正常")
        else:
            print("高密度脂蛋白：異常")

        if TG == -1:
            print("三酸甘油酯：未檢查")
        elif TG < 150:
            print("三酸甘油酯：正常")
        else:
            print("三酸甘油酯：異常")

        if Hb == -1:
            print("血色素：未檢查")
        elif 13.1 <= Hb <= 17.2:
            print("血色素：正常")
        else:
            print("血色素：異常")

        if Hct == -1:
            print("血比容：未檢查")
        elif 39.6 <= Hct <= 51.5:
            print("血比容：正常")
        else:
            print("血比容：異常")

        if PLT == -1:
            print("血小板：未檢查")
        elif 150 <= PLT <= 378:
            print("血小板：正常")
        else:
            print("血小板：異常")

        if WBC == -1:
            print("白血球：未檢查")
        elif 3.25 <= WBC <= 9.16:
            print("白血球：正常")
        else:
            print("白血球：異常")

        if RBC == -1:
            print("紅血球：未檢查")
        elif 4.21 <= RBC <= 5.9:
            print("紅血球：正常")
        else:
            print("紅血球：異常")

        if hsCRP == -1:
            print("高敏感度C反應性蛋白 : 未檢查")
        elif hsCRP < 0.1:
            print("高敏感度C反應性蛋白 : 低等風險")
        elif 0.1 <= hsCRP <= 0.3:
            print("高敏感度C反應性蛋白 : 中等風險")
        else:
            print("高敏感度C反應性蛋白 : 高等風險")

        if Alpha == -1:
            print("甲型胎兒蛋白：未檢查")
        elif Alpha < 20:
            print("甲型胎兒蛋白：正常")
        else:
            print("甲型胎兒蛋白：異常，注意肝硬化或肝癌風險")

        if CEA == -1:
            print("癌胚胎抗原：未檢查")
        elif CEA < 5.0:
            print("癌胚胎抗原：正常")
        else:
            print("癌胚胎抗原：異常")

        if CA125 == -1:
            print("癌症抗原125 未檢查")
        elif CA125 < 35:
            print("癌症抗原125 : 正常")
        else:
            print("癌症抗原125 : 異常")

        if CA199 == -1:
            print("癌症抗原19-9 : 未檢查")
        elif CA199 < 37:
            print("癌症抗原19-9 : 正常")
        else:
            print("癌症抗原19-9 : 異常")

    elif choice == 3:
        print("請依序輸入以下檢驗數值（女性）：")

        Glucose = float(input("請輸入空腹血糖 : "))
        HbA1c = float(input("請輸入糖化血色素 : "))
        Glupc = float(input("請輸入飯後血糖 : "))
        Alb = float(input("請輸入白蛋白 : "))
        TP = float(input("請輸入血清蛋白總量 : "))
        ASTGOT = float(input("請輸入天門冬胺酸轉胺酶 : "))
        ASTGPT = float(input("請輸入丙胺酸轉胺酶 : "))
        DBil = float(input("請輸入直接膽紅素 : "))
        ALP = float(input("請輸入鹼性磷酸酶 :"))
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

        if Glucose == -1 :
            print("空腹血糖：未檢查")
        elif 70 <= Glucose <= 100 :
            print("空腹血糖：正常")
        else:
            print("空腹血糖：異常")

        if HbA1c == -1 :
            print("糖化血色素：未檢查")
        elif 4.0 <= HbA1c <= 6.0 :
            print("糖化血色素：正常")
        else:
            print("糖化血色素：異常")

        if Glupc == -1 :
            print("飯後血糖：未檢查")
        elif Glupc < 140  :
            print("飯後血糖：正常")
        else:
            print("飯後血糖：異常")

        if Alb == -1 :
            print("白蛋白：未檢查")
        elif 3.5 <= Alb <= 5.7 :
            print("白蛋白：正常")
        else:
            print("白蛋白：異常")

        if TP == -1 :
            print("血清蛋白總量：未檢查")
        elif 6.4 <= TP <= 8.9:
            print("血清蛋白總量：正常")
        else:
            print("血清蛋白總量：異常")

        if ASTGOT == -1:
            print("天門冬胺酸轉胺酶(肝功能指數）：未檢查")
        elif 8 <= ASTGOT <= 31:
            print("天門冬胺酸轉胺酶(肝功能指數）：正常")
        else:
            print("天門冬胺酸轉胺酶(肝功能指數）：異常")

        if ASTGPT == -1:
            print("丙胺酸轉胺酶(肝功能指數)：未檢查")
        elif 0 <= ASTGPT <= 41:
            print("丙胺酸轉胺酶(肝功能指數)：正常")
        else:
            print("丙胺酸轉胺酶(肝功能指數)：異常")

        if DBil == -1:
            print("直接膽紅素：未檢查")
        elif 0.03 <= DBil <= 0.18:
            print("直接膽紅素：正常")
        else:
            print("直接膽紅素：異常")

        if ALP == -1:
            print("鹼性磷酸酶：未檢查")
        elif 34 <= ALP <= 104:
            print("鹼性磷酸酶：正常")
        else:
            print("鹼性磷酸酶：異常")

        if TBil == -1:
            print("總膽紅素：未檢查")
        elif 0.3 <= TBil <= 1.0:
            print("總膽紅素：正常")
        else:
            print("總膽紅素：異常")

        if UN == -1:
            print("尿素氮：未檢查")
        elif 7 <= UN <= 25:
            print("尿素氮：正常")
        else:
            print("尿素氮：異常")

        if CRE == -1:
            print("肌酸酐：未檢查")
        elif 0.6 <= CRE <= 1.3:
            print("肌酸酐：正常")
        else:
            print("肌酸酐：異常")

        if UA == -1:
            print("尿酸：未檢查")
        elif 2.3 <= UA <= 6.6:
            print("尿酸：正常")
        else:
            print("尿酸：異常")

        if TCHO == -1:
            print("總膽固醇：未檢查")
        elif TCHO < 200:
            print("總膽固醇：正常")
        else:
            print("總膽固醇：異常")

        if LDLC == -1:
            print("低密度脂蛋白：未檢查")
        elif LDLC < 130:
            print("低密度脂蛋白：正常")
        else:
            print("低密度脂蛋白：異常")

        if HDLC == -1:
            print("高密度脂蛋白：未檢查")
        elif HDLC > 40:
            print("高密度脂蛋白：正常")
        else:
            print("高密度脂蛋白：異常")

        if TG == -1:
            print("三酸甘油酯：未檢查")
        elif TG < 150:
            print("三酸甘油酯：正常")
        else:
            print("三酸甘油酯：異常")

        if Hb == -1:
            print("血色素：未檢查")
        elif 11.0 <= Hb <= 15.2:
            print("血色素：正常")
        else:
            print("血色素：異常")

        if Hct == -1:
            print("血比容：未檢查")
        elif 34.8 <= Hct <= 46.3:
            print("血比容：正常")
        else:
            print("血比容：異常")

        if PLT == -1:
            print("血小板：未檢查")
        elif 150 <= PLT <= 378:
            print("血小板：正常")
        else:
            print("血小板：異常")

        if WBC == -1:
            print("白血球：未檢查")
        elif 3.25 <= WBC <= 9.16:
            print("白血球：正常")
        else:
            print("白血球：異常")

        if RBC == -1:
            print("紅血球：未檢查")
        elif 3.78 <= RBC <= 5.25 :
            print("紅血球：正常")
        else:
            print("紅血球：異常")

        if hsCRP == -1:
            print("高敏感度C反應性蛋白 : 未檢查")
        elif hsCRP < 0.1:
            print("高敏感度C反應性蛋白 : 低等風險")
        elif 0.1 <= hsCRP <= 0.3:
            print("高敏感度C反應性蛋白 : 中等風險")
        else:
            print("高敏感度C反應性蛋白 : 高等風險")

        if Alpha == -1:
            print("甲型胎兒蛋白：未檢查")
        elif Alpha < 20:
            print("甲型胎兒蛋白：正常")
        else:
            print("甲型胎兒蛋白：異常，注意肝硬化或肝癌風險")

        if CEA == -1:
            print("癌胚胎抗原：未檢查")
        elif CEA < 5.0:
            print("癌胚胎抗原：正常")
        else:
            print("癌胚胎抗原：異常")

        if CA125 == -1:
            print("癌症抗原125 : 未檢查")
        elif CA125 < 35:
            print("癌症抗原125 : 正常")
        else:
            print("癌症抗原125 : 異常")

        if CA199 == -1:
            print("癌症抗原19-9 : 未檢查")
        elif CA199 < 37:
            print("癌症抗原19-9 : 正常")
        else:
            print("癌症抗原19-9 : 異常")


    elif choice == 4 :
        T3 = float(input("請輸入三碘甲狀腺素 : "))
        T4 = float(input("請輸入四碘甲狀腺素 : "))
        TSHRIA = float(input("請輸入甲狀腺刺激素 : "))
        FreeT4RIA = float(input("請輸入游離甲狀腺素 : "))
        FreeT4CIA = float(input("請輸入游離型甲狀腺素 : "))


        if T3 == -1:
            print("三碘甲狀腺素 : 未檢查")
        elif  78.0 <= T3 <=182.0:
            print("三碘甲狀腺素 : 正常")
        else:
            print("三碘甲狀腺素 : 異常")

        if T4 ==-1:
            print("四碘甲狀腺素 : 未檢查")    
        elif 4.6 <= T4 <= 12.4:
            print("四碘甲狀腺素 : 正常")
        else:
            print("四碘甲狀腺素 : 異常")    

        if TSHRIA==-1:
            print("甲狀腺刺激素 : 未檢查")
        elif 0.17 <= TSHRIA <= 4.05:
            print("甲狀腺刺激素 : 正常")
        else:
            print("甲狀腺刺激素 : 異常")
        if FreeT4RIA==-1:
            print("游離甲狀腺素 : 未檢查")
        elif 0.89 <= FreeT4RIA <= 1.79:
            print("游離甲狀腺素 : 正常")
        else:
            print("游離甲狀腺素 : 異常")

        if FreeT4CIA==-1:
            print("游離型甲狀腺素 : 未檢查")
        elif 0.7 <= FreeT4CIA <= 1.48:
            print("游離型甲狀腺素 : 正常")
        else:
            print("游離型甲狀腺素 : 異常")

    elif choice == 5:
        Triglyceride = float(input("請輸入三酸甘油酯 : "))
        TotalCholesterol = float(input("請輸入總膽固醇 : "))
        HDLCholesterol = float(input("請輸入高密度脂蛋白膽固醇（好的） : "))
        LDLCholesterol = float(input("請輸入低密度脂蛋白膽固醇（壞的） : "))
        CK = float(input("請輸入肌酸磷酸酶: "))
        ...


        if Triglyceride == -1:
            print("三酸甘油酯 : 未檢查")
        elif  Triglyceride <150:
            print("三酸甘油酯 : 正常")
        else:
            print("三酸甘油酯 : 異常")

        if TotalCholesterol ==-1:
            print("總膽固醇 : 未檢查")    
        elif TotalCholesterol <200:
            print("總膽固醇 : 正常")
        else:
            print("總膽固醇 : 異常")    

        if HDLCholesterol==-1:
            print("高密度脂蛋白膽固醇（好的） : 未檢查")
        elif HDLCholesterol >40:
            print("高密度脂蛋白膽固醇（好的） : 正常")
        else:
            print("高密度脂蛋白膽固醇（好的） : 異常")
        if LDLCholesterol==-1:
            print("低密度脂蛋白膽固醇（壞的） : 未檢查")
        elif LDLCholesterol <130:
            print("低密度脂蛋白膽固醇（壞的） : 正常")
        else:
            print("低密度脂蛋白膽固醇（壞的） : 異常")

        if CK==-1:
            print("肌酸磷酸酶 : 未檢查")
        elif 30 <= CK <= 223:
            print("肌酸磷酸酶 : 正常")
        else:
            print("肌酸磷酸酶 : 異常")


    elif choice ==6 :
            print("1.男性")      
            print("2.女性")
            sex=input("請選擇性別 : ")    
            if sex == '1':  
                print("查詢檢驗資料")
                test_id = input("請輸入檢驗ID: ")
                import sqlite3
                conn = sqlite3.connect("Hospital.db")
                conn.row_factory = sqlite3.Row  
                cursor = conn.cursor()
                
                cursor.execute("SELECT * FROM test WHERE test_id = ?", (test_id,))
                row = cursor.fetchone()
                
                if row:
                    
                    Glucose = row['Glucose']
                    HbA1c = row['HbA1c']
                    Glupc = row['Glupc']
                    Alb = row['Alb']
                    TP = row['TP']
                    ASTGOT = row['ASTGOT']
                    ASTGPT = row['ASTGPT']
                    DBil = row['DBil']
                    ALP = row['ALP']
                    TBil = row['TBil']
                    UN = row['UN']
                    CRE = row['CRE']
                    UA = row['UA']
                    TCHO = row['TCHO']
                    LDLC = row['LDLC']
                    HDLC = row['HDLC']
                    TG = row['TG']
                    Hb = row['Hb']
                    Hct = row['Hct']
                    PLT = row['PLT']
                    WBC = row['WBC']
                    RBC = row['RBC']
                    hsCRP = row['hsCRP']
                    Alpha = row['Alpha']
                    CEA = row['CEA']
                    CA125 = row['CA125']
                    CA199 = row['CA199']




                    print("=" * 30)
                    print(f"檢驗ID: {row['test_id']}")
                    print(f"病患ID: {row['patient_id']}")
                    print(f"空腹血糖 : {Glucose}")
                    print(f"糖化血色素 : {HbA1c}")
                    print(f"飯後血糖 : {Glupc}")
                    print(f"白蛋白 : {Alb}")
                    print(f"血清蛋白總量 : {TP}")
                    print(f"天門冬胺酸轉胺酶 : {ASTGOT}")
                    print(f"丙胺酸轉胺酶 : {ASTGPT}")
                    print(f"直接膽紅素 : {DBil}")
                    print(f"鹼性磷酸酶 : {ALP}")
                    print(f"總膽紅素 : {TBil}")
                    print(f"尿素氮 : {UN}")
                    print(f"肌酸酐 : {CRE}")
                    print(f"尿酸 : {UA}")
                    print(f"總膽固醇 : {TCHO}")
                    print(f"低密度脂蛋白 : {LDLC}")
                    print(f"高密度脂蛋白 : {HDLC}")
                    print(f"三酸甘油酯 : {TG}")
                    print(f"血色素 : {Hb}")
                    print(f"血比容 : {Hct}")
                    print(f"血小板 : {PLT}")
                    print(f"白血球 : {WBC}")
                    print(f"紅血球 : {RBC}")
                    print(f"高敏感度C反應性蛋白 : {hsCRP}")
                    print(f"甲型胎兒蛋白 : {Alpha}")
                    print(f"癌胚胎抗原 : {CEA}")
                    print(f"癌症抗原125 : {CA125}")
                    print(f"癌症抗原19-9 : {CA199}")



                    if Glucose == -1:
                        print("空腹血糖：未檢查")
                    elif 70 <= Glucose <= 100:
                        print("空腹血糖：正常")
                    else:
                        print("空腹血糖：異常")

                    if HbA1c == -1:
                        print("糖化血色素：未檢查")
                    elif 4.0 <= HbA1c <= 6.0:
                        print("糖化血色素：正常")
                    else:
                        print("糖化血色素：異常")

                    if Glupc == -1:
                        print("飯後血糖：未檢查")
                    elif Glupc < 140:
                        print("飯後血糖：正常")
                    else:
                        print("飯後血糖：異常")

                    if Alb == -1:
                        print("白蛋白：未檢查")
                    elif 3.5 <= Alb <= 5.7:
                        print("白蛋白：正常")
                    else:
                        print("白蛋白：異常")

                    if TP == -1:
                        print("血清蛋白總量：未檢查")
                    elif 6.4 <= TP <= 8.9:
                        print("血清蛋白總量：正常")
                    else:
                        print("血清蛋白總量：異常")

                    if ASTGOT == -1:
                        print("天門冬胺酸轉胺酶(肝功能指數）：未檢查")
                    elif 8 <= ASTGOT <= 31:
                        print("天門冬胺酸轉胺酶(肝功能指數）：正常")
                    else:
                        print("天門冬胺酸轉胺酶(肝功能指數）：異常")

                    if ASTGPT == -1:
                        print("丙胺酸轉胺酶(肝功能指數)：未檢查")
                    elif 0 <= ASTGPT <= 41:
                        print("丙胺酸轉胺酶(肝功能指數)：正常")
                    else:
                        print("丙胺酸轉胺酶(肝功能指數)：異常")

                    if DBil == -1:
                        print("直接膽紅素：未檢查")
                    elif 0.03 <= DBil <= 0.18:
                        print("直接膽紅素：正常")
                    else:
                        print("直接膽紅素：異常")

                    if ALP == -1:
                        print("鹼性磷酸酶：未檢查")
                    elif 34 <= ALP <= 104:
                        print("鹼性磷酸酶：正常")
                    else:
                        print("鹼性磷酸酶：異常")

                    if TBil == -1:
                        print("總膽紅素：未檢查")
                    elif 0.3 <= TBil <= 1.0:
                        print("總膽紅素：正常")
                    else:
                        print("總膽紅素：異常")

                    if UN == -1:
                        print("尿素氮：未檢查")
                    elif 7 <= UN <= 25:
                        print("尿素氮：正常")
                    else:
                        print("尿素氮：異常")

                    if CRE == -1:
                        print("肌酸酐：未檢查")
                    elif 0.6 <= CRE <= 1.3:
                        print("肌酸酐：正常")
                    else:
                        print("肌酸酐：異常")

                    if UA == -1:
                        print("尿酸：未檢查")
                    elif 4.4 <= UA <= 7.6:
                        print("尿酸：正常")
                    else:
                        print("尿酸：異常")

                    if TCHO == -1:
                        print("總膽固醇：未檢查")
                    elif TCHO < 200:
                        print("總膽固醇：正常")
                    else:
                        print("總膽固醇：異常")

                    if LDLC == -1:
                        print("低密度脂蛋白：未檢查")
                    elif LDLC < 130:
                        print("低密度脂蛋白：正常")
                    else:
                        print("低密度脂蛋白：異常")

                    if HDLC == -1:
                        print("高密度脂蛋白：未檢查")
                    elif HDLC > 40:
                        print("高密度脂蛋白：正常")
                    else:
                        print("高密度脂蛋白：異常")

                    if TG == -1:
                        print("三酸甘油酯：未檢查")
                    elif TG < 150:
                        print("三酸甘油酯：正常")
                    else:
                        print("三酸甘油酯：異常")

                    if Hb == -1:
                        print("血色素：未檢查")
                    elif 13.1 <= Hb <= 17.2:
                        print("血色素：正常")
                    else:
                        print("血色素：異常")

                    if Hct == -1:
                        print("血比容：未檢查")
                    elif 39.6 <= Hct <= 51.5:
                        print("血比容：正常")
                    else:
                        print("血比容：異常")

                    if PLT == -1:
                        print("血小板：未檢查")
                    elif 150 <= PLT <= 378:
                        print("血小板：正常")
                    else:
                        print("血小板：異常")

                    if WBC == -1:
                        print("白血球：未檢查")
                    elif 3.25 <= WBC <= 9.16:
                        print("白血球：正常")
                    else:
                        print("白血球：異常")

                    if RBC == -1:
                        print("紅血球：未檢查")
                    elif 4.21 <= RBC <= 5.9:
                        print("紅血球：正常")
                    else:
                        print("紅血球：異常")

                    if hsCRP == -1:
                        print("高敏感度C反應性蛋白 : 未檢查")
                    elif hsCRP < 0.1:
                        print("高敏感度C反應性蛋白 : 低等風險")
                    elif 0.1 <= hsCRP <= 0.3:
                        print("高敏感度C反應性蛋白 : 中等風險")
                    else:
                        print("高敏感度C反應性蛋白 : 高等風險")

                    if Alpha == -1:
                        print("甲型胎兒蛋白：未檢查")
                    elif Alpha < 20:
                        print("甲型胎兒蛋白：正常")
                    else:
                        print("甲型胎兒蛋白：異常，注意肝硬化或肝癌風險")

                    if CEA == -1:
                        print("癌胚胎抗原：未檢查")
                    elif CEA < 5.0:
                        print("癌胚胎抗原：正常")
                    else:
                        print("癌胚胎抗原：異常")

                    if CA125 == -1:
                        print("癌症抗原125 未檢查")
                    elif CA125 < 35:
                        print("癌症抗原125 : 正常")
                    else:
                        print("癌症抗原125 : 異常")

                    if CA199 == -1:
                        print("癌症抗原19-9 : 未檢查")
                    elif CA199 < 37:
                        print("癌症抗原19-9 : 正常")
                    else:
                        print("癌症抗原19-9 : 異常")

                else:   
                    print("查無此檢驗資料。")

                conn.close()


            elif sex == '2':
                print("查詢檢驗資料")
                test_id = input("請輸入檢驗ID: ")
                import sqlite3
                conn = sqlite3.connect("Hospital.db")
                conn.row_factory = sqlite3.Row  
                cursor = conn.cursor()
                
                cursor.execute("SELECT * FROM test WHERE test_id = ?", (test_id,))
                row = cursor.fetchone()
                
                if row:
                    
                    Glucose = row['Glucose']
                    HbA1c = row['HbA1c']
                    Glupc = row['Glupc']
                    Alb = row['Alb']
                    TP = row['TP']
                    ASTGOT = row['ASTGOT']
                    ASTGPT = row['ASTGPT']
                    DBil = row['DBil']
                    ALP = row['ALP']
                    TBil = row['TBil']
                    UN = row['UN']
                    CRE = row['CRE']
                    UA = row['UA']
                    TCHO = row['TCHO']
                    LDLC = row['LDLC']
                    HDLC = row['HDLC']
                    TG = row['TG']
                    Hb = row['Hb']
                    Hct = row['Hct']
                    PLT = row['PLT']
                    WBC = row['WBC']
                    RBC = row['RBC']
                    hsCRP = row['hsCRP']
                    Alpha = row['Alpha']
                    CEA = row['CEA']
                    CA125 = row['CA125']
                    CA199 = row['CA199']




                    print("=" * 30)
                    print(f"檢驗ID: {row['test_id']}")
                    print(f"病患ID: {row['patient_id']}")
                    print(f"空腹血糖 : {Glucose}")
                    print(f"糖化血色素 : {HbA1c}")
                    print(f"飯後血糖 : {Glupc}")
                    print(f"白蛋白 : {Alb}")
                    print(f"血清蛋白總量 : {TP}")
                    print(f"天門冬胺酸轉胺酶 : {ASTGOT}")
                    print(f"丙胺酸轉胺酶 : {ASTGPT}")
                    print(f"直接膽紅素 : {DBil}")
                    print(f"鹼性磷酸酶 : {ALP}")
                    print(f"總膽紅素 : {TBil}")
                    print(f"尿素氮 : {UN}")
                    print(f"肌酸酐 : {CRE}")
                    print(f"尿酸 : {UA}")
                    print(f"總膽固醇 : {TCHO}")
                    print(f"低密度脂蛋白 : {LDLC}")
                    print(f"高密度脂蛋白 : {HDLC}")
                    print(f"三酸甘油酯 : {TG}")
                    print(f"血色素 : {Hb}")
                    print(f"血比容 : {Hct}")
                    print(f"血小板 : {PLT}")
                    print(f"白血球 : {WBC}")
                    print(f"紅血球 : {RBC}")
                    print(f"高敏感度C反應性蛋白 : {hsCRP}")
                    print(f"甲型胎兒蛋白 : {Alpha}")
                    print(f"癌胚胎抗原 : {CEA}")
                    print(f"癌症抗原125 : {CA125}")
                    print(f"癌症抗原19-9 : {CA199}")


                    if Glucose == -1 :
                        print("空腹血糖：未檢查")
                    elif 70 <= Glucose <= 100 :
                        print("空腹血糖：正常")
                    else:
                        print("空腹血糖：異常")

                    if HbA1c == -1 :
                        print("糖化血色素：未檢查")
                    elif 4.0 <= HbA1c <= 6.0 :
                        print("糖化血色素：正常")
                    else:
                        print("糖化血色素：異常")

                    if Glupc == -1 :
                        print("飯後血糖：未檢查")
                    elif Glupc < 140  :
                        print("飯後血糖：正常")
                    else:
                        print("飯後血糖：異常")

                    if Alb == -1 :
                        print("白蛋白：未檢查")
                    elif 3.5 <= Alb <= 5.7 :
                        print("白蛋白：正常")
                    else:
                        print("白蛋白：異常")

                    if TP == -1 :
                        print("血清蛋白總量：未檢查")
                    elif 6.4 <= TP <= 8.9:
                        print("血清蛋白總量：正常")
                    else:
                        print("血清蛋白總量：異常")

                    if ASTGOT == -1:
                        print("天門冬胺酸轉胺酶(肝功能指數）：未檢查")
                    elif 8 <= ASTGOT <= 31:
                        print("天門冬胺酸轉胺酶(肝功能指數）：正常")
                    else:
                        print("天門冬胺酸轉胺酶(肝功能指數）：異常")

                    if ASTGPT == -1:
                        print("丙胺酸轉胺酶(肝功能指數)：未檢查")
                    elif 0 <= ASTGPT <= 41:
                        print("丙胺酸轉胺酶(肝功能指數)：正常")
                    else:
                        print("丙胺酸轉胺酶(肝功能指數)：異常")

                    if DBil == -1:
                        print("直接膽紅素：未檢查")
                    elif 0.03 <= DBil <= 0.18:
                        print("直接膽紅素：正常")
                    else:
                        print("直接膽紅素：異常")

                    if ALP == -1:
                        print("鹼性磷酸酶：未檢查")
                    elif 34 <= ALP <= 104:
                        print("鹼性磷酸酶：正常")
                    else:
                        print("鹼性磷酸酶：異常")

                    if TBil == -1:
                        print("總膽紅素：未檢查")
                    elif 0.3 <= TBil <= 1.0:
                        print("總膽紅素：正常")
                    else:
                        print("總膽紅素：異常")

                    if UN == -1:
                        print("尿素氮：未檢查")
                    elif 7 <= UN <= 25:
                        print("尿素氮：正常")
                    else:
                        print("尿素氮：異常")

                    if CRE == -1:
                        print("肌酸酐：未檢查")
                    elif 0.6 <= CRE <= 1.3:
                        print("肌酸酐：正常")
                    else:
                        print("肌酸酐：異常")

                    if UA == -1:
                        print("尿酸：未檢查")
                    elif 2.3 <= UA <= 6.6:
                        print("尿酸：正常")
                    else:
                        print("尿酸：異常")

                    if TCHO == -1:
                        print("總膽固醇：未檢查")
                    elif TCHO < 200:
                        print("總膽固醇：正常")
                    else:
                        print("總膽固醇：異常")

                    if LDLC == -1:
                        print("低密度脂蛋白：未檢查")
                    elif LDLC < 130:
                        print("低密度脂蛋白：正常")
                    else:
                        print("低密度脂蛋白：異常")

                    if HDLC == -1:
                        print("高密度脂蛋白：未檢查")
                    elif HDLC > 40:
                        print("高密度脂蛋白：正常")
                    else:
                        print("高密度脂蛋白：異常")

                    if TG == -1:
                        print("三酸甘油酯：未檢查")
                    elif TG < 150:
                        print("三酸甘油酯：正常")
                    else:
                        print("三酸甘油酯：異常")

                    if Hb == -1:
                        print("血色素：未檢查")
                    elif 11.0 <= Hb <= 15.2:
                        print("血色素：正常")
                    else:
                        print("血色素：異常")

                    if Hct == -1:
                        print("血比容：未檢查")
                    elif 34.8 <= Hct <= 46.3:
                        print("血比容：正常")
                    else:
                        print("血比容：異常")

                    if PLT == -1:
                        print("血小板：未檢查")
                    elif 150 <= PLT <= 378:
                        print("血小板：正常")
                    else:
                        print("血小板：異常")

                    if WBC == -1:
                        print("白血球：未檢查")
                    elif 3.25 <= WBC <= 9.16:
                        print("白血球：正常")
                    else:
                        print("白血球：異常")

                    if RBC == -1:
                        print("紅血球：未檢查")
                    elif 3.78 <= RBC <= 5.25 :
                        print("紅血球：正常")
                    else:
                        print("紅血球：異常")

                    if hsCRP == -1:
                        print("高敏感度C反應性蛋白 : 未檢查")
                    elif hsCRP < 0.1:
                        print("高敏感度C反應性蛋白 : 低等風險")
                    elif 0.1 <= hsCRP <= 0.3:
                        print("高敏感度C反應性蛋白 : 中等風險")
                    else:
                        print("高敏感度C反應性蛋白 : 高等風險")

                    if Alpha == -1:
                        print("甲型胎兒蛋白：未檢查")
                    elif Alpha < 20:
                        print("甲型胎兒蛋白：正常")
                    else:
                        print("甲型胎兒蛋白：異常，注意肝硬化或肝癌風險")

                    if CEA == -1:
                        print("癌胚胎抗原：未檢查")
                    elif CEA < 5.0:
                        print("癌胚胎抗原：正常")
                    else:
                        print("癌胚胎抗原：異常")

                    if CA125 == -1:
                        print("癌症抗原125 : 未檢查")
                    elif CA125 < 35:
                        print("癌症抗原125 : 正常")
                    else:
                        print("癌症抗原125 : 異常")

                    if CA199 == -1:
                        print("癌症抗原19-9 : 未檢查")
                    elif CA199 < 37:
                        print("癌症抗原19-9 : 正常")
                    else:
                        print("癌症抗原19-9 : 異常")

                else:
                    print("查無此檢驗資料")        

                    conn.close()
                    
        
    else :
            print("查無編號")


if __name__ == "__main__":
    run()