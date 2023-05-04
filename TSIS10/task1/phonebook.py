# Python ----------connection(host, database, user, password) -----query -----cursor(postman) ------ SQL

import psycopg2
import csv
import _csv


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="nn22913705"
)

cur = conn.cursor()

name = input("name: ")
phone = input("phone: ")

add_user = '''
    INSERT into phonebook_table(user_name, phone_number)
        VALUES (%s, %s);
'''

update = '''
    UPDATE phonebook_table SET phone_number = 11 WHERE user_name = 'Nazym';
'''

query = '''
    SELECT user_name, phone_number from phonebook_table order by user_name 
'''

delete_user = '''
    DELETE from phonebook_table where user_name = %s
'''


cur.execute(add_user, (name, phone, ))
# cur.execute('''COPY phonebook_table(user_name, phone_number)
#     FROM '"C://phonebook_table.csv"'
#     DELIMITER ',' CSV HEADER;
# ''')

cur.execute(query)
row = cur.fetchall()
print(row)

cur.execute(update)
cur.execute(delete_user, (name, ))
conn.commit()

cur.close()
conn.close()
