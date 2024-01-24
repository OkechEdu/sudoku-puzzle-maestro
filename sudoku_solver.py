class SudokuSolver:
    # Create a class variable of the board
    board = []
    def __init__(self):
        self.scanner = None

     #Task 1:Function to taken input from user to create sudoku board
    def read_user_input(self, board):
        board = [[ None for _ in range(9)] for _ in range(9)]
        self.board = board
        print("Enter the Sudoku puzzle row by row (use '0' for empty cells):")
        for i in range(len(self.board)):
            row_data = input(f'Row {i+1}: ')
            print(row_data)
            self.board[i]=list(map(row_data))
        
       

    #Task 1:Function to print the sudoku board
    def print_board(self, board):
        for i in board:
            print(' '.join(i))
        

    #Task 2:Function to check whether the sudoku board given from user is valid or not
    def initial_valid_board(self, board):
        # a counter to check if the board has specified number of rows and columns
        cnt_rows, cnt_cols = 0, 0
        for r in board:
            if r.count() > 1:
                return False
            cnt_rows += 1
            for c in r:
                if c.count() > 1:
                    return False
                cnt_cols += 1
                if cnt_rows!= cnt_cols:
                    return False
                return True
        return False

    #Task 2:Helper Function to check intial placement of numbers on the sudoku board given from user
    def initial_valid_placement(self, board, row, col, num):
        valid_row,valid_col = {}, {}
        for i in range(9):
            valid_row[i] = True
            valid_col[i] = True
            for j in range(9):
                if board[i][j] == num:
                    valid_row[i] = False
                    valid_col[j] = False
                    if i!= row and j!= col:
                        if board[row][col] == num:
                            return False
                        else:
                            return True
                    else:
                        return True
        return False

    #Task 3:Function to solve the sudoku
    def solve_sudoku(self, board):
        
        return False

    #Task 3:Helper Function to check for empty spaces on the board
    def find_empty_cell(self, board):
        return [-1, -1]

    # Task 3:Helper Function to check  placement of numbers on the sudoku board for solving
    def is_valid_placement(self, board, row, col, num):
        return False
        
    #Main Function
    def main(self):
        print("Sudoku Board");
        self.read_user_input([])

if __name__ == "__main__":
    sudoku_solver = SudokuSolver()
    sudoku_solver.main()
