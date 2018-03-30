from pymongo import MongoClient, UpdateOne
from bson.objectid import ObjectId

mongo_client = MongoClient('10.0.0.161', 27017)

sts9db = mongo_client.sts9_db.setlists


def update(old, new):
    for doc in sts9db.find({"setlist" : old}):
        sts9db.update_one({ '_id':ObjectId(doc['_id']), 'setlist': old}, { '$set' : {'setlist.$' : new }})


def main():
    while True:
        old_in = input('False Title: ')
        new_in = input('Correct Title: ')
        update(old_in, new_in)
        another = input('Another?')
        if another == 'y':
            continue
        else:
            break


main()