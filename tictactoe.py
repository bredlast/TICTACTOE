import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.geometry("300x300")
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = 1
        self.winner = None
        self.ai_player = 2
        self.create_board()
        self.create_buttons()
        self.check_winner()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = tk.Button(self.master, text=" ", font=("Helvetica", 24), command=lambda i=i, j=j: self.place_marker(i, j))
                self.board[i][j].grid(row=i, column=j)

    def create_buttons(self):
        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3)

    def place_marker(self, row, col):
        if self.board[row][col]['text'] == " ":
            if self.current_player == 1:
                self.board[row][col]['text'] = "X"
                self.current_player = 2
            else:
                self.board[row][col]['text'] = "O"
                self.current_player = 1
            self.check_winner()
            if self.current_player == self.ai_player:
                self.ai_move()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0]['text'] == self.board[i][1]['text'] == self.board[i][2]['text'] != " ":
                self.winner = self.board[i][0]['text']
                break
            if self.board[0][i]['text'] == self.board[1][i]['text'] == self.board[2][i]['text'] != " ":
                self.winner = self.board[0][i]['text']
                break
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] != " ":
            self.winner = self.board[0][0]['text']
        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] != " ":
            self.winner = self.board[0][2]['text']
        if self.winner is not None:
            print(f"{self.winner} wins!")

    def ai_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j]['text'] == " "]
        if available_moves:
            move = random.choice(available_moves)
            self.board[move[0]][move[1]]['text'] = "O"
            self.board[move[0]][move[1]]['state'] = 'normal'
            self.current_player = 1
            self.check_winner()

    def restart_game(self):
        self.current_player = 1
        self.winner = None
        for i in range(3):
            for j in range(3):
                self.board[i][j]['text'] = " "
                self.board[i][j]['state'] = 'normal'

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()