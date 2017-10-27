from time import sleep
findAlpha = list('abcdefghijklmnopqrstuvwxyz')
for x in range(26):
    findAlpha[x] = findAlpha[x].upper()


class Piece():
    def __init__(self, colour, position):
        self.position = position
        self.colour = colour

    def checkKill(self, dest):  # check if the move is killing a piece of the opponent.
        colour = self.colour
        position = self.position
        src_x = findAlpha.uppercase.index(position[0])
        src_y = position[1]
        self.dest = dest
        dest_x = dest[0]
        dest_y = dest[1]
        if colour == "R":
            if dest_x > src_x:  # check if the destination move is 2 boxes away in the x and y direction
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

    def checkLegal(self, dest):  # check if the move being made is a legal move.
        colour = self.colour
        position = self.position
        src_x = findAlpha.uppercase.index(position[0])  # index of letter
        src_y = position[1]
        self.dest = dest
        dest_x = dest[0]
        dest_y = dest[1]
        columnNum = src_x + 1  # cartesian row number
        rowNum = src_y
        if checkKill(dest) == False:
            if colour == "R":
                if columnNum >= 2 and columnNum <= 7:  # check if its in in the center portion of the board
                    for i in [-1, 1]:
                        if type(layout[x + i][y + 1]) != Piece:
                            return True
                        else:
                            return False
                elif columnNum == 1:  # check if its on left/right edges
                    if type(layout[x + 1][y + 1]) != Piece:
                        return True
                    else:
                        return False
                elif columnNum == 8:
                    if type(layout[x - 1][y + 1]) != Piece:
                        return True
                    else:
                        return False
            if colour == "B":
                if columnNum >= 2 and columnNum <= 7:
                    for i in [-1, 1]:
                        if type(layout[x + i][y - 1]) != Piece:
                            return True
                        else:
                            return False
                elif columnNum == 1:
                    if type(layout[x + 1][y - 1]) != Piece:
                        return True
                    else:
                        return False
                elif columnNum == 8:
                    if type(layout[x - 1][y - 1]) != Piece:
                        return True
                    else:
                        return False

    def move(self, dest, layout):
        self.position = dest
        Board.updateDataStructure(layout)


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

    def createDataStructure(self, layout):
        print()
        print()
        temp = []
        layout_temp = []
        for i in Board.alpha_co:
            for j in layout:
                if type(j) == Piece:
                    if j.position[0] == i:
                        temp.append(j)
                else:
                    if j[0] == i:
                        temp.append(j)
            layout_temp.append(temp)
            temp = []
        print(layout_temp)
        return layout_temp

    def updateDataStructure(layout):
        updated = False
        temp = []
        loop1 = True
        while not updated:
            for x in range(0, len(layout)):
                for y in range(0, len(layout[x])):
                    current_pos = findAlpha[x] + str(y + 1)
                    current_obj = layout[x][y]
                    if (x, y) != (8, 8) and loop1 == True:
                        if type(current_obj) == Piece:
                            if current_obj.position != current_pos:
                                temp.append(current_obj)
                                updated = False
                                layout[x][y] = current_pos

                    else:
                        for item in temp:
                            if item.position == current_pos:
                                layout[x][y] = item
                                temp.remove(item)
                                if len(temp) == 0:
                                    updated = True
            loop1 = False

    def printLayout(self, layout):
        temp = []
        final = []
        count = 0
        for w in Board.num_co:
            for x in layout:
                for y in x:
                    if type(y) == Piece:
                        if y.position[1] == str(w):
                            temp.append(y.colour)
                    else:
                        if y[1] == str(w):
                            temp.append("X")
            final.append(temp)
            temp = []
        for t in reversed(final):
            print(" ".join(t))


board = Board()
pieces = board.createBoard()
layout = board.createDataStructure(pieces)
board.printLayout(layout)
print()
print()
layout[1][2].move('A5', layout)
board.printLayout(layout)