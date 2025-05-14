import tkinter as tk
from tkinter import messagebox

buttons = [] #global list to hold the 9 button widgets

# Console Functions
def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] not in ['X', 'O']:
                board[move] = player
                break
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid input. Enter a number from 1 to 9.")

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] in ['X', 'O']:
            return board[condition[0]]  # Return the winner ('X' or 'O')
    return None  # No winner yet

def check_draw(board):
    return all(spot in ['X', 'O'] for spot in board)

def start_console():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = 'X'

    while True:  # Loop for replay after each game
        for _ in range(9):  # Maximum 9 moves
            display_board(board)
            player_move(board, current_player)

            winner = check_winner(board)  # Check for winner
            if winner:
                display_board(board)
                print(f"Wohoo! Player {winner} wins!")
                break

            if check_draw(board):  # Check if it's a draw
                display_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        # Ask for replay or exit
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break  # Exit the loop if no replay

        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Reset the board


# GUI Functions
def reset_gui_board():
    global board, current_player
    board = [''] * 9
    current_player = 'X'
    for button in buttons:
        button.config(text='', state=tk.NORMAL)

def check_gui_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] in ['X', 'O']:
            return board[condition[0]]
    return None

def check_gui_draw():
    return all(spot in ['X', 'O'] for spot in board)

def player_gui_move(index):
    global current_player, board
    if board[index] == '':
        board[index] = current_player
        buttons[index].config(text=current_player, state=tk.DISABLED)
        winner = check_gui_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_gui_board()
        elif check_gui_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_gui_board()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            turn_label.config(text=f"Player {current_player}'s Turn")


def start_gui():
    global root, buttons, board, current_player, turn_label

    board = [''] * 9
    current_player = 'X'

    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Set size and center
    window_width = 400
    window_height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.configure(bg="#e0f7fa")  # Light blue background

    # Title
    title = tk.Label(
        root, text="🎮 Tic Tac Toe", font=("Helvetica", 22, "bold"),
        bg="#e0f7fa", fg="#01579b"
    )
    title.pack(pady=10)

    # Turn label
    turn_label = tk.Label(
        root, text="Player X's Turn", font=("Helvetica", 14, "bold"),
        bg="#e0f7fa", fg="#00695c"
    )
    turn_label.pack(pady=5)

    # Button frame
    button_frame = tk.Frame(root, bg="#e0f7fa")
    button_frame.pack()

    buttons.clear()
    for i in range(9):
        button = tk.Button(
            button_frame,
            text='',
            width=10,
            height=4,
            font=("Helvetica", 16, "bold"),
            bg="#ffffff",               # button background
            fg="#e53935",              # default X color
            activebackground="#cfd8dc",
            relief="groove",
            command=lambda i=i: player_gui_move(i)
        )
        button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        buttons.append(button)

    root.mainloop()


# Main function to choose the mode
def main():
    choice = input("Choose mode (1: Console, 2: GUI): ").strip()
    if choice == '1':
        start_console()
    elif choice == '2':
        start_gui()
    else:
        print("Invalid choice. Exiting.")
        
if __name__ == "__main__":
    main()
