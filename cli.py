# third-party imports
import click

# local imports
import sudoku as sdku


@click.command()
@click.option('--input_file', required=True)
@click.option('--output_file', default='solutions.txt')
def sudoku(input_file, output_file):
    problems = sdku.from_file(input_file)
    solutions = []

    for problem in problems:
        solutions.append(sdku.Solver(problem).solve(validate=True))

    sdku.to_file(solutions, output_file)   