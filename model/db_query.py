"""
This file contains mysql query for the database we created.
Author: Rutuja Tikhile.
Date:1/3/2020
"""

from config.mysql_connection import con


class Query:  # Data access layer

    def __init__(self):
        self.mydb = con

    # Dynamic insert query for inserting data into the specific table of database.
    def insert(self, data, table_name):
        column = []
        rows_values = []
        val = []
        for key, value in data.items():
            column.append(key)
            rows_values.append("%s")
            val.append(value)
        print(column)
        print(rows_values)
        print(val)
        column = ','.join(column)
        val_ = ','.join(['%s'] * len(val))
        query = f'''INSERT INTO %s (%s) VALUES (%s)''' % (table_name, column, val_)
        self.mydb.query_execute(query=query, value=val)

    # Read query for reading all the data in tables from database.
    def read(self, table_name, column_name, column_value):
        val = (column_value, )
        if column_value is None and column_name is None:
            query = f"SELECT * FROM {table_name}"
            result = self.mydb.run_query(query)
        else:
            query = f"SELECT * FROM {table_name} WHERE {column_name}= %s"
            result = self.mydb.run_query(query, value=val)
        return result

    # Update query to update the specific data in note table.
    def update(self, data, table_name):
        column = []
        rows_values = []
        val = []
        id = 0
        for key, values in data.items():
            if key != 'id':
                column.append(key)
                val.append(values)
            if key == 'id':
                id = values

        val.append(id)
        set_tokens = ','.join([f'{x}=%s' for x in column])
        sql = f"UPDATE {table_name} SET {set_tokens} WHERE id = %s"
        self.mydb.query_execute(query=sql, value=val)

    # Delete query to delete the specific data.
    def delete(self, delete_id, table_name):
        sql = f"DELETE FROM {table_name} WHERE id ={delete_id}"
        self.mydb.query_execute(query=sql, value=None)

