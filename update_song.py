from pymongo import MongoClient

mongo_client = MongoClient('labops-bldr-lnx', 27017)

sts9db = mongo_client.sts9_db.setlists


def update(old, new):
    for result in db.collection.find({"items" : old}):
        for i in result["items"]:
            if i == old:
                db.collection.update({"_id": result["._id"]}, {"$set": {"items": new}})


update('Get Loud', 'Get Loud')