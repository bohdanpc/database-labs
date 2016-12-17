import view
import db

def add_time():
    st_date = ""
    end_date = ""
    st_date += "'" + view.enter_value("start_date (YY-MM-DD): ") + "'"
    end_date += "'" + view.enter_value("end_date (YY-MM-DD): ") + "'"

    lst_field = ["start_date", "end_date"]
    lst_values = [st_date, end_date]

    db.insert_table("time_tab", lst_field, lst_values)
    return db.max_pred("time_tab", "time_id")


def add_client():
    desc, rows = db.select_table("bank_tab")
    view.print_table(desc, rows)
    bank_id = view.enter_value("bank_id: ")

    desc, rows = db.select_table("client_tab")
    view.print_table(desc, rows)
    client_id = view.enter_value("client_id: ")

    values = view.enter_value("summa, percentage, currency: ")

    time_id = str(add_time())
    time_id = time_id[1:-3]
    lst_field = ["client_id", "time_id", "bank_id", "summa", "percentage", "currency"]

    lst_values = [client_id, time_id, bank_id]
    lst_values += (values.split(" "))

    db.insert_table("credit", lst_field, lst_values)


def del_client():
    credit_id = view.enter_value(" credit_id:")
    db.delete_query("credit", str("credit_id = " + credit_id))


def credit_func(choice):
    if choice == "1":
        add_client()
    elif choice == "2":
        print "updating"
    elif choice == "3":
        del_client()


def main_function():
    choice = ''
    while choice != "6":
        choice = str(view.main_menu())
        if choice == "1":
            desc, rows = db.select_table("credit")
            view.print_table(desc, rows)
            choice = str(view.credit_sub_menu())
            credit_func(choice)
        elif choice == "2":
            desc, rows = db.select_table("bank_tab")
            view.print_table(desc, rows)
        elif choice == "3":
            desc, rows = db.select_table("client_tab")
            view.print_table(desc, rows)
        elif choice == "4":
            desc, rows = db.select_table("time_tab")
            view.print_table(desc, rows)
        elif choice == "5":
            db.fill_db_from_json()
        elif choice == "6":
            view.exit_key()
        else:
            view.invalid_input()


main_function()
