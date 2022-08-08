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
        command = "SELECT PREV_ANNUITY_median, PREV_CREDIT_sum,RATE_DOWN_PAYMENT_median, DAYS_DECISION_median,CNT_PAYMENT_median, DAYS_PERIOD_median,YIELD_high, HOUR_APPR_PROCESS_START_y, WEEKDAY_APPR_PROCESS_START, 'Cash through the bank' FROM database_prev"

        # 執行指令
        cursor.execute(command)

        # 取得所有資料
        result = cursor.fetchall()
        print(result)

except Exception as ex:
    print(ex)