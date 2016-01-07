#!/bin/python
#
# Conway's Game of Life in Python3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
import time
from sys import argv

def main(argv):
    # process arguments & start sim
    # init size to 0 width and 0 height
    default_size = 50
    rate = 25
    w, h = default_size, default_size
    options = ['name', 'width', 'height', 'rate']
    args = dict(zip(options,argv))
    # process arguments
    if 'help' in argv:
        print_usage()
        exit()
    if 'width' in args and args['width'].isdigit():
        w = int(args['width'])
    if 'height' in args and args['height'].isdigit():
        h = int(args['height'])
    if 'rate' in args and args['rate'].isdigit():
        rate = int(args['rate'])
    size = [w,h]
    run(size, rate)

def run(size,rate):
    "run the sim with the given height/width"
    board = gen_random(size, rate)
    display(board)
    # start the update-display loop
    running = True
    while running:
        board = update(board)
        display(board)
        time.sleep(1)
        
def gen_random(size, rate):
    "@ means the cell is filled"
    width, height = size
    board = [[' ' for x in range(width)] for x in range(height)]
    for row in range(len(board)):
        for col in range(len(board[row])):
            t = random.randint(1,100)
            if t <= rate:
                board[row][col] = "@"
    return board

def update(board):
    "loop through the board, updating each cell, return new board"
    # next_gen = [[' ' for x in range(len(board))] \
    #                  for x in range(len(board[0]))]
    # perhaps implement true "instantaneosly update by using the
    # above list and filling it in while looping through last_gen
    # board
    for row in range(len(board)):
        for col in range(len(board[row])):
            n = neighbors(board,row,col)
            alive = isalive(board,row,col)
            if alive and n < 2:
                board[row][col] = ' '
            if alive and n == 2 or n == 3:
                board[row][col] = '@'
            if alive and n > 3:
                board[row][col] = ' '
            if not alive and n == 3:
                board[row][col] == '@'
    return board

def isalive(board,row,col):
    "if the given row and col are valid in the board and == '@'"
    max_r = len(board)
    max_c = len(board[0])
    return ((row>= 0) and
            (col>=0) and
            (row<max_r) and
            (col<max_c) and
            (board[row][col] == '@'))

def neighbors(board, row, col):
    "return count of neighbors for a given cell"
    count = 0
    if isalive(board,row-1,col-1): count += 1
    if isalive(board,row-1,col  ): count += 1
    if isalive(board,row-1,col+1): count += 1
    if isalive(board,row  ,col-1): count += 1
    #if isalive(board[row ,col  ): count += 1
    if isalive(board,row  ,col+1): count += 1
    if isalive(board,row+1,col-1): count += 1
    if isalive(board,row+1,col  ): count += 1
    if isalive(board,row+1,col+1): count += 1
    return count

def display(board):
    "print the board"
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end="")
        print()

def print_usage():
    print("Conway's Game of Life in Python3")
    print("Author: Shane O'Neill")
    print("life.py - [width] [height] [rate-of-random-generation]")
    print("[width] - integer")
    print("[height] - integer")
    print("[rate-of-random-generation] - <= 0 integer <= 100")
    
if __name__ == '__main__':
    main(argv)
