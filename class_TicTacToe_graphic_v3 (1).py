import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Initialize board
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        
        # Status label
        self.status_label = tk.Label(root, text="Player X's turn", font='Arial 15')
        self.status_label.pack(pady=20)
        
        # Create a frame for the game buttons
        self.game_frame = tk.Frame(root)
        self.game_frame.pack(pady=20)
        
        # Create buttons within the game frame
        #self.buttons = [[tk.Button(self.game_frame, text='', font='Arial 24', width=5, height=1, bg='lightgray', command=lambda i=i, j=j: self.make_move(i, j)) for j in range(3)] for i in range(3)]

        self.buttons = [[tk.Button(self.game_frame, text='', font='Arial 24', width=5, height=2, bg='lightgray', command=lambda i=i, j=j: self.make_move(i, j)) for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
        
        # Restart button
        self.restart_button = tk.Button(root, text="Restart Game", font='Arial 15', bg='lightblue', command=self.reset_game)
        self.restart_button.pack(pady=20)

    def make_move(self, row, col):
        if not self.board[row][col] and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col]['text'] = self.current_player
            if self.current_player == 'X':
                self.buttons[row][col]['fg'] = 'blue'
            else:
                self.buttons[row][col]['fg'] = 'green'
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif all(cell for row in self.board for cell in row):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()
                self.status_label['text'] = f"Player {self.current_player}'s turn"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''
                self.buttons[i][j]['text'] = ''
                self.buttons[i][j]['fg'] = 'black'
        self.current_player = 'X'
        self.status_label['text'] = f"Player X's turn"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
