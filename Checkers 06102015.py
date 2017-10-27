#----------------------
##BY ROHIT PRASAD
#----------------------



from time import sleep
import pygame
from pygame.locals import *

fpsClock = pygame.time.Clock()
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
            if colour == "W":
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
                        if layout[dest_x - 1][dest_y + 1].colour == "W":
                            if dest_x - 2 == src_x and dest_y + 2 == src_y:
                                return (True, layout[dest_x - 1][dest_y + 1])
                            else: return noResult
                        else: return noResult
                    else: return noResult
                elif dest_x < src_x:
                    if type(layout[dest_x + 1][dest_y + 1]) == Piece:
                        if layout[dest_x + 1][dest_y + 1].colour == "W":
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
        return noResult


    def checkLegal(self, dest, override):  # check if the move being made is a legal move.
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

        if override:
            kill = False
        else:
            kill = self.checkLegalKill(dest)[0]
            
        if kill == False:
            if self.rank == 1:
                if colour == "W":
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
        elif kill == True:
            return (True, self.checkLegalKill(dest)[1])

    def checkPromotion(self):
        colour = self.colour
        position = self.position

        if self.colour == "B":
            if self.position[1] == "1":
                self.rank = 2
        if self.colour == "W":
            if self.position[1] == "8":
                self.rank = 2


    def move(self, dest, layout):
        legal = self.checkLegal(dest, False)
        if legal[0] == True:
            self.position = dest
            self.checkPromotion()
            BoardStructure.updateDataStructure(layout, legal)
        else:
            print("Invalid Move")

class BoardStructure():
    layout = []
    num_co = [t for t in range(1, 9)]
    alpha_co = ["A", "B", "C", "D", "E", "F", "G", "H"]

    def __init__(self):
        pass

    def createBoard(self):
        blank = True
        for yCo in BoardStructure.num_co[0:3]:
            for xCo in range(0, 8):
                if blank == False:
                    BoardStructure.layout.append(Piece("W", (BoardStructure.alpha_co[xCo] + str(yCo)), 1))
                    blank = True
                elif blank == True:
                    BoardStructure.layout.append(BoardStructure.alpha_co[xCo] + str(yCo))
                    blank = False
            blank = not blank
        for yCo in BoardStructure.num_co[3:5]:
            for xCo in range(0, 8):
                BoardStructure.layout.append(BoardStructure.alpha_co[xCo] + str(yCo))
        for yCo in BoardStructure.num_co[5:8]:
            for xCo in range(0, 8):
                if blank == False:
                    BoardStructure.layout.append(Piece("B", (BoardStructure.alpha_co[xCo] + str(yCo)), 1))
                    blank = True
                elif blank == True:
                    BoardStructure.layout.append(BoardStructure.alpha_co[xCo] + str(yCo))
                    blank = False
            blank = not blank
        return BoardStructure.layout

    def createDataStructure(self, layout):
        temp = []
        layout_temp = []
        for i in BoardStructure.alpha_co:
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
        for w in BoardStructure.num_co:
            for x in layout:
                for y in x:
                    if type(y) == Piece:
                        if y.position[1] == str(w):
                            temp.append(y.colour)
                    else:
                        if y[1] == str(w):
                            temp.append("#")
            final.append(temp)
            temp = []
        for t,z in zip(reversed(final),range(8,0,-1)):
            print(str(z) +  " |" + " ".join(t))
        print("   " + "- - - - - - - -")
        print("   " + "A B C D E F G H")

