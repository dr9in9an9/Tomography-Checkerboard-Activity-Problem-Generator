# author: Jesus Sisniega-Serrano
# version: 10-8-2025

# scroll to very bottom to use.

import random

mineboard = [] # 
xrayboard = []
boardsize = 0

debug = False # debugger mode.

# generates a board with mines.
def mineboardGen(size, crossNum):
    global mineboard
    global xrayboard
    global boardsize

    boardsize = size

    # initializes board to a square 2-D array of x size.
    mineboard = [0]*size
    for i in range(size):
        mineboard[i] = [0]*size

    # sets x number of crosses.
    for i in range(crossNum):
        spotR = random.randint(0, size-1)
        spotC = random.randint(0, size-1)
        
        while mineboard[spotR][spotC] == 1:
            spotR = random.randint(0, size-1)
            spotC = random.randint(0, size-1)
        
        mineboard[spotR][spotC] = 1

# finds the amount of mines in the path of a certain point.
def xraySpot(spotR, spotC):
    global mineboard
    global xrayboard
    global boardsize

    count = 0

    # checks row and column.
    for i in range(boardsize):
        if mineboard[spotR][i] == 1:
            count = count + 1
            if debug: print("found in row")
        
        if mineboard[i][spotC] == 1:
            count = count + 1
            if debug: print("found in column")

    # used to check diagonals.
    currR = spotR
    currC = spotC

    # checks top-left to bottom-right diagonal.
    while (currR != 0) and (currC != 0):
        currR = currR - 1
        currC = currC - 1

    while (currR + 1 < boardsize) and (currC + 1 < boardsize):
        if mineboard[currR][currC] == 1:
            count = count + 1
            if debug: print("found in tl-br1")

        currR = currR + 1
        currC = currC + 1

    if mineboard[currR][currC] == 1:
        count = count + 1
        if debug: print("found in tl-br2")
        

    # checks bottom-left to top-right diagonal.
    currR = spotR
    currC = spotC

    while (currR + 1 < boardsize) and (currC - 1 >= 0):
        currR = currR + 1
        currC = currC - 1

    if mineboard[currR][currC] == 1:
        count = count + 1
        if debug: print("found in bl-tr1")

    while (currR - 1 >= 0) and (currC + 1 < boardsize):
        currR = currR - 1
        currC = currC + 1

        if mineboard[currR][currC] == 1:
            count = count + 1
            if debug: print("found in bl-tr2")

    return count
    
# simple array printer.
def arrPrint(arr):
    size = len(arr)

    for i in range(size):
        for j in range(size):
            print(arr[i][j], end=" ")
        print(" ")
    print(" ")

# generates an xrayboard from the mineboard.
def xrayboardGen():
    global mineboard
    global xrayboard
    global boardsize
    
    # initializes xrayboard to a square 2-D array of x size.
    xrayboard = [0]*boardsize
    for i in range(boardsize):
        xrayboard[i] = [0]*boardsize

    for i in range(boardsize):
        for j in range(boardsize):
            if debug: print(i, end=" ")
            if debug: print(j)
            xrayboard[i][j] = xraySpot(i, j)

# only edit below this line.
############################################################################################################

mineboardGen(5,5) # set size of square board, set number of crosses to populate board with.

# below, remove the hastag and change the 1s and 0s to desired board if you want to test a certain board.
#mineboard = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]

############################################################################################################
# DON'T TOUCH BELOW THIS LINE.
xrayboardGen()
arrPrint(mineboard)
arrPrint(xrayboard)