from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from gwa_process import *
from gwa_about import Ui_Dialog
from gwa_surprise import Ui_DialogSurprise
import resources

createTablesDB()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1186, 716)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint) # Removes the titlebar

        # Center window
        qtRectangle = MainWindow.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        MainWindow.move(qtRectangle.topLeft())
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        MainWindow.move(qtRectangle.topLeft())

        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/macbook_medal_96px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/macbook_medal_96px.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/macbook_medal_96px.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/macbook_medal_96px.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/macbook_medal_96px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/macbook_medal_96px.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #2A0C31;color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 250, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(70, 110, 163, 42))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.rbtn_1stYear = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.rbtn_1stYear.setStyleSheet("")
        self.rbtn_1stYear.setObjectName("rbtn_1stYear")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rbtn_1stYear)
        self.rbtn_2ndYear = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.rbtn_2ndYear.setObjectName("rbtn_2ndYear")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rbtn_2ndYear)
        self.rbtn_3rdYear = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.rbtn_3rdYear.setObjectName("rbtn_3rdYear")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rbtn_3rdYear)
        self.rbtn_4thYear = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.rbtn_4thYear.setObjectName("rbtn_4thYear")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rbtn_4thYear)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 61, 21))
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(70, 190, 162, 21))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.rbtn_1stSem = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.rbtn_1stSem.setObjectName("rbtn_1stSem")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rbtn_1stSem)
        self.rbtn_2ndSem = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.rbtn_2ndSem.setObjectName("rbtn_2ndSem")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rbtn_2ndSem)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 310, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 240, 160, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_subject = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_subject.setObjectName("input_subject")
        self.verticalLayout.addWidget(self.input_subject)
        self.input_grade = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_grade.setObjectName("input_grade")
        self.verticalLayout.addWidget(self.input_grade)
        self.input_creditUnit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_creditUnit.setObjectName("input_creditUnit")
        self.verticalLayout.addWidget(self.input_creditUnit)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 280, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.label_4.setObjectName("label_4")
        self.btn_proceed = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.proceed())
        self.btn_proceed.setGeometry(QtCore.QRect(30, 350, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.btn_proceed.setFont(font)
        self.btn_proceed.setAutoFillBackground(False)
        self.btn_proceed.setStyleSheet("QPushButton#btn_proceed {color: #fff;background-color: #06B4DB;border-radius: 3px;    }QPushButton#btn_proceed:hover:!pressed {background-color: #05A3C7;}")
        self.btn_proceed.setObjectName("btn_proceed")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 110, 411, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lw_OneFS = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.lw_OneFS.setStyleSheet("border: 1px solid white;")
        self.lw_OneFS.setObjectName("lw_OneFS")
        self.horizontalLayout.addWidget(self.lw_OneFS)
        self.lw_OneSS = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.lw_OneSS.setStyleSheet("border: 1px solid white;")
        self.lw_OneSS.setObjectName("lw_OneSS")
        self.horizontalLayout.addWidget(self.lw_OneSS)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(600, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save(True))
        self.btn_save.setGeometry(QtCore.QRect(30, 560, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton#btn_save {color: #fff;background-color: #0CD498;border-radius: 3px;    }QPushButton#btn_save:hover:!pressed{background-color: #0BC18A;}")
        self.btn_save.setObjectName("btn_save")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(320, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(390, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(470, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(530, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(600, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(680, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.calculate())
        self.btn_calculate.setGeometry(QtCore.QRect(160, 560, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setStyleSheet("QPushButton#btn_calculate {color: #fff;background-color: #FF6F59;border-radius: 3px;    }QPushButton#btn_calculate:hover:!pressed{background-color: #FF6047;}")
        self.btn_calculate.setObjectName("btn_calculate")
        self.container9 = QtWidgets.QLabel(self.centralwidget)
        self.container9.setGeometry(QtCore.QRect(30, 600, 241, 31))
        self.container9.setStyleSheet("QLabel#container9{color: #fff;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container9:hover{border-left: 3px solid #00FF1F;}")
        self.container9.setText("")
        self.container9.setObjectName("container9")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(54, 600, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));")
        self.label_12.setObjectName("label_12")
        self.finalGWA = QtWidgets.QLabel(self.centralwidget)
        self.finalGWA.setGeometry(QtCore.QRect(130, 600, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.finalGWA.setFont(font)
        self.finalGWA.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(230, 21, 193, 255), stop:1 rgba(227, 111, 13, 255));")
        self.finalGWA.setObjectName("finalGWA")
        self.container1 = QtWidgets.QLabel(self.centralwidget)
        self.container1.setGeometry(QtCore.QRect(310, 340, 201, 21))
        self.container1.setStyleSheet("QLabel#container1{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container1:hover{border-left: 3px solid #00FF1F;}")
        self.container1.setText("")
        self.container1.setObjectName("container1")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(320, 340, 37, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: #39163A;")
        self.label_11.setObjectName("label_11")
        self.gwa_OneFS = QtWidgets.QLabel(self.centralwidget)
        self.gwa_OneFS.setGeometry(QtCore.QRect(360, 340, 41, 21))
        self.gwa_OneFS.setStyleSheet("background-color: #39163A;")
        self.gwa_OneFS.setObjectName("gwa_OneFS")
        self.checkPL_OneFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPL_OneFS.setEnabled(False)
        self.checkPL_OneFS.setGeometry(QtCore.QRect(400, 340, 31, 21))
        self.checkPL_OneFS.setStyleSheet("background-color: #39163A;")
        self.checkPL_OneFS.setObjectName("checkPL_OneFS")
        self.checkDL_OneFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDL_OneFS.setEnabled(False)
        self.checkDL_OneFS.setGeometry(QtCore.QRect(440, 340, 31, 21))
        self.checkDL_OneFS.setStyleSheet("background-color: #39163A;")
        self.checkDL_OneFS.setObjectName("checkDL_OneFS")
        self.checkN_OneFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkN_OneFS.setEnabled(False)
        self.checkN_OneFS.setGeometry(QtCore.QRect(480, 340, 31, 21))
        self.checkN_OneFS.setStyleSheet("background-color: #39163A;")
        self.checkN_OneFS.setObjectName("checkN_OneFS")
        self.container2 = QtWidgets.QLabel(self.centralwidget)
        self.container2.setGeometry(QtCore.QRect(520, 340, 201, 21))
        self.container2.setStyleSheet("QLabel#container2{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container2:hover{border-left: 3px solid #00FF1F;}")
        self.container2.setText("")
        self.container2.setObjectName("container2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(530, 340, 37, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: #39163A;")
        self.label_13.setObjectName("label_13")
        self.gwa_OneSS = QtWidgets.QLabel(self.centralwidget)
        self.gwa_OneSS.setGeometry(QtCore.QRect(570, 340, 41, 21))
        self.gwa_OneSS.setStyleSheet("background-color: #39163A;")
        self.gwa_OneSS.setObjectName("gwa_OneSS")
        self.checkPL_OneSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPL_OneSS.setEnabled(False)
        self.checkPL_OneSS.setGeometry(QtCore.QRect(610, 340, 31, 21))
        self.checkPL_OneSS.setStyleSheet("background-color: #39163A;")
        self.checkPL_OneSS.setObjectName("checkPL_OneSS")
        self.checkDL_OneSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDL_OneSS.setEnabled(False)
        self.checkDL_OneSS.setGeometry(QtCore.QRect(650, 340, 31, 21))
        self.checkDL_OneSS.setStyleSheet("background-color: #39163A;")
        self.checkDL_OneSS.setObjectName("checkDL_OneSS")
        self.checkN_OneSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkN_OneSS.setEnabled(False)
        self.checkN_OneSS.setGeometry(QtCore.QRect(690, 340, 31, 21))
        self.checkN_OneSS.setStyleSheet("background-color: #39163A;")
        self.checkN_OneSS.setObjectName("checkN_OneSS")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(750, 110, 411, 191))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lw_TwoFS = QtWidgets.QListWidget(self.horizontalLayoutWidget_5)
        self.lw_TwoFS.setStyleSheet("border: 1px solid white;")
        self.lw_TwoFS.setObjectName("lw_TwoFS")
        self.horizontalLayout_6.addWidget(self.lw_TwoFS)
        self.lw_TwoSS = QtWidgets.QListWidget(self.horizontalLayoutWidget_5)
        self.lw_TwoSS.setStyleSheet("border: 1px solid white;")
        self.lw_TwoSS.setObjectName("lw_TwoSS")
        self.horizontalLayout_6.addWidget(self.lw_TwoSS)
        self.header1 = QtWidgets.QPushButton(self.centralwidget)
        self.header1.setGeometry(QtCore.QRect(450, 50, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.header1.setFont(font)
        self.header1.setToolTip("")
        self.header1.setWhatsThis("")
        self.header1.setStyleSheet("QPushButton#header1 {color: #fff;background-color: #39163A;border-radius: 10px;}")
        self.header1.setObjectName("header1")
        self.header2 = QtWidgets.QPushButton(self.centralwidget)
        self.header2.setGeometry(QtCore.QRect(460, 60, 111, 21))
        self.header2.setToolTip("")
        self.header2.setWhatsThis("")
        self.header2.setStyleSheet("QPushButton#header2 {color: #fff; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255)); border-radius:10px;}")
        self.header2.setText("")
        self.header2.setObjectName("header2")
        self.header3 = QtWidgets.QPushButton(self.centralwidget)
        self.header3.setGeometry(QtCore.QRect(460, 40, 111, 20))
        self.header3.setToolTip("")
        self.header3.setWhatsThis("")
        self.header3.setStyleSheet("QPushButton#header3 {color: #fff; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255)); border-radius:10px;}")
        self.header3.setText("")
        self.header3.setObjectName("header3")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1040, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(830, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.header4 = QtWidgets.QPushButton(self.centralwidget)
        self.header4.setGeometry(QtCore.QRect(890, 50, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.header4.setFont(font)
        self.header4.setToolTip("")
        self.header4.setWhatsThis("")
        self.header4.setStyleSheet("QPushButton#header4 {color: #fff;background-color: #39163A;border-radius: 10px;}")
        self.header4.setObjectName("header4")
        self.header6 = QtWidgets.QPushButton(self.centralwidget)
        self.header6.setGeometry(QtCore.QRect(900, 40, 111, 20))
        self.header6.setToolTip("")
        self.header6.setWhatsThis("")
        self.header6.setStyleSheet("QPushButton#header6 {color: #fff;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));border-radius: 10px;}")
        self.header6.setText("")
        self.header6.setObjectName("header6")
        self.header5 = QtWidgets.QPushButton(self.centralwidget)
        self.header5.setGeometry(QtCore.QRect(900, 60, 111, 20))
        self.header5.setToolTip("")
        self.header5.setWhatsThis("")
        self.header5.setStyleSheet("QPushButton#header5 {color: #fff;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));border-radius: 10px;}")
        self.header5.setText("")
        self.header5.setObjectName("header5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(310, 310, 411, 21))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn1FS_clear = QtWidgets.QPushButton(self.gridLayoutWidget, clicked=lambda: self.clear_all_items(1))
        self.btn1FS_clear.setStyleSheet("QPushButton#btn1FS_clear {color: #fff;background-color: #99110A;border-radius: 3px;    padding: 3px;}QPushButton#btn1FS_clear:hover:!pressed {background-color: #860F09;}")
        self.btn1FS_clear.setObjectName("btn1FS_clear")
        self.gridLayout.addWidget(self.btn1FS_clear, 0, 1, 1, 1)
        self.btn1FS_delete = QtWidgets.QPushButton(self.gridLayoutWidget, clicked=lambda: self.delete_item(1))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn1FS_delete.setFont(font)
        self.btn1FS_delete.setStyleSheet("QPushButton#btn1FS_delete {color: #fff;background-color: #E9190F;border-radius: 3px;padding: 3px;} QPushButton#btn1FS_delete:hover:!pressed {background-color: #D3170D;}")
        self.btn1FS_delete.setObjectName("btn1FS_delete")
        self.gridLayout.addWidget(self.btn1FS_delete, 0, 0, 1, 1)
        self.btn1SS_delete = QtWidgets.QPushButton(self.gridLayoutWidget, clicked=lambda: self.delete_item(2))
        self.btn1SS_delete.setStyleSheet("QPushButton#btn1SS_delete {color: #fff;background-color: #E9190F;border-radius: 3px;padding: 3px;}QPushButton#btn1SS_delete:hover:!pressed {background-color: #D3170D;}")
        self.btn1SS_delete.setObjectName("btn1SS_delete")
        self.gridLayout.addWidget(self.btn1SS_delete, 0, 2, 1, 1)
        self.btn1SS_clear = QtWidgets.QPushButton(self.gridLayoutWidget, clicked=lambda: self.clear_all_items(2))
        self.btn1SS_clear.setStyleSheet("QPushButton#btn1SS_clear {color: #fff;background-color: #99110A;border-radius: 3px;    padding: 3px;}QPushButton#btn1SS_clear:hover:!pressed {background-color: #860F09;}")
        self.btn1SS_clear.setObjectName("btn1SS_clear")
        self.gridLayout.addWidget(self.btn1SS_clear, 0, 3, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(750, 310, 411, 21))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn2SS_delete = QtWidgets.QPushButton(self.gridLayoutWidget_2, clicked=lambda: self.delete_item(4))
        self.btn2SS_delete.setStyleSheet("QPushButton#btn2SS_delete {color: #fff;background-color: #E9190F;border-radius: 3px;padding: 3px;}QPushButton#btn2SS_delete:hover:!pressed {background-color: #D3170D;}")
        self.btn2SS_delete.setObjectName("btn2SS_delete")
        self.gridLayout_2.addWidget(self.btn2SS_delete, 0, 2, 1, 1)
        self.btn2FS_delete = QtWidgets.QPushButton(self.gridLayoutWidget_2, clicked=lambda: self.delete_item(3))
        self.btn2FS_delete.setStyleSheet("QPushButton#btn2FS_delete {color: #fff;background-color: #E9190F;border-radius: 3px;    padding: 3px;}QPushButton#btn2FS_delete:hover:!pressed {background-color: #D3170D;}")
        self.btn2FS_delete.setObjectName("btn2FS_delete")
        self.gridLayout_2.addWidget(self.btn2FS_delete, 0, 0, 1, 1)
        self.btn2FS_clear = QtWidgets.QPushButton(self.gridLayoutWidget_2, clicked=lambda: self.clear_all_items(3))
        self.btn2FS_clear.setStyleSheet("QPushButton#btn2FS_clear {color: #fff;background-color: #99110A;border-radius: 3px;    padding: 3px;}QPushButton#btn2FS_clear:hover:!pressed {background-color: #860F09;}")
        self.btn2FS_clear.setObjectName("btn2FS_clear")
        self.gridLayout_2.addWidget(self.btn2FS_clear, 0, 1, 1, 1)
        self.btn2SS_clear = QtWidgets.QPushButton(self.gridLayoutWidget_2, clicked=lambda: self.clear_all_items(4))
        self.btn2SS_clear.setStyleSheet("QPushButton#btn2SS_clear {color: #fff;background-color: #99110A;border-radius: 3px;padding: 3px;}QPushButton#btn2SS_clear:hover:!pressed {background-color: #860F09;}")
        self.btn2SS_clear.setObjectName("btn2SS_clear")
        self.gridLayout_2.addWidget(self.btn2SS_clear, 0, 3, 1, 1)
        self.checkDL_TwoFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDL_TwoFS.setEnabled(False)
        self.checkDL_TwoFS.setGeometry(QtCore.QRect(880, 340, 31, 21))
        self.checkDL_TwoFS.setStyleSheet("background-color: #39163A;")
        self.checkDL_TwoFS.setObjectName("checkDL_TwoFS")
        self.checkPL_TwoFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPL_TwoFS.setEnabled(False)
        self.checkPL_TwoFS.setGeometry(QtCore.QRect(840, 340, 31, 21))
        self.checkPL_TwoFS.setStyleSheet("background-color: #39163A;")
        self.checkPL_TwoFS.setObjectName("checkPL_TwoFS")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(970, 340, 37, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("background-color: #39163A;")
        self.label_28.setObjectName("label_28")
        self.gwa_TwoFS = QtWidgets.QLabel(self.centralwidget)
        self.gwa_TwoFS.setGeometry(QtCore.QRect(800, 340, 41, 21))
        self.gwa_TwoFS.setStyleSheet("background-color: #39163A;")
        self.gwa_TwoFS.setObjectName("gwa_TwoFS")
        self.gwa_TwoSS = QtWidgets.QLabel(self.centralwidget)
        self.gwa_TwoSS.setGeometry(QtCore.QRect(1010, 340, 41, 21))
        self.gwa_TwoSS.setStyleSheet("background-color: #39163A;")
        self.gwa_TwoSS.setObjectName("gwa_TwoSS")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(760, 340, 37, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("background-color: #39163A;")
        self.label_29.setObjectName("label_29")
        self.checkDL_TwoSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDL_TwoSS.setEnabled(False)
        self.checkDL_TwoSS.setGeometry(QtCore.QRect(1090, 340, 31, 21))
        self.checkDL_TwoSS.setStyleSheet("background-color: #39163A;")
        self.checkDL_TwoSS.setObjectName("checkDL_TwoSS")
        self.checkN_TwoSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkN_TwoSS.setEnabled(False)
        self.checkN_TwoSS.setGeometry(QtCore.QRect(1130, 340, 31, 21))
        self.checkN_TwoSS.setStyleSheet("background-color: #39163A;")
        self.checkN_TwoSS.setObjectName("checkN_TwoSS")
        self.checkPL_TwoSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPL_TwoSS.setEnabled(False)
        self.checkPL_TwoSS.setGeometry(QtCore.QRect(1050, 340, 31, 21))
        self.checkPL_TwoSS.setStyleSheet("background-color: #39163A;")
        self.checkPL_TwoSS.setObjectName("checkPL_TwoSS")
        self.container3 = QtWidgets.QLabel(self.centralwidget)
        self.container3.setGeometry(QtCore.QRect(750, 340, 201, 21))
        self.container3.setStyleSheet("QLabel#container3{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container3:hover{border-left: 3px solid #00FF1F;}")
        self.container3.setText("")
        self.container3.setObjectName("container3")
        self.container4 = QtWidgets.QLabel(self.centralwidget)
        self.container4.setGeometry(QtCore.QRect(960, 340, 201, 21))
        self.container4.setStyleSheet("QLabel#container4{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container4:hover{border-left: 3px solid #00FF1F;}")
        self.container4.setText("")
        self.container4.setObjectName("container4")
        self.checkN_TwoFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkN_TwoFS.setEnabled(False)
        self.checkN_TwoFS.setGeometry(QtCore.QRect(920, 340, 31, 21))
        self.checkN_TwoFS.setStyleSheet("background-color: #39163A;")
        self.checkN_TwoFS.setObjectName("checkN_TwoFS")
        self.checkPL_ThreeFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPL_ThreeFS.setEnabled(False)
        self.checkPL_ThreeFS.setGeometry(QtCore.QRect(400, 670, 31, 21))
        self.checkPL_ThreeFS.setStyleSheet("background-color: #39163A;")
        self.checkPL_ThreeFS.setObjectName("checkPL_ThreeFS")
        self.checkPL_ThreeSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPL_ThreeSS.setEnabled(False)
        self.checkPL_ThreeSS.setGeometry(QtCore.QRect(610, 670, 31, 21))
        self.checkPL_ThreeSS.setStyleSheet("background-color: #39163A;")
        self.checkPL_ThreeSS.setObjectName("checkPL_ThreeSS")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(600, 390, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(760, 670, 37, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: #39163A;")
        self.label_31.setObjectName("label_31")
        self.checkDL_FourFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDL_FourFS.setEnabled(False)
        self.checkDL_FourFS.setGeometry(QtCore.QRect(880, 670, 31, 21))
        self.checkDL_FourFS.setStyleSheet("background-color: #39163A;")
        self.checkDL_FourFS.setObjectName("checkDL_FourFS")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(1040, 390, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.gwa_FourFS = QtWidgets.QLabel(self.centralwidget)
        self.gwa_FourFS.setGeometry(QtCore.QRect(800, 670, 41, 21))
        self.gwa_FourFS.setStyleSheet("background-color: #39163A;")
        self.gwa_FourFS.setObjectName("gwa_FourFS")
        self.checkN_ThreeFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkN_ThreeFS.setEnabled(False)
        self.checkN_ThreeFS.setGeometry(QtCore.QRect(480, 670, 31, 21))
        self.checkN_ThreeFS.setStyleSheet("background-color: #39163A;")
        self.checkN_ThreeFS.setObjectName("checkN_ThreeFS")
        self.header7 = QtWidgets.QPushButton(self.centralwidget)
        self.header7.setGeometry(QtCore.QRect(450, 380, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.header7.setFont(font)
        self.header7.setToolTip("")
        self.header7.setWhatsThis("")
        self.header7.setStyleSheet("QPushButton#header7 {color: #fff;background-color: #39163A;border-radius: 10px;}")
        self.header7.setObjectName("header7")
        self.gwa_FourSS = QtWidgets.QLabel(self.centralwidget)
        self.gwa_FourSS.setGeometry(QtCore.QRect(1010, 670, 41, 21))
        self.gwa_FourSS.setStyleSheet("background-color: #39163A;")
        self.gwa_FourSS.setObjectName("gwa_FourSS")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(750, 640, 411, 21))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn4SS_delete = QtWidgets.QPushButton(self.gridLayoutWidget_3, clicked=lambda: self.delete_item(8))
        self.btn4SS_delete.setStyleSheet("QPushButton#btn4SS_delete {color: #fff;background-color: #E9190F;border-radius: 3px;    padding: 3px;}QPushButton#btn4SS_delete:hover:!pressed {background-color: #D3170D;}")
        self.btn4SS_delete.setObjectName("btn4SS_delete")
        self.gridLayout_3.addWidget(self.btn4SS_delete, 0, 2, 1, 1)
        self.btn4FS_delete = QtWidgets.QPushButton(self.gridLayoutWidget_3, clicked=lambda: self.delete_item(7))
        self.btn4FS_delete.setStyleSheet("QPushButton#btn4FS_delete {color: #fff;background-color: #E9190F;border-radius: 3px;padding: 3px;}QPushButton#btn4FS_delete:hover:!pressed {background-color: #D3170D;}")
        self.btn4FS_delete.setObjectName("btn4FS_delete")
        self.gridLayout_3.addWidget(self.btn4FS_delete, 0, 0, 1, 1)
        self.btn4FS_clear = QtWidgets.QPushButton(self.gridLayoutWidget_3, clicked=lambda: self.clear_all_items(7))
        self.btn4FS_clear.setStyleSheet("QPushButton#btn4FS_clear {color: #fff;background-color: #99110A;border-radius: 3px;padding: 3px;}QPushButton#btn4FS_clear:hover:!pressed {background-color: #860F09;}")
        self.btn4FS_clear.setObjectName("btn4FS_clear")
        self.gridLayout_3.addWidget(self.btn4FS_clear, 0, 1, 1, 1)
        self.btn4SS_clear = QtWidgets.QPushButton(self.gridLayoutWidget_3, clicked=lambda: self.clear_all_items(8))
        self.btn4SS_clear.setStyleSheet("QPushButton#btn4SS_clear {color: #fff;background-color: #99110A;border-radius: 3px;    padding: 3px;}QPushButton#btn4SS_clear:hover:!pressed {background-color: #860F09;}")
        self.btn4SS_clear.setObjectName("btn4SS_clear")
        self.gridLayout_3.addWidget(self.btn4SS_clear, 0, 3, 1, 1)
        self.container8 = QtWidgets.QLabel(self.centralwidget)
        self.container8.setGeometry(QtCore.QRect(960, 670, 201, 21))
        self.container8.setStyleSheet("QLabel#container8{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container8:hover{border-left: 3px solid #00FF1F;}")
        self.container8.setText("")
        self.container8.setObjectName("container8")
        self.container6 = QtWidgets.QLabel(self.centralwidget)
        self.container6.setGeometry(QtCore.QRect(520, 670, 201, 21))
        self.container6.setStyleSheet("QLabel#container6{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container6:hover{border-left: 3px solid #00FF1F;}")
        self.container6.setText("")
        self.container6.setObjectName("container6")
        self.checkN_FourFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkN_FourFS.setEnabled(False)
        self.checkN_FourFS.setGeometry(QtCore.QRect(920, 670, 31, 21))
        self.checkN_FourFS.setStyleSheet("background-color: #39163A;")
        self.checkN_FourFS.setObjectName("checkN_FourFS")
        self.header8 = QtWidgets.QPushButton(self.centralwidget)
        self.header8.setGeometry(QtCore.QRect(460, 390, 111, 21))
        self.header8.setToolTip("")
        self.header8.setWhatsThis("")
        self.header8.setStyleSheet("QPushButton#header8 {color: #fff;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));border-radius: 10px;}")
        self.header8.setText("")
        self.header8.setObjectName("header8")
        self.header9 = QtWidgets.QPushButton(self.centralwidget)
        self.header9.setGeometry(QtCore.QRect(460, 370, 111, 20))
        self.header9.setToolTip("")
        self.header9.setWhatsThis("")
        self.header9.setStyleSheet("QPushButton#header9 {color: #fff;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));border-radius: 10px;}")
        self.header9.setText("")
        self.header9.setObjectName("header9")
        self.header11 = QtWidgets.QPushButton(self.centralwidget)
        self.header11.setGeometry(QtCore.QRect(900, 390, 111, 20))
        self.header11.setToolTip("")
        self.header11.setWhatsThis("")
        self.header11.setStyleSheet("QPushButton#header11 {color: #fff;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));border-radius: 10px;}")
        self.header11.setText("")
        self.header11.setObjectName("header11")
        self.container7 = QtWidgets.QLabel(self.centralwidget)
        self.container7.setGeometry(QtCore.QRect(750, 670, 201, 21))
        self.container7.setStyleSheet("QLabel#container7{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container7:hover{border-left: 3px solid #00FF1F;}")
        self.container7.setText("")
        self.container7.setObjectName("container7")
        self.checkPL_FourSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPL_FourSS.setEnabled(False)
        self.checkPL_FourSS.setGeometry(QtCore.QRect(1050, 670, 31, 21))
        self.checkPL_FourSS.setStyleSheet("background-color: #39163A;")
        self.checkPL_FourSS.setObjectName("checkPL_FourSS")
        self.checkDL_FourSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDL_FourSS.setEnabled(False)
        self.checkDL_FourSS.setGeometry(QtCore.QRect(1090, 670, 31, 21))
        self.checkDL_FourSS.setStyleSheet("background-color: #39163A;")
        self.checkDL_FourSS.setObjectName("checkDL_FourSS")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(310, 440, 411, 191))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lw_ThreeFS = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.lw_ThreeFS.setStyleSheet("border: 1px solid white;")
        self.lw_ThreeFS.setObjectName("lw_ThreeFS")
        self.horizontalLayout_2.addWidget(self.lw_ThreeFS)
        self.lw_ThreeSS = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.lw_ThreeSS.setStyleSheet("border: 1px solid white;")
        self.lw_ThreeSS.setObjectName("lw_ThreeSS")
        self.horizontalLayout_2.addWidget(self.lw_ThreeSS)
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(970, 670, 37, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("background-color: #39163A;")
        self.label_40.setObjectName("label_40")
        self.checkN_FourSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkN_FourSS.setEnabled(False)
        self.checkN_FourSS.setGeometry(QtCore.QRect(1130, 670, 31, 21))
        self.checkN_FourSS.setStyleSheet("background-color: #39163A;")
        self.checkN_FourSS.setObjectName("checkN_FourSS")
        self.header12 = QtWidgets.QPushButton(self.centralwidget)
        self.header12.setGeometry(QtCore.QRect(900, 370, 111, 20))
        self.header12.setToolTip("")
        self.header12.setWhatsThis("")
        self.header12.setStyleSheet("QPushButton#header12 {color: #fff;background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));border-radius: 10px;}")
        self.header12.setText("")
        self.header12.setObjectName("header12")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(310, 640, 411, 21))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn3FS_clear = QtWidgets.QPushButton(self.gridLayoutWidget_4, clicked=lambda: self.clear_all_items(5))
        self.btn3FS_clear.setStyleSheet("QPushButton#btn3FS_clear {color: #fff;background-color: #99110A;border-radius: 3px;    padding: 3px;}QPushButton#btn3FS_clear:hover:!pressed {background-color: #860F09;}")
        self.btn3FS_clear.setObjectName("btn3FS_clear")
        self.gridLayout_4.addWidget(self.btn3FS_clear, 0, 1, 1, 1)
        self.btn3FS_delete = QtWidgets.QPushButton(self.gridLayoutWidget_4, clicked=lambda: self.delete_item(5))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn3FS_delete.setFont(font)
        self.btn3FS_delete.setStyleSheet("QPushButton#btn3FS_delete {color: #fff;background-color: #E9190F;border-radius: 3px;    padding: 3px;}QPushButton#btn3FS_delete:hover:!pressed {background-color: #D3170D;}")
        self.btn3FS_delete.setObjectName("btn3FS_delete")
        self.gridLayout_4.addWidget(self.btn3FS_delete, 0, 0, 1, 1)
        self.btn3SS_delete = QtWidgets.QPushButton(self.gridLayoutWidget_4, clicked=lambda: self.delete_item(6))
        self.btn3SS_delete.setStyleSheet("QPushButton#btn3SS_delete {color: #fff;background-color: #E9190F;border-radius: 3px;    padding: 3px;}QPushButton#btn3SS_delete:hover:!pressed {background-color: #D3170D;}")
        self.btn3SS_delete.setObjectName("btn3SS_delete")
        self.gridLayout_4.addWidget(self.btn3SS_delete, 0, 2, 1, 1)
        self.btn3SS_clear = QtWidgets.QPushButton(self.gridLayoutWidget_4, clicked=lambda: self.clear_all_items(6))
        self.btn3SS_clear.setStyleSheet("QPushButton#btn3SS_clear {color: #fff;background-color: #99110A;border-radius: 3px;    padding: 3px;}QPushButton#btn3SS_clear:hover:!pressed {background-color: #860F09;}")
        self.btn3SS_clear.setObjectName("btn3SS_clear")
        self.gridLayout_4.addWidget(self.btn3SS_clear, 0, 3, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(530, 670, 37, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("background-color: #39163A;")
        self.label_42.setObjectName("label_42")
        self.checkN_ThreeSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkN_ThreeSS.setEnabled(False)
        self.checkN_ThreeSS.setGeometry(QtCore.QRect(690, 670, 31, 21))
        self.checkN_ThreeSS.setStyleSheet("background-color: #39163A;")
        self.checkN_ThreeSS.setObjectName("checkN_ThreeSS")
        self.gwa_ThreeSS = QtWidgets.QLabel(self.centralwidget)
        self.gwa_ThreeSS.setGeometry(QtCore.QRect(570, 670, 41, 21))
        self.gwa_ThreeSS.setStyleSheet("background-color: #39163A;")
        self.gwa_ThreeSS.setObjectName("gwa_ThreeSS")
        self.header10 = QtWidgets.QPushButton(self.centralwidget)
        self.header10.setGeometry(QtCore.QRect(890, 380, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.header10.setFont(font)
        self.header10.setToolTip("")
        self.header10.setWhatsThis("")
        self.header10.setStyleSheet("QPushButton#header10 {color: #fff;background-color: #39163A;border-radius: 10px;}")
        self.header10.setObjectName("header10")
        self.checkDL_ThreeFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDL_ThreeFS.setEnabled(False)
        self.checkDL_ThreeFS.setGeometry(QtCore.QRect(440, 670, 31, 21))
        self.checkDL_ThreeFS.setStyleSheet("background-color: #39163A;")
        self.checkDL_ThreeFS.setObjectName("checkDL_ThreeFS")
        self.gwa_ThreeFS = QtWidgets.QLabel(self.centralwidget)
        self.gwa_ThreeFS.setGeometry(QtCore.QRect(360, 670, 41, 21))
        self.gwa_ThreeFS.setStyleSheet("background-color: #39163A;")
        self.gwa_ThreeFS.setObjectName("gwa_ThreeFS")
        self.checkPL_FourFS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkPL_FourFS.setEnabled(False)
        self.checkPL_FourFS.setGeometry(QtCore.QRect(840, 670, 31, 21))
        self.checkPL_FourFS.setStyleSheet("background-color: #39163A;")
        self.checkPL_FourFS.setObjectName("checkPL_FourFS")
        self.container5 = QtWidgets.QLabel(self.centralwidget)
        self.container5.setGeometry(QtCore.QRect(310, 670, 201, 21))
        self.container5.setStyleSheet("QLabel#container5{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}QLabel#container5:hover{border-left: 3px solid #00FF1F;}")
        self.container5.setText("")
        self.container5.setObjectName("container5")
        self.checkDL_ThreeSS = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDL_ThreeSS.setEnabled(False)
        self.checkDL_ThreeSS.setGeometry(QtCore.QRect(650, 670, 31, 21))
        self.checkDL_ThreeSS.setStyleSheet("background-color: #39163A;")
        self.checkDL_ThreeSS.setObjectName("checkDL_ThreeSS")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(830, 390, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(390, 390, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(320, 670, 37, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("background-color: #39163A;")
        self.label_48.setObjectName("label_48")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(750, 440, 411, 191))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lw_FourFS = QtWidgets.QListWidget(self.horizontalLayoutWidget_6)
        self.lw_FourFS.setStyleSheet("border: 1px solid white;")
        self.lw_FourFS.setObjectName("lw_FourFS")
        self.horizontalLayout_7.addWidget(self.lw_FourFS)
        self.lw_FourSS = QtWidgets.QListWidget(self.horizontalLayoutWidget_6)
        self.lw_FourSS.setStyleSheet("border: 1px solid white;")
        self.lw_FourSS.setObjectName("lw_FourSS")
        self.horizontalLayout_7.addWidget(self.lw_FourSS)
        self.gb_award = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_award.setGeometry(QtCore.QRect(30, 640, 241, 51))
        self.gb_award.setStyleSheet("QGroupBox#gb_award{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}")
        self.gb_award.setObjectName("gb_award")
        self.checkSCL = QtWidgets.QCheckBox(self.gb_award)
        self.checkSCL.setEnabled(False)
        self.checkSCL.setGeometry(QtCore.QRect(20, 20, 47, 17))
        self.checkSCL.setStyleSheet("background-color: #39163A;")
        self.checkSCL.setObjectName("checkSCL")
        self.checkMCL = QtWidgets.QCheckBox(self.gb_award)
        self.checkMCL.setEnabled(False)
        self.checkMCL.setGeometry(QtCore.QRect(80, 20, 51, 17))
        self.checkMCL.setStyleSheet("background-color: #39163A;")
        self.checkMCL.setObjectName("checkMCL")
        self.checkCL = QtWidgets.QCheckBox(self.gb_award)
        self.checkCL.setEnabled(False)
        self.checkCL.setGeometry(QtCore.QRect(140, 20, 47, 17))
        self.checkCL.setStyleSheet("background-color: #39163A;")
        self.checkCL.setObjectName("checkCL")
        self.checkN = QtWidgets.QCheckBox(self.gb_award)
        self.checkN.setEnabled(False)
        self.checkN.setGeometry(QtCore.QRect(190, 20, 41, 17))
        self.checkN.setStyleSheet("background-color: #39163A;")
        self.checkN.setObjectName("checkN")
        self.gb_legend = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_legend.setGeometry(QtCore.QRect(30, 390, 241, 161))
        self.gb_legend.setStyleSheet("QGroupBox#gb_legend{color: #fff;background-color: #39163A;border-radius-top-right: 3px;border-radius-bottom-right: 3px;border-left: 3px solid white;}")
        self.gb_legend.setObjectName("gb_legend")
        self.label_50 = QtWidgets.QLabel(self.gb_legend)
        self.label_50.setGeometry(QtCore.QRect(30, 30, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("background-color: #39163A;")
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.gb_legend)
        self.label_51.setGeometry(QtCore.QRect(30, 50, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("background-color: #39163A;")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.gb_legend)
        self.label_52.setGeometry(QtCore.QRect(30, 70, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("background-color: #39163A;")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.gb_legend)
        self.label_53.setGeometry(QtCore.QRect(30, 90, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("background-color: #39163A;")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.gb_legend)
        self.label_54.setGeometry(QtCore.QRect(30, 110, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("background-color: #39163A;")
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.gb_legend)
        self.label_55.setGeometry(QtCore.QRect(30, 130, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("background-color: #39163A;")
        self.label_55.setObjectName("label_55")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(1140, 10, 31, 31))
        self.btn_close.setStyleSheet("image: url(:/icons/icons/close_window_96px.png);background-color: #2A0C31;")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.minimize = QtWidgets.QPushButton(self.centralwidget)
        self.minimize.setGeometry(QtCore.QRect(1110, 10, 31, 31))
        self.minimize.setStyleSheet("image: url(:/icons/icons/minimize_window_96px.png);background-color: #2A0C31;")
        self.minimize.setText("")
        self.minimize.setObjectName("minimize")
        self.about = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.btn_about())
        self.about.setGeometry(QtCore.QRect(1080, 10, 31, 31))
        self.about.setStyleSheet("image: url(:/icons/icons/info_squared_96px.png);background-color: #2A0C31;")
        self.about.setText("")
        self.about.setObjectName("about")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1120, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(970, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(760, 90, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(910, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(830, 90, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(1040, 90, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(680, 420, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(530, 420, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(320, 420, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(470, 420, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(390, 420, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("")
        self.label_43.setObjectName("label_43")
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setGeometry(QtCore.QRect(600, 420, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(1120, 420, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(970, 420, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(760, 420, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(910, 420, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(830, 420, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("")
        self.label_44.setObjectName("label_44")
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(1040, 420, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 16, 731))
        self.label.setStyleSheet("background-color: white;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1180, 0, 31, 711))
        self.label_8.setStyleSheet("background-color: white;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        self.label_56.setGeometry(QtCore.QRect(-20, 710, 1211, 21))
        self.label_56.setStyleSheet("background-color: white;")
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.centralwidget)
        self.label_57.setGeometry(QtCore.QRect(0, -15, 1211, 21))
        self.label_57.setStyleSheet("background-color: white;")
        self.label_57.setText("")
        self.label_57.setObjectName("label_57")
        self.surprise = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.btn_surprise())
        self.surprise.setGeometry(QtCore.QRect(20, 30, 51, 31))
        self.surprise.setStyleSheet("image: url(:/icons/icons/macbook_medal_96px.png);background-color: #2A0C31;")
        self.surprise.setText("")
        self.surprise.setObjectName("surprise")
        self.label_58 = QtWidgets.QLabel(self.centralwidget)
        self.label_58.setGeometry(QtCore.QRect(90, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));")
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.centralwidget)
        self.label_59.setGeometry(QtCore.QRect(60, 30, 16, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(227, 111, 13, 255), stop:1 rgba(230, 21, 193, 255));")
        self.label_59.setText("")
        self.label_59.setObjectName("label_59")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(279, 40, 21, 651))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_60 = QtWidgets.QLabel(self.centralwidget)
        self.label_60.setGeometry(QtCore.QRect(220, 0, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("image: url(:/icons/icons/cat-1.png);")
        self.label_60.setText("")
        self.label_60.setObjectName("label_60")
        self.line.raise_()
        self.label_60.raise_()
        self.label_59.raise_()
        self.container8.raise_()
        self.header3.raise_()
        self.header2.raise_()
        self.label_5.raise_()
        self.formLayoutWidget_2.raise_()
        self.label_2.raise_()
        self.formLayoutWidget_3.raise_()
        self.label_7.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.btn_proceed.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.btn_save.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.btn_calculate.raise_()
        self.container9.raise_()
        self.label_12.raise_()
        self.finalGWA.raise_()
        self.container1.raise_()
        self.label_11.raise_()
        self.gwa_OneFS.raise_()
        self.checkPL_OneFS.raise_()
        self.checkDL_OneFS.raise_()
        self.checkN_OneFS.raise_()
        self.container2.raise_()
        self.label_13.raise_()
        self.gwa_OneSS.raise_()
        self.checkPL_OneSS.raise_()
        self.checkDL_OneSS.raise_()
        self.checkN_OneSS.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.header1.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.header6.raise_()
        self.header5.raise_()
        self.header4.raise_()
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.container3.raise_()
        self.container4.raise_()
        self.label_29.raise_()
        self.checkPL_TwoFS.raise_()
        self.checkN_TwoFS.raise_()
        self.checkDL_TwoFS.raise_()
        self.gwa_TwoFS.raise_()
        self.checkN_TwoSS.raise_()
        self.checkPL_TwoSS.raise_()
        self.checkDL_TwoSS.raise_()
        self.label_28.raise_()
        self.gwa_TwoSS.raise_()
        self.label_30.raise_()
        self.label_32.raise_()
        self.gwa_FourSS.raise_()
        self.gridLayoutWidget_3.raise_()
        self.container6.raise_()
        self.header8.raise_()
        self.header9.raise_()
        self.header11.raise_()
        self.container7.raise_()
        self.checkPL_FourSS.raise_()
        self.checkDL_FourSS.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.label_40.raise_()
        self.checkN_FourSS.raise_()
        self.header12.raise_()
        self.gridLayoutWidget_4.raise_()
        self.label_42.raise_()
        self.checkN_ThreeSS.raise_()
        self.gwa_ThreeSS.raise_()
        self.header10.raise_()
        self.container5.raise_()
        self.label_45.raise_()
        self.label_47.raise_()
        self.horizontalLayoutWidget_6.raise_()
        self.header7.raise_()
        self.gwa_ThreeFS.raise_()
        self.label_48.raise_()
        self.checkPL_ThreeFS.raise_()
        self.checkDL_ThreeFS.raise_()
        self.checkN_ThreeFS.raise_()
        self.checkPL_ThreeSS.raise_()
        self.checkDL_ThreeSS.raise_()
        self.gwa_FourFS.raise_()
        self.checkPL_FourFS.raise_()
        self.checkDL_FourFS.raise_()
        self.label_31.raise_()
        self.checkN_FourFS.raise_()
        self.gb_award.raise_()
        self.gb_legend.raise_()
        self.btn_close.raise_()
        self.minimize.raise_()
        self.about.raise_()
        self.label_20.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_33.raise_()
        self.label_35.raise_()
        self.label_39.raise_()
        self.label_41.raise_()
        self.label_43.raise_()
        self.label_49.raise_()
        self.label_34.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_44.raise_()
        self.label_46.raise_()
        self.label.raise_()
        self.label_8.raise_()
        self.label_56.raise_()
        self.label_57.raise_()
        self.surprise.raise_()
        self.label_58.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.grab_all()

    def grab_all(self):
        data = getDataFromDB()
        # print(data)
        # 1
        ffirstSem = data[0]
        fsecondSem = data[1]
        # Loop tru records and present in the screen
        for record in ffirstSem:
            item = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2])
            self.lw_OneFS.addItem(item)
        for record in fsecondSem:
            item = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2])
            self.lw_OneSS.addItem(item)

        # 2
        sfirstSem = data[2]
        ssecondSem = data[3]
        for record in sfirstSem:
            item = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2])
            self.lw_TwoFS.addItem(item)
        for record in ssecondSem:
            item = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2])
            self.lw_TwoSS.addItem(item)

        # 3
        tfirstSem = data[4]
        tsecondSem = data[5]
        for record in tfirstSem:
            item = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2])
            self.lw_ThreeFS.addItem(item)
        for record in tsecondSem:
            item = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2])
            self.lw_ThreeSS.addItem(item)

        # 4
        frfirstSem = data[6]
        frsecondSem = data[7]
        for record in frfirstSem:
            item = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2])
            self.lw_FourFS.addItem(item)
        for record in frsecondSem:
            item = str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2])
            self.lw_FourSS.addItem(item)

    def proceed(self):
        if (self.rbtn_1stYear.isChecked() or self.rbtn_2ndYear.isChecked() or self.rbtn_3rdYear.isChecked() or self.rbtn_4thYear.isChecked()) and (self.rbtn_1stSem.isChecked() or self.rbtn_2ndSem.isChecked()) and (self.input_subject.text() and self.input_grade.text() and self.input_creditUnit.text()):
            if self.rbtn_1stYear.isChecked():
                year = 1
            if self.rbtn_2ndYear.isChecked():
                year = 2
            if self.rbtn_3rdYear.isChecked():
                year = 3
            if self.rbtn_4thYear.isChecked():
                year = 4

            if self.rbtn_1stSem.isChecked():
                sem = 1
            if self.rbtn_2ndSem.isChecked():
                sem = 2
            
            subject = self.input_subject.text()
            grade = float(self.input_grade.text())
            creditUnit = float(self.input_creditUnit.text())

            # 1 - Show to the screen
            if year==1 and sem==1:
                self.lw_OneFS.addItem(subject + "\t" + str(creditUnit) + "\t" + str(grade))
            elif year==1 and sem==2:
                self.lw_OneSS.addItem(subject + "\t" + str(creditUnit) + "\t" + str(grade))

            # 2 - Show to the screen
            if year==2 and sem==1:
                self.lw_TwoFS.addItem(subject + "\t" + str(creditUnit) + "\t" + str(grade))
            elif year==2 and sem==2:
                self.lw_TwoSS.addItem(subject + "\t" + str(creditUnit) + "\t" + str(grade))

            # 3 - Show to the screen
            if year==3 and sem==1:
                self.lw_ThreeFS.addItem(subject + "\t" + str(creditUnit) + "\t" + str(grade))
            elif year==3 and sem==2:
                self.lw_ThreeSS.addItem(subject + "\t" + str(creditUnit) + "\t" + str(grade))

            # 4 - Show to the screen
            if year==4 and sem==1:
                self.lw_FourFS.addItem(subject + "\t" + str(creditUnit) + "\t" + str(grade))
            elif year==4 and sem==2:
                self.lw_FourSS.addItem(subject + "\t" + str(creditUnit) + "\t" + str(grade))

            self.input_subject.clear()
            self.input_grade.clear()
            self.input_creditUnit.clear()

            self.save(False)
        else:
            # Pop up warning
            msg = QMessageBox()
            msg.setWindowTitle("Input Error")
            msg.setWindowIcon(QtGui.QIcon(":/icons/icons/macbook_medal_96px.png"))
            msg.setText("Baka! The information you have entered is not enough.")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

    def save(self, proceed):
        executeCommand("DELETE FROM first_firstSem;")
        executeCommand("DELETE FROM first_secondSem;")

        executeCommand("DELETE FROM second_firstSem;")
        executeCommand("DELETE FROM second_secondSem;")

        executeCommand("DELETE FROM third_firstSem;")
        executeCommand("DELETE FROM third_secondSem;")

        executeCommand("DELETE FROM fourth_firstSem;")
        executeCommand("DELETE FROM fourth_secondSem;")

        # 1 - 1
        items11 = [] # Blank list to hold the value
        for index in range(self.lw_OneFS.count()):
            items11.append(self.lw_OneFS.item(index))
        insertDB(items11, "first_firstSem")

        # 1 - 2
        items12 = [] # Blank list to hold the value
        for index in range(self.lw_OneSS.count()):
            items12.append(self.lw_OneSS.item(index))
        insertDB(items12, "first_secondSem")

        # 2 - 1
        items21 = [] # Blank list to hold the value
        for index in range(self.lw_TwoFS.count()):
            items21.append(self.lw_TwoFS.item(index))
        insertDB(items21, "second_firstSem")

        # 2 - 2
        items22 = [] # Blank list to hold the value
        for index in range(self.lw_TwoSS.count()):
            items22.append(self.lw_TwoSS.item(index))
        insertDB(items22, "second_secondSem")

        # 3 - 1
        items31 = [] # Blank list to hold the value
        for index in range(self.lw_ThreeFS.count()):
            items31.append(self.lw_ThreeFS.item(index))
        insertDB(items31, "third_firstSem")

        # 3 - 2
        items32 = [] # Blank list to hold the value
        for index in range(self.lw_ThreeSS.count()):
            items32.append(self.lw_ThreeSS.item(index))
        insertDB(items32, "third_secondSem")

        # 4 - 1
        items41 = [] # Blank list to hold the value
        for index in range(self.lw_FourFS.count()):
            items41.append(self.lw_FourFS.item(index))
        insertDB(items41, "fourth_firstSem")

        # 4 - 2
        items42 = [] # Blank list to hold the value
        for index in range(self.lw_FourSS.count()):
            items42.append(self.lw_FourSS.item(index))
        insertDB(items42, "fourth_secondSem")

        # Pop up confirmation
        if proceed:
            msg = QMessageBox()
            msg.setWindowTitle("Database Info")
            msg.setWindowIcon(QtGui.QIcon(":/icons/icons/macbook_medal_96px.png"))
            msg.setText("Successfully saved to the database!")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
        else:
            pass

    def delete_item(self, choice):
        if choice == 1:
            clicked = self.lw_OneFS.currentRow() # Grabs selected row in the list
            self.lw_OneFS.takeItem(clicked) # Deletes selected row
        elif choice == 2:
            clicked = self.lw_OneSS.currentRow() # Grabs selected row in the list
            self.lw_OneSS.takeItem(clicked) # Deletes selected row
        elif choice == 3:
            clicked = self.lw_TwoFS.currentRow() 
            self.lw_TwoFS.takeItem(clicked) 
        elif choice == 4:
            clicked = self.lw_TwoSS.currentRow() 
            self.lw_TwoSS.takeItem(clicked) 
        elif choice == 5:
            clicked = self.lw_ThreeFS.currentRow() 
            self.lw_ThreeFS.takeItem(clicked) 
        elif choice == 6:
            clicked = self.lw_ThreeSS.currentRow() 
            self.lw_ThreeSS.takeItem(clicked) 
        elif choice == 7:
            clicked = self.lw_FourFS.currentRow() 
            self.lw_FourFS.takeItem(clicked) 
        elif choice == 8:
            clicked = self.lw_FourSS.currentRow() 
            self.lw_FourSS.takeItem(clicked)

    def clear_all_items(self, choice):
        if choice == 1:
            self.lw_OneFS.clear()
        elif choice == 2:
            self.lw_OneSS.clear()
        elif choice == 3:
            self.lw_TwoFS.clear()
        elif choice == 4:
            self.lw_TwoSS.clear()
        elif choice == 5:
            self.lw_ThreeFS.clear()
        elif choice == 6:
            self.lw_ThreeSS.clear()
        elif choice == 7:
            self.lw_FourFS.clear()
        elif choice == 8:
            self.lw_FourSS.clear()

    def calculate(self):
        ffs = self.lw_OneFS.count()
        fss = self.lw_OneSS.count()
        sfs = self.lw_TwoFS.count()
        sss = self.lw_TwoSS.count()
        tfs = self.lw_ThreeFS.count()
        tss = self.lw_ThreeSS.count()
        frfs = self.lw_FourFS.count()
        frss = self.lw_FourSS.count()
        if ffs != 0:
            ffirstSem_gradeCredit = executeFetch("SELECT SUM(credit_score*grade) FROM first_firstSem")
            ffirstSem_creditSum = executeFetch("SELECT SUM(credit_score) FROM first_firstSem")

            # 1st - First Sem GWA
            for item in ffirstSem_gradeCredit:
                ffsresult1 = str(item[0])

            for item in ffirstSem_creditSum:
                ffsresult2 = str(item[0])

            ffsresult = float(ffsresult1)/float(ffsresult2)
            self.award(1, 1, ffsresult) # PL, CL, N
            self.gwa_OneFS.setText("{:.3f}".format(ffsresult)) # Presenting to GWA Label
        if fss != 0:
            fsecondSem_gradeCredit = executeFetch("SELECT SUM(credit_score*grade) FROM first_secondSem")
            fsecondSem_creditSum = executeFetch("SELECT SUM(credit_score) FROM first_secondSem")
            
            # 1st - Second Sem GWA
            for item in fsecondSem_gradeCredit:
                fssresult1 = str(item[0])

            for item in fsecondSem_creditSum:
                fssresult2 = str(item[0])

            fssresult = float(fssresult1)/float(fssresult2)
            self.award(1, 2, fssresult) # PL, CL, N
            self.gwa_OneSS.setText("{:.3f}".format(fssresult)) # Presenting to GWA Label
        if sfs != 0:
            sfirstSem_gradeCredit = executeFetch("SELECT SUM(credit_score*grade) FROM second_firstSem")
            sfirstSem_creditSum = executeFetch("SELECT SUM(credit_score) FROM second_firstSem")

            # 2nd - First Sem GWA
            for item in sfirstSem_gradeCredit:
                sfsresult1 = str(item[0])

            for item in sfirstSem_creditSum:
                sfsresult2 = str(item[0])

            sfsresult = float(sfsresult1)/float(sfsresult2)
            self.award(2, 1, sfsresult) # PL, CL, N
            self.gwa_TwoFS.setText("{:.3f}".format(sfsresult)) # Presenting to GWA Label
        if sss != 0:
            ssecondSem_gradeCredit = executeFetch("SELECT SUM(credit_score*grade) FROM second_secondSem")
            ssecondSem_creditSum = executeFetch("SELECT SUM(credit_score) FROM second_secondSem")
            
            # 2nd - Second Sem GWA
            for item in ssecondSem_gradeCredit:
                sssresult1 = str(item[0])

            for item in ssecondSem_creditSum:
                sssresult2 = str(item[0])

            sssresult = float(sssresult1)/float(sssresult2)
            self.award(2, 2, sssresult) # PL, CL, N
            self.gwa_TwoSS.setText("{:.3f}".format(sssresult)) # Presenting to GWA Label
        if tfs != 0:
            tfirstSem_gradeCredit = executeFetch("SELECT SUM(credit_score*grade) FROM third_firstSem")
            tfirstSem_creditSum = executeFetch("SELECT SUM(credit_score) FROM third_firstSem")

            # 3rd - First Sem GWA
            for item in tfirstSem_gradeCredit:
                tfsresult1 = str(item[0])

            for item in tfirstSem_creditSum:
                tfsresult2 = str(item[0])

            tfsresult = float(tfsresult1)/float(tfsresult2)
            self.award(3, 1, tfsresult) # PL, CL, N
            self.gwa_ThreeFS.setText("{:.3f}".format(tfsresult)) # Presenting to GWA Label
        if tss != 0:
            tsecondSem_gradeCredit = executeFetch("SELECT SUM(credit_score*grade) FROM third_secondSem")
            tsecondSem_creditSum = executeFetch("SELECT SUM(credit_score) FROM third_secondSem")
            
            # 3rd - Second Sem GWA
            for item in tsecondSem_gradeCredit:
                tssresult1 = str(item[0])

            for item in tsecondSem_creditSum:
                tssresult2 = str(item[0])

            tssresult = float(tssresult1)/float(tssresult2)
            self.award(3, 2, tssresult) # PL, CL, N
            self.gwa_ThreeSS.setText("{:.3f}".format(tssresult)) # Presenting to GWA Label
        if frfs != 0:
            frfirstSem_gradeCredit = executeFetch("SELECT SUM(credit_score*grade) FROM fourth_firstSem")
            frfirstSem_creditSum = executeFetch("SELECT SUM(credit_score) FROM fourth_firstSem")

            # 4th - First Sem GWA
            for item in frfirstSem_gradeCredit:
                frfsresult1 = str(item[0])

            for item in frfirstSem_creditSum:
                frfsresult2 = str(item[0])

            frfsresult = float(frfsresult1)/float(frfsresult2)
            self.award(4, 1, frfsresult) # PL, CL, N
            self.gwa_FourFS.setText("{:.3f}".format(frfsresult)) # Presenting to GWA Label
        if frss != 0:
            frsecondSem_gradeCredit = executeFetch("SELECT SUM(credit_score*grade) FROM fourth_secondSem")
            frsecondSem_creditSum = executeFetch("SELECT SUM(credit_score) FROM fourth_secondSem")
            
            # 3rd - Second Sem GWA
            for item in frsecondSem_gradeCredit:
                frssresult1 = str(item[0])

            for item in frsecondSem_creditSum:
                frssresult2 = str(item[0])

            frssresult = float(frssresult1)/float(frssresult2)
            self.award(4, 2, frssresult) # PL, CL, N
            self.gwa_FourSS.setText("{:.3f}".format(frssresult)) # Presenting to GWA Label

        self.calculateFinal()

    def award(self, year, sem, gwa):
        if year == 1 and sem == 1:
            if gwa >= 1.0 and gwa <= 1.45:
                self.checkPL_OneFS.setChecked(True)
                self.checkPL_OneFS.setEnabled(True)
            elif gwa >= 1.46 and gwa <= 1.75:
                self.checkDL_OneFS.setChecked(True)
                self.checkDL_OneFS.setEnabled(True)
            else:
                self.checkN_OneFS.setChecked(True)
                self.checkN_OneFS.setEnabled(True)

        if year == 1 and sem == 2:
            if gwa >= 1.0 and gwa <= 1.45:
                self.checkPL_OneSS.setChecked(True)
                self.checkPL_OneSS.setEnabled(True)
            elif gwa >= 1.46 and gwa <= 1.75:
                self.checkDL_OneSS.setChecked(True)
                self.checkDL_OneSS.setEnabled(True)
            else:
                self.checkN_OneSS.setChecked(True)
                self.checkN_OneSS.setEnabled(True)

        if year == 2 and sem == 1:
            if gwa >= 1.0 and gwa <= 1.45:
                self.checkPL_TwoFS.setChecked(True)
                self.checkPL_TwoFS.setEnabled(True)
            elif gwa >= 1.46 and gwa <= 1.75:
                self.checkDL_TwoFS.setChecked(True)
                self.checkDL_TwoFS.setEnabled(True)
            else:
                self.checkN_TwoFS.setChecked(True)
                self.checkN_TwoFS.setEnabled(True)

        if year == 2 and sem == 2:
            if gwa >= 1.0 and gwa <= 1.45:
                self.checkPL_TwoSS.setChecked(True)
                self.checkPL_TwoSS.setEnabled(True)
            elif gwa >= 1.46 and gwa <= 1.75:
                self.checkDL_TwoSS.setChecked(True)
                self.checkDL_TwoSS.setEnabled(True)
            else:
                self.checkN_TwoSS.setChecked(True)
                self.checkN_TwoSS.setEnabled(True)

        if year == 3 and sem == 1:
            if gwa >= 1.0 and gwa <= 1.45:
                self.checkPL_ThreeFS.setChecked(True)
                self.checkPL_ThreeFS.setEnabled(True)
            elif gwa >= 1.46 and gwa <= 1.75:
                self.checkDL_ThreeFS.setChecked(True)
                self.checkDL_ThreeFS.setEnabled(True)
            else:
                self.checkN_ThreeFS.setChecked(True)
                self.checkN_ThreeFS.setEnabled(True)

        if year == 3 and sem == 2:
            if gwa >= 1.0 and gwa <= 1.45:
                self.checkPL_ThreeSS.setChecked(True)
                self.checkPL_ThreeSS.setEnabled(True)
            elif gwa >= 1.46 and gwa <= 1.75:
                self.checkDL_ThreeSS.setChecked(True)
                self.checkDL_ThreeSS.setEnabled(True)
            else:
                self.checkN_ThreeSS.setChecked(True)
                self.checkN_ThreeSS.setEnabled(True)

        if year == 4 and sem == 1:
            if gwa >= 1.0 and gwa <= 1.45:
                self.checkPL_FourFS.setChecked(True)
                self.checkPL_FourFS.setEnabled(True)
            elif gwa >= 1.46 and gwa <= 1.75:
                self.checkDL_FourFS.setChecked(True)
                self.checkDL_FourFS.setEnabled(True)
            else:
                self.checkN_FourFS.setChecked(True)
                self.checkN_FourFS.setEnabled(True)

        if year == 4 and sem == 2:
            if gwa >= 1.0 and gwa <= 1.45:
                self.checkPL_FourSS.setChecked(True)
                self.checkPL_FourSS.setEnabled(True)
            elif gwa >= 1.46 and gwa <= 1.75:
                self.checkDL_FourSS.setChecked(True)
                self.checkDL_FourSS.setEnabled(True)
            else:
                self.checkN_FourSS.setChecked(True)
                self.checkN_FourSS.setEnabled(True)

    def calculateFinal(self):
        # 1 - 1
        ffsCredit = executeFetch("SELECT SUM(credit_score) FROM first_firstSem")
        for record in ffsCredit:
            if record[0] is None:
                ffsCredit = 0
            else:
                ffsCredit = record[0]
        
        # 1 - 2
        fssCredit = executeFetch("SELECT SUM(credit_score) FROM first_secondSem")
        for record in fssCredit:
            if record[0] is None:
                fssCredit = 0
            else:
                fssCredit = record[0]

        # 2 - 1
        sfsCredit = executeFetch("SELECT SUM(credit_score) FROM second_firstSem")
        for record in sfsCredit:
            if record[0] is None:
                sfsCredit = 0
            else:
                sfsCredit = record[0]
        
        # 2 - 2
        sssCredit = executeFetch("SELECT SUM(credit_score) FROM second_secondSem")
        for record in sssCredit:
            if record[0] is None:
                sssCredit = 0
            else:
                sssCredit = record[0]

        # 3 - 1
        tfsCredit = executeFetch("SELECT SUM(credit_score) FROM third_firstSem")
        for record in tfsCredit:
            if record[0] is None:
                tfsCredit = 0
            else:
                tfsCredit = record[0]
        
        # 3 - 2
        tssCredit = executeFetch("SELECT SUM(credit_score) FROM third_secondSem")
        for record in tssCredit:
            if record[0] is None:
                tssCredit = 0
            else:
                tssCredit = record[0]

        # 4 - 1
        frfsCredit = executeFetch("SELECT SUM(credit_score) FROM fourth_firstSem")
        for record in frfsCredit:
            if record[0] is None:
                frfsCredit = 0
            else:
                frfsCredit = record[0]
        
        # 4 - 2
        frssCredit = executeFetch("SELECT SUM(credit_score) FROM fourth_secondSem")
        for record in frssCredit:
            if record[0] is None:
                frssCredit = 0
            else:
                frssCredit = record[0]

        # Calculate Final Credit Unit
        totalCredit = ffsCredit + fssCredit + sfsCredit + sssCredit + tfsCredit + tssCredit + frfsCredit + frssCredit

        # 1 - 1
        ffsGrade = executeFetch("SELECT SUM(grade*credit_score) FROM first_firstSem")
        for record in ffsGrade:
            if record[0] is None:
                ffsGrade = 0
            else:
                ffsGrade = record[0]

        # 1 - 2
        fssGrade = executeFetch("SELECT SUM(grade*credit_score) FROM first_secondSem")
        for record in fssGrade:
            if record[0] is None:
                fssGrade = 0
            else:
                fssGrade = record[0]

        # 2 - 1
        sfsGrade = executeFetch("SELECT SUM(grade*credit_score) FROM second_firstSem")
        for record in sfsGrade:
            if record[0] is None:
                sfsGrade = 0
            else:
                sfsGrade = record[0]

        # 2 - 2
        sssGrade = executeFetch("SELECT SUM(grade*credit_score) FROM second_secondSem")
        for record in sssGrade:
            if record[0] is None:
                sssGrade = 0
            else:
                sssGrade = record[0]

        # 3 - 1
        tfsGrade = executeFetch("SELECT SUM(grade*credit_score) FROM third_firstSem")
        for record in tfsGrade:
            if record[0] is None:
                tfsGrade = 0
            else:
                tfsGrade = record[0]

        # 3 - 2
        tssGrade = executeFetch("SELECT SUM(grade*credit_score) FROM third_secondSem")
        for record in tssGrade:
            if record[0] is None:
                tssGrade = 0
            else:
                tssGrade = record[0]

        # 4 - 1
        frfsGrade = executeFetch("SELECT SUM(grade*credit_score) FROM fourth_firstSem")
        for record in frfsGrade:
            if record[0] is None:
                frfsGrade = 0
            else:
                frfsGrade = record[0]

        # 4 - 2
        frssGrade = executeFetch("SELECT SUM(grade*credit_score) FROM fourth_secondSem")
        for record in frssGrade:
            if record[0] is None:
                frssGrade = 0
            else:
                frssGrade = record[0]
        
        # Calculate Final Weighted Grade
        totalGrade = ffsGrade + fssGrade + sfsGrade + sssGrade + tfsGrade + tssGrade + frfsGrade + frssCredit

        # Calculate Final GWA
        finalGWA = totalGrade/totalCredit

        self.final(finalGWA)

    def final(self, result):
        if result >= 1.0 and result <= 1.25:
            self.checkSCL.setEnabled(True)
            self.checkSCL.setChecked(True)
        elif result >= 1.26 and result <= 1.45:
            self.checkMCL.setEnabled(True)
            self.checkMCL.setChecked(True)
        elif result >= 1.46 and result <= 1.75:
            self.checkCL.setEnabled(True)
            self.checkCL.setChecked(True)
        else:
            self.checkN.setEnabled(True)
            self.checkN.setChecked(True)

        self.finalGWA.setText("{:.4f}".format(result))

    def btn_about(self):
        self.new = QtWidgets.QWidget() 
        self.about_dialog = Ui_Dialog()
        self.about_dialog.setupUi(self.new)
        self.new.show() 

    def btn_surprise(self):
        self.new = QtWidgets.QWidget()
        self.surprise = Ui_DialogSurprise()
        self.surprise.setupUi(self.new)
        self.new.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GWA Compute - Royland Pepaño - BSIT"))
        self.label_5.setText(_translate("MainWindow", " Subject:"))
        self.rbtn_1stYear.setText(_translate("MainWindow", "First Year"))
        self.rbtn_2ndYear.setText(_translate("MainWindow", "Second Year"))
        self.rbtn_3rdYear.setText(_translate("MainWindow", "Third Year"))
        self.rbtn_4thYear.setText(_translate("MainWindow", "Fourth Year"))
        self.label_2.setText(_translate("MainWindow", "What year?"))
        self.rbtn_1stSem.setText(_translate("MainWindow", "First Sem  "))
        self.rbtn_2ndSem.setText(_translate("MainWindow", "Second Sem"))
        self.label_7.setText(_translate("MainWindow", "Credit Unit:"))
        self.label_6.setText(_translate("MainWindow", "Grade:"))
        self.label_3.setText(_translate("MainWindow", "What semester?"))
        self.label_4.setText(_translate("MainWindow", "Fill up the required text fields:"))
        self.btn_proceed.setText(_translate("MainWindow", "NEXT"))
        self.label_10.setText(_translate("MainWindow", "Second Sem"))
        self.label_9.setText(_translate("MainWindow", "First Sem"))
        self.btn_save.setText(_translate("MainWindow", "SAVE TO DATABASE"))
        self.label_14.setText(_translate("MainWindow", "Subject"))
        self.label_15.setText(_translate("MainWindow", "Unit"))
        self.label_16.setText(_translate("MainWindow", "Grade"))
        self.label_17.setText(_translate("MainWindow", "Subject"))
        self.label_18.setText(_translate("MainWindow", "Unit"))
        self.label_19.setText(_translate("MainWindow", "Grade"))
        self.btn_calculate.setText(_translate("MainWindow", "CALCULATE"))
        self.label_12.setText(_translate("MainWindow", "FINAL GWA:"))
        self.finalGWA.setText(_translate("MainWindow", "1.0000"))
        self.label_11.setText(_translate("MainWindow", "GWA:"))
        self.gwa_OneFS.setText(_translate("MainWindow", "1.0000"))
        self.checkPL_OneFS.setText(_translate("MainWindow", "PL"))
        self.checkDL_OneFS.setText(_translate("MainWindow", "DL"))
        self.checkN_OneFS.setText(_translate("MainWindow", "N"))
        self.label_13.setText(_translate("MainWindow", "GWA:"))
        self.gwa_OneSS.setText(_translate("MainWindow", "1.0000"))
        self.checkPL_OneSS.setText(_translate("MainWindow", "PL"))
        self.checkDL_OneSS.setText(_translate("MainWindow", "DL"))
        self.checkN_OneSS.setText(_translate("MainWindow", "N"))
        self.header1.setText(_translate("MainWindow", "FIRST YEAR"))
        self.label_21.setText(_translate("MainWindow", "Second Sem"))
        self.label_22.setText(_translate("MainWindow", "First Sem"))
        self.header4.setText(_translate("MainWindow", "SECOND YEAR"))
        self.btn1FS_clear.setText(_translate("MainWindow", "CLEAR ALL"))
        self.btn1FS_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn1SS_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn1SS_clear.setText(_translate("MainWindow", "CLEAR ALL"))
        self.btn2SS_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn2FS_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn2FS_clear.setText(_translate("MainWindow", "CLEAR ALL"))
        self.btn2SS_clear.setText(_translate("MainWindow", "CLEAR ALL"))
        self.checkDL_TwoFS.setText(_translate("MainWindow", "DL"))
        self.checkPL_TwoFS.setText(_translate("MainWindow", "PL"))
        self.label_28.setText(_translate("MainWindow", "GWA:"))
        self.gwa_TwoFS.setText(_translate("MainWindow", "1.0000"))
        self.gwa_TwoSS.setText(_translate("MainWindow", "1.0000"))
        self.label_29.setText(_translate("MainWindow", "GWA:"))
        self.checkDL_TwoSS.setText(_translate("MainWindow", "DL"))
        self.checkN_TwoSS.setText(_translate("MainWindow", "N"))
        self.checkPL_TwoSS.setText(_translate("MainWindow", "PL"))
        self.checkN_TwoFS.setText(_translate("MainWindow", "N"))
        self.checkPL_ThreeFS.setText(_translate("MainWindow", "PL"))
        self.checkPL_ThreeSS.setText(_translate("MainWindow", "PL"))
        self.label_30.setText(_translate("MainWindow", "Second Sem"))
        self.label_31.setText(_translate("MainWindow", "GWA:"))
        self.checkDL_FourFS.setText(_translate("MainWindow", "DL"))
        self.label_32.setText(_translate("MainWindow", "Second Sem"))
        self.gwa_FourFS.setText(_translate("MainWindow", "1.0000"))
        self.checkN_ThreeFS.setText(_translate("MainWindow", "N"))
        self.header7.setText(_translate("MainWindow", "THIRD YEAR"))
        self.gwa_FourSS.setText(_translate("MainWindow", "1.0000"))
        self.btn4SS_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn4FS_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn4FS_clear.setText(_translate("MainWindow", "CLEAR ALL"))
        self.btn4SS_clear.setText(_translate("MainWindow", "CLEAR ALL"))
        self.checkN_FourFS.setText(_translate("MainWindow", "N"))
        self.checkPL_FourSS.setText(_translate("MainWindow", "PL"))
        self.checkDL_FourSS.setText(_translate("MainWindow", "DL"))
        self.label_40.setText(_translate("MainWindow", "GWA:"))
        self.checkN_FourSS.setText(_translate("MainWindow", "N"))
        self.btn3FS_clear.setText(_translate("MainWindow", "CLEAR ALL"))
        self.btn3FS_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn3SS_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn3SS_clear.setText(_translate("MainWindow", "CLEAR ALL"))
        self.label_42.setText(_translate("MainWindow", "GWA:"))
        self.checkN_ThreeSS.setText(_translate("MainWindow", "N"))
        self.gwa_ThreeSS.setText(_translate("MainWindow", "1.0000"))
        self.header10.setText(_translate("MainWindow", "FOURTH YEAR"))
        self.checkDL_ThreeFS.setText(_translate("MainWindow", "DL"))
        self.gwa_ThreeFS.setText(_translate("MainWindow", "1.0000"))
        self.checkPL_FourFS.setText(_translate("MainWindow", "PL"))
        self.checkDL_ThreeSS.setText(_translate("MainWindow", "DL"))
        self.label_45.setText(_translate("MainWindow", "First Sem"))
        self.label_47.setText(_translate("MainWindow", "First Sem"))
        self.label_48.setText(_translate("MainWindow", "GWA:"))
        self.gb_award.setTitle(_translate("MainWindow", "Award"))
        self.checkSCL.setText(_translate("MainWindow", "SCL"))
        self.checkMCL.setText(_translate("MainWindow", "MCL"))
        self.checkCL.setText(_translate("MainWindow", "CL"))
        self.checkN.setText(_translate("MainWindow", "N"))
        self.gb_legend.setTitle(_translate("MainWindow", "LEGEND"))
        self.label_50.setText(_translate("MainWindow", "SCL - Summa Cum Laude"))
        self.label_51.setText(_translate("MainWindow", "MCL - Magna Cum Laude"))
        self.label_52.setText(_translate("MainWindow", "CL - Cum Laude"))
        self.label_53.setText(_translate("MainWindow", "PL - President\'s Lister"))
        self.label_54.setText(_translate("MainWindow", "DL - Dean\'s Lister"))
        self.label_55.setText(_translate("MainWindow", "N - None"))
        self.label_20.setText(_translate("MainWindow", "Grade"))
        self.label_23.setText(_translate("MainWindow", "Subject"))
        self.label_24.setText(_translate("MainWindow", "Subject"))
        self.label_25.setText(_translate("MainWindow", "Grade"))
        self.label_26.setText(_translate("MainWindow", "Unit"))
        self.label_27.setText(_translate("MainWindow", "Unit"))
        self.label_33.setText(_translate("MainWindow", "Grade"))
        self.label_35.setText(_translate("MainWindow", "Subject"))
        self.label_39.setText(_translate("MainWindow", "Subject"))
        self.label_41.setText(_translate("MainWindow", "Grade"))
        self.label_43.setText(_translate("MainWindow", "Unit"))
        self.label_49.setText(_translate("MainWindow", "Unit"))
        self.label_34.setText(_translate("MainWindow", "Grade"))
        self.label_36.setText(_translate("MainWindow", "Subject"))
        self.label_37.setText(_translate("MainWindow", "Subject"))
        self.label_38.setText(_translate("MainWindow", "Grade"))
        self.label_44.setText(_translate("MainWindow", "Unit"))
        self.label_46.setText(_translate("MainWindow", "Unit"))
        self.label_58.setText(_translate("MainWindow", "GWA Compute"))

# Main Window
class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.minimize.clicked.connect(self.showMinimized)
        self.btn_close.clicked.connect(self.close)
            
    def mousePressEvent(self, event):                                 
        self.dragPos = event.globalPos()
            
    def mouseMoveEvent(self, event):                                  
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())