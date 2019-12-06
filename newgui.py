from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import QTimer , QTime

class Ui_Eye(object):

    time_ ="00:00" 
    txt_b1 = 0
    txt_b2 = 0

    def start_press(self):
        if self.button1.text() == "Start":
            self.button1.setText("Pause")

        else:
            self.button1.setText("Start")     
       
    

    def reset_Press(self):
        self.textBrowser1.setText("Reset Initiated!")

    def showTime():
        time = QTime.currentTime()
        text = time.toString('mm:ss')
        if time.second() %2 == 0:
            text = text[:2] + " " + text[:3]
        
        self.lcdNumber.display(text)

    def valuechange_1(self):
        self.txt_b1 = str(self.horizontalSlider.value())
        self.textBrowser1.setText(self.txt_b1)
        
        
        
    def valuechange_2(self):
        self.txt_b2 = str(self.horizontalSlider_2.value())
        self.textBrowser2.setText(self.txt_b2)


    def setupUi(self, Eye):
        # Basic Design of the programme 

        # timer = QTimer(self)
        # timer.timeout.connect(self.showTime)
        # timer.start(1000)
        #self.showTime()
        Eye.setObjectName("Eye")
        Eye.resize(547, 370)
        self.centralwidget = QtWidgets.QWidget(Eye)
        self.centralwidget.setObjectName("centralwidget")

#-----------------------------------------------
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-4, -8, 561, 381))
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setPixmap(QtGui.QPixmap("bg.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        #--------
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 310, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        #---------
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #---------
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("sans seref")
        font.setPointSize(11)
        #font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #---------
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 30, 240, 51))
        font = QtGui.QFont()
        #font.setFamily("Forte")
        font.setFamily("sans seref")
        font.setPointSize(22)
        font.setWeight(75)
        self.label1.setFont(font)
        #self.label1.setAutoFillBackground(True)
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label1")
        self.label1.setStyleSheet('color: white')
        #----------
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 190, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        #font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        

#------------------------------------------------
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(30, 110, 121, 41))
        self.button1.setMouseTracking(True)
        self.button1.setFlat(False)
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.start_press)
        #-----
        self.button1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button1_2.setGeometry(QtCore.QRect(180, 110, 121, 41))
        self.button1_2.setMouseTracking(True)
        self.button1_2.setFlat(False)
        self.button1_2.clicked.connect(self.reset_Press)
        self.button1_2.setObjectName("button1_2")
#----------------------------------------------
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(390, 290, 141, 41))
        self.radioButton.setObjectName("radioButton")
        #self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.radioButton.setChecked(True)
        self.radioButton.setStyleSheet("QRadioButton {  color:white ; }")
        #----------
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(390, 250, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("QRadioButton {  color:white ; }")
        #----------
       #self.radioButton_3{color: rgb(255, 255, 255);}
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget )
        self.radioButton_3.setGeometry(QtCore.QRect(390, 200, 111, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setStyleSheet("QRadioButton {  color:white ; }")
#-------------------------------------------------------
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 20, 231, 71))
        self.lcdNumber.setObjectName("lcdNumber")
       # self.lcdNumber.display("10:00")
#---------------------------------------------------------  
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 230, 161, 31))
        self.horizontalSlider.setMaximum(60)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setObjectName("horizontalSlider")
        #self.horizontalSlider.setTickPosition()
        self.horizontalSlider.valueChanged.connect(self.valuechange_1)
        
        #--------------
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(20, 300, 161, 31))
        self.horizontalSlider_2.setMaximum(120)
        self.horizontalSlider_2.setSingleStep(5)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(self.valuechange_2)
#-------------------------------------------------------------
        self.textBrowser1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser1.setGeometry(QtCore.QRect(190, 230, 51, 31))
        self.textBrowser1.setObjectName("textBrowser1")
        #----------------
        self.textBrowser2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser2.setGeometry(QtCore.QRect(190, 300, 51, 31))
        self.textBrowser2.setObjectName("textBrowser2")
#------------------------------------------------------------------    
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-3, 149, 551, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

#--------------------------------------------------------------------   
        self.label_2.setStyleSheet('color: white')
        self.label_3.setStyleSheet('color: white')
        self.label_4.setStyleSheet('color: white')
        self.label.setStyleSheet('color: white')
#--------------------------------------------------------------------
#-----------------------EXPERIMENTAL AREA ---------------------------
        self.textBrowser1.setText(str(self.horizontalSlider.value()))






#--------------------------------------------------------------------
        #Imp code parts
        #self.radioButton_1.toggled.connect(lambda:self.btnstate(self.b1))
        
        Eye.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(Eye)
        # self.statusbar.setObjectName("statusbar")
        # Eye.setStatusBar(self.statusbar)

        self.retranslateUi(Eye)
        QtCore.QMetaObject.connectSlotsByName(Eye)

    def retranslateUi(self, Eye):
        _translate = QtCore.QCoreApplication.translate
        Eye.setWindowTitle(_translate("Eye", "Eye Protector"))
        self.button1.setText(_translate("Eye", "Start"))
        self.radioButton.setText(_translate("Eye", "Custom Timer","color: white"))
        self.label1.setText(_translate("Eye", "Time Remaining"))
        self.label.setText(_translate("Eye", "Working Timer"))
        self.label_2.setText(_translate("Eye", "Rest Timer"))
        self.button1_2.setText(_translate("Eye", "Reset"))
        self.radioButton_2.setText(_translate("Eye", "Timer"))
        self.radioButton_3.setText(_translate("Eye", "Eye Protection"))
        self.label_3.setText(_translate("Eye", "Min"))
        self.label_4.setText(_translate("Eye", "Sec"))
#import abc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Eye = QtWidgets.QMainWindow()
    ui = Ui_Eye()
    ui.setupUi(Eye)
    Eye.show()
    sys.exit(app.exec_())
