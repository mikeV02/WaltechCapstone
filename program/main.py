#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
Waltech Ladder Maker is distributed under the MIT License. 
Copyright (c) 2014 Karl Walter.  karl (at) waltech.com
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""



"""
to add element tool:
    need big icon and small icon. 36x27 and 58x60
    Add a button 
        to UI with QT designer
    Add element 
        to list in clsss elementList
    Add toolActionGroup.addAction(self.ui.actionContNO) <--example ContNO
        to mainwindowUI
    Add self.connect(self.ui.actionContNO, QtCore.SIGNAL("triggered()"),lambda who=1: self.anyButton(who))
        to signalConnections
    THEN:    
    give it a function in manageGrid (managegrid.py) if it is an edit tool.
    give it an elif in showMarker (if edit tool)
    call that function apropriatly in leftClick function
    popup
    popup as edit
todos for ver:
(anything with ###)
 
"""
"""
useful links:
SEGFAULT and text on qgraphicsitem:
http://www.riverbankcomputing.com/pipermail/pyqt/2013-January/032258.html
https://wiki.python.org/moin/HowTo/Sorting/
http://stackoverflow.com/questions/11945183/what-are-good-practices-for-avoiding-crashes-hangs-in-pyqt
http://www.diveintopython.net/object_oriented_framework/defining_classes.html
"""



from managegrid import ManageGrid, cellStruct
from LadderToOutLine import ladderToOutLine
from OutLineToC import OutLineToC
from tester import tester

#import SerialCommunication				#importing Chris's function\
import threading
import time
import popupDialogs
import copy
import sys
import os
import time
import re
import pickle #for saving the file
from PyQt4 import QtCore, QtGui
from PyQt4 import QtSvg
from PyQt4.QtGui import QApplication, QDialog, QMainWindow, QActionGroup
from PyQt4.QtGui import QPrinter, QPainter
from PyQt4.QtCore import Qt
from PyQt4.Qt import QFont
from PyQt4.Qt import QString
from PyQt4.Qt import QStringList
from SerialCommunication import SerialCommunicator

