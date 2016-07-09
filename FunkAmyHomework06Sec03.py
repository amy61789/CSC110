# Project:      Homework 06 (FunkAmyHomework06Sec03.py)
# Name:         Amy Funk
# Date:         06/15/2016
# Description:  This program will allow the user to import a file
#               that will have information on any number of
#               families income, size, and state they reside in.
#               The user will be able to generate reports on the given
#               information. Report 1 will consist of writing out a file
#               of the families that fall below the poverty level. Report 2
#               displays in the window the families that are above
#               average income. Report 3 will display the percentage of
#               families that fall below the poverty level and a bar chart
#               associating with the percentage. The last report (Report 4)
#               will write out a file all the data and have an added field
#               that indicates if the family falls below the poverty level.
#               Lastly, there is an exit button located on the window so
#               the user can exit the program.

from graphics import *

def drawWindow():

    # creates the window
    win = GraphWin("Homework 6", 600,500)
    win.setBackground("light steel blue")

    # draws the first rectangle and Import File label
    rectImportFile = Rectangle(Point(75,50),Point(200,125))
    rectImportFile.setFill("floral white")
    rectImportFile.setOutline("dark slate gray")
    rectImportFile.setWidth(4)
    rectImportFile.draw(win)
    lblImportFile = Text(Point(137.5,87.5),"Import File")
    lblImportFile.setStyle("bold")
    lblImportFile.setTextColor("navy")
    lblImportFile.draw(win)

    # draws the second rectangle and Report 1 label
    rectReport1 = rectImportFile.clone()
    rectReport1.move(150,0)
    rectReport1.draw(win)
    lblReport1 = Text(Point(287.5,87.5),"Report 1")
    lblReport1.setStyle("bold")
    lblReport1.setTextColor("navy")
    lblReport1.draw(win)

    # draws the third rectangle and Report 2 label
    rectReport2 = rectReport1.clone()
    rectReport2.move(150,0)
    rectReport2.draw(win)
    lblReport2 = Text(Point(437.5,87.5),"Report 2")
    lblReport2.setStyle("bold")
    lblReport2.setTextColor("navy")
    lblReport2.draw(win)

    # draws the fourth rectangle and Report 3 label
    rectReport3 = rectImportFile.clone()
    rectReport3.move(0,100)
    rectReport3.draw(win)
    lblReport3 = Text(Point(137.5, 187.5),"Report 3")
    lblReport3.setStyle("bold")
    lblReport3.setTextColor("navy")
    lblReport3.draw(win)

    # draws the fifth rectangle and Report 4 label
    rectReport4 = rectReport3.clone()
    rectReport4.move(150,0)
    rectReport4.draw(win)
    lblReport4 = Text(Point(287.5,187.5),"Report 4")
    lblReport4.setStyle("bold")
    lblReport4.setTextColor("navy")
    lblReport4.draw(win)

    # draws the sixth rectangle and Exit label
    rectExit = rectReport4.clone()
    rectExit.move(150,0)
    rectExit.draw(win)
    lblExit = Text(Point(437.5,187.5),"EXIT")
    lblExit.setStyle("bold")
    lblExit.setTextColor("slate gray")
    lblExit.draw(win)

    # returns win value
    return win

def bar(point1,point2,color,win):

    # draw bar for percentage of impoverished families
    rectGrade = Rectangle(point1,point2)
    rectGrade.setFill(color)
    rectGrade.setOutline(color)
    rectGrade.draw(win)


def displayPercentBelowPoverty(fltPercent,win):

    # draws the percent label
    lblPercent = Text(Point(300, 350),"Percent of families that fall below the poverty level: ")
    lblPercent.setStyle("bold")
    lblPercent.setFace("arial")
    lblPercent.setTextColor("snow")
    lblPercent.draw(win)

    # draws the percentage of below poverty rounded to 2 decimal places
    lblReport03 = Text(Point(300,375),str(round(fltPercent,2)) + "%")
    lblReport03.setTextColor("snow")
    lblReport03.draw(win)
    
def percentBelowPoverty(mlstFamilySurvey,lstBelowPoverty):

    # assigns variable to percentage below poverty 
    fltPercent = (len(lstBelowPoverty) / len(mlstFamilySurvey)) * 100

    # returns fltPercent value
    return fltPercent

def displayAboveAverageIncome(lstAboveAverageIncome, win):

    # draws the above average income label
    lblAboveAveIncome = Text(Point(300,300),"Family ID's that are above average income:")
    lblAboveAveIncome.setStyle("bold")
    lblAboveAveIncome.setFace("arial")
    lblAboveAveIncome.setTextColor("snow")
    lblAboveAveIncome.draw(win)

    # draws the family id's that are above average income
    lblReport02 = Text(Point(300,325),lstAboveAverageIncome)
    lblReport02.setTextColor("snow")
    lblReport02.draw(win)   

def averageIncome(mlstFamilySurvey):
    
    # initializes intTotalIncome to equal 0
    intTotalIncome = 0

    # loops through every line in mlstFamilySurvey
    for line in mlstFamilySurvey:
        
        # adds income to total income to keep running total
        intTotalIncome += int(line[2])

    # calculates average income by dividing the total income accumulated
    # from data by the length of the master list
    intAveIncome = intTotalIncome / len(mlstFamilySurvey)

    # returns value of intAveIncome
    return intAveIncome

def aboveAveIncomeFam(mlstFamilySurvey,intAveIncome):

    # initializes a list for above average incomes
    lstAboveAveIncome = []

    # loops through every line in mlstFamilySurvey
    for line in mlstFamilySurvey:

        # if family income is greater than the intAveIncome
        # it is then appened to the above average income list
        if line[2] > intAveIncome:
            
            lstAboveAveIncome.append(line[0])
            
    # returns value of lstAboveAveIncome       
    return lstAboveAveIncome
                
