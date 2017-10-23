import pprint, json
import pymongo

from pymongo import MongoClient
from bson.code import Code
from bson.son import SON
from bson.json_util import dumps


# under construction?
def topFive(hashtag):

    # Create a connection
    print("Connecting..")
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    print("Connected.")

    # Access database
    db = client['bdam']
    collection = db['twitter_{0}'.format(hashtag)]
    pipeline = [ {"$unwind": "$user.name"}, {"$group": {"_id": "$user.name", "count": {"$sum": 1}}}, {"$sort": SON([("count", -1), ("_id", -1)])} ]
    return dumps(list(collection.aggregate(pipeline).decode('utf-8')))

# This function is for debugging purposes.
# It simply outputs the entire given collection as a JSON string
def rawResponse(hashtag):
    # Create a connection
    print("Connecting..")
    client = MongoClient('mongodb://admin:admin@ds229435.mlab.com:29435/bdam')
    print("Connected.")

    # Access database
    db = client['bdam']
    collection = db['twitter_{0}'.format(hashtag)]
    return dumps(list(collection.find()))

topFive("sport")
#pipeline = [{"$unwind": "$tags"}, {"$group": {"_id": "$tags", "count": {"$sum": 1}}}, {"$sort": SON([("count", -1), ("_id", -1)])}]
#client = MongoClient('mongodb://lgdillin:Big.Data-1@bdam-shard-00-00-awflg.mongodb.net:27017,bdam-shard-00-01-awflg.mongodb.net:27017,bdam-shard-00-02-awflg.mongodb.net:27017/test?ssl=true&replicaSet=bdam-shard-0&authSource=admin', 27017)
#client = MongoClient('ds147034.mlab.com/tweets', 29435)
    #agg_results = json.load(list(collection.find()))

    #query = collection.find()
    #l = list(query)
    #data = json.loads(dumps(l))
    #print(data)
    #db.command('aggregate', 'twitter_sport', pipeline=pipeline, explain=True)
    #return
    #result = list(collection.aggregate(pipeline))
    #result = collection.count()
    #pprint.pprint(list(db.things.aggregate(pipeline)))
    # Execute the map and reduce JavaScript files
    #map = Code(open('map.js', 'r').read())
    #reduce = Code(open('reduce.js', 'r').read())
    #map = Code("function map() {var user = this.user.name.match(/\w+/g);if(user == null) {return;}for(var i = 0; i < user.length; ++i) {emit(this.user[i], {count:1});}}")
    #reduce = Code("function reduce(key, values) {var total = 0;for(var i = 0; i < values.length; ++i) {total += values[i].count;}return {count: total};}")
    #result = collection.map_reduce(map, reduce, "twitter_sport")

    # Sort the query and map it into a dictionary
    #sortedresult = result.find().sort([('value.count', -1)])
    #sortedresult = collection.aggregate(pipeline)
    #for sr in cursor:
    #    print(sr)
        #data.update({sr['_id']:sr['value']['count']})
    #return data
