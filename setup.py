import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="my_first_calculator",
    version="0.1",
    author="Alexander Lewis",
    author_email="info@acelewis.com",
    description="This is my first calculator",
    url="https://github.com/AceLewis/my_first_calculator.py",
    packages=[],
    py_modules=['my_first_calculator'],
    long_description=read('README.md'),
)
