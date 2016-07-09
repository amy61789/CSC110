# Project:      Homework 5 (FunkAmyHomework05Sec03.py)
# Name:         Amy Funk
# Date:         06/05/2016
# Description:  This program will allow the user to "throw"
#               5 dice. The program will display a running total
#               of the dice. At the end of 5 throws the program
#               will display a message on how lucky the user is. The
#               user will not be allowed more than one roll per dice
#               and will be able to exit the program by clicking
#               the exit button.


from graphics import *


def intRandomNum():

    # imports random library
    import random

    # assigns variable to random number
    intDiceNum = random.randint(1,6)

    # returns value of intDiceNum
    return intDiceNum

def dot(center,win):

    # assigns intDiceNum to intRandomNum() function
    intDiceNum = intRandomNum()

    # if value of intDiceNum is equal to 1
    if intDiceNum == 1:

        # draws the dot in the 1 position
        circDotOne = Circle(Point((center.getX() - 13),(center.getY() - 13)),4)
        circDotOne.setFill("black")
        circDotOne.draw(win)

    # if value of intDiceNum is equal to 2
    if intDiceNum == 2:

        # draws the 2 dots in the 2 position
        circDotTwo = Circle(Point((center.getX() + 10),(center.getY() - 35)),4)
        circDotTwo.setFill("black")
        circDotTwo.draw(win)
        circDotTwoPair = Circle(Point((center.getX() - 35),(center.getY() + 10)),4)
        circDotTwoPair.setFill("black")
        circDotTwoPair.draw(win)

    # if value of intDiceNum is equal to 3
    if intDiceNum == 3:

        # draws the 2 dots in the 2 position
        circDotTwo = Circle(Point((center.getX() + 10),(center.getY() - 35)),4)
        circDotTwo.setFill("black")
        circDotTwo.draw(win)
        circDotTwoPair = Circle(Point((center.getX() - 35),(center.getY() + 10)),4)
        circDotTwoPair.setFill("black")
        circDotTwoPair.draw(win)

        # draws the dot in the 1 position
        circDotOne = Circle(Point((center.getX() - 13),(center.getY() - 13)),4)
        circDotOne.setFill("black")
        circDotOne.draw(win)

    # if value of intDiceNum is equal to 4
    if intDiceNum == 4:

        # draws the 2 dots in the 2 position and drawing the 2
        # additional dots
        circDotTwo = Circle(Point((center.getX() + 10),(center.getY() - 35)),4)
        circDotTwo.setFill("black")
        circDotTwo.draw(win)
        circDotTwoPair = Circle(Point((center.getX() - 35),(center.getY() + 10)),4)
        circDotTwoPair.setFill("black")
        circDotTwoPair.draw(win)
        circDotFour = Circle(Point((center.getX() - 35),(center.getY() - 35)),4)
        circDotFour.setFill("black")
        circDotFour.draw(win)
        circDotFourPair = Circle(Point((center.getX() + 10),(center.getY() + 10)),4)
        circDotFourPair.setFill("black")
        circDotFourPair.draw(win)

    # if value of intDiceNum is equal to 5
    if intDiceNum == 5:

        # draws the 2 dots in the 2 position, 2 additional dots in the 4
        # position, and the 1 dot in the 1 position
        circDotTwo = Circle(Point((center.getX() + 10),(center.getY() - 35)),4)
        circDotTwo.setFill("black")
        circDotTwo.draw(win)
        circDotTwoPair = Circle(Point((center.getX() - 35),(center.getY() + 10)),4)
        circDotTwoPair.setFill("black")
        circDotTwoPair.draw(win)
        circDotFour = Circle(Point((center.getX() - 35),(center.getY() - 35)),4)
        circDotFour.setFill("black")
        circDotFour.draw(win)
        circDotFourPair = Circle(Point((center.getX() + 10),(center.getY() + 10)),4)
        circDotFourPair.setFill("black")
        circDotFourPair.draw(win)        
        circDotOne = Circle(Point((center.getX() - 13),(center.getY() - 13)),4)
        circDotOne.setFill("black")
        circDotOne.draw(win)

    # if value of intDiceNum is equal to 6
    if intDiceNum == 6:

        # draws the 4 dots in the 4 position and two additional dots
        # in the 6 position
        circDotTwo = Circle(Point((center.getX() + 10),(center.getY() - 35)),4)
        circDotTwo.setFill("black")
        circDotTwo.draw(win)
        circDotTwoPair = Circle(Point((center.getX() - 35),(center.getY() + 10)),4)
        circDotTwoPair.setFill("black")
        circDotTwoPair.draw(win)
        circDotFour = Circle(Point((center.getX() - 35),(center.getY() - 35)),4)
        circDotFour.setFill("black")
        circDotFour.draw(win)
        circDotFourPair = Circle(Point((center.getX() + 10),(center.getY() + 10)),4)
        circDotFourPair.setFill("black")
        circDotFourPair.draw(win)
        circDotSix = Circle(Point((center.getX() - 35),(center.getY() - 10)),4)
        circDotSix.setFill("black")
        circDotSix.draw(win)
        circDotSixPair = Circle(Point((center.getX() + 10), (center.getY() - 10)),4)
        circDotSixPair.setFill("black")
        circDotSixPair.draw(win)

    # returns the value of intDiceNum    
    return intDiceNum

