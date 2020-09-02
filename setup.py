#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: xingming
# Mail: huoxingming@gmail.com
# Created Time:  2015-12-11 01:25:34 AM
#############################################


from setuptools import setup, find_packages

setup(
    name = "fengmm521Touchapi",
    version = "0.1.3",
    keywords = ("touchapi","fengmm521", "mage"),
    description = "touch api tool",
    long_description = "touch api tool",
    license = "GPL Licence",

    url = "",
    author = "fengmm521.taobao.com",
    author_email = "gp@woodcol.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ['pyserial']
)