#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, exit
import re, os

if "upl" in argv[1:]:
    import os
    os.system("python setup.py register -r pypi")
    os.system("python setup.py sdist upload -r pypi")
    exit()

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup

version = re.findall(r"__version__ = \"(.*?)\"", open("byt/byt.py").read())[0]


setup(
    name="byt",
    version=version,
    author="Guillaume Schworer",
    author_email="guillaume.schworer@gmail.com",
    py_modules=["byt"],
    url="https://github.com/ceyzeriat/byt/",
    license="GNU",
    description="Version-independent bytes-chains",
    long_description=open("README.rst").read() + "\n\n"
                    + "Changelog\n"
                    + "---------\n\n"
                    + open("HISTORY.rst").read(),
    install_requires=[],
    package_data={"": ["README.rst", "LICENSE", "HISTORY.rst"]},
    include_package_data=True,
    keywords = ['bytes', 'chain', 'octet', 'string', 'hexa', 'hexadecimal', 'python2', 'python3', 'version', 'independent'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
)


# http://peterdowns.com/posts/first-time-with-pypi.html
