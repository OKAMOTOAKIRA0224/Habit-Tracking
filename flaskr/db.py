import sqlite3
DATABASE='database.db'
def create_training_table():
    con=sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS training(day,title,kaisuu)")
    con.close()