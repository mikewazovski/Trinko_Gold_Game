#CS 177 - milestone3
# (Nabi, 00328-20364)
# Following the Coding Standards and Guidelines
# This program brings everything together and completes Trinko Gold animated video game



#creative part1 shows the correct answer if the clicked answer is incorrect
#creative part2 makes the ball fall and the ball count is the same as the score number. Moreover,
# the recommendation is prompted after the game finishes.





from graphics import *
from random import *


def control():
    #create a graphics window as specified
    win = GraphWin('Game Control', 500, 200)
    win.setBackground('lightgrey')
    # insert the TrinkoTitle.gif
    image = Image(Point(250, 50), "TrinkoTitle.gif")
    # image.setPixel(32,18,'blue')
    image.draw(win)

    #draw 110x30 red-filled rectangle lower right as specified
    rect1 = Rectangle(Point(120, 130), Point(230, 160)).draw(win)
    rect1.setFill("green")
    button = Text(Point(175, 145), "PLAY")
    button.setSize(24)
    button.setTextColor('white')
    #button.setStyle('bold')
    button.draw(win)

    rect = Rectangle(Point(270, 130), Point(380, 160)).draw(win)
    rect.setFill("red")
    button = Text(Point(325, 145), "EXIT")
    button.setSize(24)
    button.setTextColor('white')
    # button.setStyle('bold')
    button.draw(win)

    a = False
    #while not quit
    while clicked(a, rect) is False:
        a = win.checkMouse()
        #if play button is pressed
        if clicked(a, rect1) is True:
            #close the window
            win.close()
            return True
    win.close()




def board():
    #create a graphics window as specified
    win = GraphWin("Game Board", 500, 700, autoflush=False)
    #insert the TrinkoTitle.gif 500x100 pixels
    image = Image(Point(250,50),"LetsPlay.gif")
    #image.setPixel(32,18,'blue')
    image.draw(win)

    #draw 500x100 white fulled rectangle as specified
    rect = Rectangle(Point(0, 600), Point(500, 700)).draw(win)
    rect.setFill('white')

    #create two horizontal lines with width of 3
    line1 = Line(Point(0, 100), Point(500, 100))
    line2 = Line(Point(0, 600), Point(500, 600))
    line1.setWidth(3)
    line2.setWidth(3)
    line1.draw(win)
    line2.draw(win)

    # append and draw text for chip  as specified
    bottomtxt = Text(Point(90, 640), 'Chips: 0').draw(win)
    bottomtxt.setSize(24)

    # append and draw text for score  as specified
    bottomtxt1 = Text(Point(410, 640), 'Score:  0').draw(win)
    bottomtxt1.setSize(24)

    # return both the graphics window  and texts
    return win, bottomtxt, bottomtxt1


# def bins function
def bins(win):
    # set variable equal to the xcoord of first upper line
    xcoord = 5
    # display all upper lines as specified
    for i in range(0,9):
        line = Line(Point(xcoord, 100), Point(xcoord, 139))
        line.setWidth(3)
        line.draw(win)
        xcoord += 70
    # set variable equal to the xcoord of first lower line
    xcoord = 5
    # display all lower lines as specified
    for i in range(0,9):
        line = Line(Point(xcoord, 560), Point(xcoord, 599))
        line.setWidth(3)
        line.draw(win)
        xcoord += 70
    # insert text between lines
    Text(Point(40, 579.5), "40").draw(win)
    Text(Point(110, 579.5), "0").draw(win)
    Text(Point(180, 579.5), "60").draw(win)
    Text(Point(250, 579.5), "100").draw(win)
    Text(Point(320, 579.5), "20").draw(win)
    Text(Point(390, 579.5), "0").draw(win)
    Text(Point(460, 579.5), "80").draw(win)

