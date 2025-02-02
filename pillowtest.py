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
        if (inRectangle(closeButton, coords1)):
            win.close()
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
            break
    puzzleDone()

def listInOrder(list):
    i = 0
    while i < len(list) - 1:
        if list[i] > list [i+1]:
            return False
        i = i+1
    return True

def puzzleDone(SIZE_X, SIZE_Y, win, Imglist):
    done_message = Text(Point(SIZE_X/2, SIZE_Y/4), "Puzzle Complete!")
    done_message.setSize(20)
    done_message.setTextColor("white")
    done_message.draw(win)
    for k in range(0, len(Imglist)):
        os.remove("crop" + str(k) + ".gif")

def swap(piece1, piece2, piece_list, Imglist, solve):
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

def autoSolve(Imglist, piece_list):
    for i in range(len(Imglist)):
        indexCorrect = findPiece(Imglist, i)
        swap(piece_list[i], piece_list[indexCorrect], piece_list, Imglist, len(Imglist))

def findPiece(Imglist, i):
    for index in range(len(Imglist)):
        if Imglist[index] == i:
            return index

def main():
    NUM_COLS = "not an int"
    NUM_ROWS = "not an int"
    image_name = 12345

    while (not isinstance(NUM_COLS,int) or not isinstance(NUM_ROWS,int) or not isinstance(image_name,str)):
        startwin = GraphWin("Startup screen", 800, 400)
        startwin.setBackground("white")
        title = Text(Point(400, 45), "Jigsaw Generator")
        title.setSize(30)
        title.setFace("helvetica")
        title.setStyle("italic")
        title.setTextColor("purple")
        title.draw(startwin)
        #Solve the Jigsaw Puzzle by swapping two pieces at a time(click on one piece then clikc on another piece to swap them)

        texti1 = Text(Point(670, 150), "Solve the Jigsaw puzzle")
        texti2 = Text(Point(670, 165), "by swapping two pieces")
        texti3 = Text(Point(670, 180), "at a time (click on one")
        texti4 = Text(Point(670, 195), "piece, then click on")
        texti5 = Text(Point(670, 210), "another to swap them)")
        texti6 = Text(Point(670, 225), "Make sure to type in the")
        texti7 = Text(Point(670, 240), "number of rows and columns.")
        texti1.draw(startwin)
        texti2.draw(startwin)
        texti3.draw(startwin)
        texti4.draw(startwin)
        texti5.draw(startwin)
        texti6.draw(startwin)
        texti7.draw(startwin)

        cover = Rectangle(Point(250,68), Point(550,335))
        cover.draw(startwin)

        button1 = Rectangle(Point(40, 140), Point(160, 160))
        button2 = Rectangle(Point(40, 190), Point(160, 210))
        button3 = Rectangle(Point(40, 240), Point(160, 260))
        button4 = Rectangle(Point(40, 290), Point(160, 310))
        button5 = Rectangle(Point(630, 275), Point(710, 325))
        button1.setOutline("black")
        button1.setFill("yellow")
        button2.setOutline("black")
        button2.setFill("yellow")
        button3.setOutline("black")
        button3.setFill("yellow")
        button4.setOutline("black")
        button4.setFill("yellow")
        button5.setOutline("black")
        button5.setFill("green")
        button1.draw(startwin)
        button2.draw(startwin)
        button3.draw(startwin)
        button4.draw(startwin)
        button5.draw(startwin)

        text1 = Text(Point(100, 150), "Panda")
        text2 = Text(Point(100, 200), "UMN")
        text3 = Text(Point(100, 250), "Grasshopper")
        text4 = Text(Point(100, 300), "Custom")
        text5 = Text(Point(670, 300), "Start")
        text5.setSize(20)
        text1.draw(startwin)
        text2.draw(startwin)
        text3.draw(startwin)
        text4.draw(startwin)
        text5.draw(startwin)

        rowsprompt = Text(Point(startwin.getWidth()/2-100, 375), "Rows:")
        colsprompt = Text(Point(startwin.getWidth()/2+55, 375), "Cols:")
        rowsprompt.draw(startwin)
        colsprompt.draw(startwin)

        rowsbox = Entry(Point(startwin.getWidth()/2-45, 375), 5)
        colsbox = Entry(Point(startwin.getWidth()/2+105, 375), 5)

        rowsbox.draw(startwin)
        colsbox.draw(startwin)

        image_name = "resizelogo.gif"
        if Img.open(image_name).size[0] > 225:
            basewidth = 225
            img = Img.open(image_name)
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Img.ANTIALIAS)
            img.save("resize" + image_name)
        previewImage = Image(Point(400, 200), image_name)
        previewImage.draw(startwin)

        start_screen = True
        while start_screen:
            selectPuzzle = startwin.getMouse()
            if(inRectangle(button1, selectPuzzle)):
                cover = Rectangle(Point(250,68), Point(550,335))
                cover.setFill("white")
                cover.draw(startwin)
                image_name = "panda.gif"
                if Img.open(image_name).size[0] > 225:
                    basewidth = 225
                    img = Img.open(image_name)
                    wpercent = (basewidth / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    img = img.resize((basewidth, hsize), Img.ANTIALIAS)
                    img.save("resize" + image_name)
                previewImage = Image(Point(400,200),image_name)
                previewImage.draw(startwin)

            if(inRectangle(button2, selectPuzzle)):
                cover = Rectangle(Point(250,68), Point(550,335))
                cover.setFill("white")
                cover.draw(startwin)
                image_name = "umn.gif"
                if Img.open(image_name).size[0] > 225:
                    basewidth = 225
                    img = Img.open(image_name)
                    wpercent = (basewidth / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    img = img.resize((basewidth, hsize), Img.ANTIALIAS)
                    img.save("resize" + image_name)
                previewImage = Image(Point(400,200),image_name)
                previewImage.draw(startwin)

            if(inRectangle(button3, selectPuzzle)):
                cover = Rectangle(Point(250,68), Point(550,335))
                cover.setFill("white")
                cover.draw(startwin)
                image_name = "grasshopper.gif"
                if Img.open(image_name).size[0] > 225:
                    basewidth = 225
                    img = Img.open(image_name)
                    wpercent = (basewidth / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    img = img.resize((basewidth, hsize), Img.ANTIALIAS)
                    img.save("resize" + image_name)
                previewImage = Image(Point(400,200),image_name)
                previewImage.draw(startwin)

            if(inRectangle(button4, selectPuzzle)):
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
                        break
                try:
                    Img.open(image_name)
                except:
                    image_name = "resizelogo.gif"
                customwin.close()

                cover = Rectangle(Point(250, 68), Point(550, 335))
                cover.setFill("white")
                cover.draw(startwin)
                img = Img.open(image_name)

                if img.size[0] > 225:
                    basewidth = 225
                    wpercent = (basewidth / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    img = img.resize((basewidth, hsize), Img.ANTIALIAS)
                    img.save("resize" + image_name)
                    previewImage = Image(Point(400, 200), "resize" + image_name)
                else:
                    previewImage = Image(Point(400, 200), image_name)
                previewImage.draw(startwin)

            if (inRectangle(button5, selectPuzzle)):
                start_screen = False

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
    shuffle(Imglist)

    win = GraphWin(image_name+" puzzle", SIZE_X, 1.5*SIZE_Y)

    solveButton = Rectangle(Point(SIZE_X/2 - 24, SIZE_Y + SIZE_Y/4 - 7),Point(SIZE_X/2 + 24, SIZE_Y + SIZE_Y/4 + 7))
    solveButton.setOutline("black")
    solveButton.setFill("yellow")
    solveButton.draw(win)

    solveButtonText = Text(Point(SIZE_X/2, SIZE_Y + SIZE_Y/4), "SOLVE")
    solveButtonText.setSize(10)
    solveButtonText.draw(win)

    closeButton = Rectangle(Point(SIZE_X/2 - 24, SIZE_Y + SIZE_Y/4 + 20 - 7),Point(SIZE_X/2 + 24, SIZE_Y + SIZE_Y/4 + 20 + 7))
    closeButton.setOutline("black")
    closeButton.setFill("yellow")
    closeButton.draw(win)

    closeButtonText = Text(Point(SIZE_X/2, SIZE_Y + SIZE_Y/4 + 20), "CLOSE")
    closeButtonText.setSize(10)
    closeButtonText.draw(win)

    piece_list = [None]*len(Imglist)
    for i in range(0, len(Imglist)):
        x = i % NUM_COLS
        y = i // NUM_COLS
        pt = Point(x*size_x+size_x//2, y*size_y+size_y//2)
        piece_list[i] = Image(pt, "crop"+str(Imglist[i])+".gif")
        piece_list[i].draw(win)

    number_of_swaps = 0
    number_message = Text(Point(SIZE_X * 0.5, SIZE_Y * 1.05), "Number of Swaps: " + str(number_of_swaps))
    number_message.setTextColor("black")
    number_message.draw(win)
    while True:
        coords1 = win.getMouse()
        if(inRectangle(solveButton, coords1)):
            autoSolve(Imglist,piece_list)
            if listInOrder(Imglist):
                break
        if (inRectangle(closeButton, coords1)):
            win.close()
            break
        for piece1 in piece_list:
            if inPiece(piece1, coords1):
                coords2 = win.getMouse()
                for piece2 in piece_list:
                    if inPiece(piece2, coords2):
                        swap(piece1, piece2, piece_list, Imglist, 1)
                        break
                break
        number_of_swaps += 1
        number_message.undraw()
        number_message = Text(Point(SIZE_X * 0.5, SIZE_Y * 1.05), "Number of Swaps: " + str(number_of_swaps))
        number_message.setTextColor("black")
        number_message.draw(win)
        if listInOrder(Imglist):
            break
    puzzleDone(SIZE_X, SIZE_Y, win, Imglist)

    replayButton = Rectangle(Point(3*SIZE_X/4 - 28, SIZE_Y + SIZE_Y/4 + 10 - 7),Point(3*SIZE_X/4 + 28, SIZE_Y + SIZE_Y/4 + 10 + 7))
    replayButton.setOutline("black")
    replayButton.setFill("yellow")
    replayButton.draw(win)

    replayButtonText = Text(Point(3*SIZE_X/4, SIZE_Y + SIZE_Y/4 + 10), "REPLAY")
    replayButtonText.setSize(10)
    replayButtonText.draw(win)
    while(True):
        if(inRectangle(replayButton, win.getMouse())):
            main()
        if(inRectangle(closeButton, win.getMouse())):
            break
    win.close()

if __name__ == "__main__":
    main()
