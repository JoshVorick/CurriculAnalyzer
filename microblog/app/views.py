from flask import render_template, flash, redirect
import sqlite3 as sql


@app.route('/searchCourse', methods=['GET', 'POST'])
def searchCourse():
    form = classForm()
    if form.validate_on_submit():
      dept = form.dept.data
      subNumber = form.subNumber.data
      con = sql.connect("database.db")
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("select * from Course where dept = '%s' and subNumber = '%s'" % (dept, subNumber))
      rows = cur.fetchall()
      if len(rows) != 0:
        return redirect('/index')

    return render_template('search.html', title='Sign In',form=form)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('index.html')

