import sqlite3

def createattend():
    dbname = 'attendsystem.db'
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

def insertattend():
    num = 19002
    name = "山本涼平"
    dbname = 'attendsystem.db'
    conn = sqlite3.connect(dbname)
    #SQLを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    sql="INSERT INTO attend (number,name) values (?,?)"
    data = (num,name)
    conn.execute(sql,data)
    conn.commit()
    conn.close()

def selectattend():
    dbname = 'attendsystem.db'
    conn = sqlite3.connect(dbname)
    #SQLを操作するカーソルオブジェクトを作成
    c = conn.cursor()
    sql = "SELECT * FROM attend"
    c.execute(sql)
    rows = c.fetchall()
    print(len(rows),"行のデータがありました")
    temp =[]
    for row in rows:
        #print(type(row),row)
        temp.append(row)
    conn.close()
    return temp
#createattend()
#insertattend()
temp = selectattend()
print(temp)