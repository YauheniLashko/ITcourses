import os


def goods_to_file(good, category, price, count):
    with open("goods.txt", 'a', encoding='utf-8') as f:
        good_id = os.stat("goods.txt").st_size
        f.write(f'{good_id};{good};{category};{price};{count}\n')


def get_all_goods():
    goods = {}
    with open("goods.txt", 'r', encoding='utf-8') as f:

        for line in f:
            line = line.replace("\n", "")
            line = line.split(";")
            goods[line[0]] = {"good": line[1],
                              "category": line[2],
                              "price": line[3],
                              "count": line[4]}
    return goods


def users_to_file(name, mail, phone):
    with open("users.txt", 'a', encoding='utf-8') as f:
        user_id = os.stat("users.txt").st_size
        f.write(f'{user_id};{name};{mail};{phone}\n')


def get_all_users():
    users = {}
    with open("users.txt", 'r', encoding='utf-8') as f:

        for line in f:
            line = line.replace("\n", "")
            line = line.split(";")
            goods[line[0]] = {"name": line[1],
                              "mail": line[2],
                              "phone": line[3],
                              }
    return users

