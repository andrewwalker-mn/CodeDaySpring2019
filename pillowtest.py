from PIL import Image as Img
from random import shuffle
from graphics import *
import os
from pygame import mixer

mixer.init()
mixer.music.load("TD13.Crows_Playing_with_Water.mp3")
mixer.music.play()

def crop(coords, start, finish):
    image = Img.open(start)
    cropped = image.crop(coords)
    cropped.save(finish)

def solvingStage(piece_list):
    number_of_swaps = 0
    number_message = Text(Point(SIZE_X * 0.5, SIZE_Y * 1.05), "Number of Swaps: " + str(number_of_swaps))
    number_message.setTextColor("black")
    number_message.draw(win)
    while True:
        coords1 = win.getMouse()
        if(inRectangle(solveButton, coords1)):
            autoSolve(Imglist)
            if listInOrder(Imglist):
                puzzleDone()
            break
        for piece1 in piece_list:
            if inPiece(piece1, coords1):
                coords2 = win.getMouse()
                for piece2 in piece_list:
                    if inPiece(piece2, coords2):
                        swap(piece1, piece2, 1)
                        break
                break
        number_of_swaps += 1
        number_message.undraw()
        number_message = Text(Point(SIZE_X * 0.5, SIZE_Y * 1.05), "Number of Swaps: " + str(number_of_swaps))
        number_message.setTextColor("black")
        number_message.draw(win)
        if listInOrder(Imglist):
            puzzleDone()

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
    for k in range(0, len(Imglist)):
        os.remove("crop" + str(k) + ".gif")

def swap(piece1, piece2, solve):
    topleft1 = Point(piece1.getAnchor().getX()-piece1.getWidth()//2, piece1.getAnchor().getY()-piece1.getHeight()//2)
    piece1x = topleft1.getX()
    piece1y = topleft1.getY()
    topleft2 = Point(piece2.getAnchor().getX()-piece2.getWidth()//2, piece2.getAnchor().getY()-piece2.getHeight()//2)
    piece2x = topleft2.getX()
    piece2y = topleft2.getY()
    if solve == 1:
        moveAnimation(piece1, (piece2x - piece1x)/20, (piece2y - piece1y)/20, 20, 0.01)
        moveAnimation(piece2, (piece1x - piece2x)/20, (piece1y - piece2y)/20, 20, 0.01)
    else:
        moveAnimation(piece1, (piece2x - piece1x)/5, (piece2y - piece1y)/5, 5, 0.01)
        moveAnimation(piece2, (piece1x - piece2x)/5, (piece1y - piece2y)/5, 5, 0.01)
    index1 = piece_list.index(piece1)
    index2 = piece_list.index(piece2)
    piece_list[index1] = piece2
    piece_list[index2] = piece1
    temp = Imglist[index1]
    Imglist[index1] = Imglist[index2]
    Imglist[index2] = temp

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

def inRectangle(rect, coords):
    x = coords.getX()
    y = coords.getY()
    topleft = rect.getP1()
    tlx = topleft.getX()
    tly = topleft.getY()
    botright = rect.getP2()
    brx = botright.getX()
    bry = botright.getY()
    return (x > tlx and x < brx and y > tly and y < bry)

def moveAnimation(piece, dx, dy, repetitions, delay):
    for i in range(repetitions):
        piece.move(dx, dy)
        time.sleep(delay)

def cropPics():
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

def autoSolve(Imglist):
    for i in range(len(Imglist)):
        indexCorrect = findPiece(Imglist, i)
        swap(piece_list[i], piece_list[indexCorrect], len(Imglist))

def findPiece(Imglist, i):
    for index in range(len(Imglist)):
        if Imglist[index] == i:
            return index


NUM_COLS = "not an int"
NUM_ROWS = "not an int"
image_name = 12345

while (not isinstance(NUM_COLS,int) or not isinstance(NUM_ROWS,int) or not isinstance(image_name,str)):
    startwin = GraphWin("Startup screen", 800, 400)
    rowsprompt = Text(Point(startwin.getWidth()/2-100, 100), "Rows:")
    colsprompt = Text(Point(startwin.getWidth()/2+55, 100), "Cols:")
    text1 = Text(Point(100, 150), "Panda")
    text2 = Text(Point(100, 200), "UMN")
    text3 = Text(Point(100, 250), "Grasshopper")
    text4 = Text(Point(100, 300), "Custom")
    title = Text(Point(400, 50), "Jigsaw Generator")
    text5 = Text(Point(700, 300), "Start")
    title.setSize(30)
    title.setFace("helvetica")
    title.setStyle("italic")
    text5.setSize(20)
    text1.draw(startwin)
    text2.draw(startwin)
    text3.draw(startwin)
    text4.draw(startwin)
    title.draw(startwin)
    text5.draw(startwin)

    button1 = Rectangle(Point(40, 140), Point(160, 160))
    button2 = Rectangle(Point(40, 190), Point(160, 210))
    button3 = Rectangle(Point(40, 240), Point(160, 260))
    button4 = Rectangle(Point(40, 290), Point(160, 310))
    button5 = Rectangle(Point(660, 275), Point(740, 325))
    button1.draw(startwin)
    button2.draw(startwin)
    button3.draw(startwin)
    button4.draw(startwin)
    button5.draw(startwin)

    rowsprompt.draw(startwin)
    colsprompt.draw(startwin)

    rowsbox = Entry(Point(startwin.getWidth()/2-45, 375), 5)
    colsbox = Entry(Point(startwin.getWidth()/2+105, 375), 5)

    rowsbox.draw(startwin)
    colsbox.draw(startwin)

    while True:
        selectPuzzle = startwin.getMouse()
        if(inRectangle(button1, selectPuzzle)):
            image_name = "panda.gif"
            if Img.open(image_name).size[0] > 225:
                basewidth = 225
                img = Img.open(image_name)
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Img.ANTIALIAS)
                img.save("panda.gif")
            previewImage = Image(Point(400,200),"panda.gif")
            previewImage.draw(startwin)

        if(inRectangle(button2, selectPuzzle)):
            image_name = "umn.gif"
            if Img.open(image_name).size[0] > 225:
                basewidth = 225
                img = Img.open(image_name)
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Img.ANTIALIAS)
                img.save("umn.gif")
            previewImage = Image(Point(400,200),"umn.gif")
            previewImage.draw(startwin)

        if(inRectangle(button3, selectPuzzle)):
            if Img.open("grasshopper.gif").size[0] > 300:
                basewidth = 300
                img = Img.open("grasshopper.gif")

            image_name = "grasshopper.gif"
            if Img.open(image_name).size[0] > 225:
                basewidth = 225
                img = Img.open(image_name)
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Img.ANTIALIAS)
                img.save("grasshopper.gif")
            previewImage = Image(Point(400,200),"grasshopper.gif")
            previewImage.draw(startwin)

        if(inRectangle(button4, selectPuzzle)):
            while not isinstance(image_name, str):
                customwin = GraphWin("Input image name", 250, 100)
                prompt = Text(Point(customwin.getWidth()/2, 20), "What is the name of the image\nyou want to puzzle-ify?")
                prompt.draw(customwin)
                promptbox = Entry(Point(90,60),18)
                promptbox.draw(customwin)
                OKtext = Text(Point(210, 60), "OK")
                OKtext.setSize(15)
                OKtext.draw(customwin)
                OKbox = Rectangle(Point(190, 45), Point(230, 75))
                OKbox.draw(customwin)
                while True:
                    if inRectangle(OKbox, customwin.getMouse()):
                        image_name = promptbox.getText()
                        print(" clkc")
                        break
                customwin.close()



    #prompt.draw(startwin)

    clickprompt = Text(Point(startwin.getWidth()/2, 220), "Click outside a box when done with input.")
    clickprompt.draw(startwin)

    startwin.getMouse()
    #image_name = promptbox.getText()
    try:
        NUM_COLS = int(colsbox.getText())
    except:
        NUM_COLS = NUM_COLS
    try:
        NUM_ROWS = int(rowsbox.getText())
    except:
        NUM_ROWS = NUM_ROWS
    startwin.close()

