import os
import random
import pdb

def clear():
    os.system('cls')

def display_board(board):
    clear()
    print('   |   |')
    print (' ' + board[7] + ' | ' + board[8] +' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' ' + board[4] + ' | ' + board[5] +' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' ' + board[1] + ' | ' + board[2] +' | ' + board[3])
    print('   |   |')



def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('Player 1: do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

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

def choose_first():
    player = random.randint(1,2)
    return player

def space_check(board, position):
    return (board[position] == ' ')

def full_board_check(board):
    for i in range (1, 10):
        if(board[i] == ' '):
            return False   
    return True

def player_choice(board):
    position = '0'
    while (position not in '1 2 3 4 5 6 7 8 9'.split(' ')) or not (space_check(board, int(position))):
        position = input ('Choose your next position (1,9)')
    return int(position)

def replay():
    playagain = ''
    playagain = input('Do you want to play again? Y or N ').upper()
    if(playagain.startswith('Y')):
        return True
    return False


def main():
    print('Welcome to Tic Tac Toe!')
    while True:
        theBoard = [' ']*10
        player1_marker, player2_marker = player_input()

        player_int = choose_first()
        print ('player_int is ', player_int)
        print( 'player' , player_int , 'choose first')

        game_on = True

        while game_on:
            if player_int == 1:
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Player 1 has won the game')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('Draw!')
                        break
                    else:
                        player_int = 2
                        
            else:
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won the game')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('Draw!')
                        break
                    else:
                        player_int = 1
                
        if not replay():
            break

main()
