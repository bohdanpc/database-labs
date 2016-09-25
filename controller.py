from model import *

import view

database = Database("type.pcl", "articles.pcl")


def form_articles_list(t_num):
    """form list of articles from input to add to the new type"""
    cond = 'y'
    art_list = []
    while cond == 'y':
        art_name, amount, price = view.fill_article("article's")
        if amount.isalpha() or price.isalpha():
            view.invalid_int_input()
            continue
        article = Article(art_name, amount, price, t_num)
        art_list.append(article)
        cond = view.enter_cond()
    return art_list


def print_all_types():
    view.print_types(database.get_type_list())


def print_all_types_with_articles():
    """Function is checked"""
    for item in database.get_type_list():
        view.print_type(item)
        view.print_articles(database.get_t_num_articles(item.get_t_num()))


def print_articles():
    for article in database.get_art_list():
        view.print_article(article)


def find_type_by_name():
    to_find = view.enter_name("type")
    view.print_type(database.find_type(to_find))


def del_type():
    to_find = view.enter_name("type")
    if not database.del_by_name(to_find):
        view.invalid_input()


def add_type():
    name, country, vol = view.fill_art_type("type's")
    t_num = 0
    t_len = len(database.type_list)
    if t_len > 0:
        t_num = database.get_next_t_num()
    art_type = ArticleType(name, country, vol, t_num)
    database.get_type_list().append(art_type)
    articles_list = form_articles_list(art_type.get_t_num())
    database.add_articles_lst(articles_list)


def delete_type():
    view.type_delete_caution()
    name = view.enter_name("type")
    if not database.del_by_name(name):
        view.invalid_type()


def exit_case():
    view.exit_key()
    database.save_state()


def print_greater_10():
    view.print_types(database.filter_by_price_all())


def edit_article_by_name():
    to_change = view.enter_name("article's")
    art_to_change = database.find_article(to_change)
    if not art_to_change:
        view.invalid_input()
    else:
        name, amount, price = view.fill_article("new article's")
        article = Article(name, amount, price, art_to_change.get_t_num())
        database.edit_article_by_name(to_change, article)


def add_article(type_item):
    to_add_list = form_articles_list(type_item.get_t_num())
    database.add_articles_lst(to_add_list)


def del_article():
    to_del = view.enter_name("article")
    if not database.del_article_by_name(to_del):
        view.invalid_input()


def edit_articles():
    _choice = view.edit_articles()
    if _choice == "1":
        edit_article_by_name()
    elif _choice == "2":
        """Add article bounded to the entered type"""
        name = view.enter_name("type's")
        type_item = database.find_type(name)
        if not type_item:
            view.invalid_input()
        else:
            add_article(type_item)
    elif _choice == "3":
        del_article()
    else:
        view.invalid_input()


def edit_type():
    to_change = view.enter_name("type's")
    type_to_change = database.find_type(to_change)
    if not type_to_change:
       view.invalid_input()
    else:
        name, country, vol = view.fill_art_type("new type's")
        _type = ArticleType(name, country, vol, type_to_change.get_t_num())
        database.edit_type(to_change, _type)


def main_func():
    choice = ''
    while choice != "9":
        choice = str(view.main_menu())
        if choice == "1":
            print_all_types_with_articles()
        elif choice == "2":
            view.print_types(database.type_list)
        elif choice == "3":
            print_articles()
        elif choice == "4":
            add_type()
        elif choice == "5":
            edit_type()
        elif choice == "6":
            delete_type()
        elif choice == "7":
            edit_articles()
        elif choice == "8":
            print_greater_10()
        elif choice == "9":
            exit_case()
        else:
            view.invalid_input()

main_func()
