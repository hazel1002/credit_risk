import pymysql

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "12345678",
    "db": "bdseprojects",
    "charset": "utf8"
}

try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)

    # 建立Cursor物件
    with conn.cursor() as cursor:

        # 查詢資料SQL語法
        command = "SELECT AMT_INCOME_TOTAL, DAYS_BIRTH, DAYS_EMPLOYED, DAYS_REGISTRATION, DAYS_ID_PUBLISH, CNT_FAM_MEMBERS, HOUR_APPR_PROCESS_START,OBS_60_CNT_SOCIAL_CIRCLE, DAYS_LAST_PHONE_CHANGE,AMT_REQ_CREDIT_BUREAU_YEAR FROM applications"

        # 執行指令
        cursor.execute(command)

        # 取得所有資料
        result = cursor.fetchall()
        print(result)

except Exception as ex:
    print(ex)