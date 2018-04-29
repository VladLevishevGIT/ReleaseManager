from app import app
from flask import render_template
import psycopg2

def read_row():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows_builds")
    row = cur.fetchall()
    conn.close()
    return row


@app.route("/")
def homepage():
    row = read_row()
    return render_template('homepage.html', row = row)

