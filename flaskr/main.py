from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'


@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_training = con.execute("SELECT * FROM training").fetchall()
    con.close()

    training = []
    for row in db_training:
        training.append({
            'id': row[0],
            'category': row[1],
            'day': row[2],
            'title': row[3],
            'kaisuu': row[4]
})



    return render_template('index.html', training=training)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/register', methods=['POST'])
def register():
    category = request.form["category"]
    day = request.form["day"]
    title = request.form["title"]
    kaisuu = request.form["kaisuu"]

    con = sqlite3.connect(DATABASE)
    con.execute(
    "INSERT INTO training (category, day, title, kaisuu) VALUES (?, ?, ?, ?)",
    (category, day, title, kaisuu)
)


    con.commit()
    con.close()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    print("削除ID:", id)   
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute("DELETE FROM training WHERE id = ?", (id,))
    con.commit()
    con.close()
    return redirect(url_for('index'))
