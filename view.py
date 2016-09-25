def main_menu():
    raw_input("Press 'enter' to continue...")
    print "\n---Database type - articles ----"
    print "---   Make a choice ---"

    print "1 - Print all presented types with articles"
    print "2 - Print types"
    print "3 - Print articles"
    print "4 - Add type"
    print "5 - Edit type"
    print "6 - Delete type"
    print "7 - Edit articles"
    print "8 - Print all types with minimal article's cost greater than 10"

    print "9 - Exit the database"

    return raw_input("\nEnter a choice:")


def print_article(article):
    print "\tName:%s, amount:%s, price:%s, t_num:%d " \
          % (article.get_name(), article.get_amount(), article.get_price(), article.get_t_num())


def print_articles(articles):
    for article in articles:
        print_article(article)


def print_type(item):
    if not item:
        print "Sorry, no such item..."
    else:
        print "Type:%s, country:%s, volume:%s,  t_num:%d" \
              % (item.get_name(), item.get_country(), item.get_vol(), item.get_t_num())


def print_types(lst):
    for item in lst:
        print_type(item)


def enter_name(ident):
    input_val = "Enter " + ident + " name:"
    return str(raw_input(str(input_val)))


def invalid_input():
    print "Entered invalid value, try again"


def invalid_int_input():
    print "Sorry, digit's value expected, try again"


def invalid_type():
    print "Sorry, no such type was found, try again"


def exit_key():
    return raw_input("Press enter to exit...")


def fill_art_type(prompt):
    return (raw_input("Enter %s name:" % prompt),
            raw_input("Enter type's country:"),
            raw_input("Enter type's overall volume:"))


def fill_article(prompt):
    return (raw_input("Enter %s name:" % prompt),
            raw_input("Enter amount:"),
            raw_input("Enter price:"))


def fill_list_of_a_type():
    return (raw_input("\tEnter article's name:"),
            raw_input("\tEnter amount:"),
            raw_input("\tEnter price:"),
            raw_input("\tContinue(y,n):"))


def enter_cond():
    return raw_input("\tContinue(y,n):")


def edit_articles():
    print "\t\tEdit article by name - 1"
    print "\t\tAdd new article - 2"
    print "\t\tDelete article - 3"
    return raw_input("Enter a choice:")


def type_delete_caution():
    print "Caution: all articles of the type will be gone"
