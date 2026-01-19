import sqlite3
DATABASE='database.db'
def create_training_table():
    con=sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS training(day TEXT, title TEXT, kaisuu TEXT, category TEXT)")
    con.close()
if __name__ == "__main__":
    create_training_table()