import string as findAlpha
from time import sleep

class Piece():
    def __init__(self, colour, position):
        self.position = position
        self.colour = colour

    def checkKill(self, dest): #check if the move is killing a piece of the opponent.
        colour = self.colour
        position = self.position
        src_x = findAlpha.uppercase.index(position[0])
        src_y = position[1]
        self.dest = dest
        dest_x = dest[0]
        dest_y = dest[1]
        if colour == "R":
            if dest_x > src_x: #check if the destination move is 2 boxes away in the x and y direction
                if dest_x - 2 == src_x and dest_y - 2 == src_y:
                    return True
                else:
                    return False
            elif dest_x < src_x:
                if dest_x + 2 == src_x and dest_y - 2 == src_y:
                    return True
                else:
                    return False
        elif colour == "B":
            if dest_x > src_x:
                if dest_x - 2 == src_x and dest_y + 2 == src_y:
                    return True
                else:
                    return False
            elif dest_x < src_x:
                if dest_x + 2 == src_x and dest_y + 2 == src_y:
                    return True
                else:
                    return False

    def checkLegal(self, dest): #check if the move being made is a legal move.
        colour = self.colour
        position = self.position
        src_x = findAlpha.uppercase.index(position[0]) #index of letter
        src_y = position[1]
        self.dest = dest
        dest_x = dest[0]
        dest_y = dest[1]
        columnNum = src_x + 1  # cartesian row number
        rowNum = src_y
        if checkKill(dest) == False:
            if colour == "R":
                if columnNum >= 2 and columnNum <= 7: #check if its in in the center portion of the board
                    for i in [-1, 1]:
                        if type(layout[x + i][y+1]) != Piece:
                            return True
                        else: return False
                elif columnNum == 1: #check if its on left/right edges
                    if type(layout[x+1][y+1]) != Piece:
                        return True
                    else: return False
                elif columnNum == 8:
                    if type(layout[x-1][y+1]) != Piece:
                        return True
                    else: return False
            if colour == "B":
                if columnNum >= 2 and columnNum <= 7:
                    for i in [-1, 1]:
                        if type(layout[x + i][y-1]) != Piece:
                            return True
                        else: return False
                elif columnNum == 1:
                    if type(layout[x+1][y-1]) != Piece:
                        return True
                    else: return False
                elif columnNum == 8:
                    if type(layout[x-1][y-1]) != Piece:
                        return True
                    else: return False



    def move(self, dest):
        src = self.position


class Board():
    layout = []
    num_co = [t for t in range(1, 9)]
    alpha_co = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def __init__(self):
        pass


    def createBoard(self):
        blank = True
        start = 0
        end = 8
        for yCo in Board.num_co[0:3]:
            for xCo in range(0, 8):
                if blank == False:
                    Board.layout.append(Piece("R", (Board.alpha_co[xCo] + str(yCo))))
                    blank = True
                elif blank == True:
                    Board.layout.append(Board.alpha_co[xCo] + str(yCo))
                    blank = False
            blank = not blank
        for yCo in Board.num_co[3:5]:
            for xCo in range(0, 8):
                Board.layout.append(Board.alpha_co[xCo] + str(yCo))
        for yCo in Board.num_co[5:8]:
            for xCo in range(0, 8):
                if blank == False:
                    Board.layout.append(Piece("B", (Board.alpha_co[xCo] + str(yCo))))
                    blank = True
                elif blank == True:
                    Board.layout.append(Board.alpha_co[xCo] + str(yCo))
                    blank = False
            blank = not blank
        return Board.layout

    def printPiecePositions(self, layout):
        temp = []
        final = []
        count = 0
        for x in layout:
            if type(x) == Piece:
                temp.append(x.colour)
            else:
                temp.append("X")

            if count == 7:
                final.append(temp)
                temp = []
                count = 0
            else:
                count += 1
        for t in reversed(final):
            print(" ".join(t))
        
    def createDataStructure(self, layout):
        print(layout)
        print()
        print()
        temp = []
        layout_temp = []
        for i in Board.alpha_co:
            for j in layout:
                if type(j) == Piece:
                    if j.position[0] == i:
                        temp.append(j)
                        print(temp)
                        sleep(1)
                else:
                    if j[0] == i:
                        temp.append(j)
                        print(temp)
                        sleep(1)
            layout_temp.append(temp)
            temp = []
        return layout_temp

board = Board()
pieces = board.createBoard()
board.printPiecePositions(pieces)
#layout = board.createDataStructure(pieces)

#board.printLayout(layout)
