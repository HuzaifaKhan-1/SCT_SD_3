def is_valid(board, row, col, num):
    # Checking if 'num' is not in the current row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Checking if 'num' is not in the current column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Checking if 'num' is not in the current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Finding an empty cell
                for num in range(1, 10):  # Trying numbers 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Placing the number
                        
                        if solve_sudoku(board):  # Recursively solving the rest of the board
                            return True
                        
                        board[row][col] = 0  # Backtracking if no solution is found
                return False  # Triggering backtracking if no valid number is found
    return True  # The board is solved

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def input_sudoku():
    board = []
    print("\nEnter the Sudoku puzzle row by row, using 0 for empty cells:")
    for i in range(9):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        board.append(row)
    return board

# Taking Input the Sudoku puzzle
sudoku_board = input_sudoku()

# Solving and printing the result
if solve_sudoku(sudoku_board):
    print("\n\nSudoku puzzle solved:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")
