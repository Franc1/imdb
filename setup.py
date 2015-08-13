#!/usr/bin/env python

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup


setup(name='imdb',
      version='0.1.0.0',
      license='MIT',
      description="Searches and Collects imdb data with title or imdb id",
      long_description=open('README.md').read(),
      url='https://github.com/fatihsucu/imdb',
      author='Fatih Sucu',
      author_email='fatihsucu0@gmail.com',
      packages=['imdb'],
      package_data={'imdb': ['*']},
      platforms='any')