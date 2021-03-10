import sqlite3
from sqlite3 import Error


class TodosSQLite:
    def __init__(self):
        self.db_name = 'testbase.sqlite'

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except Error as error:
            print(error)
        return conn

    def select_all(self, table_name: str) -> list:
        """
        Return list of dictionaries with all entries from table [table_name].
        Column name is used as dictionary Keys
        :param table_name: table from database
        :return: list
        """
        sql = f"""SELECT * FROM {table_name}"""
        with self.create_connection() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql)
                cols_name = [item[0] for item in cur.description]
                rows = cur.fetchall()
                result = []
                for row in rows:
                    result.append(dict(zip(cols_name, row)))
                return result
            except Error as error:
                print(error)
            return []

    def get_record_by_id(self, table_name: str, id: int) -> dict:
        """
        Return dictionary with data from table [table name] based on ID.
        :param table_name: table for database
        :param id: id number of record
        :return: dictionary with column names as keys
        """
        sql = f"""SELECT * FROM {table_name} WHERE id = ?"""
        with self.create_connection() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, (id, ))
                row = cur.fetchone()
                if row:
                    cols_name = [item[0] for item in cur.description]
                    return dict(zip(cols_name, row))
            except Error as error:
                print(error)
            return {}

    def update_record_by_id(self, table_name: str, id: int, **kwargs):
        """
        Update record based on ID and table name
        :param table_name: table in database
        :param id: number of the record
        :param kwargs: pass dictionary with column name as keys
        :return:
        """
        parameters = [f"{key} = ?" for key in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(value for value in kwargs.values())
        values += (id,)

        sql = f'''UPDATE {table_name}
                 SET {parameters}
                 WHERE id = ?'''
        with self.create_connection() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, values)
                conn.commit()
            except sqlite3.OperationalError as error:
                print(error)

    def add_to_table(self, table_name: str, **kwargs):
        """
        Add data to table [table_name] kwargs dictionary must contain correct column names as keys
        :param table_name: table name in database
        :param kwargs:
        :return:
        """
        question_marks = ['?' for qmark in range(len(kwargs.keys()))]
        question_marks = ', '.join(question_marks)
        parameters = [f"{key}" for key in kwargs.keys()]
        parameters = ', '.join(parameters)
        values = tuple(value for value in kwargs.values())
        sql = f"""INSERT INTO {table_name}({parameters}) VALUES({question_marks})"""

        with self.create_connection() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, values)
                conn.commit()
            except Error as error:
                print(error)

    def delete_record_by_id(self, table_name: str, id: int):
        """
        Delete record in table [table_name] with chosen ID
        :param table_name: table in database
        :param id: record ID
        :return: Ture if any records were deleted, else return False
        """
        sql = f"""DELETE FROM {table_name} WHERE id = ?"""
        with self.create_connection() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, (id, ))
                conn.commit()
                if cur.rowcount >= 1:
                    return True
            except Error as error:
                print(error)
        return False


todos_sqlite = TodosSQLite()
