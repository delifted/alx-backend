#!/usr/bin/env python3
'''
Task 5: Most Recently Used Caching Module
'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    REpresents an object that allows storing and retrieving
    items from a dict with an MRU removal mechanism when the
    limit is reached
    '''
    def __init__(self):
        '''
        Initializes the cache
        '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''
        Adds an item in the cache
        '''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = self.queue.pop()
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        '''
        Retrieves an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