#CONSTANTS
WX = (87,88)
WY = (87,88)
SX = 346.5
SY = 664.46
cellColour = (65,161,133)
cellHighlight = (72, 113, 159)
class Board():
    def __init__(self, layout):
        self.layout = layout

    def generateDrawLayout(self):

        drawLayout = []
        tempX, tempY = SX, SY
        lessY, lessX = True, True
        WIDTH, HEIGHT = WX[0], WY[0]
        tempList = []
        #tempList.append((tempX, tempY, WIDTH, HEIGHT))
        for i in range(8):
            tempList.append((tempX, tempY, WIDTH, HEIGHT))
            for j in range(7):
                if lessY:
                    HEIGHT = WY[0]
                    tempY -= HEIGHT
                    lessY = False
                elif not lessY:
                    HEIGHT = WY[1]
                    tempY -= HEIGHT
                    lessY = True
                tempList.append((tempX, tempY, WIDTH, HEIGHT))
            drawLayout.append(tempList)
            tempList = []
            if lessX:
                WIDTH = WX[0]
                lessX = False
            elif not lessX:
                WIDTH = WX[1]
                lessX = True

            tempX += WIDTH
            tempY = SY
            lessY = True

        return drawLayout

    def getRect(piece_image, coordinates, drawLayout):
        xCo = findAlpha.index(coordinates[0])
        yCo = int(coordinates[1]) - 1
        rect = drawLayout[xCo][yCo]
        x = rect[0]
        y = rect[1]
        width = rect[2]
        height = rect[3]
        piece_rect = piece_image.get_rect()
        piece_rect.x = x + ((width - 70)/2)
        piece_rect.y = y + ((height - 70)/2)
        piece_rect.width = width
        piece_rect.height = height
        return piece_rect


    def drawBoard(self):
        pygame.init()
        size = (1100, 800)
        global screen
        screen = pygame.display.set_mode(size)
        #screen = pygame.display.set_mode(size, FULLSCREEN)
        pygame.display.set_caption("Checkers")

        #BLIT BACKGROUND
        bg_image = pygame.image.load("bg.jpg")
        bg_rect = bg_image.get_rect()
        screen.fill([255, 255, 255])
        screen.blit(bg_image, bg_rect)


        #GENERATE RECTS
        global drawLayout
        drawLayout = self.generateDrawLayout()
        #BLIT PIECES
        for f in layout:
            for g in f:
                if type(g) == Piece:
                    if g.rank == 1:
                        imgLoc = "Pieces/" + g.colour + "_pawn.png"
                    else:
                        imgLoc = "Pieces/" + g.colour + "_king.png"
                    blitPiece(imgLoc, g)

    def runGame(self):
        self.drawBoard()
        done = False
        highlighted = False
        while not done:
            # HIGHLIGHT PIECES ON ROLLOVER
            mousePos = pygame.mouse.get_pos()
            clicked = False
            clickedPiece = None
            mouseX, mouseY = mousePos[0],mousePos[1]
            withinGrid = (SX <= mouseX <= 1046.5) and (52.46 <= mouseY <= (SY + 87))
            if withinGrid:
                arrayLoc = mouseToArray(mousePos)
                pPiece = self.layout[arrayLoc[0]][arrayLoc[1]]
                position = findAlpha[arrayLoc[0]] + str(arrayLoc[1] + 1)
                unblitList = []
                if type(pPiece) == Piece:
                    blitted = False
                    clicked = False
                    highlighted = False
                    while position == pPiece.position or clicked:
                        if blitted == False:
                            if pPiece.rank == 1:
                                imgLoc = "Pieces/" + pPiece.colour + "_pawn_highlight.png"
                            else:
                                imgLoc = "Pieces/" + pPiece.colour + "_king_highlight.png"
                            blitPiece(imgLoc, pPiece)
                            blitted = True
                        if clicked and not highlighted:
                            cPiece = layout[clickedPiece[0]][int(clickedPiece[1])]
                            a = [findAlpha.index(cPiece.position[0]) - 2, findAlpha.index(cPiece.position[0]) + 2]
                            b = [int(cPiece.position[1]) - 3, int(cPiece.position[1]) + 1]
                            if a[0] < 0: a[0] = 0
                            elif a[1] > 7: a[1] = 7
                            if b[0] < 0: b[0] = 0
                            elif b[1] > 7: b[1] = 7
                            for x in layout[a[0]: a[1]+1]:
                                for y in range(b[0], b[1] + 1):
                                    if type(x[y]) != Piece:
                                        print(x[y])
                                        if cPiece.checkLegal(x[y], True)[0]:
                                            blitRect(x[y], cellHighlight)
                                            unblitList.append(x[y])
                                        if cPiece.rank == 1:
                                            if int(x[y][1]) < int(cPiece.position[1]):
                                                if cPiece.checkLegalKill(x[y])[0]:
                                                    blitRect(x[y], cellHighlight)
                                                    unblitList.append(x[y])
                                        elif cPiece.rank == 2:
                                            if cPiece.checkLegalKill(x[y])[0]:
                                                blitRect(x[y], cellHighlight)
                                                unblitList.append(x[y])
                                            
                            pygame.display.flip()
                            highlighted = True
                        elif not clicked:
                            for t in unblitList:
                                blitRect(t, cellColour)
                            unblitList = []
                            pygame.display.flip()
                            highlighted = False
                        pygame.display.flip()
                        mousePos = pygame.mouse.get_pos()
                        arrayLoc = mouseToArray(mousePos)
                        for event in pygame.event.get():
                            if pygame.mouse.get_pressed()[0]:
                                if withinGrid:
                                    if clickedPiece != arrayLoc and not clicked:
                                        clickedPiece = arrayLoc
                                        clicked = True
                                    elif clickedPiece == arrayLoc and clicked:
                                        clicked = False
                            if event.type == pygame.QUIT:
                                pygame.quit()
                        position = findAlpha[arrayLoc[0]] + str(arrayLoc[1] + 1)
                    if pPiece.rank == 1:
                        imgLoc = "Pieces/" + pPiece.colour + "_pawn.png"
                    else:
                        imgLoc = "Pieces/" + pPiece.colour + "_king.png"
                    blitPiece(imgLoc, pPiece)

            #END HIGHLIGHT PIECES ON ROLLOVER

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            pygame.display.flip()
            fpsClock.tick(400)
        pygame.quit()