# create pins function
def pins(win):
    # create an empty list
    ll = list()
    # assign the initial row for the pins
    row1 = 180
    row2 = 220
    # create a for loop to create a 5 row of 7 circles and 5 row 6 circles
    for x in range(1, 6):
        # create an if statement starting from the 2nd row
        if x > 1:
            # change the rows as specified
            row1 += 80
            row2 += 80
        # assign the first coordinate of  pins for both rows
        numerator1 = 40
        numerator2 = 75
        # create a for loop to draw 7 circles on the row indicated by the previous loop as specified
        for i in range(1, 8):
            c = Circle(Point(numerator1, row1), 5)
            numerator1 += 70
            # change the color of circle
            c.setFill('black')
            # draw the circle
            c.draw(win)
            # append it to the list
            ll.append(c)
        # create a for loop to draw 6 circles on the row indicated by the previous loop as specified
        for i in range(1, 7):
            c = Circle(Point(numerator2, row2), 5)
            numerator2 += 70
            # change the color of circle
            c.setFill('black')
            # draw the circle
            c.draw(win)
            # append it to the list
            ll.append(c)
    # return the list
    return ll

def clicked(mouse, rect):
    # create if statement to determine the state of mouse
    if not mouse:
        return False
    # retrive the coords of mouse
    mx, my = mouse.getX(), mouse.getY()
    # retrieve the coords of rect
    x1, y1 = rect.getP1().getX(), rect.getP1().getY()
    x2, y2 = rect.getP2().getX(), rect.getP2().getY()
    # determine if click inside rect or not
    return (x1 < mx < x2) and (y1 < my < y2)


#def makeQuiz
def makeQuiz():
    #create window as specified
    win = GraphWin('quiz',400,400)
    win.setBackground('darkgrey')
    #import an image as specified
    image = Image(Point(200, 40), "TriviaTime.gif")
    image.draw(win)
    #create a list for texts
    text = []
    #draw text for questions
    question = Text(Point(200,142), '').draw(win)
    #append the text to list
    text.append(question)
    p1 = 350
    p2 = 305
    #list for rectangles
    rect = []
    #draw and append 4 rectangles as specified
    for i in range(4):
        a = Rectangle(Point(0,p1),Point(399,p2)).draw(win)
        a.setFill('gold')
        rect.append(a)
        p1-=45
        p2-=45
    #question answers text
    p2 = 327.5
    #draw and append 4 texts as specified
    for i in range(4):
        txt = Text(Point(199.5,p2),'').draw(win)
        text.append(txt)
        p2-=45
    #draw rectangle for question num and correct answers as specified
    bottom = Rectangle(Point(0,360),Point(399,400)).draw(win)
    bottom.setFill('black')
    #append and draw text for question num as specified
    bottomtxt = Text(Point(55, 380), 'Question #1').draw(win)
    bottomtxt.setFill('white')
    bottomtxt.setSize(10)
    text.append(bottomtxt)
    #append and draw text for coorect answers as specified
    bottomtxt1 = Text(Point(350, 380), 'Correct:  0').draw(win)
    bottomtxt1.setFill('white')
    bottomtxt1.setSize(10)
    text.append(bottomtxt1)
    #reutrn 3 variables
    return win, rect, text
#def PickQs func
def pickQs():
    #open the assigned file, read it and then close it
    file = open('questions.txt', 'r', encoding="utf8")
    lines = file.readlines()
    file.close()
    i = 5
    x = 0
    #create an empty list
    ll = []
    #create a loop that is true when number of picked lines is less than 5
    while x<i:
        #randomly choose a line
        chosen = choice(lines)
        #append non duplicate questions to list
        if chosen not in ll:
            ll.append(chosen)
            x+=1
    #create a dict
    data = dict()
    #loop through the list
    for i in ll:
        #replace \n with empty string
        i = i.replace('\n','')
        #split the string
        i = i.split(',')
        #create a dict as specified
        data.update({i[0]: (i[1], i[2], i[3], i[4], i[5])})
    #return data
    return data

