import sys
import jenkins
import psycopg2
from datetime import datetime

server = jenkins.Jenkins('http://192.168.11.63/jenkins', username='user', password='bitnami')

def create_table():
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS windows_builds (date TEXT, number INTEGER, revision INTEGER, comments TEXT, console_output TEXT)")
    conn.commit()
    conn.close()

def import_build(date, number, revision, comments, console_output):
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO windows_builds VALUES (%s, %s, %s, %s, %s)", (date, number, revision, comments, console_output))
    conn.commit()
    conn.close

def read_build_info(build_number):
    build_number = build_number -1
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows_builds WHERE number = " + str(build_number))
    row = cur.fetchall()
    conn.close()
    revision = row[0][2]
    comments = row[0][3]
    return revision, comments


build_info = server.get_build_info('Windows IncrediBuild setup building', int(sys.argv[1]), depth=0)
build_console_output = server.get_build_console_output('Windows IncrediBuild setup building', int(sys.argv[1]))
#print(build_info.keys())
changeSet = build_info.get('changeSet')

timestamp = build_info.get('timestamp')
time = datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')

build_number = build_info.get('number')

revision = 0
comments = ""
items = changeSet.get('items')
for item in items:
    comment = "Rev: " + str(item.get('revision')) + " Msg: " + item.get('msg') + "\n"
    comments = comments + comment
    if revision < item.get('revision'):
        revision = item.get('revision')

if (revision == 0):
    revision, comments = read_build_info(build_number)

create_table()
import_build(time, build_number, revision, comments, build_console_output)


