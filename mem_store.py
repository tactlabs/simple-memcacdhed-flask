#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://realpython.com/python-memcache-efficient-caching/

pip:
    pymemcache
'''

# Import necessary modules
from pymemcache.client import base as memcache_base

mem_client = memcache_base.Client(('localhost', 11211))
# print(memcache_base)

def is_key_available(key):

    global mem_client

    if(mem_client.get(key)):
        return True
    
    return False

def get_from_local_store(key):

    global mem_client

    return mem_client.get(key)

def add_in_local_store(key, value):

    global mem_client

    if(mem_client.get(key)):
        mem_client.set(key, value)
        return

    mem_client.add(key, value)

def startpy():

    # print('test1')

    # # add
    name = "Montreal"
    add_in_local_store("gc_001_name", name)

    # get the previously added value
    result = get_from_local_store("gc_001_name")
    print(result)


if __name__ == '__main__':
    startpy()