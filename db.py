import sqlite3

import pyodbc

def get_connection():
    conn = sqlite3.connect('cooking_app.db')

    return conn