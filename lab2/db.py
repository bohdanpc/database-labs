import MySQLdb as mdb;
import json

def get_connection():
    return mdb.connect(host = '127.0.0.1', user = 'root', passwd = '1111', db = 'lab2db')


def fill_db_from_json():
    connection = get_connection()
    with connection:
        cursor = connection.cursor()
        cursor.execute("delete from credit")
        cursor.execute("delete from time_tab")
        cursor.execute("delete from client_tab")
        cursor.execute("delete from bank_tab")

        cursor.execute("alter table credit auto_increment = 1")
        cursor.execute("alter table time_tab auto_increment = 1")
        cursor.execute("alter table client_tab auto_increment = 1")
        cursor.execute("alter table bank_tab auto_increment = 1")

    with open('db.json') as data_file:
        data = json.load(data_file)
        for item in data:
            for element in data[item]:
                insert_table(item, list(element.keys()), list(element.values()))

    with open('db_credit.json') as data_file:
        data = json.load(data_file)
        for item in data:
            for element in data[item]:
                insert_table(item, list(element.keys()), list(element.values()))


def insert_table(table, fields, values):
    col_names = ''; col_values = ''; i = 0; length = len(fields)
    while i < length:
        col_names += fields[i] + ', '
        col_values += values[i] + ", "
        i += 1

    connection = get_connection()
    with connection:
        cursor = connection.cursor()
        print "insert into " + table + " (" + col_names[:-2] + ") " + "values (" + col_values[:-2] + ")"
        cursor.execute("insert into " + table + " (" + col_names[:-2] + ") " + "values (" + col_values[:-2] + ")")


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


def max_pred(table, field):
    connection = get_connection()

    with connection:
        cursor = connection.cursor()
        cursor.execute("select max(" + field + ") from " + table)

        return cursor.fetchone()

def delete_query(table, clause):
    connection = get_connection()

    with connection:
        cursor = connection.cursor()
        print "delete from " + table + " where " + clause
        cursor.execute("delete from " + table + " where " + clause)
