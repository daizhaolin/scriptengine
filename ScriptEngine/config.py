# -*- coding: UTF-8 -*-
'''
Created on 2020-03-08

@author: daizhaolin
'''


class Config(dict):
    def __init__(self, defaults=None):
        dict.__init__(self, defaults or {})

    def from_object(self, obj):
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)
