#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, exit
import re, os

m = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "byt", "byt.py")).read()
version = re.findall(r"__version__ *= *\"(.*?)\"", m)[0]

if "upl" in argv[1:]:
    import os
    os.system("python setup.py sdist")
    os.system("twine upload -r pypi ./dist/byt-{}.tar.gz".format(version))
    exit()

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup
    setup


setup(
    name="byt",
    version=version,
    author="Guillaume Schworer",
    author_email="guillaume.schworer@gmail.com",
    packages=["byt"],
    url="https://github.com/ceyzeriat/byt/",
    license="GNU",
    description="Version-independent bytes-chains",
    long_description=open("README.rst").read() + "\n\n"
                    + "Changelog\n"
                    + "---------\n\n"
                    + open("HISTORY.rst").read(),
    install_requires=[],
    package_data={"": ["README.rst", "AUTHORS.rst", "LICENSE", "HISTORY.rst"]},
    include_package_data=True,
    download_url = 'https://github.com/ceyzeriat/byt/tree/master/dist',
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