if Img.open(image_name).size[0] > 500:
    basewidth = 500
    img = Img.open(image_name)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Img.ANTIALIAS)
    img.save(image_name)

SIZE_X = Img.open(image_name).size[0]-Img.open(image_name).size[0]%NUM_COLS
SIZE_Y = Img.open(image_name).size[1]-Img.open(image_name).size[1]%NUM_ROWS
size_x = SIZE_X/NUM_COLS
size_y = SIZE_Y/NUM_ROWS
crop((0, 0, SIZE_X, SIZE_Y), image_name, "crop.gif")

cropPics()

Imglist = [item for item in range(0, NUM_ROWS*NUM_COLS)]
shuffle(Imglist)

win = GraphWin(image_name+" puzzle", SIZE_X, 1.5*SIZE_Y)

solveButton = Rectangle(Point(SIZE_X/2 - 24, SIZE_Y + SIZE_Y/4 - 7),Point(SIZE_X/2 + 24, SIZE_Y + SIZE_Y/4 + 7))
solveButton.setOutline("black")
solveButton.setFill("yellow")
solveButton.draw(win)

solveButtonText = Text(Point(SIZE_X/2, SIZE_Y + SIZE_Y/4), "SOLVE")
solveButtonText.setSize(10)
solveButtonText.draw(win)

piece_list = [None]*len(Imglist)
for i in range(0, len(Imglist)):
    x = i % NUM_COLS
    y = i // NUM_COLS
    pt = Point(x*size_x+size_x//2, y*size_y+size_y//2)
    piece_list[i] = Image(pt, "crop"+str(Imglist[i])+".gif")
    piece_list[i].draw(win)

solvingStage(piece_list)
win.getMouse()
