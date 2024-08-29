import sqlite3

class Database:
    def __init__(self, db_path="main.db"):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = None, fetchall=False, fetchone=False, commit=None):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data
    def create_user_table(self):
        sql = """CREATE TABLE IF NOT EXISTS User(
                id INT PRIMARY KEY,
                name VARCHAR NOT NULL,
                username VARCHAR,
                email VARCHAR
        )
        """
        self.execute(sql, commit=True)