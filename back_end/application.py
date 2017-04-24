from flask import Flask, render_template, request, redirect, url_for, json, jsonify
import sqlite3 as sql
application = Flask(__name__)


@application.route('/')
def introPage():
   return render_template('introPage.html')
   

@application.route('/treeView')
def treeView():
   return render_template('treeView.html')
   


@application.route('/data')
def data():
   data = open('threads/out/this.json').read()
   return data


@application.route('/ListAllCourses', methods=['GET'])
def ListAllCourses():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from Course")

   rows = cur.fetchall();
   return render_template("threadSelect.html",rows = rows)


@application.route('/ListAllUsers', methods=['GET'])
def ListAllCourse():

   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from User")

   rows = cur.fetchall();
   return render_template("users.html",rows = rows)

@application.route('/searchCourse')
def searchCourse():
   fullName = request.args.get('a')
   a = 'CS'
   b = fullName[2:]

   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Course where dept = '%s' and subNumber = '%s'" % (a, b))
   rows = cur.fetchall()

   if len(rows) != 0:
      return jsonify(result=a + " " + b)

   return jsonify(result=False)

if __name__ == '__main__':
   application.run(debug = True)
