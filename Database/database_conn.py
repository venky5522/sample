import psycopg2 as pg
db_conn = pg.connect(dbname="workDB",user="postgres",password="venky.123",host="localhost",port="5432")
print(db_conn)
cur = db_conn.cursor()
cur.execute('select * from employee')
print(cur)
data = cur.fetchall()
print(data)







