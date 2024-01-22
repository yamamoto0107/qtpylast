import sqlite3

def createrecord():
    dbname = 'recordsystem.db'
    conn = sqlite3.connect(dbname)
    #SQLを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    sql="""CREATE TABLE attend(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER,
        name VARCHAR(20),
        kana VARCHAR(50),
        gender VARCHAR(10),
        mail VARCHAR(100),
        abbre VARCHAR(50)
        );
        """

    conn.execute(sql)
    conn.close()
createattend()