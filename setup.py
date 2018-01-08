#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from BitcoinPi.core import release

setup(name=release.name,
      version=release.__version__,
      description=release.description,
      author=release.author,
      author_email=release.author_email,
      url=release.url,
      packages=['BitcoinPi'],
      scripts=['pi'],
      include_package_data=True,
      data_files=[("", ["LICENSE"])],
     )
