import tkinter as tk
from tkinter import messagebox

# Define the board dimensions
ROWS = 6
COLS = 7

# Define the players and their pieces
PLAYER1 = 1
PLAYER2 = 2
PLAYER1_PIECE = 'X'
PLAYER2_PIECE = 'O'

# Create the empty game board
board = []
for row in range(ROWS):
    board.append([0] * COLS)

# Create the GUI window
window = tk.Tk()
window.title("Connect 4")

# Create the canvas to draw the game board
canvas = tk.Canvas(window, width=COLS * 50, height=(ROWS + 1) * 50)
canvas.pack()
canvas["state"] = tk.DISABLED

# Draw the horizontal lines of the board
for row in range(ROWS + 1):
    canvas.create_line(0, row * 50, COLS * 50, row * 50)

# Draw the vertical lines of the board
for col in range(COLS + 1):
    canvas.create_line(col * 50, 0, col * 50, ROWS * 50)

# Initialize the players
current_player = PLAYER1
player1_name = ""
player2_name = ""


# Function to start the game after getting player names
def start_game():
    global player1_name
    global player2_name
    player1_name = player1_entry.get()
    player2_name = player2_entry.get()
    if player1_name and player2_name:
        player1_label.config(text=player1_name)
        player2_label.config(text=player2_name)
        player1_entry.config(state=tk.DISABLED)
        player2_entry.config(state=tk.DISABLED)
        start_button.config(state=tk.DISABLED)
        canvas["state"] = tk.NORMAL


# Create labels and entry fields for player names
player1_label = tk.Label(window, text="Player 1:")
player1_label.pack()
player1_entry = tk.Entry(window)
player1_entry.pack()

player2_label = tk.Label(window, text="Player 2:")
player2_label.pack()
player2_entry = tk.Entry(window)
player2_entry.pack()

start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()


# Define the function to handle player moves
def make_move(event):
    global board
    global current_player

    # Calculate the column based on the mouse click position
    col = event.x // 50

    # Find the first empty slot in the chosen column
    row = ROWS - 1
    while row >= 0 and board[row][col] != 0:
        row -= 1

    # If the column is full, do nothing
    if row < 0:
        return

    # Update the game board and draw the player's piece
    board[row][col] = current_player
    if current_player == PLAYER1:
        canvas.create_oval(col * 50 + 5, row * 50 + 5, col * 50 + 45, row * 50 + 45, fill='red')
        current_player = PLAYER2
    else:
        canvas.create_oval(col * 50 + 5, row * 50 + 5, col * 50 + 45, row * 50 + 45, fill='yellow')
        current_player = PLAYER1

    # Check for a win
    if check_win():
        if current_player == PLAYER1:
            winner = player2_name
        else:
            winner = player1_name
        messagebox.showinfo("Game Over", "Congratulations " + winner + ", you won!")
        window.quit()


# Define the function to check for a win
def check_win():
    global board

    # Check for a win in rows
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] != 0:
                return True

    # Check for a win in columns
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != 0:
                return True

    # Check for a win in diagonal lines (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != 0:
                return True

    # Check for a win in diagonal lines (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] != 0:
                return True

    # If no win was found, return False
    return False


# Bind the mouse click event to the make_move function
canvas.bind("<Button-1>", make_move)

window.mainloop()