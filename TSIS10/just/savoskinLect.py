import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="nn22913705"
)

cur = conn.cursor()

cur.execute("SELECT * FROM account_roles")

results = cur.fetchall()

cur.close()
conn.close()



