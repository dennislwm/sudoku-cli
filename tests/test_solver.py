# stdlib imports
import unittest
import copy

# local imports
from sudoku.solver import Solver
from sudoku.exceptions import InvalidProblemError


class TestSolver(unittest.TestCase):
    def test_it_solves_correctly(self):
        problem = [
            [0,9,0,0,0,0,0,0,6],
            [0,0,0,9,6,0,4,8,5],
            [0,0,0,5,8,1,0,0,0],
            [0,0,4,0,0,0,0,0,0],
            [5,1,7,2,0,0,9,0,0],
            [6,0,2,0,0,0,3,7,0],
            [1,0,0,8,0,4,0,2,0],
            [7,0,6,0,0,0,8,1,0],
            [3,0,0,0,9,0,0,0,0]
        ]
        expected_solution = [
            [8,9,5,7,4,2,1,3,6],
            [2,7,1,9,6,3,4,8,5],
            [4,6,3,5,8,1,7,9,2],
            [9,3,4,6,1,7,2,5,8],
            [5,1,7,2,3,8,9,6,4],
            [6,8,2,4,5,9,3,7,1],
            [1,5,9,8,7,4,6,2,3],
            [7,4,6,3,2,5,8,1,9],
            [3,2,8,1,9,6,5,4,7]
        ]

        solver = Solver(problem)
        solution = solver.solve()

        self.assertEqual(solution, expected_solution)

    def test_it_solves_correctly_for_other_sizes(self):
        problem = [
            [0,1,0,0],
            [4,0,0,3],
            [1,0,0,2],
            [0,0,3,0]
        ]
        expected_solution = [
            [3,1,2,4],
            [4,2,1,3],
            [1,3,4,2],
            [2,4,3,1]
        ]

        solver = Solver(problem)
        solution = solver.solve()

        self.assertEqual(solution, expected_solution)

    def test_it_does_not_alter_the_problem(self):
        problem = [
            [0,9,0,0,0,0,0,0,6],
            [0,0,0,9,6,0,4,8,5],
            [0,0,0,5,8,1,0,0,0],
            [0,0,4,0,0,0,0,0,0],
            [5,1,7,2,0,0,9,0,0],
            [6,0,2,0,0,0,3,7,0],
            [1,0,0,8,0,4,0,2,0],
            [7,0,6,0,0,0,8,1,0],
            [3,0,0,0,9,0,0,0,0]
        ]
        original_problem = copy.deepcopy(problem)

        solver = Solver(problem)
        solver.solve()

        self.assertEqual(problem, original_problem)

    def test_returns_false_for_unsolvable_problems(self):
        unsolvable_problem = [
            [1,0,2,3,4,5,6,7,8],
            [0,9,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]

        solver = Solver(unsolvable_problem)
        solution = solver.solve()

        self.assertEqual(solution, False)

    def test_raises_an_error_for_non_square_problems(self):
        invalid_problem = [
            [0,0,0],
            [0,0,0]
        ]

        with self.assertRaises(InvalidProblemError):
            Solver(invalid_problem)

    def test_raises_an_error_when_the_size_is_not_a_square(self):
        invalid_problem = [
            [0,0],
            [0,0]
        ]

        with self.assertRaises(InvalidProblemError):
            Solver(invalid_problem)

    def test_raises_an_error_when_a_row_is_not_a_list(self):
        invalid_problem = [
            '00',
            [0,0]
        ]

        with self.assertRaises(InvalidProblemError):
            Solver(invalid_problem)


if __name__ == '__main__':
    unittest.main()
