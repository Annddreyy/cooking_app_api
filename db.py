import sqlite3


def get_connection():
    conn = sqlite3.connect('cooking_app.db')

    return conn