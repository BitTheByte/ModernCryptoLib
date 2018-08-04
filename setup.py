# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
        name = 'ModernCryptoLib',
        version = "0.0.11",
        description = 'Cryptography Library ',
        license = "MIT",
        author = "Ahmed Ezzat (BitTheByte)",
        packages = find_packages(),
        install_requires = ['pycrypto','requests','sym','cryptography','sympy'],
    )
