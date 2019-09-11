
def Print(matrix):
    for m in matrix:
        print(m)

def Matrix(size):
    return [[None for _ in range(size)] for _ in range(size)]


def __empty_cell(sudoku):
    size = len(sudoku)
    for row in range(size):
        for col in range(size):
            if sudoku[row][col] == 0:
                return True, row, col
    return False, -1, -1

def __is_valid_num(n, row, col, sudoku):
    return (__validate_row(n, row, sudoku) and 
           __validate_col(n, col, sudoku) and
           __validate_box(n, row, col, sudoku))

def __validate_row(n, row, sudoku):
    size = len(sudoku)
    for col in range(size):
        if sudoku[row][col] == n:
            return False
    return True

def __validate_col(n, col, sudoku):
    size = len(sudoku)
    for row in range(size):
        if sudoku[row][col] == n:
            return False
    return True

def __validate_box(n, row, col, sudoku):
    box_size = 3
    r = row // box_size * box_size
    c = col // box_size * box_size
    for row in range(r, r + box_size):
        for col in range(c, c + box_size):
            if( sudoku[row][col] == n ):
                return False
    return True

def Solve(sudoku):
    if __solve(sudoku):
        return True
    return False

def __solve(sudoku):
    size = len(sudoku)
    hasEmpty, row, col = __empty_cell(sudoku)
    
    if not hasEmpty:
        return True
    
    for n in range(1, size + 1):
        if __is_valid_num(n, row, col, sudoku):
            sudoku[row][col] = n
            if __solve(sudoku):
                return True
            sudoku[row][col] = 0
    return False