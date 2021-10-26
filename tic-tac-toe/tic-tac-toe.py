import random

board = ["-" for i in range(1, 11)]
game_started = True


def display_board():
    print(board[1] + "|" + board[2] + "|"+board[3])
    print(board[4] + "|" + board[5] + "|"+board[6])
    print(board[7] + "|" + board[8] + "|"+board[9]+"\n")


print("Lets play TIC-TAC-TOE\n")
shuf_player = ["X", "0"]
current_player = random.choice(shuf_player)


def take_in():
    print(f"{current_player}'s turn")
    postion = int(input("enter the position :: "))
    print("")

    if postion not in range(1, 10):
        print("Postion should be between 1-9\n")
    elif board[postion] == "X" or board[postion] == "0":
        print("position is already filled up")
        take_in()
    else:
        board[postion] = current_player


def check_winner():
    if (board[1] == board[2] == board[3] == current_player) or (board[4] == board[5] == board[6] == current_player) or (board[7] == board[8] == board[9] == current_player) or (board[1] == board[4] == board[7] == current_player) or (board[2] == board[5] == board[8] == current_player) or (board[3] == board[6] == board[9] == current_player) or (board[1] == board[5] == board[9] == current_player) or (board[3] == board[5] == board[7] == current_player):
        print(current_player + " is a winner")
        exit()

    elif "-" not in board[1:10]:
        print("game tied")
        exit()


def shuffle_player():
    global current_player
    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"


while game_started:
    display_board()
    take_in()
    check_winner()
    shuffle_player()
