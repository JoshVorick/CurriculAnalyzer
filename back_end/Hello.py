from flask import Flask, render_template, request, redirect, url_for, json, jsonify
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
   








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

@app.route('/searchCourse')
def searchCourse():
   a = request.args.get('a')
   b = request.args.get('b')
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Course where dept = '%s' and subNumber = '%s'" % (a, b))
   rows = cur.fetchall()    

   if len(rows) != 0:
      return jsonify(result=a + b)
   
   return jsonify(result=False)

if __name__ == '__main__':
   app.run(debug = True)