
def main_menu():
    raw_input("\nEnter to continue...")
    print "\n--Database credits--"
    print "1 - Credits"
    print "2 - Banks"
    print "3 - Clients"
    print "4 - time's table"
    print "5 - fill db from json file"
    print "6 - exit"

    return raw_input("\nEnter a choice:")


def credit_sub_menu():
    print "\n1 - Add credit"
    print "2 - update credit"
    print "3 - delete credit"
    print "4 - .."

    return raw_input("\nEnter a choice:")


def time_sub_menu():
    print "\n1 - select where start date in range"
    print "\2 - select where end date in range"
    print "3 - .."

    return raw_input("Enter a choice:")


def time_range():
    return raw_input("Write range of date, separated by space: \n")


def client_sub_menu():
    print "\n1 - select only working"
    print "2 - select not working"
    print "3 - .."

    return raw_input("\nEnter a choice:")

def bank_sub_menu():
    print "\n1 - Select only solvent"
    print "2 - Select not solvent"
    print "3 - .."

    return raw_input("\nEnter a choice:")


def exit_key():
    print "Press any key to exit"


def invalid_input():
    print "invalid input..."


def print_table(desc, rows):
    for curr in desc:
        print "%-13s" % curr,

    print
    for row in rows:
        for elem in row:
            print "%-13s" % elem,
        print

def enter_value(value):
    return raw_input("Enter " + value)