#def takequiz
def takeQuiz():
    z = 1
    c = 0
    #call makeQuiz() and assign the returned to 3 variables
    win, rect, text = makeQuiz()
    #call pickQs and assign returned to data
    data = pickQs()
    #create a rectangle that has the same area as 4 rectangles combined
    checkrect = Rectangle(Point(0,350),Point(399,170))
    #list keys and values in data
    for keys, values in data.items():
        #split the question
        keys = keys.split()
        #create an empty string
        empty = ''
        i = 0
        #loop until i equals length of question
        while i <= len(keys):
            #create a new line after 5 words
            empty += ' '.join(keys[i:i + 5]) + '\n'
            i += 5
        #set the question in a graphics window
        text[0].setText(empty)
        #set answer options in graphics window
        for i in range(4):
            text[4 - i].setText(values[i])
        #create an empty answer string
        answer = ''
        a = False
        #While mouse is inside four rectangles
        while clicked1(a,checkrect) is False:
            a = win.checkMouse()
            #if mouse clicked inside the 1st retangle
            if clicked1(a, rect[3]) is True:
                #if answer is A
                if 'A' == values[4]:
                    #assign answer to correct
                    answer = 'correct'
                else:
                    #assign answer to incorrect
                    answer = 'incorrect'
            elif clicked1(a, rect[2]) is True:
                if 'B' == values[4]:
                    answer = 'correct'
                else:
                    answer = 'incorrect'
            elif clicked1(a, rect[1]) is True:
                if 'C' == values[4]:
                    answer = 'correct'
                else:
                    answer = 'incorrect'
            elif clicked1(a, rect[0]) is True:
                if 'D' == values[4]:
                    answer = 'correct'
                else:
                    answer = 'incorrect'
        #create a rectangle
        answerbox = Rectangle(Point(110, 180), Point(290, 100))
        ll = []
        #if answer is correct
        if answer == 'correct':
            #change the answerbox as specified
            answerbox.draw(win)
            answerbox.setFill('gold')
            answerbox.setOutline('white')
            #append specified texts  to the list as specified
            txt = Text(Point(200, 120), 'You are correct!').draw(win)
            txt.setStyle('bold')
            txt.setSize(10)
            txt1 = Text(Point(200, 160), 'Click to continue').draw(win)
            txt1.setStyle('italic')
            txt1.setSize(10)
            ll.append(txt)
            ll.append(txt1)
        #if answer is incorrect
        elif answer == 'incorrect':
            # change the answerbox as specified
            answerbox.draw(win)
            answerbox.setOutline('white')
            answerbox.setFill('red')
            # append specified texts  to the list as specified
            txt = Text(Point(200, 120), 'Sorry, that is incorrect').draw(win)
            txt.setStyle('bold')
            txt.setSize(11)
            txt1 = Text(Point(200, 160), 'Click to continue').draw(win)
            txt1.setStyle('italic')
            txt1.setSize(10)
            ll.append(txt)
            ll.append(txt1)
            #creative part1
            #prompt the user for the correct answer
            txt = Text(Point(200,370), 'The correct answer is: ').draw(win)
            txt.setTextColor('yellow')
            txt.setStyle('italic')
            txt.setSize(9)
            txt1 = Text(Point(200, 390), values[4]).draw(win)
            txt1.setTextColor('yellow')
            txt1.setStyle('italic')
            txt1.setSize(10)
            ll.append(txt)
            ll.append(txt1)


        flag = True
        #while true
        while flag:
            #if mouse is inside answerbox
            if clicked1(win.getMouse(),answerbox) is True:
                #undraw answerbox as specified
                answerbox.undraw()
                for i in ll:
                    i.undraw()
                #if question count is 5
                if z == 5:
                    #if answer is correct
                    if answer == 'correct':
                        c += 1
                        # set and change correct answers
                        text[6].setText(f"Correct: {c}")
                    #change answerbox as specified
                    answerbox.draw(win)
                    answerbox.setOutline('white')
                    answerbox.setFill('gold')
                    # append specified texts  to the list as specified
                    txt = Text(Point(200, 120), f'Your final score is: {c}').draw(win)
                    txt.setStyle('bold')
                    txt1 = Text(Point(200, 160), 'Click to continue').draw(win)
                    txt1.setStyle('italic')
                    txt1.setSize(10)
                    bool = True
                    #while true
                    while bool:
                        # if mouse click inside answrbox is true
                        if clicked1(win.getMouse(), answerbox) is True:
                            #return correct answers
                            c = int(c)
                            win.close()
                            return c


                flag = False
        #if answer is correct
        if answer == 'correct':
            c += 1
            #set and change correct answers
            text[6].setText(f"Correct: {c}")
        #create an if statement for both answers being true
        if answer == 'correct' or answer == 'incorrect':
            z += 1
            # set and change question count
            text[5].setText(f"Question #{z}")

