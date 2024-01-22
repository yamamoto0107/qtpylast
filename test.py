import sqlite3

# データベースファイルのパスを設定
db_name = 'record.db'

# データベースに接続
con = sqlite3.connect(db_name)

# データベースを操作するカーソルを作成
cur = con.cursor()

# Select文を作成
table=record
sql = f'INSERT INTO {table} (id, date, reason) ()' # テーブル名は適宜設定してください
# SQLを実行
cur.execute(sql)
# SQLの結果を出力
# データベース接続を終了
con.close()