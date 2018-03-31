from pymongo import MongoClient

mongo_client = MongoClient('10.0.0.161', 27017)

sts9db = mongo_client.sts9_db.setlists


def update(old, new):
    sts9db.update_many({'setlist': old}, { '$set' : {'setlist.$' : new }})


def main():
    while True:
        old_in = input('False Title: ')
        new_in = input('Correct Title: ')
        update(old_in, new_in)
        input('Press Enter')


main()