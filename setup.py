from setuptools import setup

setup(
    name='sudoku',
    version='0.1',
    py_modules=['sudoku'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sudoku=cli:sudoku
    ''',
)