def outFileReport(mlstFamilySurvey,strOutFileName,convertIntToStr):

    # opens file to write out 
    outFileRep = open(strOutFileName,"w")

    # if convertIntToStr is equal to True
    if convertIntToStr == True:

        # converts each line[0][1][2] in the mater list
        # back to strings
        for line in mlstFamilySurvey:
            line[0] = str(line[0])
            line[1] = str(line[1])
            line[2] = str(line[2])
        # write the output file     
        for line in mlstFamilySurvey:
            print(" ".join(line), file=outFileRep)
    # any other condition besides True
    else:
        # write the output file
        for line in mlstFamilySurvey:
            print(line, file=outFileRep)
            
    # closes file
    outFileRep.close()

def insertPovertyField(mlstFamilySurvey):
    
    # loops through each line of the master list
    for line in mlstFamilySurvey:
        
        # if the family income falls below or equal to
        # the selected state poverty level a field is added to
        # indicate they fall below the poverty level
        if line[3] == "AK":
            intPovertyLevel = 7650 + (line[1] * 3980)
            if line[2] <= intPovertyLevel:
                line.append("FALLS BELOW POVERTY LEVEL")
        elif line[3] == "HI":
            intPovertyLevel = 7040 + (line[1] * 3660)
            if line[2] <= intPovertyLevel:
                line.append("FALLS BELOW POVERTY LEVEL")
        else:
            intPovertyLevel = 6130 + (line[1] * 3180)
            if line[2] <= intPovertyLevel:
                line.append("FALLS BELOW POVERTY LEVEL")
                
    # returns the value of mlstFamilySurvey
    return mlstFamilySurvey

def belowPoverty(mlstFamilySurvey):

    # initializes a list for below poverty families
    lstBelowPoverty = []

    # loops through each line of the master list
    for line in mlstFamilySurvey:
        
        # appends the family id to the lstBelowPoverty if family
        # falls below state poverty level
        if line[3] == "AK":
            intPovertyLevel = 7650 + (line[1] * 3980)
            if line[2] <= intPovertyLevel:
                lstBelowPoverty.append(line[0])
        elif line[3] == "HI":
            intPovertyLevel = 7040 + (line[1] * 3660)
            if line[2] <= intPovertyLevel:
                lstBelowPoverty.append(line[0])
        else:
            intPovertyLevel = 6130 + (line[1] * 3180)
            if line[2] <= intPovertyLevel:
                lstBelowPoverty.append(line[0])
                
    # returns the value of lstBelowPoverty
    return lstBelowPoverty

def createMasterList():

    # imports and opens the family survey data text file
    inFileFamilySurvey = open("familySurveyData.txt","r")

    # initializes a list for each line in the file
    lstFamilySurvey = inFileFamilySurvey.read().splitlines()

    # initializes a master list
    mlstFamilySurvey = []

    # loops through each line in lstFamilySurvey
    # and converts the [0][1][2] indexes to integers
    # appends to master list
    for line in lstFamilySurvey:
        line = line.split()
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[2] = int(line[2])
        mlstFamilySurvey.append(line)
        
    # closes file
    inFileFamilySurvey.close()

    # returns the value of mlstFamilySurvey
    return mlstFamilySurvey

def main():

    # assigns the variable win to the drawwindow() function    
    win = drawWindow()

    # sets familyData equal to True
    familyData = True

    # run loop while familyData is equal to True condition
    while familyData == True:

        # captures the users mouse clicks
        ClickXY = win.getMouse()
        xPoint = ClickXY.getX()
        yPoint = ClickXY.getY()

        # if mouse clicks are between these points exit the window
        if xPoint > 375 and xPoint < 500 and yPoint > 150 and yPoint < 225:
            win.close()
            familyData = False

        # if mouse clicks are between these points import file
        elif xPoint > 75 and xPoint < 200 and yPoint > 50 and yPoint < 125:
            mlstFamilySurvey = createMasterList()

        # if mouse clicks are between these points run Report 1
        # and write out file
        elif xPoint > 225 and xPoint < 350 and yPoint > 50 and yPoint < 125:   
            lstReport01 = belowPoverty(mlstFamilySurvey)
            outFileReport(lstReport01,"FunkAmyReport01.txt",False)

        # if mouse clicks are between these points run Report 2 and
        # display in window
        elif xPoint > 375 and xPoint < 500 and yPoint > 50 and yPoint < 125:
            intAveIncome = averageIncome(mlstFamilySurvey)
            lstAboveAverageIncome = aboveAveIncomeFam(mlstFamilySurvey,intAveIncome)
            displayAboveAverageIncome(lstAboveAverageIncome, win)
            
        # if mouse clicks are between these points run Report 3 and 
        # display percentage in window
        elif xPoint > 75 and xPoint < 200 and yPoint > 150 and yPoint < 225:
            lstBelowPoverty = belowPoverty(mlstFamilySurvey)
            fltPercent = percentBelowPoverty(mlstFamilySurvey,lstBelowPoverty)
            displayPercentBelowPoverty(fltPercent,win)

            # creates bar chart to represent percentage
            for i in range(0,101,10):
                lblKey = Text(Point(((5.7 * i) + 10),475), i)
                lblKey.setTextColor("snow")
                lblKey.setSize(8)
                lblKey.draw(win)
            bar(Point(10,430),Point(5.7 * fltPercent,460),"midnight blue",win)
        # if mouse clicks are between these points run Report 4
        # and write out file
        elif xPoint >225 and xPoint <350 and yPoint > 150 and yPoint < 225:
            lstReport04 = insertPovertyField(mlstFamilySurvey)
            outFileReport(lstReport04,"FunkAmyReport04.txt",True)
main()
