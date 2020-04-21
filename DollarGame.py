from graphics import *
import time

class MoneyCircle():
    def __init__(self, x, y, money):
        self.x = x
        self.y = y
        self.money = money
        self.circleImage = Circle(Point(x, y), 50)
        self.circleImage.setFill('white')
        self.circleImage.setWidth(6)
        self.moneyText = Text(Point(x, y), str(self.money))
        self.moneyText.setSize(16)
        self.connections = []
    
    def drawCircle(self, win):
        self.circleImage.draw(win)
        self.moneyText.draw(win)
        
    def undrawCircle(self):
        self.circleImage.undraw()
        self.moneyText.undraw()
    
    def setConnections(self, connections):
        self.connections = connections
        
    def getConnections(self):
        return self.connections
    
    def increaseMoney(self):
        self.money += 1
        self.moneyText.setText(str(self.money))
    
    def decreaseMoney(self):
        self.money -= 1
        self.moneyText.setText(str(self.money))
        
    def lendMoney(self):
        for i in self.connections:
            i.increaseMoney()
            self.money -= 1
            self.moneyText.setText(str(self.money))
            time.sleep(1)
            
    
    def borrowMoney(self):
        for i in self.connections:
            i.decreaseMoney()
            self.money += 1
            self.moneyText.setText(str(self.money))
            time.sleep(1)
            
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getMoney(self):
        return self.money
    
    def getP1(self):
        return self.circleImage.getP1()
    
    def getP2(self):
        return self.circleImage.getP2()
    
    def selectColor(self, color):
        self.circleImage.setFill(color)

def allPos(CircleList):
    for i in CircleList:
        if (i.getMoney() < 0):
            return True
    
    return False

def circleClicked(CP, CircleList):
    for i in CircleList:
        if (CP.getX() >= i.getP1().getX() and CP.getX() <= i.getP2().getX() and CP.getY() >= i.getP1().getY() and CP.getY() <= i.getP2().getY()):
            return i
    
    return 0

width = 900
height = 900
gap = 20
rectHeight = (height - 4 * gap) / 3 

win = GraphWin('The Dollar Game', width, height)
background = Image(Point(width / 2, height / 2), 'Background.png')
background.draw(win)

Easy = Rectangle(Point(gap, gap), Point(width - gap, gap + rectHeight))
Easy.setFill('green')
EasyText = Text(Easy.getCenter(), 'Easy Mode')
EasyText.setSize(32)
EasyText.setStyle('bold')

Medium = Rectangle(Point(gap, 2 * gap + rectHeight), Point(width - gap, 2 * gap + 2 * rectHeight))
Medium.setFill('yellow')
MediumText = Text(Medium.getCenter(), 'Medium Mode')
MediumText.setSize(32)
MediumText.setStyle('bold')

Hard = Rectangle(Point(gap, 3 * gap + 2 * rectHeight), Point(width - gap, 3 * gap + 3 * rectHeight))
Hard.setFill('red')
HardText = Text(Hard.getCenter(), 'Hard Mode')
HardText.setSize(32)
HardText.setStyle('bold')

Lend = Rectangle(Point(width / 8, 6 * height / 8), Point(3 * width / 8, 7 * height / 8))
Lend.setFill('red')
LendText = Text(Lend.getCenter(), 'Lend')
LendText.setSize(16)

Borrow = Rectangle(Point(5 * width / 8, 6 * height / 8), Point(7 * width / 8, 7 * height / 8))
Borrow.setFill('red')
BorrowText = Text(Borrow.getCenter(), 'Borrow')
BorrowText.setSize(16)

DividingLine = Line(Point(0, 5 * height / 8), Point(width, 5 * height / 8))
DividingLine.setFill('red')
DividingLine.setOutline('red')
DividingLine.setWidth(10)

YouWin = Text(Point(width / 2, 6 * height / 8), 'You Win!')
YouWin.setSize(28)
YouWin.setTextColor('green')
YouWin.setStyle('bold')

ClickHere = Image(Point(width / 2, 7 * height / 8), 'Click.PNG')

