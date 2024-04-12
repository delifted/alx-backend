#!/usr/bin/env python3
'''
Task 2: Last In First Out Caching Module
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    Represents an Object that allows storing and retrieving
    items from a dict with a LIFO removal mechanism when
    the limit is reached
    '''
    def __init__(self):
        '''
        Initializes the cache
        '''
        super().__init__()
        self.stack = []

    def put(self, key, item):
        '''
        Adds an item in the cache
        '''
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.stack:
                discarded_key = self.stack.pop()
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        '''
        Retries an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
