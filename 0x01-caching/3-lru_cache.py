#!/usr/bin/env python3
''' Task 3: Least Recently Used Caching Module '''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' Represents an object that allows storing and retrieving
    items from a dictionary with a LRU removal mechanism
    when the limit is reached
    '''
    def __init__(self):
        '''
        initializes the cache
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
            lru_key = self.queue.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))
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
