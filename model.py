import pickle

# checking, if pickle's file already exist
import os.path


class ArticleType(object):

    def __init__(self, name, country, overall_vol, t_num):
        self.name = name
        self.country = country
        self.overall_vol = overall_vol
        self.t_num = t_num

    def get_name(self):
        return self.name

    def get_t_num(self):
        return self.t_num

    def get_country(self):
        return self.country

    def get_vol(self):
        return self.overall_vol

    def set_name(self, name):
        self.name = name

    def set_country(self, country):
        self.country = country

    def set_overall_vol(self, vol):
        self.overall_vol = vol


class Article(object):
    def __init__(self, name, amount, price, t_num):
        self.name = name
        self.amount = amount
        self.price = price
        self.t_num = t_num

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_price(self):
        return self.price

    def get_t_num(self):
        return self.t_num

    def set_name(self, name):
        self.name = name

    def set_amount(self, amount):
        self.amount = amount

    def set_price(self, price):
        self.price = price


class Database(object):
    type_list = []
    art_list = []

    def __init__(self, t_file, a_file):
        self.t_file = t_file
        self.a_file = a_file
        if os.path.exists(t_file) and os.path.exists(a_file):
            self.pckl_type = open(t_file, "rb")
            self.pckl_art = open(a_file, "rb")
            self.type_list = pickle.load(self.pckl_type)
            self.art_list = pickle.load(self.pckl_art)
            self.pckl_type.close()
            self.pckl_art.close()

    def get_type_list(self):
        return self.type_list

    def get_art_list(self):
        return self.art_list

    def find_type(self, name):
        """return articles_type if it's found or False otherwise"""
        for item in self.type_list:
            if item.get_name() == name:
                return item
        return False

    def find_article(self, name):
        """Return article if it's found or False otherwise"""
        for item in self.art_list:
            if item.get_name() == name:
                return item
        return False

    def del_articles_by_t_num(self, t_num):
        ind = 0
        while ind < len(self.art_list):
            if self.art_list[ind].get_t_num() == t_num:
                del(self.art_list[ind])
            else:
                ind += 1

    def del_by_name(self, name):
        ind = 0
        while ind < len(self.type_list):
            if self.type_list[ind].get_name() == name:
                self.del_articles_by_t_num(self.type_list[ind].get_t_num())
                del(self.type_list[ind])

                return True
            ind += 1
        return False

    def filter_by_price_all(self):
        res_list = []
        for item in self.type_list:
            t_num = item.get_t_num()
            is_add = True
            for article in self.art_list:
                if article.get_t_num() == t_num and int(article.get_price()) <= 10:
                    is_add = False
                    break
            if is_add:
                res_list.append(item)
        return res_list

    def save_state(self):
        """save structure of type's and articles' lists to pickle files"""
        self.pckl_type = open(self.t_file, "wb")
        self.pckl_art = open(self.a_file, "wb")
        pickle.dump(self.type_list, self.pckl_type)
        self.pckl_type.close()
        pickle.dump(self.art_list, self.pckl_art)
        self.pckl_art.close()

    def get_id_by_name(self, type_name):
        """get type's identifier or return False if it's not found"""
        for item in self.type_list:
            if item.get_name() == type_name:
                return item.get_t_num()
        return False

    def get_t_num_articles(self, t_num):
        res = []
        for item in self.art_list:
            if item.get_t_num() == t_num:
                res.append(item)

        return res

    def del_article_by_name(self, art_name):
        ind = 0
        while ind < len(self.art_list):
            if self.art_list[ind].get_name() == art_name:
                del(self.art_list[ind])
                return True
            ind += 1
        return False

    def add_articles_lst(self, to_add_list):
        self.art_list += to_add_list

    def edit_article_by_name(self, to_change, article):
        """return True if article is edited, false return otherwise"""
        ind = 0
        while ind < len(self.art_list):
            if self.art_list[ind].get_name() == to_change:
                self.art_list[ind] = article
                return True
            ind += 1
        return False

    def edit_type(self, name, _type):
        ind = 0
        while ind < len(self.type_list):
            if self.type_list[ind].get_name() == name:
                self.type_list[ind] = _type
                return True
            ind += 1
        return False

    def get_next_t_num(self):
        return self.type_list[len(self.type_list) - 1].get_t_num() + 1
