# third-party imports
import click

# local imports
from sudoku.io import from_file, to_file
from sudoku.solver import Solver


@click.command()
@click.option('--input_file', required=True)
@click.option('--output_file', default='solutions.txt')
def sudoku(input_file, output_file):
    problems = from_file(input_file)
    solutions = []

    for problem in problems:
        solutions.append(Solver(problem).solve(validate=True))

    to_file(solutions, output_file)   