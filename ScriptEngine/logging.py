# -*- coding: UTF-8 -*-
'''
Created on 2020-03-08

@author: daizhaolin
'''

import sys
import logging


def create_logger(app):
    logger = logging.getLogger(app.name)

    if app.debug:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            )
        )

        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

    return logger
