import copy


class Solver:
    def __init__(self, problem):
        self.problem = problem
        self.solution = copy.deepcopy(problem)

    def solve(self):
        next_empty_cell = self._next_empty_cell()

        if not next_empty_cell:
            return self.solution
        else:
            row, column = next_empty_cell

        for number in range(1, 10):
            if self._is_valid_move(row, column, number):
                self.solution[row][column] = number

                if self.solve():
                   return self.solution 
                else:
                    self.solution[row][column] = 0

        return False

    def _is_valid_move(self, row, column, value):
        return not self._used_in_row(row, value) and \
               not self._used_in_column(column, value) and \
               not self._used_in_box(row, column, value)

    def _next_empty_cell(self):
        for row in range(9):
            for column in range(9):
                if self.solution[row][column] == 0:
                    return (row, column)

    def _used_in_row(self, row, value):
        return value in self.solution[row]

    def _used_in_column(self, column, value):
        for row in range(9):
            if self.solution[row][column] == value:
                return True
        return False

    def _used_in_box(self, row, column, value):
        box_rows, box_columns = self._find_box(row, column)

        for box_row in box_rows:
            for box_column in box_columns:
                if self.solution[box_row][box_column] == value:
                    return True
        return False

    def _find_box(self, row, column):
        box_row_start = (row / 3) * 3
        box_rows = range(box_row_start, box_row_start + 3)

        box_column_start = (column / 3) * 3
        box_columns = range(box_column_start, box_column_start + 3)

        return (box_rows, box_columns)