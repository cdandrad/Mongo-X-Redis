#!/usr/bin/env python2.7
import sys, time
from pymongo import Connection
import redis

# connect to redis & mongodb
redis = redis.Redis()
mongo = Connection().test
collection = mongo['test']
cursor = mongo['test']
collection.ensure_index('key', unique=True)

REDIS_ADDRESS = '127.0.0.1'

def __init__(self, name):
        self.name = name
        self.redis = redis.Redis(REDIS_ADDRESS)

def mongo_set(data):
    for k, v in data.iteritems():
        collection.insert({'key': k, 'value': v})
		
def mongo_del(data):
   	collection.remove()

def mongo_del(data):
   	collection.remove()
	
def mongo_get(data):
	for k in data.iterkeys():
		val = collection.find_one({'key': k}, fields=('value',)).get('value')

#update in mongo		
		
def mongo_update(data): 
	for k in data.iterkeys():
		collection.update({'key': k}, {"$set": {"value" : k  }})
		
def mongo_sort():
	val = collection.find().sort({'value': -1})				
		
def mongo_push(data):
	for k in data.iterkeys():
		val = collection.find_one({'key': k}, fields=('value',)).get('value')		

def redis_set(data):
    for k, v in data.iteritems():
        redis.set(k, v)

def redis_get(data):
    for k in data.iterkeys():
        val = redis.get(k)

def redis_update(data):
    for k in data.iterkeys():
        a = redis.append(k, "k")		
		

def do_tests(num, tests):
    # setup dict with key/values to retrieve
    data = {'key' + str(i): 'val' + str(i)*100 for i in range(num)}
    # run tests
    for test in tests:
        start = time.time()
        test(data)
        elapsed = time.time() - start
        print "Completed %s: %d ops in %.2f seconds : %.1f ops/sec" % (test.__name__, num, elapsed, num / elapsed)

if __name__ == '__main__':
    num = 1000 if len(sys.argv) == 1 else int(sys.argv[1])
    tests = [mongo_set, mongo_get, mongo_update,  redis_set, redis_get, redis_update] # order of tests is significant here!
    do_tests(num, tests)