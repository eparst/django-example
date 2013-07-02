#!/usr/bin/env python

from setuptools import setup

setup(
    name='Satchmo',
    version='1.0',
    description='Satchmo Shop App',
    author='Eparst',
    author_email='rus-f1@ya.ru',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django==1.4'],
    install_requires=['pycrypto'],
    install_requires=['PyYAML'],    
    install_requires=['reportlab'],
    install_requires=['south'],
    install_requires=['sorl-thumbnail'],    
    install_requires=['django-registration'],
    install_requires=['django-livesettings'],
    install_requires=['django-threaded-multihost'],
    install_requires=['django-caching-app-plugins'],
    install_requires=['django-signals-ahoy'],
    install_requires=['django-keyedcache'],
)
