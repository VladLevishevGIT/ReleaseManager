import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS windows_builds (number INTEGER, revision INTEGER)")
    conn.commit()
    conn.close()

def read_row():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows_builds")
    row = cur.fetchall()
    conn.close()
    return row

def import_build(number, revision):
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO windows_builds VALUES (%s, %s)", (number, revision))
    conn.commit()
    conn.close

# create_table()
# import_build(1956, 25896)

print(read_row())
