#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    
'''

# Import necessary modules
from pymemcache.client import base as memcache_base

def get_from_local_store():

    return None

def add_in_local_store(key, value):

    return None


def startpy():

    mem_client = memcache_base.Client(('localhost', 11211))
    print(memcache_base)

    # print('test1')

    # # add
    # name = "Priyanka"
    # add_in_local_store("name", name)

    # get the previously added value



if __name__ == '__main__':
    startpy()