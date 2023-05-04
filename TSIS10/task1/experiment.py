#Python ----------connection(host, database, user, password) -----query -----cursor(postman) ------ SQL

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="nn22913705"
)

cur = conn.cursor()

name = input("name: ")
phone = input("phone: ")

# create_phonebook_table = """
#     CREATE TABLE phonebook_table(
#         user_name VARCHAR(15) NOT NULL,
#         phone_number VARCHAR(20) NOT NULL
#     )
# """

# cur.execute(create_phonebook_table)

add_user = '''
    INSERT into phonebook_table(user_name, phone_number)
        VALUES (%s, %s);
'''

# experiment_query = '''
#     INSERT INTO experiment(name)
#         VALUES (%s)
# '''
# cur.execute(experiment_query, ["tuple"])
cur.execute(add_user, (name, phone, ))



conn.commit()
conn.close()