from mainwindow_ui import Ui_MainWindow


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class mainWindowUI(QMainWindow): #mainwindow inheriting from QMainWindow here.

    def __init__(self):
        QDialog.__init__(self)# Constructs a dialog with parent parent. self being ImageDailog
        # Set up the UI from Designer:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.DontAdjustForAntialiasing #seems to help fix artifacts left by mouse track markers
        #make a scene:
        self.scene = QtGui.QGraphicsScene()

        self.CounterList = []
        self.TimerList = []
        
        #set it to show in the graphicsview window:
        self.ui.graphicsView.setScene(self.scene)
        self.items=[QtGui.QGraphicsTextItem(),QtGui.QGraphicsRectItem()]#for squares and indexes that follow mouse
        self.ui.graphicsView.viewport().installEventFilter(self)#for mouse functions
        #Setup IO table on right
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 45)
        self.ui.tableWidget.setColumnWidth(2, 50)
        self.ui.tableWidget.setColumnWidth(3, 40)
        self.ui.tableWidget.setColumnWidth(4, 30)
        #self.ui.tableWidget.setColumnWidth(5, 140)
        #Strech = QtGui.QHeaderView.Stretch
        #self.ui.tableWidget.horizontalHeader().setResizeMode(Strech)
		
		#Setup Data table on right:
        #self.ui.tableDataFiles.setColumnWidth(0, 75)

        #setup datagrid and elements:
        self.Tools = elementList(elementStruct)
        self.setupDataGrid()#set up rung variables:
        self.signalConnections()
        self.setupIOarrays()

        #default:
        self.currentHW = "Waltech"
        self.ui.actionPWM.setEnabled(False)
        self.ui.actionADC.setEnabled(False)
        self.projectName = None
        self.currentFileDir = None
        
    def setupIOarrays(self):
        self.live = False
        self.inputs = [None] * 23
        self.outputs = [None] * 23

    def signalConnections(self):
        #connect signals:
        self.ui.actionUndo.triggered.connect(self.unDo)
        self.ui.actionRedo.triggered.connect(self.reDo)
        self.ui.actionSave_As.triggered.connect(self.saveFileAs)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionNew.triggered.connect(self.newFile)
        self.ui.actionWhatsThis.triggered.connect(self.whatsThis)
        self.ui.actionCheck_HW_2.triggered.connect(self.checkHW)
        self.ui.actionUSBHelp.triggered.connect(self.USBHelp)
        self.ui.actionArduinoMega_IO.triggered.connect(self.ArduinoMegaIOHelp)
        self.ui.actionArduinoUno_IO.triggered.connect(self.ArduinoUnoIOHelp)
        self.ui.actionArduinoNano_IO.triggered.connect(self.ArduinoNanoIOHelp)
        self.ui.actionAbout.triggered.connect(self.AboutHelp)

        self.ui.infoButton.clicked.connect(self.parseGrid)
        self.ui.liveButton.clicked.connect(self.startFeedback)
        #FOR DEBUG BUTTON
        #self.ui.pushButton.clicked.connect(self.showInfo)
        #self.ui.pushButton_3.clicked.connect(self.printLadder)

        ##003##
        #action group for tool buttons:
        self.connect(self.ui.actionContNO, QtCore.SIGNAL("triggered()"),lambda who="contNO": self.anyButton(who))
        self.connect(self.ui.actionContNC, QtCore.SIGNAL("triggered()"),lambda who="contNC": self.anyButton(who))
        self.connect(self.ui.actionCoil, QtCore.SIGNAL("triggered()"),lambda who="Coil": self.anyButton(who))
        #self.connect(self.ui.actionCoilNot, QtCore.SIGNAL("triggered()"),lambda who="CoilNot": self.anyButton(who))
        self.connect(self.ui.actionaddRung, QtCore.SIGNAL("triggered()"),lambda who="addRung": self.anyButton(who))
        self.connect(self.ui.actionWiden, QtCore.SIGNAL("triggered()"),lambda who="Widen": self.anyButton(who))
        #self.connect(self.ui.actionORbranch, QtCore.SIGNAL("triggered()"),lambda who="blankOR": self.anyButton(who))
        self.connect(self.ui.actionDEL, QtCore.SIGNAL("triggered()"),lambda who="Del": self.anyButton(who))
        self.connect(self.ui.actionORwire, QtCore.SIGNAL("triggered()"),lambda who="ORwire": self.anyButton(who))
        self.connect(self.ui.actionNarrow, QtCore.SIGNAL("triggered()"),lambda who="Narrow": self.anyButton(who))
        #self.connect(self.ui.actionRising, QtCore.SIGNAL("triggered()"),lambda who="Rising": self.anyButton(who))
        self.connect(self.ui.actionFalling, QtCore.SIGNAL("triggered()"),lambda who="Fall": self.anyButton(who))
        self.connect(self.ui.actionTimer, QtCore.SIGNAL("triggered()"),lambda who="Timer": self.anyButton(who))
        self.connect(self.ui.actionCounter, QtCore.SIGNAL("triggered()"),lambda who="Counter": self.anyButton(who))
        self.connect(self.ui.actionEquals, QtCore.SIGNAL("triggered()"),lambda who="Equals": self.anyButton(who))
        self.connect(self.ui.actionPlus, QtCore.SIGNAL("triggered()"),lambda who="Plus": self.anyButton(who))
        self.connect(self.ui.actionMinus, QtCore.SIGNAL("triggered()"),lambda who="Minus": self.anyButton(who))
        self.connect(self.ui.actionMove, QtCore.SIGNAL("triggered()"),lambda who="Move": self.anyButton(who))
        self.connect(self.ui.actionMult, QtCore.SIGNAL("triggered()"),lambda who="Mult": self.anyButton(who))
        self.connect(self.ui.actionGreater, QtCore.SIGNAL("triggered()"),lambda who="Greater": self.anyButton(who))
        self.connect(self.ui.actionLessthan, QtCore.SIGNAL("triggered()"),lambda who="Lessthan": self.anyButton(who))
        self.connect(self.ui.actionGreaterOrEq, QtCore.SIGNAL("triggered()"),lambda who="GreaterOrEq": self.anyButton(who))
        self.connect(self.ui.actionLessOrEq, QtCore.SIGNAL("triggered()"),lambda who="LessOrEq": self.anyButton(who))
        self.connect(self.ui.actionPWM, QtCore.SIGNAL("triggered()"),lambda who="PWM": self.anyButton(who))
        self.connect(self.ui.actionADC, QtCore.SIGNAL("triggered()"),lambda who="ADC": self.anyButton(who))
        self.connect(self.ui.actionDivide, QtCore.SIGNAL("triggered()"),lambda who="Divide": self.anyButton(who))


        ##002##
        #make a actiongroup so tools are exclusive (only one clicked)
        toolActionGroup = QActionGroup(self.ui.toolBar)#toolbar is named in _ui.py
        toolActionGroup.addAction(self.ui.actionContNO)
        toolActionGroup.addAction(self.ui.actionContNC)
        toolActionGroup.addAction(self.ui.actionCoil)
        #toolActionGroup.addAction(self.ui.actionCoilNot)
        toolActionGroup.addAction(self.ui.actionaddRung)
        toolActionGroup.addAction(self.ui.actionWiden)
        #toolActionGroup.addAction(self.ui.actionORbranch)
        toolActionGroup.addAction(self.ui.actionDEL)
        toolActionGroup.addAction(self.ui.actionORwire)
        toolActionGroup.addAction(self.ui.actionNarrow)
        #toolActionGroup.addAction(self.ui.actionRising)
        toolActionGroup.addAction(self.ui.actionFalling)
        toolActionGroup.addAction(self.ui.actionTimer)
        toolActionGroup.addAction(self.ui.actionCounter)
        toolActionGroup.addAction(self.ui.actionEquals)
        toolActionGroup.addAction(self.ui.actionPlus)
        toolActionGroup.addAction(self.ui.actionMinus)
        toolActionGroup.addAction(self.ui.actionMove)
        toolActionGroup.addAction(self.ui.actionMult)
        toolActionGroup.addAction(self.ui.actionGreater)
        toolActionGroup.addAction(self.ui.actionLessthan)
        toolActionGroup.addAction(self.ui.actionGreaterOrEq)
        toolActionGroup.addAction(self.ui.actionLessOrEq)
        toolActionGroup.addAction(self.ui.actionPWM)
        toolActionGroup.addAction(self.ui.actionADC)
        toolActionGroup.addAction(self.ui.actionDivide)

        toolActionGroup.setExclusive(True)

        self.connect(self.ui.actionWaltech, QtCore.SIGNAL("triggered()"),lambda HW="Waltech": self.chooseHW(HW))
        self.connect(self.ui.actionArduinoUno, QtCore.SIGNAL("triggered()"),lambda HW="ArduinoUno": self.chooseHW(HW))
        self.connect(self.ui.actionArduinoNano, QtCore.SIGNAL("triggered()"),lambda HW="ArduinoNano": self.chooseHW(HW))
        self.connect(self.ui.actionArduinoMega, QtCore.SIGNAL("triggered()"),lambda HW="ArduinoMega": self.chooseHW(HW))
        hwActionGroup = QActionGroup(self.ui.menuDiagnostics)
        hwActionGroup.addAction(self.ui.actionWaltech)
        hwActionGroup.addAction(self.ui.actionArduinoUno)
        hwActionGroup.addAction(self.ui.actionArduinoNano)
        hwActionGroup.addAction(self.ui.actionArduinoMega)

    def checkmarkHW(self):
            pass
        #print "hardware clicked"
    ##########hardware choosing
    def chooseHW(self,HW):
        oldHW = self.currentHW
        self.currentHW = HW
        if self.checkForHiIO(HW)==True:
            #make popup refusing to change
            self.dialog = popupDialogs.ardIODialog()
            self.dialog.exec_()# For Modal dialogs
            self.currentHW = oldHW #change back
            HW = oldHW
        if str(HW)=="Waltech":
            self.ui.actionPWM.setEnabled(False)
            self.ui.actionADC.setEnabled(False) 
            self.ui.actionWaltech.setChecked(True)
        if str(HW)=="ArduinoUno": 
            self.ui.actionPWM.setEnabled(True)
            self.ui.actionADC.setEnabled(True)
            self.ui.actionArduinoUno.setChecked(True)
        if str(HW)=="ArduinoNano": 
            self.ui.actionPWM.setEnabled(True)
            self.ui.actionADC.setEnabled(True)
            self.ui.actionArduinoNano.setChecked(True)
        if str(HW)=="ArduinoMega": 
            self.ui.actionPWM.setEnabled(True)
            self.ui.actionADC.setEnabled(True)
            self.ui.actionArduinoMega.setChecked(True)
        print "Hardware:", HW
        ##ADDED BY MIGUEL
        self.checkHW()
        ###
           
    def checkForHiIO(self,oldHW):
        #go through grid and look for I higher than 12 for Waltech, 5 for ArduinoUno , 6 for ArduinoNano 
        if self.currentHW == "Waltech" and ( self.checkInputNums() > 12 or self.checkOutputNums() >12 or self.checkADCPWMNs() != [0,0]):
            print ">>too high number io or have PWM or ADC"
            return True
        if self.currentHW == "ArduinoUno" and ( self.checkInputNums() > 5 or self.checkOutputNums() >7 or self.checkADCPWMNs()[0] > 4 or self.checkADCPWMNs()[1] > 2):
            print ">>too high number io or PWM or ADC"
            return True
        if self.currentHW == "ArduinoNano" and ( self.checkInputNums() > 6 or self.checkOutputNums() >8 or self.checkADCPWMNs()[0] > 4 or self.checkADCPWMNs()[1] > 2):
            print ">>too high number io or PWM or ADC"
            return True
        return False 

    def checkADCPWMNs(self):
        #count up PWMs and ADCs
        #PWMADC[0] is number pf PWMs
        #PWMADC[1] is number pf ADCs
        height = len(self.grid)
        width = len(self.grid[0])
        PWMADC = [0,0]
        for i in range(height):
            for j in range(width):
                if self.grid[i][j].MTorElement != None:
                    print"mtorelement", self.grid[i][j].MTorElement
                    if self.grid[i][j].MTorElement[:3] == 'PWM': 
                        PWMADC[0] = PWMADC[0] +1
                    if self.grid[i][j].MTorElement[:3] == 'ADC':
                        PWMADC[1] = PWMADC[1] +1
        print "PWM,ADC ",PWMADC
        return PWMADC

    #def checkInputNums(self):
        #for i in range(22, 0, -1):
        #    if self.inputs[i] != None: return i

    #def checkOutputNums(self):
        #for i in range(22, 0, -1):
        #    if self.outputs[i] != None: return i

    ### TEDDY
    def checkInputNums(self):
        height = len(self.grid)
        width = len(self.grid[0])
        MaxIONum = 0
        for i in range(height):

            for j in range(width):
                if self.grid[i][j].ioAssign != None and self.grid[i][j].ioAssign[:3] == 'in_':
                    #print "input:  ", self.grid[i][j].ioAssign[3:]
                    if int(self.grid[i][j].ioAssign[3:]) > MaxIONum: MaxIONum = int(self.grid[i][j].ioAssign[3:])
        return MaxIONum

    def checkOutputNums(self):
        height = len(self.grid)
        width = len(self.grid[0])
        MaxIONum = 0
        for i in range(height):

            for j in range(width):
                if self.grid[i][j].ioAssign != None and self.grid[i][j].ioAssign[:4] == 'out_':
                    #print "input:  ", self.grid[i][j].ioAssign[3:]
                    if int(self.grid[i][j].ioAssign[4:]) > MaxIONum: MaxIONum = int(self.grid[i][j].ioAssign[4:])
        return MaxIONum
    ##########hardware choosing^^^^^   

    def USBHelp(self):
       self.dialog = popupDialogs.USBHelpDialog()
       self.dialog.exec_()# For Modal dialogs

    def ArduinoUnoIOHelp(self):
       self.dialog = popupDialogs.ArduinoUnoIOHelpDialog()
       self.dialog.exec_()# For Modal dialogs
    def ArduinoNanoIOHelp(self):
       self.dialog = popupDialogs.ArduinoNanoIOHelpDialog()
       self.dialog.exec_()# For Modal dialogs
    def ArduinoMegaIOHelp(self):
       self.dialog = popupDialogs.ArduinoMegaIOHelpDialog()
       self.dialog.exec_()# For Modal dialogs
       
    def AboutHelp(self):
        self.dialog = popupDialogs.AboutHelpDialog()
        self.dialog.setWindowTitle('About')
        self.dialog.exec_()# For Modal dialogs
       
    def checkHW(self):
        plat = sys.platform.lower()    # try to detect the OS so that a device can be selected...
        print "checked platform"
        if   plat[:5] == 'linux': opSys = "NIX"
        elif plat == 'win32': opSys = "WIN"
        elif plat == "darwin": opSys = "MAC"
        else: opSys = "WIN"
        
        ###MODIFIED BY MIGUEL
        DUDE, self.PORT = tester(opSys,self.currentHW).test1(self.ui.textBrowser)
        self.CheckPort(self.PORT)
        ###
    
    ###ADDED BY MIGUEL
    def CheckPort(self, DUDE):
        print "THIS IS THE SERIAL PORT ", self.PORT
    ###


    def printLadder(self):
        #printer = QPrinter(QPrinter.HighResolution)
        printer = QPrinter()
        dialog = QtGui.QPrintDialog(printer, self)   

        if dialog.exec_() != QDialog.Accepted:
            return
        #printer.setResolution(600)
        #resolution = printer.resolution()
        #pageRect = printer.pageRect()
        painter = QPainter(printer)
        self.scene.render(painter)
        #self.ui.tableWidget.render(painter)
        del painter

    def makeImage(self):
    #def printLadder(self):   
        image = QtGui.QImage(400,400,QtGui.QImage.Format_ARGB32)#for png
        #image = QtGui.QImage(256,256,QtGui.QImage.Format_RGB32)
        painter = QtGui.QPainter(image)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        self.scene.render(painter)
        painter.end()
        print "saving image"

        if image.save('hexes/newImage.png', 'PNG'):
            print('saved')
        else:
            print("didn't save")
        #image.save("out.png")
        del painter




    def setupDataGrid(self):
        #x,y, element there, rung there, & there, element name, variable name, i/o connection.
        self.grid = [[]] # grid: list of rows  ex: grid [2][6] gives cell 6 in row(rung) 2
        self.reDoGrid = [[[]]]# list of grids for redo
        self.unDoGrid = [[[]]]# list of grids for undo
        self.currentTool = 0 #to track the tool being used
        width=10
        for i in range(width):#fill the first row
            self.grid[0].append(cellStruct(i*60, 60, "MT","Rung", None, None, None, None, None, False, False, False, False, False, False,None,None,None,None,None, False, None))
            #self.grid[0].append(cellStruct(i*60, 60, "MT","Rung", None, None, None, None, None, False, False, False, False, False, False,None,None,None,None,None))
        for i in range(1,6):# add 5 more rungs to start
            ManageGrid(self.grid, self.scene,self.Tools,self.items).insertRung(i)        
  


    def reFillList(self,uiList):
        #clear list
        while uiList.rowCount() > 0 : uiList.removeRow(0)
        #rows = uiList.rowCount()
        #for i in range(rows):
        #    #delete this row
        #   uiList.removeRow(0)
        #refill list
        print "refilling list"
        height = len(self.grid)
        width = len(self.grid[0])
        for i in range(height):
            for j in range(width):
                if self.grid[i][j].MTorElement != "MT" and self.grid[i][j].MTorElement !="blankOR":
                    uiList.setSortingEnabled(False)#stop sorting while adding row
                    uiList.setRowCount(uiList.rowCount()+1)
                    numRows= uiList.rowCount()
                    try: uiList.setItem(numRows-1,0,QtGui.QTableWidgetItem(self.grid[i][j].variableName))
                    except: pass
                    try: uiList.setItem(numRows-1,2,QtGui.QTableWidgetItem(self.grid[i][j].ioAssign))
                    except: pass
                    try: uiList.setItem(numRows-1,1,QtGui.QTableWidgetItem(self.grid[i][j].MTorElement))
                    except: pass
                    try: uiList.setItem(numRows-1,3,QtGui.QTableWidgetItem(str(i)+","+str(j)))
                    except: pass
                    try: uiList.setItem(numRows-1,4,QtGui.QTableWidgetItem(str(i)+","+str(j)))
                    except: pass

                    ###ADDED BY MIGUEL Done Bit on Left Table
                    try:
                        if "Select" not in self.grid[i][j].doneBit:
                            try: uiList.setItem(numRows-1,5,QtGui.QTableWidgetItem(self.grid[i][j].doneBit))
                            except: pass
                    except: pass
                    ###

                    uiList.setSortingEnabled(True)
  

    #track which tool is being used. maybe use names here?
    def anyButton(self,who): 
        self.currentTool = who  
        #print who
   
    def parseGrid(self):
        #self.showInfo()
        font=self.ui.textBrowser.currentFont()
        font.setWeight(QFont.Bold)
        self.ui.textBrowser.setCurrentFont(font)
        self.ui.textBrowser.setText("compiling with avr-gcc")
        QApplication.processEvents()#this makes the UI update before going on.
        font.setWeight(QFont.Normal)
        self.ui.textBrowser.setCurrentFont(font)
        QApplication.processEvents()#this makes the UI update before going on.
        outLine,self.CounterList,self.TimerList = ladderToOutLine(self.grid).makeOutLine()
        #self.CounterandTimerCheck(outLine)
        #print "Counter List: \n"
        #for i in range(len(self.CounterList)):
        #    print self.CounterList[i], "\n"
        #print "Timer List: \n"
        #for i in range(len(self.TimerList)):
        #    print self.TimerList[i], "\n"
        OutLineToC(self.grid,self.currentHW).makeC(outLine,self.ui.textBrowser)
        #hexMaker(self).self.saveCfileAndCompile(C_txt,displayOutputPlace)
		
    def CounterandTimerCheck(self,outLine):
        
        self.CounterList = 0
        self.TimerList = 0
    
        #for i in range (len(outLine)): 
        #
        #    if outLine[i][0][:8]== "Counter_"  : 
        #        print str(outLine[i][0]),"\n",i,"\n\n"
        #        #if "\n    uint8_t "+ str(outLine[i][0]) +" = 0;\n" not in C_txt and "rungstate_" not in outLine[i][0]:
        #    
        #    
        #    if  outLine[i][0][:6] == "Timer_" : 
        #        print str(outLine[i][0]),"\n",i,"\n\n"
        #        #if "\n    uint8_t "+ str(outLine[i][0]) +" = 0;\n" not in C_txt and "rungstate_" not in outLine[i][0]:
        
        
    def startFeedback(self):
        self.live = True
        self.ui.liveButton.clicked.disconnect()
        self.ui.liveButton.clicked.connect(self.stopFeedback)
        self.ui.liveButton.setText("Stop Live")

        


        CounterLocations = []
        TimerLocations = []
        
        CounterPrecedingElement = []
        TimerPrecedingElement = []
        
        #x = 0
        feedback = []
        
        WaltSerial = SerialCommunicator(self.PORT, self.currentHW)

		##START ADDED BY CHRIS
		
        from CounterTimer import Counter,Timer

        #for timer in range(len(self.grid)):
        TimerListLive = []
        CounterListLive = []
            
        if len(self.TimerList) > 0:    
            for timer in range(len(self.TimerList)):
                temp = Timer(self.TimerList[timer])
                TimerListLive.append(temp)
                
        print len(self.TimerList) , "\n"
                
        if len(self.CounterList) > 0:
            for counter in range(len(self.CounterList)):
                temp = Counter(self.CounterList[counter])
                CounterListLive.append(temp)
   
		
        counterIndex = 0
        timerIndex = 0
        
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y].variableName is not None:
                    if(counterIndex < len(CounterListLive)):
                        if (self.grid[x][y].MTorElement+"_"+self.grid[x][y].variableName) == CounterListLive[counterIndex].name:
                            CounterListLive[counterIndex].setLocationType(x,y,self.grid[x][y].type)
                            CounterListLive[counterIndex].preset = self.grid[x][y].setPoint
                            counterIndex = counterIndex + 1
                    if(timerIndex < len(TimerListLive)):

                        if (self.grid[x][y].MTorElement+"_"+self.grid[x][y].variableName) == TimerListLive[timerIndex].name:
                            TimerListLive[timerIndex].setLocationType(x,y,self.grid[x][y].type)
                            TimerListLive[timerIndex].preset = int(float(self.grid[x][y].setPoint) * 100)
                            timerIndex = timerIndex + 1
                    
        counterIndex = 0
        timerIndex = 0
                    
        #for x in range(len(CounterListLive)):
        #    print CounterListLive[x].name, CounterListLive[x].x, CounterListLive[x].y, "\n"
        #    
        #for x in range(len(TimerListLive)):
        #    print TimerListLive[x].name, TimerListLive[x].x, TimerListLive[x].y, "\n"                   


                       
        

        
        if len(TimerListLive) > 0:
            for timer in range(len(TimerListLive)):
                x,y = TimerListLive[timer].x, (TimerListLive[timer].y - 1)



                if y < 0:
                        TimerListLive[timer].setPrevElement(-1,-1,"None")

                
                while y > -1:
                    if self.grid[x][y].variableName is not None:
                        TimerListLive[timer].setPrevElement(x,y,self.grid[x][y].MTorElement)

                        break            
                    elif y == 0:
                        TimerListLive[timer].setPrevElement(-1,-1,"None")

                        y = y - 1
        

                    y = y - 1
                    
        if len(CounterListLive) > 0:
            for counter in range(len(CounterListLive)):
                x,y = CounterListLive[counter].x, (CounterListLive[counter].y - 1)



                if y < 0:
                        CounterListLive[counter].setPrevElement(-1,-1,"None")

                
                while y > -1:
                    if self.grid[x][y].variableName is not None:
                        CounterListLive[counter].setPrevElement(x,y,self.grid[x][y].MTorElement)

                        break            
                    elif y == 0:
                        CounterListLive[counter].setPrevElement(-1,-1,"None")

                        y = y - 1
        

                    y = y - 1

                    
        for x in range(len(CounterListLive)):
            print CounterListLive[x].name, CounterListLive[x].x, CounterListLive[x].y, CounterListLive[x].type, CounterListLive[x].preset, "\n"
            print CounterListLive[x].Prevelement, CounterListLive[x].Prevx, CounterListLive[x].Prevy, "\n"
            
        for x in range(len(TimerListLive)):
            print TimerListLive[x].name, TimerListLive[x].x, TimerListLive[x].y,TimerListLive[x].type, TimerListLive[x].preset, "\n"
            print TimerListLive[x].Prevelement, TimerListLive[x].Prevx, TimerListLive[x].Prevy, "\n"
                       
                    
        #        
        #
        #
        #print "Previous Elements: \n"
        #
        #for i in range(len(TimerPrecedingElement)/2):
        #    print TimerPrecedingElement[(i*2)], " ", TimerPrecedingElement[(i*2) +1], "\n"
        #
        #for i in range(len(CounterPrecedingElement)/2):
        #    print CounterPrecedingElement[(i*2)], " ", CounterPrecedingElement[(i*2) +1], "\n"
        #
        #print "Timers: \n"
        #for i in range(len(self.TimerList)):
        #    #print len(TimerLocations), "\n"
        #    print self.TimerList[i], " ",TimerLocations[i * 2], " ",TimerLocations[(i * 2) + 1] , "\n"
        #    
        #print "Counters: \n"
        #for i in range(len(self.CounterList)):
        #    print self.CounterList[i], " ",CounterLocations[i * 2], " ", CounterLocations[(i * 2) + 1] , "\n"
        #
        #
        #prevInputToCounter = []    
        #Countervalues = []
        #
        #for i in range(len(self.CounterList)):
        #    prevInputToCounter.append(0);
        #    
        #for i in range(len(self.CounterList)):
        #    Countervalues.append(0);
        #


        
        import threading
        
        def TimerTracker(Timer, CounterListLive, TimerListLive):
            while self.live:
                now = time.time()
                tempPrevx = int(Timer.Prevx)
                tempPrevy = int(Timer.Prevy)
                tempPrevElement = self.grid[tempPrevx][tempPrevy].MTorElement
                
                if((tempPrevElement == "contNC" or tempPrevElement == "contNO") and Timer.type == "Timer_On_Delay"):       

                    SwitchValue = 45
                    
                    if(tempPrevElement == "contNC"):
                        #print "Cont nc\n"
                        SwitchValue = self.grid[tempPrevx][tempPrevy].switch
                    else:
                        #print "Cont no\n"
                        SwitchValue = (self.grid[tempPrevx][tempPrevy].switch == 0)
                
                    if SwitchValue == 1:
                        Timer.currentValue += 1
                        #print Timer.currentValue, "\n"
                        if Timer.currentValue >= Timer.preset:
                            Timer.done = 1
                            self.grid[Timer.x][Timer.y].switch = 1
                    elif SwitchValue == 0:
                        Timer.currentValue = 0
                        Timer.done = 0
                        self.grid[Timer.x][Timer.y].switch = 0
                    Timer.prevInput = self.grid[tempPrevx][tempPrevy].switch
                elif ((tempPrevElement == "Counter" or tempPrevElement == "Timer") and Timer.type == "Timer_On_Delay"):
                    tempVariableName = self.grid[tempPrevx][tempPrevy].MTorElement+"_"+self.grid[tempPrevx][tempPrevy].variableName
                    if tempPrevElement == "Counter":
                        for counter in range(len(CounterListLive)):
                            if CounterListLive[counter].name == tempVariableName:
                                if CounterListLive[counter].done == 1:
                                    Timer.currentValue += 1
                                    if Timer.currentValue >= Timer.preset:
                                        Timer.done = 1
                                        self.grid[Timer.x][Timer.y].switch = 1
                                elif CounterListLive[counter].done == 0:
                                    Timer.currentValue = 0
                                    Timer.done = 0
                                    self.grid[Timer.x][Timer.y].switch = 0
                    elif tempPrevElement == "Timer":
                        for timer in range(len(TimerListLive)):
                            if TimerListLive[timer].name == tempVariableName:
                                if TimerListLive[timer].done == 1:
                                    Timer.currentValue += 1
                                    if Timer.currentValue >= Timer.preset:
                                        Timer.done = 1
                                        self.grid[Timer.x][Timer.y].switch = 1
                                elif TimerListLive[timer].done == 0:
                                    Timer.currentValue = 0
                                    Timer.done = 0
                                    self.grid[Timer.x][Timer.y].switch = 0

                #    elif tempPrevElement == "Timer":
                #            for timer in range(len(TimerListLive)):
                #                if TimerListLive[timer].name == tempVariableName:
                #                    if TimerListLive[timer].done == 1 and CounterListLive[i].prevInput == 0:
                #                        CounterListLive[i].currentValue += 1
                #                        if CounterListLive[i].currentValue >= CounterListLive[i].preset:
                #                            CounterListLive[i].done = 1
                #                    CounterListLive[i].prevInput = TimerListLive[timer].done
                
                if((tempPrevElement == "contNC" or tempPrevElement == "contNO") and Timer.type == "Retentive_Timer_On"):
                    
                    SwitchValue = 45
                    
                    if(tempPrevElement == "contNC"):
                        SwitchValue = self.grid[tempPrevx][tempPrevy].switch
                    else:
                        SwitchValue = (self.grid[tempPrevx][tempPrevy].switch == 0)
                    
                    if SwitchValue == 1:
                        Timer.currentValue += 1
                        if Timer.currentValue >= Timer.preset:
                            Timer.done = 1
                            self.grid[Timer.x][Timer.y].switch = 1
                            #print "Threaded Retentive Done Bit Triggered \n"
                elif ((tempPrevElement == "Counter" or tempPrevElement == "Timer") and Timer.type == "Retentive_Timer_On"):
                    tempVariableName = self.grid[tempPrevx][tempPrevy].MTorElement+"_"+self.grid[tempPrevx][tempPrevy].variableName
                    if tempPrevElement == "Counter":
                        for counter in range(len(CounterListLive)):
                            if CounterListLive[counter].name == tempVariableName:
                                if CounterListLive[counter].done == 1:
                                    Timer.currentValue += 1
                                    #print "Threaded Retentive Done Bit Triggered \n"
                                    if Timer.currentValue >= Timer.preset:
                                        Timer.done = 1
                                        self.grid[Timer.x][Timer.y].switch = 1
                                   
                
                #later = time.time()
                
                #print "{0:0.8f}".format((later - now)), "\n"
                
                self.TimeDone = 0
                time.sleep(.01)
            
        def TimeKeeping():
            while 1:
                time.sleep(.1)
                self.TimeDone = 1
            
        TimerThread = []

        
        self.TimeDone = 0


        
        TimeKeeper = threading.Thread(target = TimeKeeping)
        TimeKeeper.setDaemon(True)
        TimeKeeper.start()
            


        

        for i in range(len(TimerListLive)):
            TimerThread = threading.Thread(target = TimerTracker,args=(TimerListLive[i],CounterListLive,TimerListLive,))
            TimerThread.setDaemon(True)
            TimerThread.start()


        
        while self.live:
            # if(self.currentHW == "ArduinoNano"):
                # print "Hardware is Nano"
            # elif(self.currentHW == "ArduinoUno"):
                # print "Hardware is Uno"
            # elif(self.currentHW == "ArduinoMega"):
                # print "Hardware is Mega"
            # else:
                # print "No hardware selected"
            

            
            
            
            for i in range(len(CounterListLive)):
                tempPrevx = int(CounterListLive[i].Prevx)
                tempPrevy = int(CounterListLive[i].Prevy)
                tempPrevElement = self.grid[tempPrevx][tempPrevy].MTorElement
                if(tempPrevElement == "contNC" and CounterListLive[i].type == "Counter_Up"):         
                    if self.grid[tempPrevx][tempPrevy].switch == 1 and CounterListLive[i].prevInput == 0:
                        CounterListLive[i].currentValue += 1
                        print "Counter: " , CounterListLive[i].currentValue, "\n"                       
                        if CounterListLive[i].currentValue >= CounterListLive[i].preset:
                            print "Counter done\n"
                            CounterListLive[i].done = 1
                            self.grid[CounterListLive[i].x][CounterListLive[i].y].switch = 1
                    CounterListLive[i].prevInput = self.grid[tempPrevx][tempPrevy].switch
                elif ((tempPrevElement == "Counter" or tempPrevElement == "Timer") and CounterListLive[i].type == "Counter_Up"):
                    tempVariableName = self.grid[tempPrevx][tempPrevy].MTorElement+"_"+self.grid[tempPrevx][tempPrevy].variableName
                    if tempPrevElement == "Counter":
                        for counter in range(len(CounterListLive)):
                            if CounterListLive[counter].name == tempVariableName:
                                if CounterListLive[counter].done == 1:
                                    CounterListLive[i].currentValue += 1
                                    if CounterListLive[i].currentValue >= CounterListLive[i].preset:
                                        CounterListLive[i].done = 1
                                CounterListLive[i].prevInput = CounterListLive[counter].done
                    elif tempPrevElement == "Timer":
                            for timer in range(len(TimerListLive)):
                                if TimerListLive[timer].name == tempVariableName:
                                    if TimerListLive[timer].done == 1 and CounterListLive[i].prevInput == 0:
                                        CounterListLive[i].currentValue += 1
                                        if CounterListLive[i].currentValue >= CounterListLive[i].preset:
                                            CounterListLive[i].done = 1
                                            self.grid[CounterListLive[i].x][CounterListLive[i].y].switch = 1
                                    CounterListLive[i].prevInput = TimerListLive[timer].done
                        
                
                if(self.grid[tempPrevx][tempPrevy].MTorElement == "contNC" and CounterListLive[i].type == "Counter_Down"):  
                    if self.grid[tempPrevx][tempPrevy].switch == 1 and CounterListLive[i].prevInput == 0:
                        CounterListLive[i].preset -= 1
                        if CounterListLive[i].preset <= 0:
                            CounterListLive[i].done = 1
                    CounterListLive[i].prevInput = self.grid[tempPrevx][tempPrevy].switch
                elif ((tempPrevElement == "Counter" or tempPrevElement == "Timer") and CounterListLive[i].type == "Counter_Down"):
                    tempVariableName = self.grid[tempPrevx][tempPrevy].MTorElement+"_"+self.grid[tempPrevx][tempPrevy].variableName
                    
                    if tempPrevElement == "Counter":    ###Probaly will not be used                                                
                        for counter in range(len(CounterListLive)):
                            if CounterListLive[counter].name == tempVariableName:
                                if CounterListLive[counter].done == 1:
                                    CounterListLive[i].preset -= 1
                                    if CounterListLive[i].preset >= CounterListLive[i].preset:
                                        CounterListLive[i].done = 1
                    elif tempPrevElement == "Timer":
                            for timer in range(len(TimerListLive)):
                                if TimerListLive[timer].name == tempVariableName:
                                    if TimerListLive[timer].done == 1 and CounterListLive[i].prevInput == 0:
                                        CounterListLive[i].preset -= 1
                                        if CounterListLive[i].preset <= 0:
                                            CounterListLive[i].done = 1
                                            self.grid[CounterListLive[i].x][CounterListLive[i].y].switch = 1
                                    CounterListLive[i].prevInput = TimerListLive[timer].done                
					
					
                
					
		#####END ADDED BY CHRIS
        









            ###MODIFIED BY MIGUEL GO LIVE TIMERS
            if (WaltSerial.getArduinoState() is not None):
                feedback = WaltSerial.getArduinoState()
            
            if self.currentHW == "ArduinoMega":
                feedback = "{0:08b}".format(ord(feedback[0])) + "{0:08b}".format(ord(feedback[1])) + "{0:08b}".format(ord(feedback[2]))[0:6]\
                + "{0:08b}".format(ord(feedback[3]))  + "{0:08b}".format(ord(feedback[4]))  + "{0:08b}".format(ord(feedback[5]))[0:6]

            if self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
                feedback = "{0:08b}".format(ord(feedback[0]))[0:5] + "{0:08b}".format(ord(feedback[1]))[0:7]

            print feedback
            

            ####check counters current value

            
            
            ###
            
            #########################ADDED/MODIFIED BY MIGUEL OPTIONAL THREADING
            # import threading
            
            # def INS():
            #     if self.currentHW == "ArduinoNano" or self.currentHW == "ArduinoUno":
            #         for i in range(5):
            #             if self.inputs[i+1] != None:
            #                 self.grid[self.inputs[i+1][0]][self.inputs[i+1][1]].switch = int(feedback[i])
                            
            #     if self.currentHW == "ArduinoMega":
            #         for i in range(22):
            #             if self.inputs[i+1] != None:
            #                 self.grid[self.inputs[i+1][0]][self.inputs[i+1][1]].switch = int(feedback[i])
                        
                        
            # def OUTS():
            #     if self.currentHW == "ArduinoNano" or self.currentHW == "ArduinoUno":
            #         for i in range(7):
            #             if self.outputs[i+1] != None:
            #                 self.grid[self.outputs[i+1][0]][self.outputs[i+1][1]].switch = int(feedback[i+5])
                            
            #     if self.currentHW == "ArduinoMega":
            #         for i in range(22):
            #             if self.outputs[i+1] != None:
            #                 self.grid[self.outputs[i+1][0]][self.outputs[i+1][1]].switch = int(feedback[i+22])
                            
            # thdIN = threading.Thread(target = INS)
            # thdOUT = threading.Thread(target = OUTS)
            
            # thdIN.setDaemon(True)
            # thdOUT.setDaemon(True)
            
            # thdIN.start()
            # thdOUT.start()
            
            # thdIN.join()
            # thdOUT.join()
            ####################################################################
            
            ####ADDED BY MICHAEL, MODIFIED BY MIGUEL (IF STATEMENT)
            if self.currentHW == "ArduinoNano" or self.currentHW == "ArduinoUno":
               for i in range(5):
                   if self.inputs[i+1] != None:
                       self.grid[self.inputs[i+1][0]][self.inputs[i+1][1]].switch = int(feedback[i])
               for i in range(7):
                   if self.outputs[i+1] != None:
                       self.grid[self.outputs[i+1][0]][self.outputs[i+1][1]].switch = int(feedback[i+5])
            
            if self.currentHW == "ArduinoMega":
               for i in range(22):
                   if self.inputs[i+1] != None:
                       self.grid[self.inputs[i+1][0]][self.inputs[i+1][1]].switch = int(feedback[i])
               for i in range(22):
                   if self.outputs[i+1] != None:
                       self.grid[self.outputs[i+1][0]][self.outputs[i+1][1]].switch = int(feedback[i+22])
            ####


            #x += 1
        
            ###ADDED BY MIGUEL (FIXING DELAY)
            ManageGrid(self.grid, self.scene,self.Tools,self.items).totalRedraw()
            ###
            
            ManageGrid(self.grid, self.scene,self.Tools,self.items).updateIOelements(self.inputs, self.outputs)
            #time.sleep(.1)
            
            QApplication.processEvents()
            
    def stopFeedback(self):
        self.live = False
        self.ui.liveButton.clicked.disconnect()
        self.ui.liveButton.clicked.connect(self.startFeedback)
        self.ui.liveButton.setText("Go Live") ###ADDED BY MIGUEL
        
        ###ADDED BY MIGUEL ____ CLEAR FEEDBACK AFTER STOP LIFE
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].variableName is not None:
                    self.grid[i][j].switch = 0

        ManageGrid(self.grid, self.scene,self.Tools,self.items).totalRedraw()
        ###

    def showInfo(self):
        """
        ManageGrid(self.grid, self.scene,self.Tools,self.items).reportCellInfo()
        ManageGrid(self.grid, self.scene,self.Tools,self.items).findStartsAndEnds()
        ManageGrid(self.grid, self.scene,self.Tools,self.items).reportCellStartsEnds()
        """

    def unDo(self):
        if len(self.unDoGrid)>1:
            self.reDoGrid.append(copy.deepcopy(self.grid))#save this grid for re-do
            self.grid = copy.deepcopy(self.unDoGrid[-1])#make current grid last one in undo
            self.unDoGrid.pop()#delete last one in undo 
            ManageGrid(self.grid, self.scene,self.Tools,self.items).totalRedraw()
            print("undone")
        else:
            print("no more undoes")

    def reDo(self):
        if len(self.reDoGrid)>0:
            self.unDoGrid.append(copy.deepcopy(self.grid))#save this grid for re-do
            if len(self.unDoGrid) >20:#limit to 20 undos
                self.unDoGrid.pop(0)#pop 0 
            self.grid = copy.deepcopy(self.reDoGrid[-1])
            self.reDoGrid.pop()
            ManageGrid(self.grid, self.scene,self.Tools,self.items).totalRedraw()
            print("redone")
        else:
            print("no more redoes")
 
    def newFile(self):
        #verify popup
        self.clearList(self.ui.tableWidget)
        self.setupDataGrid()#set up rung variables:


    def saveFile(self):
        if self.projectName == None:
            format = "wlm"
            initialPath = os.getcwd() + "/untitled." + format;
            filename = QtGui.QFileDialog.getSaveFileName(self, 'Save As',initialPath)
            self.projectName = filename
        else: 
            filename = self.projectName 
        print "filename", filename
        f = open(filename, 'w')
        gridToSave = copy.deepcopy(self.grid)
        gridToSave.insert(0,self.currentHW)#put current hardware in list at 0
        pickle.dump(gridToSave, f)
        f.close()


    def saveFileAs(self):
        format = "wlm"
        if self.currentFileDir == None:
            initialPath = os.getcwd() + "/untitled." + format;
        else:
            initialPath = self.currentFileDir + "untitled." + format;
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save As',initialPath)
        import ntpath
        justName = ntpath.basename(str(filename))
        self.currentFileDir = filename[0:(len(filename) - len(justName))]
        self.projectName = filename
        print "filename", filename
        f = open(filename, 'w')  
        gridToSave = copy.deepcopy(self.grid)
        gridToSave.insert(0,self.currentHW)#put current hardware in list at 0
        pickle.dump(gridToSave, f)
        f.close()

    def openFile(self):
        filedialog = QtGui.QFileDialog()
        #filedialog.setNameFilter('*.jpg')
        filename = filedialog.getOpenFileName(self, 'Open File', os.path.expanduser("~"),"*.wlm")
        f = open(filename, 'r') 
        import ntpath
        justName = ntpath.basename(str(filename))
        self.currentFileDir = filename[0:(len(filename) - len(justName))]
        self.projectName = filename
        self.grid = pickle.load(f) 
        f.close()
        self.currentHW = self.grid.pop(0)#get current hardware from file
        print self.currentHW
        self.chooseHW(self.currentHW)
        #check width and height, make bounding box
        ManageGrid(self.grid, self.scene,self.Tools,self.items).changeRectangle()

        try: ManageGrid(self.grid, self.scene,self.Tools,self.items).totalRedraw()
        except:
            self.dialog = popupDialogs.wrongVersionDialog()
            self.dialog.exec_()# For Modal dialogs
            self.setupDataGrid()
        else:
            self.reFillList(self.ui.tableWidget)



    def whatsThis(self):
        QtGui.QWhatsThis.enterWhatsThisMode()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove:
            self.eraseMarker()
            cellNum = self.findCell(event)
            self.showMarker(cellNum)
        elif event.type() == QtCore.QEvent.Leave or event.type() == QtCore.QEvent.Wheel:
            self.eraseMarker()
        elif event.type() == QtCore.QEvent.MouseButtonPress:
            self.eraseMarker()
            cellNum = self.findCell(event)
            if cellNum != [None,None,None,None]:
                if event.button() == QtCore.Qt.LeftButton:
                    print "left"
                    self.leftClick(cellNum)
                elif event.button() == QtCore.Qt.RightButton:
                    print "right"
                    self.rightClick(cellNum)  
            #if cellNum == [None,None,None,None]:
        else:
            pass # do other stuff

        return QtGui.QMainWindow.eventFilter(self, source, event)
        #self.ui.graphicsView.viewport().installEventFilter(self)

    def findCell(self,event):
        #Pos = event.globalPos() #doesn't stay when window moves
        #Pos = event.pos()# offset -60,-50 
        #Pos = self.ui.graphicsView.mapToScene(event.globalPos()) #doesn't stay when window moves
        Pos = self.ui.graphicsView.mapToScene(event.pos())
        #things that don't work:

        #Pos = event.screenPos()
        #Pos = self.ui.graphicsView.mapToScene(event.screenPos())
        #Qmousevent has no attribute screenPos

        #Pos = event.scenePos()
        #Pos = self.ui.graphicsView.mapToScene(event.scenePos())
        #Qmousevent has no attribute scenePos

        #x=Pos.x()-172
        x=Pos.x()  -30
        y=Pos.y() +60

        self.ui.label_2.setNum(x)# set x,y display values
        self.ui.label_4.setNum(y)
        if 1 == 1:#disabled if
            #pos = self.ui.graphicsView.mapToScene(event.pos())
            #pos = event.pos()
            #x = pos.x()-30
            #y = pos.y()+60
            cellNum = [None,None,None,None]
            for i in range(len(self.grid)): #cellNum[0]=i    #backwards: row,col 
                for j in range(len(self.grid[i])):
                    if (self.grid[i][j].midPointX-30< x < self.grid[i][j].midPointX+30) and (self.grid[i][j].midPointY-30< y< self.grid[i][j].midPointY+30):
                        cellNum = [i,j,None,None]
                        if y<self.grid[cellNum[0]][cellNum[1]].midPointY: #insert above
                            cellNum[2] = "up"
                        else:#insert below
                            cellNum[2] = "dn"
                        if x<self.grid[cellNum[0]][cellNum[1]].midPointX: #insert left or right
                            cellNum[3] = "rt"
                        else:
                            cellNum[3] = "lt"   
        return cellNum
    def eraseMarker(self):
        itemlist = self.scene.items() #this is a list of ALL items in the scene
        for k in range(len(itemlist)): #compare to items placed last mousemove
            if itemlist[k] == self.items[0]:
                self.scene.removeItem(self.items[0])
            if itemlist[k] == self.items[1]:
                self.scene.removeItem(self.items[1])

    #puts a box around cell or marks or wire, or rung insert spot.  called by mouse move in event filter   
    def showMarker(self, cellNum):  
        i=cellNum[0]
        j=cellNum[1]
        #see if the item was deleted elsewhere, like by scene.clear()

        #self.eraseMarker()

        if cellNum != [None,None,None,None]:
            #Optional: Don't show mouse pointer on graphiscview
            #self.ui.graphicsView.viewport().setCursor(QtCore.Qt.BlankCursor )
            #show cell numbers:   
            if self.currentTool != "addRung":
                self.items[0] = QtGui.QGraphicsTextItem("%d, %d" %(i,j))
                self.items[0].setPos(self.grid[i][j].midPointX+35,self.grid[i][j].midPointY-35)
                self.scene.addItem(self.items[0])

            #go through elementList and see which tool is being used

            if self.currentTool == "addRung":  
                if cellNum[2] =="up" and cellNum[0] == 0:
                    x=self.grid[i][j].midPointX
                    y=self.grid[i][j].midPointY-90
                else:
                    x=self.grid[i][j].midPointX
                    y=self.grid[i][j].midPointY-30
                #y=self.grid[i][j].midPointY-90
                w=200
                h=1
                self.items[1] = QtGui.QGraphicsRectItem(x-100,y,w,h)
                self.items[1].setPen(QtGui.QColor("blue"))
                self.scene.addItem(self.items[1])
                self.items[0] = QtGui.QGraphicsTextItem("<                               >")
                self.items[0].setPos(self.grid[i][j].midPointX-111,y-15)
                self.items[0].setFont(QtGui.QFont("Arial",16))
                self.items[0].setDefaultTextColor(QtGui.QColor("blue")) 
                self.scene.addItem(self.items[0])

            elif self.currentTool == "Widen":  
                x=self.grid[i][j].midPointX
                y=self.grid[i][j].midPointY-90
                w=1
                h=62
                self.items[1] = QtGui.QGraphicsRectItem(x,y,w,h)
                self.items[1].setPen(QtGui.QColor("blue"))
                self.scene.addItem(self.items[1])
            elif self.currentTool == "ORwire": 
                if cellNum[2] =="up":
                     y=self.grid[i][j].midPointY-120
                if cellNum[2] =="dn":
                     y=self.grid[i][j].midPointY-60
                x=self.grid[i][j].midPointX
                #y=self.grid[i][j].midPointY-60
                w=1
                h=60
                self.items[1] = QtGui.QGraphicsRectItem(x,y,w,h)
                self.items[1].setPen(QtGui.QColor("blue"))
                self.scene.addItem(self.items[1])
            elif self.currentTool == "blankOR":  #"blankOR" 5
                pixmap = QtGui.QPixmap(_fromUtf8(":/icons/icons/OR_big.png"))
                self.items[1] = QtGui.QGraphicsPixmapItem(pixmap)
                x=self.grid[i][j].midPointX
                y=self.grid[i][j].midPointY-60
                self.items[1].setPos(x,y)
                self.scene.addItem(self.items[1])    
            else:
                #show box around cell:
                x=self.grid[i][j].midPointX
                y=self.grid[i][j].midPointY-90
                w=58
                h=58
                self.items[1] = QtGui.QGraphicsRectItem(x,y,w,h)
                self.items[1].setPen(QtGui.QColor("blue"))
                self.scene.addItem(self.items[1])

    def rightClick(self, cellNum):
        if cellNum != [None,None,None,None]:
            tool =  self.grid[cellNum[0]][cellNum[1]].MTorElement
            clickSuccssful = False
            #update undo/redo stack here
            del self.reDoGrid[:]#first clear re-do satck
            self.unDoGrid.append(copy.deepcopy(self.grid))#save a copy(list) of this grid for undo
            if len(self.unDoGrid) >30:#limit to 30 undos
                self.unDoGrid.pop(0)#pop 0
            #run popup:    
            tempCellData = self.runPopup(tool,cellNum,1)
            if tempCellData != False:# Yes, new data entered, so update list at right:
                orphan = False
                if self.grid[cellNum[0]][cellNum[1]].variableName != tempCellData.variableName:#check if leaving orphan names
                    orphan = ManageGrid(self.grid, self.scene, self.Tools,self.items).checkOrphanName(cellNum)   
                if orphan == False:
                #update cell:
                ##014##
                    """
                    #check that name is OK
                    if not re.match(r'^[a-zA-Z0-9_]+$', tempCellData.variableName):
                        print "bad name"
                        self.grid[cellNum[0]][cellNum[1]].variableName = "rename_this"
                    else:
                        self.grid[cellNum[0]][cellNum[1]].variableName = tempCellData.variableName
                        print "varname:", tempCellData.variableName
                    """    
                    
                    if self.grid[cellNum[0]][cellNum[1]].ioAssign != None and self.grid[cellNum[0]][cellNum[1]].ioAssign != "Internal":
                        if self.grid[cellNum[0]][cellNum[1]].ioAssign[:3] == "in_":
                            self.inputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[3:])] = None
                        if self.grid[cellNum[0]][cellNum[1]].ioAssign[:4] == "out_":
                            self.outputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[4:])] = None
                    
                    self.grid[cellNum[0]][cellNum[1]].variableName = tempCellData.variableName
                    print "varname:", tempCellData.variableName    
                    self.grid[cellNum[0]][cellNum[1]].comment = tempCellData.comment
                    print "comment:", tempCellData.comment
                    self.grid[cellNum[0]][cellNum[1]].ioAssign = tempCellData.ioAssign
                    print "ioassign:", tempCellData.ioAssign
                    self.grid[cellNum[0]][cellNum[1]].setPoint = tempCellData.setPoint
                    print "setpoint:", tempCellData.setPoint
                    self.grid[cellNum[0]][cellNum[1]].source_A = tempCellData.source_A
                    print "source_A:", tempCellData.source_A
                    self.grid[cellNum[0]][cellNum[1]].source_B = tempCellData.source_B
                    print "source_B:", tempCellData.source_B
                    self.grid[cellNum[0]][cellNum[1]].const_A = tempCellData.const_A
                    print "const_A:", tempCellData.const_A
                    self.grid[cellNum[0]][cellNum[1]].const_B = tempCellData.const_B
                    print "const_B:", tempCellData.const_B
                    self.grid[cellNum[0]][cellNum[1]].functType = tempCellData.functType #not used
                    print "functType:", tempCellData.functType #not used

                    ###ADDED BY MIGUEL
                    self.grid[cellNum[0]][cellNum[1]].doneBit = tempCellData.doneBit
                    print "doneBit:", tempCellData.doneBit

                    self.grid[cellNum[0]][cellNum[1]].type = tempCellData.type
                    print "Type:", tempCellData.type
                    ###
                    
                    if self.grid[cellNum[0]][cellNum[1]].ioAssign != None and self.grid[cellNum[0]][cellNum[1]].ioAssign != "Internal":
                        if self.grid[cellNum[0]][cellNum[1]].ioAssign[:3] == 'in_':
                            self.inputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[3:])] = cellNum
                        if self.grid[cellNum[0]][cellNum[1]].ioAssign[:4] == 'out_':
                            self.outputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[4:])] = cellNum
                    
                    for i in range(22):
                        print "input #", i, " is ", self.inputs[i]
                    for i in range(22):
                        print "output #", i, " is ", self.outputs[i]
                    

                    clickSuccssful = True

            #>>>>>cleanup and redraw:
            if clickSuccssful == False:
                print("nothing done")
                self.unDoGrid.pop()#delete last one in undo 
            ManageGrid(self.grid, self.scene, self.Tools,self.items).totalRedraw()
            self.reFillList(self.ui.tableWidget)

    def leftClick(self, cellNum): #this def is a specific one, automatically connected to mousePressEvent in UI
        if cellNum != [None,None,None,None]:#mouse click was located in cells
            #variable bridge from findng position (todo: change this):
            if cellNum[2] == "up":UpDwn = 0
            if cellNum[2] == "dn":UpDwn = 1
            if cellNum[3] == "rt":RtLft = 1
            if cellNum[3] == "lt":RtLft = 0
            clickSuccssful = False #will be set to true if an action is taken, allows undo to be rolled back of not
            #update undo/redo stack here
            del self.reDoGrid[:]#first clear re-do satck
            self.unDoGrid.append(copy.deepcopy(self.grid))#save a copy(list) of this grid for undo
            if len(self.unDoGrid) >30:#limit to 30 undos
                self.unDoGrid.pop(0)#pop 0

            #go through elementList and see which tool is being used
            numTools = len(self.Tools.toolList)
            toolToPlace = ("0",0)#name and index of tool in toolList
            for i in range(0,numTools):
                if self.Tools.toolList[i].toolName == self.currentTool:
                    toolToPlace = (self.Tools.toolList[i].toolName,i)
                    print("tool #: %d" %(toolToPlace[1]))
            #>>>>>↓↓↓ELEMENT PLACEMENT↓↓↓<<<<<<<<<
            #>>>>place Element on rung:    
            if self.Tools.toolList[toolToPlace[1]].toolType == "Element"\
                        and self.grid[cellNum[0]][cellNum[1]].rungOrOR != "OR": #tool to place is an elememt, (not widen or add rung)
                #>>>>place non-coil Element on rung:  
                if self.Tools.toolList[toolToPlace[1]].position == "any":
                    if self.grid[cellNum[0]][cellNum[1]].MTorElement == "MT"\
                            and cellNum[1] != len(self.grid[cellNum[0]])-1: #not at the far right
                        # cause popup dialog
                        tempCellInfo = self.runPopup(toolToPlace[0],cellNum,0)
                        if tempCellInfo != False:
                            #update list at right
                            #self.addToList(self.ui.tableWidget,tempCellInfo,(cellNum[0],cellNum[1]))            
                            #place element on grid
                            ManageGrid(self.grid, self.scene, self.Tools,self.items)\
                                    .placeElememt(cellNum,tempCellInfo,toolToPlace)
                        clickSuccssful = True
 
                #>>element that should shift to right if "right" (coil, timerreset..)
                elif self.Tools.toolList[toolToPlace[1]].position == "right":
                    cellNum[1] = len(self.grid[0])-1 #right most spot
                    if self.grid[cellNum[0]][cellNum[1]].MTorElement == "MT":
                        # cause popup dialog
                        tempCellInfo = self.runPopup(toolToPlace[0],cellNum,0)
                        if tempCellInfo != False:
                            #update list at right
                            #self.addToList(self.ui.tableWidget,tempCellInfo,(cellNum[0],cellNum[1]))            
                            #place element on grid
                            ManageGrid(self.grid, self.scene, self.Tools,self.items)\
                                    .placeElememt(cellNum,tempCellInfo,toolToPlace)
                            clickSuccssful = True

            #>>>>place Element on OR: 
            if self.Tools.toolList[toolToPlace[1]].toolType == "Element"\
                        and self.grid[cellNum[0]][cellNum[1]].MTorElement == "blankOR":
                if self.Tools.toolList[toolToPlace[1]].position == "any":
                    # cause popup dialog
                    tempCellInfo = self.runPopup(toolToPlace[0],cellNum,0)
                    if tempCellInfo != False:
                        ManageGrid(self.grid, self.scene, self.Tools,self.items)\
                                .placeElememt(cellNum,tempCellInfo,toolToPlace)
                        clickSuccssful = True 

                #>>element only allowed on rt (coil, timerreset..)
                elif self.Tools.toolList[toolToPlace[1]].position == "right":
                    cellNum[1] = len(self.grid[0])-1 #right most spot
                    print ("elemnt to right")
                    if self.grid[cellNum[0]][cellNum[1]].MTorElement == "blankOR":
                        if tempCellInfo != False:
                            ManageGrid(self.grid, self.scene, self.Tools,self.items)\
                                .placeElememt(cellNum,tempCellInfo,toolToPlace)
                            clickSuccssful = True 
             #>>>>↑↑↑ELEMENT PLACEMENT↑↑↑<<<<<         


            #>>>>>addRung:
            if self.Tools.toolList[toolToPlace[1]].toolName == "addRung":
                Ypos = cellNum[0] + UpDwn
                print "upDwn", UpDwn
                ManageGrid(self.grid, self.scene, self.Tools,self.items).insertRung(Ypos)
                clickSuccssful = True
            #>>>>>Widen:  
            elif self.Tools.toolList[toolToPlace[1]].toolName == "Widen":
                #cellNum[1] = cellNum[1] + RtLft
                ManageGrid(self.grid, self.scene, self.Tools,self.items).Widen(cellNum)
                clickSuccssful = True
            #>>>>>addOR:
            elif self.Tools.toolList[toolToPlace[1]].toolName == "blankOR":
                cellNum[0] = cellNum[0] + UpDwn
                #cellNum[1] = cellNum[1] - RtLft #adjust for right or left clickage of cell
                if cellNum[1]< 0:# don't add off left
                    cellNum[1] = 0
                if cellNum[0] <1:
                    cellNum[0]= 1#don't add an OR above
                ManageGrid(self.grid, self.scene, self.Tools,self.items).insertBlankOR(cellNum)
                clickSuccssful = True
                print("blank OR added")
            #>>>>>addORwire:
            elif self.Tools.toolList[toolToPlace[1]].toolName == "ORwire":
                cellNum[0] = cellNum[0] + UpDwn
                #cellNum[1] = cellNum[1] - RtLft #adjust for right or left clickage of cell
                if cellNum[1]< 0:# don't add off left
                    cellNum[1] = 0
                if cellNum[0] <1:
                    cellNum[0]= 1#don't add an OR above
                ManageGrid(self.grid, self.scene, self.Tools,self.items).addWire(cellNum)
                clickSuccssful = True
                print("wire placed")
            #>>>>>Delete:  
            elif self.Tools.toolList[toolToPlace[1]].toolName == "Del":
                #loc = (cellNum[0],cellNum[1])
                if ManageGrid(self.grid, self.scene, self.Tools,self.items).checkOrphanName(cellNum)==False:
                    #delete element on OR branch:
                    if self.grid[cellNum[0]][cellNum[1]].rungOrOR == "OR"\
                            and self.grid[cellNum[0]][cellNum[1]].MTorElement != "MT"\
                            and self.grid[cellNum[0]][cellNum[1]].MTorElement != "blankOR":
                        
                        #Update input and output arrays if deleted element is assigned to one
                        if self.grid[cellNum[0]][cellNum[1]].ioAssign != None and self.grid[cellNum[0]][cellNum[1]].ioAssign != "Internal":
                            if self.grid[cellNum[0]][cellNum[1]].ioAssign[:3] == "in_":
                                self.inputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[3:])] = None
                            if self.grid[cellNum[0]][cellNum[1]].ioAssign[:4] == "out_":
                                self.outputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[4:])] = None
                                
                        ManageGrid(self.grid, self.scene, self.Tools,self.items).Delete(cellNum)
                    #delete of element on Rung or delete the rung:
                    elif self.grid[cellNum[0]][cellNum[1]].rungOrOR == "Rung":
                        
                        #Update input and output arrays if deleted element is assigned to one
                        if self.grid[cellNum[0]][cellNum[1]].ioAssign != None and self.grid[cellNum[0]][cellNum[1]].ioAssign != "Internal":
                            if self.grid[cellNum[0]][cellNum[1]].ioAssign[:3] == "in_":
                                self.inputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[3:])] = None
                            if self.grid[cellNum[0]][cellNum[1]].ioAssign[:4] == "out_":
                                self.outputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[4:])] = None
                        
                        ManageGrid(self.grid, self.scene, self.Tools,self.items).Delete(cellNum)                        
                    clickSuccssful = True    
            #>>>>>Shrink
            elif self.Tools.toolList[toolToPlace[1]].toolName == "Narrow":
                #self.ui.graphicsView.prepareGeometryChange()
                ManageGrid(self.grid, self.scene, self.Tools,self.items).Shrink(cellNum)#then do function to narrow if can
		    
		    ##>>>>>toggle an element
            #if self.grid[cellNum[0]][cellNum[1]].MTorElement != "MT" and self.grid[cellNum[0]][cellNum[1]].MTorElement != "blankOR":
			#	self.grid[cellNum[0]][cellNum[1]].toggleBit()
			#	clickSuccssful = True;
			#	print "Bit currently set to: ", self.grid[cellNum[0]][cellNum[1]].switch
			##>>>>>end of toggle code

            #>>>>>cleanup and redraw:
            if clickSuccssful == False:
                print("nothing done")
                self.unDoGrid.pop()#delete last one in undo 
            ManageGrid(self.grid, self.scene, self.Tools,self.items).totalRedraw()
            self.showInfo()
            self.reFillList(self.ui.tableWidget)

            if self.grid[cellNum[0]][cellNum[1]].ioAssign != None and self.grid[cellNum[0]][cellNum[1]].ioAssign != "Internal":
                if self.grid[cellNum[0]][cellNum[1]].ioAssign[:3] == 'in_':
                    self.inputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[3:])] = cellNum
                if self.grid[cellNum[0]][cellNum[1]].ioAssign[:4] == 'out_':
                    self.outputs[int(self.grid[cellNum[0]][cellNum[1]].ioAssign[4:])] = cellNum
                
            for i in range(22):
                if self.inputs[i] != None:
                    print "input #", i, " is ", self.inputs[i]
            for i in range(22):
                if self.outputs[i] != None:
                    print "output #", i, " is ", self.outputs[i]
			
            print "mtorelement = ", self.grid[cellNum[0]][cellNum[1]].MTorElement


    #will run popup and return tempCellData with all info from popup 
    #send tool being used, cellNum 
    #doesn't do anything with the grid.          
    def runPopup(self, tool, cellNum, leftOrRight):
        popUpOKed = False #becomes true if dialog is OK'ed
        tempCellInfo = cellStruct(None,None,None,None,None,None,None,None,None, False, False, False, False, False, False,None,None,None,None,None, False, None) 
        ##004##
        if tool == "Coil" or tool =="CoilNot":#do dialog for this tool:
            self.dialog = popupDialogs.CoilDialog(self.grid, cellNum,self.currentHW)
            popUpOKed = self.dialog.exec_()# For Modal dialogs
        elif tool == "contNO" or tool =="contNC":#do dialog for this tool:
            self.dialog = popupDialogs.ContDialog(self.grid, cellNum,self.currentHW)
            popUpOKed = self.dialog.exec_()# For Modal dialogs
        elif tool == "Rising" or tool =="Fall":#do dialog for this tool:
            self.dialog = popupDialogs.EdgeDialog(self.grid, cellNum,self.currentHW)
            popUpOKed = self.dialog.exec_()# For Modal dialogs

        ###ADDED/MODIFIED BY CHRIS ____ MODIFIED BY MIGUEL    
        elif tool == "Timer" :#do dialog for this tool:
            switch = 0

            if leftOrRight == 1:
                print "\n\n\n\n\n    PAPAPAPA   "+self.grid[cellNum[0]][cellNum[1]].type
                if self.grid[cellNum[0]][cellNum[1]].type == "Retentive_Timer_On":
                    switch = 1
            
            self.dialog = popupDialogs.TimerDialog(self.grid, cellNum,self.currentHW)

            if switch == 1:
                self.dialog.switchCombo()
                    
            popUpOKed = self.dialog.exec_()# For Modal dialogs
            
        elif tool == "Counter" :#do dialog for this tool:
            switch = 0
            
            if leftOrRight == 1:
                if self.grid[cellNum[0]][cellNum[1]].type == "Counter_Down":
                    switch = 1
        
            self.dialog = popupDialogs.CounterDialog(self.grid, cellNum,self.currentHW)
            
            if switch == 1:
                self.dialog.switchCombo()
            
            popUpOKed = self.dialog.exec_()# For Modal dialogs

        ###
            
        elif tool == "Plus"or tool =="Minus"or tool =="Divide"or tool =="Mult" or tool == "Move" :#do dialog for this tool:
            self.dialog = popupDialogs.MathDialog(self.grid, cellNum,self.currentHW,tool)
            popUpOKed = self.dialog.exec_()# For Modal dialogs
        elif tool == "Equals" or tool =="Greater"or tool =="Lessthan"or tool =="GreaterOrEq"or tool =="LessOrEq":#do dialog for this tool:
            self.dialog = popupDialogs.CompairDialog(self.grid, cellNum,self.currentHW,tool)
            popUpOKed = self.dialog.exec_()# For Modal dialogs
        #elif tool == "Move" :#do dialog for this tool:
        #    self.dialog = popupDialogs.MoveDialog(self.grid, cellNum,self.currentHW)
        #    popUpOKed = self.dialog.exec_()# For Modal dialogs
        elif tool == "PWM" :#do dialog for this tool:
            self.dialog = popupDialogs.PWMDialog(self.grid, cellNum,self.currentHW)
            popUpOKed = self.dialog.exec_()# For Modal dialogs
        elif tool == "ADC" :#do dialog for this tool:
            self.dialog = popupDialogs.ADCDialog(self.grid, cellNum,self.currentHW)
            popUpOKed = self.dialog.exec_()# For Modal dialogs

            #Equals Greater Lessthan GreaterOrEq LessOrEq Plus Minus Divide Mult Move   PWM ADC 
        if popUpOKed == True:        
            ##008##
            # get all info from popup:
            
            ###ADDED BY TEDDY
            if tool == "Timer":
                self.grid[cellNum[0]][cellNum[1]].type = self.dialog.ui.comboBox_3.currentText()
            
            if tool == "Counter":
                self.grid[cellNum[0]][cellNum[1]].type = self.dialog.ui.comboBox_3.currentText()
            ###
            
            try: tempCellInfo.ioAssign = self.dialog.ui.comboBox.currentText()#I/O assign
            except: pass
            try: tempCellInfo.variableName = self.dialog.ui.comboBox_2.currentText()#variable Name
            except: pass
            else:
                #check that name is OK
                if not re.match(r'^[a-zA-Z0-9_]+$', tempCellInfo.variableName):
                    print "bad name"
                    tempCellInfo.variableName = "please_rename"

            try: tempCellInfo.type = self.dialog.ui.comboBox_3.currentText() #type ###ADDED BY TEDDY
            except: pass
            try: tempCellInfo.comment = self.dialog.ui.lineEdit.text()#comment
            except: pass
            try: tempCellInfo.setPoint = self.dialog.ui.doubleSpinBox.value() #setpoint decimal
            except: pass
            try: tempCellInfo.setPoint = self.dialog.ui.spinBox.value() #setpoint integer
            except: pass
            #try: tempCellInfo.ioAssign = self.dialog.ui.comboBox.currentText()
            #except: pass
                #for comparison operators:
            try: tempCellInfo.source_A = self.dialog.ui.comboBox_A.currentText()
            except: pass
            try: tempCellInfo.source_B = self.dialog.ui.comboBox_B.currentText()
            except: pass
            try: tempCellInfo.const_A = self.dialog.ui.spinBox_A.value()
            except: pass
            try: tempCellInfo.const_B = self.dialog.ui.spinBox_B.value()
            except: pass
            
            ###BY MIGUEL DONE BIT
            if "cont" in tool:
                try:
                    tempCellInfo.doneBit = self.dialog.ui.comboBox_3.currentText() #Done Bit
                except: pass
            ###

            tempCellInfo.MTorElement = tool
            return tempCellInfo
        else: 
            return False





