from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('threadSelect.html')

@app.route('/searchCourse/', methods=['GET', 'POST'])
def searchCourse():
   DepartmentName = request.args.get('DepartmentName')
   subNumber = request.args.get('subNumber')
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Course WHERE departmentName =? AND subNumber=?", (DepartmentName, subNumber))
   
   rows = cur.fetchall();
   return render_template("course.html",rows = rows)


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