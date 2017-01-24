import random
import sys 
import pprint


board = {'top-L': ' ', 'mid-L': " ", 'low-L': " ", 
         'top-M': " ", 'mid-M': " ", 'low-M': " ",
         'top-R': " ", 'mid-R': " ", 'low-R': " ",
         }
    
def printBoard(boardParam):
    print(boardParam['top-L'] + '|' + boardParam['top-M'] + '|' + boardParam['top-R'])
    print('-+-+-')
    print(boardParam['mid-L'] + '|' + boardParam['mid-M'] + '|' + boardParam['mid-R'])
    print('-+-+-')
    print(boardParam['low-L'] + '|' + boardParam['low-M'] + '|' + boardParam['low-R'])
    print('-+-+-')

turn = 'X'
for i in range(9):
    printBoard(board)
    print('Turn for ' + turn + '. Move to which space?')
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(board)
