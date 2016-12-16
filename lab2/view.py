
def main_menu():
    print "\n--Database credits--"
    print "1 - Credits"
    print "2 - Banks"
    print "3 - Clients"
    print "4 - fill db from json file"
    print "5 - exit"

    return raw_input("\nEnter a choice:")


def exit_key():
    print "Press any key to exit"

def invalid_input():
    print "invalid input..."

def print_table(desc, rows):
    print "--",
    for curr in desc:
        print curr,
    print "--"

    for row in rows:
        for elem in row:
            print elem,
        print