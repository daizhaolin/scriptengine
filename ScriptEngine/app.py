# -*- coding: UTF-8 -*-
'''
Created on 2020-03-08

@author: daizhaolin
'''

from .config import Config
from .helper import cached_property
from .logging import create_logger


class ScriptEngine(object):
    def __init__(self):
        self.name = __name__

        self.config = Config({
            'DEBUG': False
        })

        self.extensions = dict()

        self.controller_queue = list()

    @property
    def debug(self):
        return self.config['DEBUG']

    @cached_property
    def logger(self):
        return create_logger(self)

    def register_controller(self, controller):
        self.controller_queue.append(controller)

    def run(self):
        for controller in self.controller_queue:
            controller(self)
