#import MySQLdb as mdb;
import view
import db

#connection = mdb.connect(host = '127.0.0.1', user = 'root', passwd = '1111', db = 'lab2db')

#with connection:
    #cursor = connection.cursor()
    #cursor.execute("Drop table if exists table1")
    #cursor.execute("create table table1 (id int primary key, name varchar(20))")
    #cursor.execute("insert into table1(id, name) values(1, 'Bohdan')")
    #cursor.execute("insert into table1(id, name) values(2, 'Lena')")

#    cursor.execute("select * from table1")

 #   rows = cursor.fetchall()

  #  print cursor.description[0][0], cursor.description[1][0]
   # for row in rows:
    #    print row[0], row[1]

def main_function():
    choice = ''
    while choice != "5":
        choice = str(view.main_menu())
        if choice == "1":
            print "credits"
        elif choice == "2":
            desc, rows = db.select_table("bank_tab")
            view.print_table(desc, rows)
        elif choice == "3":
            desc, rows = db.select_table("client_tab")
            view.print_table(desc, rows)
        elif choice == "4":
            db.fill_db_from_json()
        elif choice == "5":
            view.exit_key()
        else:
            view.invalid_input()


main_function()
