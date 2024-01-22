import sqlite3

def createattend():
    dbname = 'record.db'
    conn = sqlite3.connect(dbname)
    #SQLを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    sql="""CREATE TABLE record(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER,
        data VARCHAR(20),
        reason VARCHAR(100),
        frame_num VARCHAR(10),
        late_num Boolean
        );
        """

    conn.execute(sql)
    conn.close()
createattend()