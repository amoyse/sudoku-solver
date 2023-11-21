

class SudokuSolver:

    def __init__(self, grid):
        self.grid = grid

    # Returns tuple with coordinates for emtpy square in grid
    def find_empty_square(self):
        pass

    # Returns true or false depending on if the given box works
    def check_box(self, box):
        pass

    # Returns true or false depending on if the given row works
    def check_row(self, row):
        pass

    # Returns true or false depending on if the given column works
    def check_column(self, column):
        pass

    # Check if the entire grid has been solved
    # May need to check if this works properly, but can only do that after other methods completed
    def is_grid_solved(self):
        pass

    # Main method that does the solving
    def main_solver(self, position):
        pass

    def run(self):
        pass








default_grid = [[0, 1, 0, 0, 0, 0, 9, 0, 0],
                [5, 6, 8, 0, 0, 2, 0, 0, 0],
                [0, 7, 0, 0, 1, 4, 0, 0, 5],
                [6, 9, 2, 0, 0, 8, 5, 0, 1],
                [0, 0, 5, 0, 0, 0, 2, 0, 0],
                [0, 0, 0, 2, 6, 0, 8, 0, 9],
                [3, 0, 7, 0, 0, 0, 0, 0, 0],
                [0, 0, 6, 1, 4, 0, 0, 9, 0],
                [9, 2, 0, 8, 5, 7, 0, 4, 6]]



s.SudokuSolver(default_grid)

