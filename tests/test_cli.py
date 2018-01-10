# stdlib imports
import unittest

# third-party imports
from click.testing import CliRunner

# local imports
from sudoku.cli import sudoku


class TestCLI(unittest.TestCase):
    def test_outputs_a_solution(self):
        runner = CliRunner()
        result = runner.invoke(sudoku, ['tests/fixtures/problem.txt'])
        with open('tests/fixtures/solution.txt', 'r') as file:
            expected_output = file.read()

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, expected_output)

    def test_exits_for_invalid_problems(self):
        runner = CliRunner()
        result = runner.invoke(sudoku, ['tests/fixtures/invalid_problem.txt'])
        expected_output = 'Error: problem is not a square grid on line 1\n'

        self.assertEqual(result.exit_code, 1)
        self.assertEqual(result.output, expected_output)

    def test_exits_for_unsolvable_problems(self):
        runner = CliRunner()
        result = runner.invoke(
            sudoku,
            ['tests/fixtures/unsolvable_problem.txt']
        )
        expected_output = 'Error: unsolvable problem on line 1\n'

        self.assertEqual(result.exit_code, 1)
        self.assertEqual(result.output, expected_output)

    def test_ignores_errors_for_invalid_problems(self):
        runner = CliRunner()
        result = runner.invoke(
            sudoku,
            ['-i', 'tests/fixtures/invalid_problem.txt']
        )
        expected_output = ''

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, expected_output)

    def test_ignores_errors_for_unsolvable_problems(self):
        runner = CliRunner()
        result = runner.invoke(
            sudoku,
            ['-i', 'tests/fixtures/unsolvable_problem.txt']
        )
        expected_output = ''

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, expected_output)