while (True):
    Easy.draw(win)
    EasyText.draw(win)
    Medium.draw(win)
    MediumText.draw(win)
    Hard.draw(win)
    HardText.draw(win)
    
    OptionPicked = 'None'
    
    NoOptionPicked = True
    while (NoOptionPicked):
        CP = win.getMouse()
        if (CP.getX() >= Easy.getP1().getX() and CP.getX() <= Easy.getP2().getX() and CP.getY() >= Easy.getP1().getY() and CP.getY() <= Easy.getP2().getY()):
            OptionPicked = 'Easy'
            NoOptionPicked = False
        elif (CP.getX() >= Medium.getP1().getX() and CP.getX() <= Medium.getP2().getX() and CP.getY() >= Medium.getP1().getY() and CP.getY() <= Medium.getP2().getY()):
            OptionPicked = 'Medium'
            NoOptionPicked = False
        elif (CP.getX() >= Hard.getP1().getX() and CP.getX() <= Hard.getP2().getX() and CP.getY() >= Hard.getP1().getY() and CP.getY() <= Hard.getP2().getY()):
            OptionPicked = 'Hard'
            NoOptionPicked = False
            
    Easy.undraw()
    EasyText.undraw()
    Medium.undraw()
    MediumText.undraw()
    Hard.undraw()
    HardText.undraw()
        
    DividingLine.draw(win)
    
    if (OptionPicked == 'Easy'):
        
        Circle1 = MoneyCircle(100, 200, 3)
        Circle2 = MoneyCircle(400, 150, -1)
        Circle3 = MoneyCircle(800, 300, -2)
        Circle4 = MoneyCircle(600, 400, 2)
        
        CircleList = [Circle1, Circle2, Circle3, Circle4]
        
        Circle1.setConnections([Circle2, Circle3, Circle4])
        Circle2.setConnections([Circle1])
        Circle3.setConnections([Circle1, Circle4])
        Circle4.setConnections([Circle1, Circle3])

        LineList = []
        for i in CircleList:
            for j in i.getConnections():
                LineList.append(Line(Point(i.getX(), i.getY()), Point(j.getX(), j.getY())))
        
        for i in LineList:
            i.setWidth(5)
            i.draw(win)
            
        for i in CircleList:
            i.drawCircle(win)
            
        while (allPos(CircleList)):
            NoOptionPicked = True
            while (NoOptionPicked):
                CP = win.getMouse()
                CC = circleClicked(CP, CircleList)
                if (CC != 0):
                    
                    CC.selectColor('green')
                    NoOptionPicked = False
                    Lend.draw(win)
                    LendText.draw(win)
                    Borrow.draw(win)
                    BorrowText.draw(win)
                    
                    CP = win.getMouse()
                    if (CP.getX() >= Lend.getP1().getX() and CP.getX() <= Lend.getP2().getX() and CP.getY() >= Lend.getP1().getY() and CP.getY() <= Lend.getP2().getY()):
                        CC.lendMoney()
                    elif (CP.getX() >= Borrow.getP1().getX() and CP.getX() <= Borrow.getP2().getX() and CP.getY() >= Borrow.getP1().getY() and CP.getY() <= Borrow.getP2().getY()):
                        CC.borrowMoney()
                    
                    CC.selectColor('white')
                    Lend.undraw()
                    LendText.undraw()
                    Borrow.undraw()
                    BorrowText.undraw()
        
        YouWin.draw(win)
        ClickHere.draw(win)
        win.getMouse()
        YouWin.undraw()
        ClickHere.undraw()
        DividingLine.undraw()
        for i in CircleList:
            i.undrawCircle()
            
        for i in LineList:
            i.undraw()

    elif (OptionPicked == 'Medium'):
        
        Circle1 = MoneyCircle(100, 100, 2)
        Circle2 = MoneyCircle(150, 400, -3)
        Circle3 = MoneyCircle(800, 150, 1)
        Circle4 = MoneyCircle(600, 370, 1)
        Circle5 = MoneyCircle(400, 500, -2)
        Circle6 = MoneyCircle(400, 50, 3)
        
        CircleList = [Circle1, Circle2, Circle3, Circle4, Circle5, Circle6]
        
        Circle1.setConnections([Circle2, Circle4])
        Circle2.setConnections([Circle1, Circle5, Circle6])
        Circle3.setConnections([Circle4, Circle6])
        Circle4.setConnections([Circle1, Circle3])
        Circle5.setConnections([Circle2, Circle6])
        Circle6.setConnections([Circle2, Circle3, Circle5])
        
        LineList = []
        for i in CircleList:
            for j in i.getConnections():
                LineList.append(Line(Point(i.getX(), i.getY()), Point(j.getX(), j.getY())))
        
        for i in LineList:
            i.setWidth(5)
            i.draw(win)
            
        for i in CircleList:
            i.drawCircle(win)
            
        while (allPos(CircleList)):
            NoOptionPicked = True
            while (NoOptionPicked):
                CP = win.getMouse()
                CC = circleClicked(CP, CircleList)
                if (CC != 0):
                    
                    CC.selectColor('green')
                    NoOptionPicked = False
                    Lend.draw(win)
                    LendText.draw(win)
                    Borrow.draw(win)
                    BorrowText.draw(win)
                    
                    CP = win.getMouse()
                    if (CP.getX() >= Lend.getP1().getX() and CP.getX() <= Lend.getP2().getX() and CP.getY() >= Lend.getP1().getY() and CP.getY() <= Lend.getP2().getY()):
                        CC.lendMoney()
                    elif (CP.getX() >= Borrow.getP1().getX() and CP.getX() <= Borrow.getP2().getX() and CP.getY() >= Borrow.getP1().getY() and CP.getY() <= Borrow.getP2().getY()):
                        CC.borrowMoney()
                    
                    CC.selectColor('white')
                    Lend.undraw()
                    LendText.undraw()
                    Borrow.undraw()
                    BorrowText.undraw()
        
        YouWin.draw(win)
        ClickHere.draw(win)
        win.getMouse()
        YouWin.undraw()
        ClickHere.undraw()
        DividingLine.undraw()
        for i in CircleList:
            i.undrawCircle()
            
        for i in LineList:
            i.undraw()
        
    elif (OptionPicked == 'Hard'):
        
        Circle1 = MoneyCircle(100, 100, 1)
        Circle2 = MoneyCircle(450, 60, -2)
        Circle3 = MoneyCircle(800, 150, -3)
        Circle4 = MoneyCircle(125, 340, 2)
        Circle5 = MoneyCircle(500, 300, 5)
        Circle6 = MoneyCircle(720, 300, 2)
        Circle7 = MoneyCircle(300, 475, -2)
        Circle8 = MoneyCircle(700, 450, -3)
        
        CircleList = [Circle1, Circle2, Circle3, Circle4, Circle5, Circle6, Circle7, Circle8]
        
        Circle1.setConnections([Circle2, Circle4])
        Circle2.setConnections([Circle1, Circle3, Circle5])
        Circle3.setConnections([Circle2, Circle6])
        Circle4.setConnections([Circle1, Circle5, Circle7])
        Circle5.setConnections([Circle2, Circle4, Circle6, Circle7, Circle8])
        Circle6.setConnections([Circle3, Circle5])
        Circle7.setConnections([Circle4, Circle5])
        Circle8.setConnections([Circle5])
        
        LineList = []
        for i in CircleList:
            for j in i.getConnections():
                LineList.append(Line(Point(i.getX(), i.getY()), Point(j.getX(), j.getY())))
        
        for i in LineList:
            i.setWidth(5)
            i.draw(win)
            
        for i in CircleList:
            i.drawCircle(win)
            
        while (allPos(CircleList)):
            NoOptionPicked = True
            while (NoOptionPicked):
                CP = win.getMouse()
                CC = circleClicked(CP, CircleList)
                if (CC != 0):
                    
                    CC.selectColor('green')
                    NoOptionPicked = False
                    Lend.draw(win)
                    LendText.draw(win)
                    Borrow.draw(win)
                    BorrowText.draw(win)
                    
                    CP = win.getMouse()
                    if (CP.getX() >= Lend.getP1().getX() and CP.getX() <= Lend.getP2().getX() and CP.getY() >= Lend.getP1().getY() and CP.getY() <= Lend.getP2().getY()):
                        CC.lendMoney()
                    elif (CP.getX() >= Borrow.getP1().getX() and CP.getX() <= Borrow.getP2().getX() and CP.getY() >= Borrow.getP1().getY() and CP.getY() <= Borrow.getP2().getY()):
                        CC.borrowMoney()
                    
                    CC.selectColor('white')
                    Lend.undraw()
                    LendText.undraw()
                    Borrow.undraw()
                    BorrowText.undraw()
        
        YouWin.draw(win)
        ClickHere.draw(win)
        win.getMouse()
        YouWin.undraw()
        ClickHere.undraw()
        DividingLine.undraw()
        for i in CircleList:
            i.undrawCircle()
            
        for i in LineList:
            i.undraw()
        
        
    
                    
        
    
    