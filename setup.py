#!/usr/bin/env python

import os, sys
from distutils.core import setup, Extension, Command

import base32

setup_args = {
    'name': 'base32',
    'version': base32.base32_verstr,
    'description': 'libbase32 is an implementation of base32 encoding for encoding arbitrary binary data so that humans can remember, copy, e-mail and cut-n-paste it.',
    'author': 'zooko',
    'author_email': 'zooko@zooko.com',
    'licence': 'BSD-Like',
    'package_dir': {'base32': '.'},
    'packages': ['base32'],    
}

if __name__ == '__main__':
    apply(setup, (), setup_args)
