from flaskr import app
from flask import render_template,request,redirect,url_for
import sqlite3
DATABASE='database.db'

@app.route('/')
def index():
    con=sqlite3.connect(DATABASE)
    db_training=con.execute("SELECT * FROM training").fetchall()
    con.close()


    training= []
    for row in db_training:
        training.append({'day':row[0],"title":row[1],"kaisuu":row[2]})
    

    return render_template(
        'index.html',
        training=training
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )
@app.route('/register',methods=['POST'])
def register():
    day=request.form["day"]
    title=request.form["title"]
    kaisuu=request.form["kaisuu"]

    con=sqlite3.connect(DATABASE)
    con.execute("INSERT INTO training VALUES(?,?,?)",[day,title,kaisuu])
    con.commit()
    con.close()
    return redirect(url_for('index'))