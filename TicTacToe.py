import os
import random
import pdb

def clear():
    os.system('cls')

def display_board(board):
    clear()
    print (' ' + board[1] + ' | ' + board[2] +' | ' + board[3])
    print('-----------')
    print (' ' + board[4] + ' | ' + board[5] +' | ' + board[6])
    print('-----------')
    print (' ' + board[7] + ' | ' + board[8] +' | ' + board[9])
    
# player 1 insert marker
def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('Player 1: do you want to use O or X? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# check if the player wins the game
def win_check(board, mark):
    top = (board[7] == mark and board[8] == mark and board[9] == mark)
    mid = (board[4] == mark and board[5] == mark and board[6] == mark)
    down = (board[1] == mark and board[2] == mark and board[3] == mark)
    left = (board[7] == mark and board[4] == mark and board[1] == mark)
    m = (board[8] == mark and board[5] == mark and board[2] == mark)
    right = (board[9] == mark and board[6] == mark and board[3] == mark)
    cross = (board[7] == mark and board[5] == mark and board[3] == mark)
    backcross = (board[9] == mark and board[5] == mark and board[1] == mark)
    return top or mid or down or left or m or right or cross or backcross

# check if the board has space for mark
def full_board_check(board):
    for i in range (1, 10):
        if(board[i] == ' '):
            return False   
    return True

def player_choice(board, player_int):
    position = '0'
    while (position not in '1 2 3 4 5 6 7 8 9'.split(' ')) or (board[int(position)] != ' '):
        if (board[int(position)] != ' '):
            print('This position is not empty')
        player_insert_position = 'Player '+ str(player_int) + ', please choose your next position (1,9)'
        position = input (player_insert_position)
    return int(position)

def replay():
    playagain = ''
    playagain = input('Do you want to play again? Y or N ').upper()
    if(playagain.startswith('Y')):
        return True
    return False 

def one_player_turn(player_int, board, player_marker):
    display_board(board)
    position = player_choice(board, player_int)
    board[position] = player_marker
    
    if win_check(board, player_marker):
        display_board(board)
        print('Congratulations!',  'Player ', player_int, ' has won the game')
        return False, player_int
    else:
        if full_board_check(board):
            display_board(board)
            print('Draw!')
            return False, player_int
        else:
            if player_int == 1:
                player_int = 2
            else:
                player_int = 1
    return True, player_int


def main():
    print('Welcome to Tic Tac Toe!')
    while True:
        theBoard = [' ']*10
        # players choose marker
        player1_marker, player2_marker = player_input()
        
        # decide which player choose first
        player_int = random.randint(1,2)
        print ('player_int is ', player_int)
        print( 'player' , player_int , 'choose first')

        game_on = True

        while game_on:
            if player_int == 1:
                game_on, player_int = one_player_turn(player_int, theBoard, player1_marker)
                        
            else:
                game_on, player_int = one_player_turn(player_int, theBoard, player2_marker)
                
        if not replay():
            print('Thanks for playing this game!')
            break

if __name__ == '__main__':
    main()