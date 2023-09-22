import sqlite3

class DbConnection:
    def __init__(self):
        self.conn = sqlite3.connect('fusion.db', 20)