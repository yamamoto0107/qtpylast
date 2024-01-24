import sqlite3

def createrecord():
    dbname = 'record.db'
    conn = sqlite3.connect(dbname)
    #SQLを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    sql="""CREATE TABLE record(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number VARCHAR(20),
        date VARCHAR(20),
        reason VARCHAR(50),
        frame_num VARCHAR(10),
        late_num BIT(1)
        );
        """
    conn.execute(sql)
    conn.close() 
createrecord()