# stdlib imports
import time
import sys
import statistics

# local imports
from sudoku.io import from_file
from sudoku.solver import Solver


def benchmark(filename):
    problems = from_file(filename)
    durations = []

    for problem in problems:
        start = time.time()
        Solver(problem).solve()
        finish = time.time()
        durations.append(finish - start)

        sys.stdout.write('.')
        sys.stdout.flush()
    print()

    return durations


def write_report():
    file = open('benchmarks/benchmark.txt', 'w')

    for problem_file in ['benchmarks/easy.txt', 'benchmarks/hard.txt']:
        print('Running benchmarks on {}...'.format(problem_file))
        durations = benchmark(problem_file)

        file.write('{}'.format(problem_file) + '\n')
        file.write('==========================\n')
        file.write('mean: {}s\n'.format(statistics.mean(durations)))
        file.write('min: {}s\n'.format(min(durations)))
        file.write('max: {}s\n'.format(max(durations)))
        file.write('\n')

    file.close()
    print('Report written to benchmarks/benchmark.txt')


if __name__ == '__main__':
    write_report()
