from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')







@app.route('/searchOnPlanCourse', methods=['GET', 'POST'])
def searchOnPlanCourse():
   print "hahahahahahh"
   dept = request.form['dept']
   print "wocao1"
   subNumber = request.form['subNumber']

   con = sql.connect("database.db")
   con.row_factory = sql.Row
   print "wocao2"
   cur = con.cursor()
   cur.execute("select * from Course where dept = '%s' and subNumber = '%s'" % (dept, subNumber))
   rows = cur.fetchall()
   print "wocao3"
   return render_template('index.html', onPlanRows = rows)




@app.route('/searchCompletedCourse', methods=['GET', 'POST'])
def searchCompletedCourse():
   dept = request.form['dept']
   subNumber = request.form['subNumber']
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Course where dept = '%s' and subNumber = '%s'" % (dept, subNumber))
   rows = cur.fetchall()
   return render_template('index.html', completedRows = rows)




@app.route('/ListAllCourses', methods=['GET'])
def ListAllCourses():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Course")
   
   rows = cur.fetchall();
   return render_template("threadSelect.html",rows = rows)


@app.route('/ListAllUsers', methods=['GET'])
def ListAllCourse():

   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from User")
   
   rows = cur.fetchall();
   return render_template("users.html",rows = rows)



if __name__ == '__main__':
   app.run(debug = True)