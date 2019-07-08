#!/usr/bin/env python

import copy

DEBUG = False

class Board:
    def __init__(self):
        self.openSpaces = set(range(9))
        self.xSpaces = set()
        self.oSpaces = set()

winningSets = list()
for i in range(0, 3):
    # ###
    # ...
    # ...
    winningSets.append(set(range(i * 3, i * 3 + 3)))

    # #..
    # #..
    # #..
    winningSets.append(set(range(i, i + 7, 3)))

# #..
# .#.
# ..#
winningSets.append(set(range(0, 9, 4)))
winningSets.append(set(range(2, 7, 2)))

def wonBoard(board):
    global winningSets
    for winningSet in winningSets:
        if len(board.xSpaces.intersection(winningSet)) == 3                    \
        or len(board.oSpaces.intersection(winningSet)) == 3:
            return True

    return False

i = 0
def makeMove(board):
    global i
    i += 1
    possibleBoards = list()

    if len(board.openSpaces) == 0:
        # Draw.
        possibleBoards.append(board)

    for space in board.openSpaces:
        boardCopy = Board()
        boardCopy.openSpaces = set(board.openSpaces)
        boardCopy.xSpaces = set(board.xSpaces)
        boardCopy.oSpaces = set(board.oSpaces)

        if len(boardCopy.openSpaces) % 2 == 1:
            # Need a X.
            boardCopy.xSpaces.add(space)
        else:
            # Need a Y.
            boardCopy.oSpaces.add(space)


        boardCopy.openSpaces.discard(space)

        if wonBoard(board):
            possibleBoards.append(board)
            return possibleBoards
        else:
            possibleBoards += makeMove(boardCopy)

    return possibleBoards


startBoard = Board()
possibleBoards = makeMove(startBoard)

possibility = 0
for possibleBoard in possibleBoards:
    output = list("         ")
    for xSpace in possibleBoard.xSpaces:
        output[xSpace] = 'X'
    for oSpace in possibleBoard.oSpaces:
        output[oSpace] = 'O'

    if DEBUG:
        print("Possible end-game #" + str(possibility) + ":")
        for i in range(0, 3):
            row = ""
            for j in range(0, 3):
                row += output[i * 3 + j]
            print(row)

        print("")

    possibility += 1

print("# of possible Tic Tac Toe games: " + str(possibility))
