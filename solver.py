

class SudokuSolver:

    def __init__(self, grid):
        self.grid = grid

    # Returns tuple with coordinates for empty square in grid
    def find_empty_square(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 0:
                    return (i, j)
        return (-1, -1)

    # Returns true or false depending on if the given box works
    def check_box(self, box):
        numbers = []
        counter = 0
        row1 = [1, 4, 7]
        row2 = [2, 5, 8]
        row3 = [3, 6, 9]
        start = 0
        if box in row1:
            start = row1.index(box) * 27
        elif box in row2:
            start = (row2.index(box) * 27) + 3
        elif box in row3:
            start = (row3.index(box) * 27) + 6

        to_count = []
        to_calc_box = [0, 1, 2, 9, 10, 11, 18, 19, 20]
        for i in to_calc_box:
            to_count.append(start + i)

        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if counter in to_count:
                    if self.grid[i][j] != 0:
                        numbers.append(self.grid[i][j])
                counter += 1

        unique_numbers = list(set(numbers))
        if len(numbers) == len(unique_numbers):
            return True
        return False



    # Returns true or false depending on if the given row works
    def check_row(self, row):
        numbers = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if i == row:
                    if self.grid[i][j] != 0:
                        numbers.append(self.grid[i][j])

        unique_numbers = list(set(numbers))
        if len(numbers) == len(unique_numbers):
            return True
        return False
            

    # Returns true or false depending on if the given column works
    def check_column(self, column):
        numbers = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if j == column:
                    if self.grid[i][j] != 0:
                        numbers.append(self.grid[i][j])

        unique_numbers = list(set(numbers))
        if len(numbers) == len(unique_numbers):
            return True
        return False


    def is_safe(self, pos, number):
        self.grid[pos[0]][pos[1]] = number

        for i in range(9):
            if not self.check_box(i + 1):
                self.grid[pos[0]][pos[1]] = 0
                return False
            elif not self.check_row(i):
                self.grid[pos[0]][pos[1]] = 0
                return False
            elif not self.check_column(i):
                self.grid[pos[0]][pos[1]] = 0
                return False


        self.grid[pos[0]][pos[1]] = 0
        return True


    # Check if the entire grid has been solved
    # May need to check if this works properly, but can only do that after other methods completed
    def is_grid_solved(self):
        if self.find_empty_square() != (-1, -1):
            return False

        for i in range(9):
            if not self.check_box(i + 1):
                return False
            if not self.check_row(i):
                return False
            if not self.check_box(i):
                return False
        return True

    # Main method that does the solving
    def main_solver(self):
        if self.find_empty_square() == (-1, -1):
            return True

        row, column = self.find_empty_square()

        # check if board is safe
        for i in range(1, 10):
            if self.is_safe([row, column], i):
                self.grid[row][column] = i
                if self.main_solver():
                    return True
                self.grid[row][column] = 0

        return False


    def print_grid(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j], end=" "),
            print()


    def run(self):
        while not self.is_grid_solved():
            self.main_solver()
        self.print_grid()







default_grid = [[0, 1, 0, 0, 0, 0, 9, 0, 0],
                [5, 6, 8, 0, 0, 2, 0, 0, 0],
                [0, 7, 0, 0, 1, 4, 0, 0, 5],
                [6, 9, 2, 0, 0, 8, 5, 0, 1],
                [0, 0, 5, 0, 0, 0, 2, 0, 0],
                [0, 0, 0, 2, 6, 0, 8, 0, 9],
                [3, 0, 7, 0, 0, 0, 0, 0, 0],
                [0, 0, 6, 1, 4, 0, 0, 9, 0],
                [9, 2, 0, 8, 5, 7, 0, 4, 6]]

solved_grid = [[7, 9, 2, 1, 5, 4, 3, 8, 6],
               [6, 4, 3, 8, 2, 7, 1, 5, 9],
               [8, 5, 1, 3, 9, 6, 7, 2, 4],
               [2, 6, 5, 9, 7, 3, 8, 4, 1],
               [4, 8, 9, 5, 6, 1, 2, 7, 3],
               [3, 1, 7, 4, 8, 2, 9, 6, 5],
               [1, 3, 6, 7, 4, 8, 5, 9, 2],
               [9, 7, 4, 2, 1, 5, 6, 3, 8],
               [5, 2, 8, 6, 3, 9, 4, 1, 7]]


s = SudokuSolver(default_grid)

s.run()

# print("Check row:")
# print(s.check_row(3))
# print("Check column:")
# print(s.check_column(6))

# print(s.is_grid_solved())
