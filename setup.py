# -*- coding: UTF-8 -*-
'''
Created on 2020-03-08

@author: daizhaolin
'''

from setuptools import setup, find_packages

setup(
    name='ScriptEngine',
    version='1.0',
    url='http://scriptengine.io/',
    author='daizhaolin',
    author_email='daizhaolin@gmail.com',
    license='BSD 3-Clause',
    description='Script Engine',
    long_description=__doc__,
    platforms='macOS',
    python_requires='>=3.5, <4',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
