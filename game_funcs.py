import numpy as np
from collections import defaultdict
import random

#starting game
def start_game():
    board = np.zeros((16), dtype="int")
    first=random.sample(range(16), 1)
    board[first]=2
    board = board.reshape((4,4))
    return board

#checking if game is over 
def horizontal_move_exists(board):
        for i in range(4):
            for j in range(3):
                if board[i][j] == board[i][j + 1]:
                    return True
        return False


def vertical_move_exists(board):
        for i in range(3):
            for j in range(4):
                if board[i][j] == board[i + 1][j]:
                    return True
        return False

def what_value(board,x_coor,y_coor):
    if x_coor>3 or y_coor>3:
        print("Out of Bounds")
        return
    return board[x_coor][y_coor]

def add_num_tile(board,x_coor,y_coor,num):
    board[x_coor][y_coor]=num

#functions which are used in our four game functions
def push_right(board,names):
    new = np.zeros((4,4), dtype="int")
    new_names=np.array([["" for _ in range(4)] for _ in range(4)],dtype='object')
  #  print("new_names",new_names)
    flag = False
    for row in range(4):
        count = 3
        for col in range(3, -1, -1):
            if board[row][col] != 0:
                new[row][count] = board[row][col]
                new_names[row][count]=new_names[row][count]+names[row][col]
              #  print(type(new_names[row][count]))
              #  print(type(names[row][count]))
              #  print("fox",new_names[row][count],names[row][col])
                if col != count:
                    flag = True
                count -= 1
    return (new, flag ,new_names)

def merge(board,op,names):
    score = 0
    flag = False
    for row in range(4):
        for col in range(3, 0, -1):
            if board[row][col] == board[row][col-1] and board[row][col] != 0:
                if op=='+':
                    board[row][col] *= 2
                   # print("checking",names[row][col])
                    names[row][col]=names[row][col]+names[row][col-1]
                if op=='-':
                    board[row][col] = 0
                    names[row][col]=""
                if op=='*':
                #    print("checking",names[row][col])
                    board[row][col] = board[row][col]*board[row][col-1]
                    names[row][col]=names[row][col]+names[row][col-1]
                if op=='/':
                    board[row][col] = 1
                 #   print("checking",names[row][col])
                    names[row][col]=names[row][col]+names[row][col-1]
                score += board[row][col]
                board[row][col-1] = 0
                names[row][col-1]=""
                flag = True
    return (board, flag, score ,names)

#four game functions
def move_up(board,op,names):
  ##  print(names)
    rotated_board = np.rot90(board, -1)
    rotated_names = np.rot90(names,-1)
   # print(rotated_names)
   # print("tiger")
    pushed_board, has_pushed,pushed_names = push_right(rotated_board,rotated_names)
  #  print(pushed_names)
   # print("deer")
    merged_board, has_merged, score,merged_names = merge(pushed_board,op,pushed_names)
  #  print(merged_names)
   # print('tiger2')
    second_pushed_board, _,second_pushed_names = push_right(merged_board,merged_names)
    rotated_back_board= np.rot90(second_pushed_board)
    rotated_back_names=np.rot90(second_pushed_names)
    move_made = has_pushed or has_merged
    return rotated_back_board, move_made, score,rotated_back_names
   
def move_down(board,op,names):
    board = np.rot90(board)
    names =np. rot90(names)
    board, has_pushed,names = push_right(board,names)
    board, has_merged, score,names = merge(board,op,names)
    board, _ ,names= push_right(board,names)
    board = np.rot90(board, -1)
    names = np.rot90(names,-1)
    move_made = has_pushed or has_merged
    return board, move_made, score ,names

def move_left(board,op,names):
    board = np.rot90(board, 2)
    names = np.rot90(names ,2)
    board, has_pushed ,names= push_right(board,names)
    board, has_merged, score ,names = merge(board,op,names)
    board, _,names = push_right(board,names)
    board = np.rot90(board, -2)
    names =np.rot90(names ,-2)
    move_made = has_pushed or has_merged
    return board, move_made, score,names

def move_right(board,op,names):
    board, has_pushed ,names = push_right(board,names)
    board, has_merged, score,names = merge(board,op,names)
    board, _ ,names= push_right(board,names)
    move_made = has_pushed or has_merged
    return board, move_made, score ,names

#random move for ai
def random_move(board):
    move_made = False
    possible_moves = [move_right, move_up, move_down, move_left]
    while not move_made and len(possible_moves) > 0:
        move_index = random.randint(0, len(possible_moves)-1)
        move = possible_moves[move_index]
        board, move_made, score  = move(board)
        if move_made:
            return board, True, score
        possible_moves.pop(move_index)
    return board, False, score

#adding new tile
def add_new_tile(board):
    nameList = [2,4]
    tile_value=random.choices(nameList, cum_weights=(90,10), k=1)
    tile_rows, tile_cols= np.nonzero(np.logical_not(board))
    tile_loc = random.randint(0, len(tile_rows)-1)
    board[tile_rows[tile_loc], tile_cols[tile_loc]] = tile_value[0]
    return board
