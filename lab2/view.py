
def main_menu():
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