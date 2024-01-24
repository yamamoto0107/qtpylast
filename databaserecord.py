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
    sql2="""INSERT INTO record (number,date,late_num) VALUES('AI22015','0124','0'),
						('AI22015','0130','1'),
						('AI22015','0101','1'),
						('AI22015','1212','1'),
                        ('AI22015','0114','0');"""
    conn.execute(sql2)
    conn.close() 
createrecord()