def clicked1(mouse, rect):
    # create if statement to determine the state of mouse
    if not mouse:
        return False
    # retrive the coords of mouse
    mx, my = mouse.getX(), mouse.getY()
    # retrieve the coords of rect
    x1, y1 = rect.getP1().getX(), rect.getP1().getY()
    x2, y2 = rect.getP2().getX(), rect.getP2().getY()
    # determine if click inside rect or not
    return (x1 < mx < x2) and (y2 < my < y1)

#def drop function with paramaters
def drop(c, win, ll, bottomtxt, bottomtxt1):
    #make the amount of correct questions equal to number of chips
    chips = c
    z=0
    score = 0
    bottomtxt.setText(f"Chips:{c}")
    while z<chips:
        a = win.getMouse()
        #check if mouseclick is within the specified borders
        if a.getY() in range(100, 139):
            #check all the borders
            xcoord = -65
            for i in range(0,7):
                #shift to the next border
                xcoord+=70
                if a.getX()>xcoord+2 and a.getX()<xcoord+68:
                    z+= 1
                    #set the number of chips on the lower corner
                    bottomtxt.setText(f"Chips:{c-z}")
                    #create a circle at that mouse click
                    circ = Circle(Point(a.getX(), a.getY()), 16)
                    circ.setFill('yellow')
                    circ.draw(win)
                    y=4
                    dx = 45
                    dz = 0
                    y2 = 0
                    #while that circle doesn't hit the bottom
                    while y2<=595:
                        coord = circ.getCenter()
                        y1, y2 = coord.getY() - 16, coord.getY() + 16
                        x1, x2 = coord.getX() - 16, coord.getX() + 16
                        if x1 <= 0:
                            circ.move(20, 0)
                        if x2 >= 500:
                            circ.move(-20, 0)
                        count =0
                        u = 0
                        for i in ll:
                            cent = i.getCenter()
                            z1, z2 = cent.getX(), cent.getY()
                            #check  the distance between pin and ball
                            dist = ((coord.getX() - z1) ** 2 + (coord.getY() - z2) ** 2) ** 0.5
                            count+=1



                            i.setFill('black')
                            #if it touches
                            if dist <= i.getRadius() + 16:
                                i.setFill('red')
                                u += 1
                                #if the ball touches the pin with its lower part
                                if coord.getX()>z1 and coord.getY() < cent.getY():
                                    #make the ball go up
                                    dx *= 0.9
                                    circ.move(dx, 0)
                                    circ.move(0, -4)
                                    #i.setFill('red')
                                elif coord.getX()<z1 and coord.getY() < cent.getY():
                                    dx *= 0.9
                                    circ.move(-dx, 0)
                                    circ.move(0, -4)
                                    #i.setFill('red')
                                #if the ball touches the pin in the middle move as specified
                                elif coord.getX()==cent.getX():
                                    dx *= 0.9
                                    circ.move(dx, 0)
                                    circ.move(0, -4)
                                    #i.setFill('red')

                                # if the ball touches the pin with its top part
                                elif coord.getX()>z1 and coord.getY() > cent.getY():
                                    #make the ball go down
                                    dz += 4
                                    dx *= 0.9
                                    circ.move(dx, 0)
                                    circ.move(0, dz)
                                    #i.setFill('red')


                                elif coord.getX()<z1 and coord.getY() > cent.getY():
                                    dz += 4
                                    dx *= 0.9
                                    circ.move(-dx, 0)
                                    circ.move(0, dz)
                                    #i.setFill('red')

                                # if the ball touches left center part with pin
                                elif coord.getY() == cent.getY() and coord.getX()>z1:
                                    dx *= 0.9
                                    dz += 4
                                    circ.move(0, dz)
                                    circ.move(dx, 0)
                                    #i.setFill('red')

                                # if the ball touches right center part with pin
                                elif coord.getY() == cent.getY() and coord.getX()<z1 :
                                    # dx*=0.8
                                    # circ.move(-dx, 0)
                                    dx *= 0.9
                                    dz += 4
                                    circ.move(0, dz)
                                    circ.move(-dx, 0)
                                    #i.setFill('red')
                                update(15)
                            #when all the pins are finished
                            if count==64 and u==0:
                                #move horizontally down
                                circ.move(0,y)
                                update(15)
                    coord = circ.getCenter()
                    #check the borders and specify each of them with a score
                    if coord.getX()>5 and coord.getX()<75:
                        score+=40
                    if coord.getX()>75 and coord.getX()<145:
                        score+=0
                    if coord.getX()>355 and coord.getX()<425:
                        score+=0
                    if coord.getX()>145 and coord.getX()<215:
                        score+=60
                    if coord.getX() > 215 and coord.getX() < 285:
                        score += 100
                    if coord.getX() > 285 and coord.getX() < 355:
                        score += 20
                    if coord.getX() > 425 and coord.getX() < 495:
                        score += 80
                    #set the score on the bottom right corner
                    bottomtxt1.setText(f"Score:{score}")


    #display a message box with the player’s total score
    p = Rectangle(Point(180, 190),Point(330, 150)).draw(win)
    p.setOutline('white')
    p.setFill('white')
    p1 = Text(Point(255, 180),score).draw(win)
    p2 = Text(Point(255, 160), 'Your Final Score:').draw(win)
    p1.setTextColor('black')
    p2.setStyle('bold')
    p2.setTextColor('black')

    #creative part2
    #change the pin color to white
    for i in ll:
        i.setFill('white')
    nu = 0
    #according to the score output the reccomendations
    if score >= 180:
        tex = Text(Point(250, 330), 'Perfect!').draw(win)
        tex.setSize(25)
        tex.setStyle('bold')
        nu += 40
    elif score >= 100:
        tex = Text(Point(250, 330), 'Good Job:)').draw(win)
        tex.setSize(25)
        tex.setStyle('bold')
        nu += 20
    elif score>=0:
        tex = Text(Point(250, 330), 'Could be better:(').draw(win)
        tex.setSize(25)
        tex.setStyle('bold')
        nu += 10

    colors = ['red', 'lightblue', 'yellow']
    balls = []
    #according to the score
    for i in range(nu):
        # create random balls
        center = Point(randint(0, 500), randint(-200, 0))
        circle = Circle(center,7)
        circle.draw(win)
        balls.append(circle)
    flag = True
    while flag:
        for i in range(len(balls)):
            #make the balls fall down
            balls[i].setFill(choice(colors))
            #balls[i].draw(win)
            balls[i].move(0,70)
            update(70)
            #when the ball is unseen
            if balls[i].getCenter().getY()>900:
                #create a text pointing info about closing the game
                tex = Text(Point(250, 370), '(press anywhere to close the game)').draw(win)
                tex.setSize(8)
                flag = False

    win.getMouse()

#create main function
def main():
    #if play button is pressed
    flag = True
    #while play button is pressed
    while control() is flag:
        #open up the whole game
        c = takeQuiz()
        win, bottomtxt, bottomtxt1 = board()
        bins(win)
        ll = pins(win)
        drop(c, win , ll, bottomtxt, bottomtxt1)
        win.close()



main()
