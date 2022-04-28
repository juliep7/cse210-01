'''
CSE 210: Week 2
Assignment: Tic-Tac-Toe
Author: Julie Peterson
'''

def main():
    player = next_player("")
    board = create_board()
    while not (verify_winner(board) or no_winner(board)):
        display_board(board)
        take_turn(player, board)
        player = next_player(player)
    display_board(board)
    if no_winner(board) == True:
        print("It's a draw. Thanks for playing!")
    elif verify_winner(board) == True:    
        print("WINNER! Thanks for playing!") 
    print()

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def no_winner(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True 


def verify_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


def take_turn(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"


if __name__ == "__main__":
    main()