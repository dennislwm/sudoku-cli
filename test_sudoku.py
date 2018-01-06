import unittest
from sudoku import Solver


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

if __name__ == '__main__':
    unittest.main()