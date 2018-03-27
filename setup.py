# -*- coding: utf-8 -*-
# Copyright (C) 2016 SYLEAM (<http://www.syleam.fr>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from distutils.core import setup

setup(
    name='zpl2',
    version='1.2',
    author='Sylvain Garancher',
    author_email='sylvain.garancher@syleam.fr',
    py_modules=['zpl2'],
    extras_require={
        'graphics': ['pillow'],
    },
    license='LICENSE.txt',
    description='Python library that generates ZPL II labels',
    long_description=open('README.txt').read(),
)