class elementStruct():
    def __init__(self, toolName, pixmap , position, toolType):
        self. toolName = toolName
        self. pixmap = pixmap
        self. position = position
        self. toolType = toolType 
        #example:
        #toolName= "contNO"
        #pixmap= QtGui.QPixmap(_fromUtf8(":/icons/icons/contact_NO_big.png"))
        #position= "Any" or "Right"
        #toolType = "Rung" or "Element" or "blankOR"

class elementList():#list of tools.  uses elementStruct
    def __init__(self, elementStruct):
        self.toolList = [elementStruct(0,0,0,0)]
        ##001##
        #list elements here:
        self.toolList.append(elementStruct("contNO",QtGui.QPixmap(_fromUtf8(":/icons/icons/contact_NO.svg")),"any","Element"))
        self.toolList.append(elementStruct("contNC",QtGui.QPixmap(_fromUtf8(":/icons/icons/contact_NC.svg")),"any","Element"))
        self.toolList.append(elementStruct("Coil",QtGui.QPixmap(_fromUtf8(":/icons/icons/Coil.svg")),"right","Element"))
        self.toolList.append(elementStruct("CoilNot",QtGui.QPixmap(_fromUtf8(":/icons/icons/Coil_not.svg")),"right","Element"))
        self.toolList.append(elementStruct("Rising",QtGui.QPixmap(_fromUtf8(":/icons/icons/rising.svg")),"any","Element"))
        self.toolList.append(elementStruct("Fall",QtGui.QPixmap(_fromUtf8(":/icons/icons/falling.svg")),"any","Element"))
        self.toolList.append(elementStruct("Timer",QtGui.QPixmap(_fromUtf8(":/icons/icons/timer.svg")),"any","Element"))
        self.toolList.append(elementStruct("Counter",QtGui.QPixmap(_fromUtf8(":/icons/icons/counter.svg")),"any","Element"))

        self.toolList.append(elementStruct("Equals",QtGui.QPixmap(_fromUtf8(":/icons/icons/equ.svg")),"any","Element"))
        self.toolList.append(elementStruct("Plus",QtGui.QPixmap(_fromUtf8(":/icons/icons/plus.svg")),"right","Element"))
        self.toolList.append(elementStruct("Minus",QtGui.QPixmap(_fromUtf8(":/icons/icons/minus.svg")),"right","Element"))
        self.toolList.append(elementStruct("Move",QtGui.QPixmap(_fromUtf8(":/icons/icons/move.svg")),"right","Element"))
        self.toolList.append(elementStruct("Mult",QtGui.QPixmap(_fromUtf8(":/icons/icons/times.svg")),"right","Element"))
        self.toolList.append(elementStruct("Greater",QtGui.QPixmap(_fromUtf8(":/icons/icons/greater_than.svg")),"any","Element"))
        self.toolList.append(elementStruct("Lessthan",QtGui.QPixmap(_fromUtf8(":/icons/icons/less_than.svg")),"any","Element"))
        self.toolList.append(elementStruct("GreaterOrEq",QtGui.QPixmap(_fromUtf8(":/icons/icons/greater_than_or_eq.svg")),"any","Element"))
        self.toolList.append(elementStruct("LessOrEq",QtGui.QPixmap(_fromUtf8(":/icons/icons/less_than_or_eq.svg")),"any","Element"))
        self.toolList.append(elementStruct("PWM",QtGui.QPixmap(_fromUtf8(":/icons/icons/PWM.svg")),"right","Element"))
        self.toolList.append(elementStruct("ADC",QtGui.QPixmap(_fromUtf8(":/icons/icons/ADC.svg")),"right","Element"))
        self.toolList.append(elementStruct("Divide",QtGui.QPixmap(_fromUtf8(":/icons/icons/divide.svg")),"right","Element"))
        #Equals Plus Minus Move Mult Greater Lessthan GreaterOrEq LessOrEq PWM ADC Divide

        self.toolList.append(elementStruct("addRung",None,None,"Rung"))
        self.toolList.append(elementStruct("Widen",None,None,"Rung"))
        self.toolList.append(elementStruct("blankOR",None,None,"OR"))
        self.toolList.append(elementStruct("Del",None,None,"Rung"))
        self.toolList.append(elementStruct("ORwire",None,None,"Rung"))
        self.toolList.append(elementStruct("Narrow",None,None,"Rung"))
                               

  
if __name__=='__main__':
    app = QApplication(sys.argv)#makes a QtGui thing
    window = mainWindowUI()
    window.show()
    sys.exit(app.exec_())
    
    
    

