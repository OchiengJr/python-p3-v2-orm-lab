# lib/config.py
import sqlite3

def connect_to_database(db_name='company.db'):
    '''Function to connect to a SQLite database'''
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None, None

# Usage:
# from config import connect_to_database
# CONN, CURSOR = connect_to_database('your_database_name.db')