def returnArrayCo(position):
    x = findAlpha.index(position[0])
    y = int(position[1]) - 1
    return layout[x][y]

def blitPiece(img, piece):
    img = pygame.image.load(img)
    bg_rect = Board.getRect(img, piece.position, drawLayout)
    bg_rect.x -= ((bg_rect.width - 70)/2)
    bg_rect.y -= ((bg_rect.height - 70)/2)
    pygame.draw.rect(screen, cellColour, bg_rect)
    piece_rect = Board.getRect(img, piece.position, drawLayout)
    screen.blit(img, piece_rect)
    pygame.display.flip()
    
def blitRect(position, colour):
    img = pygame.image.load("Pieces/b_king.png")
    bg_rect = Board.getRect(img, position, drawLayout)
    bg_rect.x -= ((bg_rect.width - 70)/2)
    bg_rect.y -= ((bg_rect.height - 70)/2)
    if position[1] in '1357':
        bg_rect.width += 1
    else:
        bg_rect.height += 1
    pygame.draw.rect(screen, colour, bg_rect)

    
def mouseToArray(mousePos):
    x = (mousePos[0] - SX) // 87.5
    y = 7 -((mousePos[1] - 52.46) // 87.5)
    return (int(x), int(y))
    

boardArray = BoardStructure()
pieces = boardArray.createBoard()
layout = boardArray.createDataStructure(pieces)

move_list = [['D3', 'E4'], ['G6', 'F5'], ['B3','A4'], ['A4','B5'], ['E4', 'G6'], ['E6', 'F5']]
#move_list = []
for i in move_list:
    returnArrayCo(i[0]).move(i[1], layout)
layout[6][5].rank = 2

#print(layout[2][5].checkLegal('A4'))
board = Board(layout)
board.runGame()
