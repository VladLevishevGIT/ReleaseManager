from app import app
from flask import render_template, request
import psycopg2
import datetime

def read_recent_build():
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows_builds")
    rows = cur.fetchall()
    conn.close()
    latest = ["", 0, 0, "", ""]
    for row in rows:
        if row[1] > latest[1]:
            latest = row
    return latest

def read_weekly_build():
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM weekly_windows_builds")
    rows = cur.fetchall()
    conn.close()
    latest = ["", 0]
    for row in rows:
        if row[1] > latest[1]:
            latest = row
    return latest

def weekly_build_info(number):
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows_builds WHERE number = " + str(number))
    row = cur.fetchall()
    conn.close()
    return row

def read_build_info(build_number):
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows_builds WHERE number = " + str(build_number))
    row = cur.fetchall()
    conn.close()
    return row[0]

def read_all_windows_builds():
    conn = psycopg2.connect("dbname='release_manager' user='postgres' password='postgres123' host='h9-ubu16-qa' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM windows_builds")
    windowsBuilds = cur.fetchall()
    conn.close()
    return windowsBuilds

@app.route("/")
def homepage():
    row = read_recent_build()
    weekly = read_weekly_build()
    weekly_info = weekly_build_info(weekly[1])
    build_info = weekly
    return render_template('homepage.html', row = row, weekly = weekly, weekly_info = weekly_info, build_info = weekly)

@app.route("/showWindowsBuilds", methods=['POST'])
def showWindowsBuilds():
    build_number = request.form['buildNumber']
    if build_number == "":
        chosen_build = read_recent_build()
    else:
        chosen_build = read_build_info(int(build_number))
    windowsBuilds = read_all_windows_builds()
    windowsBuilds.sort(reverse=True)
    return render_template('windowsBuildsList.html', windowsBuilds = windowsBuilds, chosen_build = chosen_build)