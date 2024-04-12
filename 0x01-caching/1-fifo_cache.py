#!/usr/bin/env python3
'''
Task 1: First-In First Out caching module
'''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    Inherits from BaseCaching and is a caching system
    '''
    def __init__(self):
        '''
        Calling parent init
        '''
        super().__init__()
        self.queue = []

    def put(self, key, item):
        '''
        Assigns toa dict self.cache_data the item value
        for the key <key>
        '''
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.queue:
                discarded_key = self.queue.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        '''
        Returns the value in self.cache_data linked to key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
