import sqlite3  # pip install pysqlite3


class Database:

    def __init__(self, path_to_db):
        self.connection = sqlite3.connect(path_to_db)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        columns = ', '.join(columns)
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        )
        self.connection.commit()

    def add_column(self, table_name, column_name, data_type):
        self.cursor.execute(
            f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}"
        )
        self.connection.commit()

    def insert_data(self, table_name, columns, data):
        try:
            columns = ', '.join(columns)
            data = ', '.join([f"'{value}'" for value in data])
            self.cursor.execute(
                f"INSERT INTO {table_name} ({columns}) VALUES ({data})")
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def get_data(self, table_name, columns):
        columns = ', '.join(columns)
        self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        # return objects in list
        data = self.cursor.fetchall()
        # return list of dictionaries
        return [dict(zip(columns.split(", "), row)) for row in data]

    def get_db_table_names(self):
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
