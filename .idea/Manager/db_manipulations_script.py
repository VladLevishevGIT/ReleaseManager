import psycopg2

def read_row():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store WHERE item = 'Book 1'")
    row = cur.fetchall()
    conn.close()
    return row

print(read_row())