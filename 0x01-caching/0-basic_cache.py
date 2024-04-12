#!/usr/bin/env python3
'''
Task 0: Basic Caching Module
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Inherits from BaseCacing
    '''
    def put(self, key, item):
        '''
        Assign to the dict self.cache_data the item
        value for the key <key>
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''
        Return the value in self.cached_data to the key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
