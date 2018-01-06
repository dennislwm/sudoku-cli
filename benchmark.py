# stdlib imports
import timeit

# local imports
from sudoku import import_problems, Solver


if __name__ == '__main__':
    print('Running benchmark...')

    problems = import_problems('problems.txt')
    durations = []
    for problem in problems:
        solver = Solver(problem)
        duration = timeit.timeit(solver.solve)
        durations.append(duration)
        print('Finished in {}s').format(duration)

    print('==============')
    print('Finished in {}s').format(sum(durations))