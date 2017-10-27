from time import sleep
findAlpha = list('abcdefghijklmnopqrstuvwxyz')
for x in range(26):
    findAlpha[x] = findAlpha[x].upper()


class Piece():
    def __init__(self, colour, position, rank):
        self.position = position
        self.colour = colour
        self.rank = rank

    def checkLegalKill(self, dest):  # check if the move is killing a piece of the opponent.
        colour = self.colour
        position = self.position
        rank = self.rank
        src_x = findAlpha.index(position[0])
        src_y = int(position[1]) - 1
        self.dest = dest
        dest_x = findAlpha.index(dest[0])
        dest_y = int(dest[1]) - 1
        noResult = (False, None)
        if rank == 1:
            if colour == "R":
                if dest_x > src_x:
                    if type(layout[dest_x - 1][dest_y - 1]) == Piece:
                        if layout[dest_x - 1][dest_y - 1].colour == "B":
                            if dest_x - 2 == src_x and dest_y - 2 == src_y:
                                return (True, layout[dest_x - 1][dest_y - 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                elif dest_x < src_x:
                    if type(layout[dest_x + 1][dest_y - 1]) == Piece:
                        if layout[dest_x + 1][dest_y - 1].colour == "B":
                            if dest_x + 2 == src_x and dest_y - 2 == src_y:
                                return (True, layout[dest_x + 1][dest_y - 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                else: return noResult
            elif colour == "B":
                if dest_x > src_x:
                    if type(layout[dest_x - 1][dest_y + 1]) == Piece:
                        if layout[dest_x - 1][dest_y + 1].colour == "R":
                            if dest_x - 2 == src_x and dest_y + 2 == src_y:
                                return (True, layout[dest_x - 1][dest_y + 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                elif dest_x < src_x:
                    if type(layout[dest_x + 1][dest_y + 1]) == Piece:
                        if layout[dest_x + 1][dest_y + 1].colour == "R":
                            if dest_x + 2 == src_x and dest_y + 2 == src_y:
                                return (True, layout[dest_x + 1][dest_y + 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                else: return noResult
        elif rank == 2:
            if dest_x > src_x:
                if dest_y > src_x:
                    if type(layout[dest_x - 1][dest_y - 1]) == Piece:
                        if layout[dest_x - 1][dest_y - 1].colour != colour:
                            if (dest_x - 2 == src_x and dest_y - 2 == src_y):
                                return (True, layout[dest_x - 1][dest_y - 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                elif dest_y < src_x:
                    if type(layout[dest_x - 1][dest_y + 1]) == Piece:
                        if layout[dest_x - 1][dest_y + 1].colour != colour:
                            if (dest_x - 2 == src_x and dest_y + 2 == src_y):
                                return (True, layout[dest_x - 1][dest_y + 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                else: return noResult
            elif dest_x < src_x:
                if dest_y > src_x:
                    if type(layout[dest_x + 1][dest_y - 1]) == Piece:
                        if layout[dest_x + 1][dest_y - 1].colour != colour:
                            if (dest_x + 2 == src_x and dest_y - 2 == src_y):
                                return (True, layout[dest_x + 1][dest_y - 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                elif dest_y < src_y:
                    if type(layout[dest_x + 1][dest_y + 1]) == Piece:
                        if layout[dest_x + 1][dest_y + 1].colour != colour:
                            if (dest_x + 2 == src_x and dest_y + 2 == src_y):
                                return (True, layout[dest_x + 1][dest_y + 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                else: return noResult
            
            
    def checkLegal(self, dest):  # check if the move being made is a legal move.
        colour = self.colour
        position = self.position
        src_x = findAlpha.index(position[0])
        src_y = int(position[1]) - 1
        self.dest = dest
        dest_x = findAlpha.index(dest[0])
        dest_y = int(dest[1]) - 1
        columnNum = src_x + 1  # cartesian row number
        rowNum = src_y
        noKillTrue = (True, None)
        noKillFalse = (False, None)
        
        if self.checkLegalKill(dest)[0] == False:
            if self.rank == 1:
                if colour == "R":
                    if type(layout[dest_x][dest_y]) != Piece:
                        if dest_x > src_x:
                            if dest_x - 1 == src_x and dest_y - 1 == src_y:
                                return noKillTrue
                            else: return noKillFalse
                        elif dest_x < src_x:
                            if dest_x + 1 == src_x and dest_y - 1 == src_y:
                                return noKillTrue
                            else: return noKillFalse
                        else: return noKillFalse
                    else: return noKillFalse            

                if colour == "B":
                    if type(layout[dest_x][dest_y]) != Piece:
                        if dest_x > src_x:
                            if dest_x - 1 == src_x and dest_y + 1 == src_y:
                                return noKillTrue
                            else: return noKillFalse
                        elif dest_x < src_x:
                            if dest_x + 1 == src_x and dest_y + 1 == src_y:
                                return noKillTrue
                            else: return noKillFalse
                        else: return noKillFalse
                    else: return noKillFalse
            elif self.rank == 2:
                if type(layout[dest_x][dest_y]) != Piece:
                    if dest_x > src_x:
                        if dest_y > src_y:
                            if dest_x - 1 == src_x and dest_y - 1 == src_y:
                                return noKillTrue
                            else: return noKillFalse
                        if dest_y < src_y:
                            if dest_x - 1 == src_x and dest_y + 1 == src_y:
                                return noKillTrue
                            else: return noKillFalse
                    elif dest_x < src_x:
                        if dest_y > src_y:
                            if dest_x + 1 == src_x and dest_y - 1 == src_y:
                                return noKillTrue
                            else: return noKillFalse
                        elif dest_y < src_y:
                            if dest_x + 1 == src_x and dest_y + 1 == src_y:
                                return noKillTrue
                            else: return noKillFalse
                        else: return noKillFalse
                    else: return noKillFalse
                else: return noKillFalse
        elif self.checkLegalKill(dest)[0] == True:
            return (True, self.checkLegalKill(dest)[1])

    def move(self, dest, layout):
        legal = self.checkLegal(dest)
        if legal[0] == True:
            self.position = dest
            Board.updateDataStructure(layout, legal)
        else:
            print("Invalid Move")
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
                    Board.layout.append(Piece("R", (Board.alpha_co[xCo] + str(yCo)), 1))
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
                    Board.layout.append(Piece("B", (Board.alpha_co[xCo] + str(yCo)), 1))
                    blank = True
                elif blank == True:
                    Board.layout.append(Board.alpha_co[xCo] + str(yCo))
                    blank = False
            blank = not blank
        return Board.layout

    def createDataStructure(self, layout):
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
        return layout_temp

    def updateDataStructure(layout, trueKill):
        updated = False
        temp = []
        loop1 = True
        while not updated:
            for x in range(0, len(layout)):
                for y in range(0, len(layout[x])):
                    current_pos = findAlpha[x] + str(y + 1)
                    current_obj = layout[x][y]
                    if current_obj == trueKill[1]:
                        layout[x][y] = current_pos
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
        for t,z in zip(reversed(final),range(8,0,-1)):
            print(str(z) +  " |" + " ".join(t))
        print("   " + "- - - - - - - -")
        print("   " + "A B C D E F G H")
def returnArrayCo(position):
    x = findAlpha.index(position[0])
    y = int(position[1]) - 1
    return layout[x][y]
board = Board()
pieces = board.createBoard()
layout = board.createDataStructure(pieces)
print()
print()

move_list = [['D3', 'C4'], ['E6', 'D5'], ['C4', 'E6'], ['F7','D5']]
for i in move_list:
    returnArrayCo(i[0]).move(i[1], layout)
board.printLayout(layout)
