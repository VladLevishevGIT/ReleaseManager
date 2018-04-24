from flask import Flask, render_template, request
import psycopg2

managerApp = Flask(__name__)

@managerApp.route("/")
def home():
    return render_template("home.html")

@managerApp.route("/windows")
def windows():
    return render_template("windows.html")

@managerApp.route("/linux")
def linux():
    return render_template("linux.html")

@managerApp.route('/enternew')
def new_student():
    return render_template('student.html')

# @managerApp.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#     if request.method == 'POST':
#         try:
#             nm = request.form['nm']
#             addr = request.form['add']
#             city = request.form['city']
#             pin = request.form['pin']
#
#             with sql.connect("database.db") as con:
#                 cur = con.cursor()
#
#                 cur.execute("INSERT INTO students (name,addr,city,pin)
#                 VALUES (?,?,?,?)",(nm,addr,city,pin) )
#
#                 con.commit()
#                 msg = "Record successfully added"
#         except:
#             con.rollback()
#             msg = "error in insert operation"
#
#         finally:
#             return render_template("result.html",msg = msg)
#             con.close()

@managerApp.route('/windows/allbuilds')
def allbuilds():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return render_template("windows.html",rows = rows)

if __name__=="__main__":
    managerApp.run(debug=True)