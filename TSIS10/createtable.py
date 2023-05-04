import psycopg2


conn = psycopg2.connect("dbname=suppliers user=postgres password=nn22913705")

def create_tables():
    ''' create tables in the PostgreSQL database '''
    commands = (
        '''
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        ''',
        '''
        CREATE TABLE parts (
            part_id SERIAL PRIMARY KEY,
            part_name VARCHAR(255) NOT NULL
        )
        ''',
        
    )
