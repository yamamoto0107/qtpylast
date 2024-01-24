import sqlite3

def createholiday():
    dbname = 'holiday.db'
    conn = sqlite3.connect(dbname)
    #SQLを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    sql="""CREATE TABLE holiday(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        year VARCHAR(20),
        month VARCHAR(50),
        holiday INTEGER(3),
        );
        """
    conn.execute(sql)
    conn.close()
createholiday()