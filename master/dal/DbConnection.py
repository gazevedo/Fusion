import sqlite3

from sqlalchemy import create_engine


class DbConnection:
    def __init__(self):
        self.conn = sqlite3.connect('fusion.db', 20)
