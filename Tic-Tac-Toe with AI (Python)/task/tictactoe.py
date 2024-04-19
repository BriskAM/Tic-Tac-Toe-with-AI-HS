class TicTacToe:
    def __init__(self, user_grid: str = '_' * 9) -> None:
        self.grid = [[user_grid[i] for i in range(j, j + 3)] for j in range(0, 9, 3)]
        self.current_move = 'X' if user_grid == '_' * 9 else 'X' if user_grid.count('X') <= user_grid.count(
            'O') else 'O'

    def print_grid(self) -> None:
        print('-' * 9)
        for row in self.grid:
            print('| ' + ' '.join(row).replace("_", " ") + ' |')
        print('-' * 9)

    def check_free_cell(self, row, col):
        return self.grid[row][col] == '_'

    def toggle_current_move(self):
        self.current_move = 'O' if self.current_move == 'X' else 'X'

    def toggle_cell(self, row, col):
        self.grid[row][col] = self.current_move
        self.toggle_current_move()

    def check_winner(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != '_':
                return self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != '_':
                return self.grid[0][i]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != '_':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != '_':
            return self.grid[0][2]

        return None

    def next_move(self):
        while True:
            try:
                print("Enter the coordinates: ", end='')
                x, y = map(int, input().split())
                x -= 1
                y -= 1
                if not self.check_free_cell(x, y):
                    print("This cell is occupied! Choose another one!")
                else:
                    self.toggle_cell(x, y)
                    winner = self.check_winner()
                    if winner:
                        self.print_grid()
                        print(f"{winner} wins")
                        break
                    else:
                        if sum((row.count('X') + row.count('O')) for row in self.grid) == 9:
                            self.print_grid()
                            print("Draw")
                        else:
                            self.print_grid()
                            print("Game not finished")
                        break
            except ValueError:
                print("You should enter numbers!")
            except IndexError:
                print("Coordinates should be from 1 to 3!")


if __name__ == "__main__":
    print("Enter the cells: ", end='')
    tic = TicTacToe(input())
    tic.print_grid()
    tic.next_move()
