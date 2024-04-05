#!/usr/bin/env python3
'''
Task 0 of Pagination Project
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Returns a tuple of size two containing a start index and
    an end corresponding with range of indexes
    '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
