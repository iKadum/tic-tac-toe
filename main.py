import os


class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]
        self.board = ""
        self.positions = []
        self.count = 0

    def display_board(self):
        self.board = f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} \n" \
                     "-----------\n" \
                     f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} \n" \
                     "-----------\n" \
                     f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} \n"
        cls()
        print(self.board)

    def write_to_board(self, cell, text):
        self.cells[cell - 1] = text
        # self.display_board()

    def check_winner(self):
        c = self.cells
        if c[0] == c[1] == c[2] == "x" or c[3] == c[4] == c[5] == "x" or c[6] == c[7] == c[8] == "x" or \
                c[0] == c[3] == c[6] == "x" or c[1] == c[4] == c[7] == "x" or c[2] == c[5] == c[8] == "x" or\
                c[0] == c[4] == c[8] == "x" or c[2] == c[4] == c[6] == "x":
            return "Player 1"
        if c[0] == c[1] == c[2] == "o" or c[3] == c[4] == c[5] == "o" or c[6] == c[7] == c[8] == "o" or \
                c[0] == c[3] == c[6] == "o" or c[1] == c[4] == c[7] == "o" or c[2] == c[5] == c[8] == "o" or\
                c[0] == c[4] == c[8] == "o" or c[2] == c[4] == c[6] == "o":
            return "Player 2"
        # return False


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def quit_game():
    cls()
    print(45 * "#")
    print("Thank you for playing 'Python Tic-Tac-Toe'\nBye!")
    print(45 * "#" + "\n\n")


cls()
print(48 * "#")
print("Welcome to 'Python Tic-Tac-Toe'")
print("You can play by entering the number of the cell.")
print(48 * "#")
input("\n(Press ENTER)")
example_board = Board()
for x in range(9):
    example_board.write_to_board(x + 1, x + 1)
example_board.display_board()
print("The cells are numerated as in this example board.\n")
input("All clear? Press ENTER to start the game!")

board = Board()
board.display_board()

while True:
    winner = board.check_winner()
    if winner or len(board.positions) > 8:
        if winner:
            print(f"Congratulations Player {winner}, you won!\n")
        else:
            print("Draw!\n")

        another = input("Do you want to play another game? (enter 'y' to play) ").lower()
        if another != "y" and another != "yes":
            quit_game()
            break

        board = Board()
        board.display_board()

    player = board.count % 2 + 1
    if player == 1:
        sign = "x"
    else:
        sign = "o"

    try:
        position = int(input(f"Player {player}, choose the cell to put {sign}! "))
    except ValueError:
        answer = input("Value error! Do you wanna quit the game? (enter 'y' to quit) ").lower()
        if answer == "y":
            quit_game()
            break
        position = 0  # to trigger elif below

    if position in board.positions:
        print("This cell is already taken, please choose another cell.")
    elif position < 1 or position > 9:
        print("Please enter a number between 1 and 9.")
    else:
        board.write_to_board(position, sign)
        board.display_board()
        board.positions.append(position)
        board.count += 1
