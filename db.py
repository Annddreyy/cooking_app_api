import sqlite3


def get_connection():
    conn = sqlite3.connect('/data/cooking_app.db')

    return conn