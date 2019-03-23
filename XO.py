class TicTacToe:
    def __init__(self):
        self.board = [[''] * 3 for j in range(3)]
        self.player = 'X'

    def mark(self, i, j):
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid board position')
        if self.board[i][j] != '':
            raise ValueError('Cell is occupied!')
        if self.winner() is not None:
            raise ValueError('Game is over!!' + self.winner() +" " +'won!')
        self.board[i][j] = self.player
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def iswin(self, mark):
        board = self.board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        for mark in 'XO':
            if self.iswin(mark):
                return mark
        return None

    def __str__(self):
        rows = [ '|'.join(self.board[r]) for r in range(3)]
        return '\n ------\n'.join(rows)

