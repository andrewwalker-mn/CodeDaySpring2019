from PIL import Image as Img
from random import shuffle
from graphics import *

def crop(coords, start, finish):
    image = Img.open(start)
    cropped = image.crop(coords)
    cropped.save(finish)

def solvingStage(piece_list):
    while(1):
        coords1 = win.getMouse()
        for piece1 in piece_list:
            if inPiece(piece1, coords1):
                coords2 = win.getMouse()
                for piece2 in piece_list:
                    if inPiece(piece2, coords2):
                        swap(piece1, piece2)
                        break
                break

def swap(piece1, piece2):
    topleft1 = Point(piece1.getAnchor().getX()-piece1.getWidth()//2, piece1.getAnchor().getY()-piece1.getHeight()//2)
    piece1x = topleft1.getX()
    piece1y = topleft1.getY()
    topleft2 = Point(piece2.getAnchor().getX()-piece2.getWidth()//2, piece2.getAnchor().getY()-piece2.getHeight()//2)
    piece2x = topleft2.getX()
    piece2y = topleft2.getY()
    moveAnimation(piece1, (piece2x - piece1x)/20, (piece2y - piece1y)/20, 20, 0.01)
    moveAnimation(piece2, (piece1x - piece2x)/20, (piece1y - piece2y)/20, 20, 0.01)

def inPiece(piece, coords):
    x = coords.getX()
    y = coords.getY()
    topleft = Point(piece.getAnchor().getX()-piece.getWidth()//2, piece.getAnchor().getY()-piece.getHeight()//2)
    tlx = topleft.getX()
    tly = topleft.getY()
    botright = Point(piece.getAnchor().getX()+piece.getWidth()//2, piece.getAnchor().getY()+piece.getHeight()//2)
    brx = botright.getX()
    bry = botright.getY()
    return (x > tlx and x < brx and y > tly and y < bry)

def moveAnimation(piece, dx, dy, repetitions, delay):
    for i in range(repetitions):
        piece.move(dx, dy)
        time.sleep(delay)

image_name = "umn.gif"
NUM_COLS = 3
NUM_ROWS = 3
SIZE_X = Img.open(image_name).size[0]-Img.open(image_name).size[0]%NUM_COLS
SIZE_Y = Img.open(image_name).size[1]-Img.open(image_name).size[1]%NUM_ROWS
size_x = SIZE_X/NUM_COLS
size_y = SIZE_Y/NUM_ROWS
crop((0, 0, SIZE_X, SIZE_Y), image_name, image_name)

xloc = 0
yloc = 0
piece_count = 0
for y in range(0, NUM_ROWS):
    for x in range(0, NUM_COLS):
        crop((xloc, yloc, xloc + size_x, yloc + size_y), image_name, "crop" + str(piece_count) + ".gif")
        xloc = xloc + size_x
        piece_count += 1
    yloc = yloc + size_y
    xloc = 0

Imglist = [item for item in range(0, NUM_ROWS*NUM_COLS)]
print(Imglist)
shuffle(Imglist)
print(Imglist)

win = GraphWin(image_name+" puzzle", SIZE_X, SIZE_Y)

piece_list = [None]*len(Imglist)
for i in range(0, len(Imglist)):
    x = i % NUM_COLS
    y = i // NUM_COLS
    pt = Point(x*size_x+size_x//2, y*size_y+size_y//2)
    piece_list[i] = Image(pt, "crop"+str(Imglist[i])+".gif")
    piece_list[i].draw(win)

<<<<<<< HEAD
solvingStage(piece_list)
=======
def listInOrder(list):
    i = 0
    while i < len(list) - 1:
        if list[i] > list [i+1]:
            return False
        i = i+1
    return True

def puzzleDone():
    done_message = Text(Point(SIZE_X/2, SIZE_Y/4), "Puzzle Complete!")
    done_message.setSize(20)
    done_message.setTextColor("white")
    done_message.draw(win)


while (1):
    coords1 = win.getMouse()
    for piece1 in piece_list:
        if inPiece(piece1, coords1):
            coords2 = win.getMouse()
            for piece2 in piece_list:
                if inPiece(piece2, coords2):
                    topleft1 = Point(piece1.getAnchor().getX()-piece1.getWidth()//2, piece1.getAnchor().getY()-piece1.getHeight()//2)
                    piece1x = topleft1.getX()
                    piece1y = topleft1.getY()
                    topleft2 = Point(piece2.getAnchor().getX()-piece2.getWidth()//2, piece2.getAnchor().getY()-piece2.getHeight()//2)
                    piece2x = topleft2.getX()
                    piece2y = topleft2.getY()
                    piece1.move(piece2x - piece1x, piece2y - piece1y)
                    piece2.move(piece1x - piece2x, piece1y - piece2y)
                    index1 = piece_list.index(piece1)
                    index2 = piece_list.index(piece2)
                    piece_list[index1] = piece2
                    piece_list[index2] = piece1
                    temp = Imglist[index1]
                    Imglist[index1] = Imglist[index2]
                    Imglist[index2] = temp
                    break
            break
    if listInOrder(Imglist):
        puzzleDone()
>>>>>>> c43913ea8353555a1c6c63b7fb53974a9174d7a7
