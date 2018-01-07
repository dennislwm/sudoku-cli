from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sudoku-cli',
    version='0.1',
    description='A CLI for solving Sudoku',
    long_description=long_description,
    url='https://github.com/lukegrecki/sudoku',
    author='Luke Grecki',
    author_email='lukegrecki@gmail.com',
    keywords='sudoku',
    install_requires=[
        'Click',
    ],
    extras_require={
        'test': ['coverage'],
    },
    entry_points='''
        [console_scripts]
        sudoku=cli:sudoku
    '''
)