def dice(center,win):

    # draws the dice
    rollDice = Rectangle(Point((center.getX() - 47),(center.getY() - 47)),Point((center.getX() + 22), (center.getY() + 22)))
    rollDice.setFill("white")
    rollDice.setOutline("black")
    rollDice.draw(win)

    # returns the dot value
    return dot(center,win)

def main():

    # sets diceRoll equal to true
    diceRoll = True

    # creates the window
    win = GraphWin("Dice",525,275)
    win.setBackground("khaki")

    # assigns a variable xCoord to 62.5
    xCoord = 62.5

    # draws the dice total label
    lblDiceTotal = Text(Point(xCoord,120),"Dice Total: ")
    lblDiceTotal.setTextColor("red")
    lblDiceTotal.draw(win)

    # draws the first dice box holder
    firstDiceBox = Rectangle(Point(25,25),Point(100,100))
    firstDiceBox.setFill("khaki")
    firstDiceBox.setOutline("gray")
    firstDiceBox.setWidth(3)
    firstDiceBox.draw(win)

    # draws the label of dice holder 1
    lblfirstDiceBox = Text(Point(62.5,62.5),"Dice 1")
    lblfirstDiceBox.setTextColor("gray")
    lblfirstDiceBox.setStyle("bold")
    lblfirstDiceBox.draw(win)

    # draws the second dice box holder
    secondDiceBox = firstDiceBox.clone()
    secondDiceBox.setFill("khaki")
    secondDiceBox.setOutline("gray")
    secondDiceBox.move(100,0)
    secondDiceBox.draw(win)

    # draws the label of dice holder 2
    lblfirstDiceBox = Text(Point(165,62.5),"Dice 2")
    lblfirstDiceBox.setTextColor("gray")
    lblfirstDiceBox.setStyle("bold")
    lblfirstDiceBox.draw(win)

    # draws the third dice box holder
    thirdDiceBox = firstDiceBox.clone()
    thirdDiceBox.setFill("khaki")
    thirdDiceBox.setOutline("gray")
    thirdDiceBox.move(200,0)
    thirdDiceBox.draw(win)

    # draws the label of dice holder 3
    lblthirdDiceBox = Text(Point(262,62.5),"Dice 3")
    lblthirdDiceBox.setTextColor("gray")
    lblthirdDiceBox.setStyle("bold")
    lblthirdDiceBox.draw(win)

    # draws the fourth dice box holder
    fourthDiceBox = firstDiceBox.clone()
    fourthDiceBox.setFill("khaki")
    fourthDiceBox.setOutline("gray")
    fourthDiceBox.move(300,0)
    fourthDiceBox.draw(win)

    # draws the label of dice holder 4
    lblfourthDiceBox = Text(Point(359,62.5),"Dice 4")
    lblfourthDiceBox.setTextColor("gray")
    lblfourthDiceBox.setStyle("bold")
    lblfourthDiceBox.draw(win)

    # draws the fifth dice box holder
    fifthDiceBox = firstDiceBox.clone()
    fifthDiceBox.setFill("khaki")
    fifthDiceBox.setOutline("gray")
    fifthDiceBox.move(400,0)
    fifthDiceBox.draw(win)

    # draws the label of dice holder 5
    lblfifthDiceBox = Text(Point(456,62.5),"Dice 5")
    lblfifthDiceBox.setTextColor("gray")
    lblfifthDiceBox.setStyle("bold")
    lblfifthDiceBox.draw(win)

    # draws the button using a rectangle and text object
    btnExitOutline = Rectangle(Point(450,225),Point(500,260))
    btnExitOutline.setFill("white")
    btnExitOutline.setOutline("white")
    btnExitOutline.draw(win)
    btnExit = Text(Point(475,240),"Exit")
    btnExit.setStyle("bold")
    btnExit.draw(win)

    # captures the user mouse clicks
    ClickXY = win.getMouse()
    xPoint = ClickXY.getX()
    yPoint = ClickXY.getY()

    # if the mouse clicks are between these points exit the window
    if xPoint > 450 and xPoint < 500 and yPoint > 225 and yPoint < 260:
        
        win.close()

    # initializing intRolls to equal 0
    intRolls = 0

    # initializing intDiceTotal to equal 0
    intDiceTotal = 0

    # boolean set to false
    blnHasDiceRolled1 = False

    # boolean set to false
    blnHasDiceRolled2 = False

    # boolean set to false
    blnHasDiceRolled3 = False

    # boolean set to false
    blnHasDiceRolled4 = False

    # boolean set to false
    blnHasDiceRolled5 = False

    # run loop while diceRoll is equal to condition
    while diceRoll == True:

        # captures the user mouse clicks        
        ClickXY = win.getMouse()
        xPoint = ClickXY.getX()
        yPoint = ClickXY.getY()

        # if the mouse clicks are between these points exit the window
        if xPoint > 450 and xPoint < 500 and yPoint > 225 and yPoint < 260:
            win.close()
            diceRoll = False

        # if the mouse clicks are between these points generate dice
        elif xPoint > 25 and xPoint < 125 and yPoint > 25 and yPoint < 125 and blnHasDiceRolled1 == False:
            intRolls += 1
            intDiceTotal += dice(Point(75,75),win)
            lblDiceNumTotal = Text(Point(62.5,135),intDiceTotal)
            lblDiceNumTotal.setTextColor("red")
            lblDiceNumTotal.draw(win)
            blnHasDiceRolled1 = True

        # if the mouse clicks are between these points generate dice
        elif xPoint > 125 and xPoint < 225 and yPoint > 25 and yPoint < 125 and blnHasDiceRolled2 == False:
            intRolls += 1
            intDiceTotal += dice(Point(175,75),win)
            lblDiceNumTotal.setText(intDiceTotal)
            lblDiceNumTotal.move(100,0)
            lblDiceTotal.move(100,0)
            blnHasDiceRolled2 = True

        # if the mouse clicks are between these points generate dice
        elif xPoint > 225 and xPoint < 325 and yPoint > 25 and yPoint < 125 and blnHasDiceRolled3 == False:
            intRolls += 1
            intDiceTotal += dice(Point(275,75),win)
            lblDiceNumTotal.setText(intDiceTotal)
            lblDiceNumTotal.move(100,0)
            lblDiceTotal.move(100,0)
            blnHasDiceRolled3 = True

        # if the mouse clicks are between these points generate dice    
        elif xPoint > 325 and xPoint < 425 and yPoint > 25 and yPoint < 125 and blnHasDiceRolled4 == False:
            intRolls += 1
            intDiceTotal += dice(Point(375,75),win)
            lblDiceNumTotal.setText(intDiceTotal)
            lblDiceNumTotal.move(100,0)
            lblDiceTotal.move(100,0)
            blnHasDiceRolled4 = True

        # if the mouse clicks are between these points generate dice
        elif xPoint > 425 and xPoint < 525 and yPoint > 25 and yPoint < 125 and blnHasDiceRolled5 == False:
            intRolls += 1
            intDiceTotal += dice(Point(475,75),win)
            lblDiceNumTotal.setText(intDiceTotal)
            lblDiceNumTotal.move(100,0)
            lblDiceTotal.move(100,0)
            blnHasDiceRolled5 = True

        # displays the congrats label if the user rolls
        # more than 4 times and diceRoll is equal to true
        if intRolls > 4 and diceRoll == True:

            # if intDiceTotal is less than or equal to 10
            if intDiceTotal <= 10:

                # draws the Your luck stinks label
                lblCongrats = Text(Point(250,175),"Your luck stinks!")
                lblCongrats.setTextColor("red")
                lblCongrats.setStyle("bold")
                lblCongrats.setSize(12)
                lblCongrats.draw(win)

            # if intDiceTotal is greater than 10 but less than
            # or equal to 20 draw You have okay luck label
            elif intDiceTotal > 10 and intDiceTotal <= 20:

                # draws the You have okay luck label
                lblCongrats = Text(Point(250,175),"You have okay luck.")
                lblCongrats.setTextColor("yellow")
                lblCongrats.setStyle("bold")
                lblCongrats.setSize(16)
                lblCongrats.draw(win)
                
            # all else conditions
            else:

                # draws the Your luck is GREAT label
                lblCongrats = Text(Point(250,175),"Your luck is GREAT!")
                lblCongrats.setTextColor("green")
                lblCongrats.setStyle("bold")
                lblCongrats.setSize(20)
                lblCongrats.draw(win)
                
# calls the main function
main()
