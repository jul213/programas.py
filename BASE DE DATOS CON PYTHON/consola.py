import psycopg2

conn = psycopg2.connect("
dbname = productos
username = juan
password = bases
host = url
port = 8000
")


cur = conn.cursor()

cur.execute("select * from pokemon;")

cur.fetchall()

for row in cur:
    print (row)

