import psycopg2


conn = psycopg2.connect("dbname=suppliers user=postgres password=nn22913705%$NT")

cur = conn.cursor()

id = cur.fetchone()[0]






