import MySQLdb as mdb;
import json

def get_connection():
    return mdb.connect(host = '127.0.0.1', user = 'root', passwd = '1111', db = 'lab2db')


def fill_db_from_json():
    with open('db.json') as data_file:
        data = json.load(data_file)
        for item in data:
            for element in data[item]:
                insert_table(item, list(element.keys()), list(element.values))


def insert_table(table, fields, values):
    return 0


def select_table(table, fields = '*', where = ''):
    connection = get_connection()

    with connection:
        cursor = connection.cursor()
        cursor.execute("select " + fields + " from " + table + where)

        field_names = []
        rows = cursor.fetchall()
        for fields in cursor.description:
            field_names.append(fields[0])

    return field_names, rows


