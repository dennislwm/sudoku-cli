# stdlib imports
import unittest
import copy

# local imports
from sudoku.serialization import serialize, deserialize


class TestSerialization(unittest.TestCase):
    def test_it_serializes_correctly(self):
        grid = [
            [2,0],
            [0,1]
        ]

        self.assertEqual(serialize(grid), '2001')

    def test_it_deserializes_correctly(self):
        string = '2001'
        expected_grid = [
            [2,0],
            [0,1]
        ]

        grid = deserialize(string, size = 2)

        self.assertEqual(grid, expected_grid)

if __name__ == '__main__':
    unittest.main()