import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS weekly_windows_builds (released_date TEXT, number INTEGER)")
    conn.commit()
    conn.close()

def read_recent_build():
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows_builds")
    rows = cur.fetchall()
    conn.close()
    latest[1] = 0
    for row in rows:
        if row[1] < latest[1]:
            latest = row
    return latest

def import_build(date, number):
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO weekly_windows_builds VALUES (%s, %s)", (date, number))
    conn.commit()
    conn.close

# create_table()
# import_build(1956, 25896)

create_table()
import_build("2018-04-29", 2269)
