This project is a task from the online job hunting and training platform "HiCounselor".

NB: The following has been copied from the platform

Module 1 - Task 1

Sudoku Odyssey Begins: Set the Board
Welcome to the Sudoku Odyssey! In this task, we embark on our journey by setting up the Sudoku board. Let's initialize and display the puzzle that will challenge your logical prowess. Get ready to input your puzzle and witness its visual manifestation on the board!

The initial step is to set up a way for the user to input the puzzle, row by row. To achieve this, we have the read_user_input() method.

Before we start, let's understand Sudoku. It's a number puzzle game with a 9x9 grid. The goal is to fill the grid so that each column, each row, and each of the nine 3x3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9.

Files to Use:

sudoku_solver.py
Steps to complete the task: Initializing and Displaying the Sudoku Board

read_user_input(board) Method: The read_user_input() method under SudokuSolver class in sudoku_solver.py is your ticket to set up the Sudoku board. This function prompts you to input each row of the puzzle row by row. Use '0' for empty cells. The journey begins with the user's interaction to lay the foundation of their unique Sudoku puzzle.
Begin the Sudoku journey by the read_user_input() method.
Display a welcoming prompt, inviting the user to input the Sudoku puzzle row by row.
Create the for loop, which iterates through each row of the Sudoku board.
Inside the loop, display the prompt for the current row number.
Utilize the input() function along with list comprehension and the map() function to convert the user input into a list of integers for the current row. 
Append the obtained row to the Sudoku board (board) list.
print_board(board) Method: The print_board() method in the SudokuSolver class is your ticket to revealing the Sudoku masterpiece you've created. This function prints the Sudoku board to the console, showcasing the arrangement of numbers in a 9x9 grid. Let's go through the steps to bring your Sudoku creation to life.
The program begins by prompting the user to display the Sudoku board, presenting the current state of the puzzle.
Display the heading "Sudoku Board:" to indicate the following output represents the Sudoku board.
Utilize a for loop to iterate through each row of the Sudoku board (board).
Inside the loop, print the value of each cell in a row, converting it to a string to ensure a clean and formatted output.
After printing all columns of the current row, initiate a new line to maintain a clear grid structure.
Main Function Exploration: Your journey now leads to the main() function, the heart of the SudoQ adventure. Here, the SudokuSolver instance comes to life, and awaits your commands.
A varibale named board of type list is initialized to store the user's Sudoku puzzle. This board is initially empty and will be filled with user input.
The read_user_input(board) method is called to prompt the user to input the Sudoku puzzle row by row. The user is guided to use '0' for empty cells.
Subsequently, the created board is displayed using the print_board(board) method.
Input for the Task: 

Enter the Sudoku puzzle row by row (use '0' for empty cells):
Row 1: 5 3 0 0 7 0 0 0 0
Row 2: 6 0 0 1 9 5 0 0 0
Row 3: 0 9 8 0 0 0 0 6 0
Row 4: 8 0 0 0 6 0 0 0 3
Row 5: 4 0 0 8 0 3 0 0 1
Row 6: 7 0 0 0 2 0 0 0 6
Row 7: 0 6 0 0 0 0 2 8 0
Row 8: 0 0 0 4 1 9 0 0 5
Row 9: 0 0 0 0 8 0 0 7 9

Output for the Task:

Sudoku Board:
5 3 0 0 7 0 0 0 0 
6 0 0 1 9 5 0 0 0 
0 9 8 0 0 0 0 6 0 
8 0 0 0 6 0 0 0 3 
4 0 0 8 0 3 0 0 1 
7 0 0 0 2 0 0 0 6 
0 6 0 0 0 0 2 8 0 
0 0 0 4 1 9 0 0 5 
0 0 0 0 8 0 0 7 9 

Congratulations on mastering Task 1! By completing this task, you have gained the essential skills to initialize and display a Sudoku board. This sets the stage for your journey into creating and visualizing unique Sudoku puzzles. Well done! 🎉



Helpful Links:
To complete this task, knowledge of Python is required. You can learn Python using the following resources:

Python - Beginner To Advanced Course
Python Interview Q&A
Python Coding Practice