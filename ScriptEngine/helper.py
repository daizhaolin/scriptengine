# -*- coding: UTF-8 -*-
'''
Created on 2020-03-08

@author: daizhaolin
'''


class cached_property(object):
    def __init__(self, func):
        self.__name__ = func.__name__
        self.func = func

    def __get__(self, instance, owner=None):
        value = self.func(instance)

        instance.__dict__[self.__name__] = value

        return value
