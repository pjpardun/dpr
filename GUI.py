# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python projects\DPR\Source\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 701)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("/* QGroupBox -------------------------------------------------------------- */\n"
"QGroupBox {\n"
"    font-weight: bold;\n"
"    border: 2px solid #DCDCDC;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    margin-top: 16px;\n"
"    background-color: #F7FBFD\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 3px;\n"
"    padding-left: 3px;\n"
"    padding-right: 5px;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 16px;\n"
"}\n"
"\n"
"QGroupBox#groupBox_7 {\n"
"    background-color: #B2D5EE;\n"
"    border: 2px solid #52636E;\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* QTabBar -------------------------------------------------------------- */\n"
"QTabBar::tab:top {\n"
"    background-color: #E1E1E1;\n"
"    color: #000000;\n"
"    margin-left: 2px;\n"
"    min-width: 5px;\n"
"    border-bottom: 3px solid #E1E1E1;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border: 1px solid #DCDCDC;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    background-color: #FFFFFF;\n"
"    color: #000000;\n"
"    border-bottom: 3px solid #FFFFFF;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected:hover {\n"
"    background-color: #E5F1FB;\n"
"    border: 1px solid #DCDCDC;\n"
"}\n"
"\n"
"/* QTabWiget -------------------------------------------------------------- */\n"
"QTabWidget::pane {\n"
"    border: 2px solid #7e99b4;\n"
"    border-radius: 4px;\n"
"    margin: 0px;\n"
"    background-color: #E6EFF4;\n"
"}\n"
"\n"
"/* QPushButton -------------------------------------------------------------- */\n"
"QPushButton {\n"
"    background-color: #E1E1E1;\n"
"    border: 1px solid #ADADAD;\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #0078D7;\n"
"    background-color: #E5F1FB;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CCE4F7;\n"
"    border: 1px solid #00559B;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #E1E1E1;\n"
"    border: 1px solid #ADADAD;\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* QDateEdit-------------------------------------------------------------- */\n"
"QDateEdit {\n"
"    background-color: white;\n"
"    selection-background-color: #1464A0;\n"
"    border-style: solid;\n"
"    border: 1px solid #7A7A7A;\n"
"    border-radius: 4px;\n"
"    padding-top: 2px;     /* This fix  #103, #111*/\n"
"    padding-bottom: 2px;  /* This fix  #103, #111*/\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    min-width: 10px;\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border-style: solid;\n"
"    border: 1px solid #000000;\n"
"}\n"
"\n"
"\n"
"QDateEdit::drop-down {\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(down_arrow.png);\n"
"}\n"
"\n"
"QDateEdit::down-arrow:on,\n"
"QDateEdit::down-arrow:hover,\n"
"QDateEdit::down-arrow:focus {\n"
"    image: url(down_arrow.png);\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 4px;\n"
"    border-style: solid;\n"
"    border: 1px solid #DCDCDC;\n"
"    selection-background-color: #0078D7;\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView:hover {\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 4px;\n"
"    border-style: solid;\n"
"    border: 1px solid #0078D7;\n"
"    selection-background-color: #0078D7;\n"
"}\n"
"\n"
"QDateEdit QCalendarWidget {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    border-style: solid; /* without this border reverts for disabled */\n"
"    border: 1px solid #7A7A7A;\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 1px solid #000000;\n"
"    background-color: #FFFFFF;\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* QCombobox -------------------------------------------------------------- */\n"
"QComboBox {\n"
"    background-color: #E1E1E1;\n"
"    border: 1px solid #ADADAD;\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox:hover,\n"
"QComboBox:checked:hover{\n"
"    border: 1px solid #0078D7;\n"
"    background-color: #E5F1FB;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    border: 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down_arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on,\n"
"QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus {\n"
"    image: url(down_arrow.png);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #E5F1FB;\n"
"    border-radius: 4px;\n"
"    border: 1px solid #F7FFF7;\n"
"    selection-color: #000000;\n"
"    selection-background-color: #CCE4F7;\n"
"}\n"
"\n"
"/* QProgressBar ----------------------------------------------------------- */\n"
"QProgressBar {\n"
"    background-color: #E6E6E6;\n"
"    border: 1px solid #BCBCBC;\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #EFC649;\n"
"    /*default background-color: #06B025;*/\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* QTableView -------------------------------------------------------------- */\n"
"QListView,\n"
"QTreeView,\n"
"QTableView,\n"
"QColumnView {\n"
"    background-color: #FFFFFF;\n"
"    border: 1.5px solid #DCDCDC;\n"
"    color: #000000;\n"
"    gridline-color: #F0F0F0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListView:hover,\n"
"QTreeView::hover,\n"
"QTableView::hover,\n"
"QColumnView::hover {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #0078D7;\n"
"}\n"
"\n"
"\n"
"QHeaderView {\n"
"    background-color: #E1E1E1;\n"
"    border: 0px transparent #E1E1E1;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #E1E1E1;\n"
"    color: #000000;\n"
"    padding: 2px;\n"
"    border-radius: 0px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QHeaderView::section:checked {\n"
"    color: #000000;\n"
"    background-color: #BCDCF4;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one {\n"
"    border-top: 1px solid #ADADAD;\n"
"}\n"
"\n"
"QHeaderView::section::vertical {\n"
"    border-top: 1px solid #ADADAD;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one {\n"
"    border-left: 1px solid #ADADAD;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal {\n"
"    border-left: 1px solid #ADADAD;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #E1E1E1;\n"
"    border: 1px solid #ADADAD;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: #E1E1E1;\n"
"    border: 1px solid #ADADAD;\n"
"}")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 991, 611))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.progressBar_1 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_1.setGeometry(QtCore.QRect(290, 230, 118, 23))
        self.progressBar_1.setStyleSheet("")
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setObjectName("progressBar_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 401, 221))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(20, 30, 141, 21))
        self.label_1.setObjectName("label_1")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 90, 381, 121))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_1.setGeometry(QtCore.QRect(20, 30, 221, 17))
        self.radioButton_1.setStyleSheet("")
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 221, 17))
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 90, 231, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 21))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(430, 0, 541, 61))
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 30, 81, 20))
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(300, 30, 113, 20))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(240, 30, 51, 21))
        self.label_8.setObjectName("label_8")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 260, 401, 281))
        self.groupBox_8.setStyleSheet("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.graphicsView_1 = MplWidget(self.groupBox_8)
        self.graphicsView_1.setGeometry(QtCore.QRect(0, 20, 401, 261))
        self.graphicsView_1.setStyleSheet("background-color: #F7FBFD")
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_9.setGeometry(QtCore.QRect(430, 70, 541, 471))
        self.groupBox_9.setStyleSheet("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.tableView_1 = QtWidgets.QTableView(self.groupBox_9)
        self.tableView_1.setGeometry(QtCore.QRect(10, 30, 521, 431))
        self.tableView_1.setStyleSheet("")
        self.tableView_1.setObjectName("tableView_1")
        self.dateEdit_1 = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_1.setGeometry(QtCore.QRect(170, 30, 91, 22))
        self.dateEdit_1.setStyleSheet("")
        self.dateEdit_1.setCalendarPopup(True)
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_2.setGeometry(QtCore.QRect(170, 60, 91, 22))
        self.dateEdit_2.setStyleSheet("")
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.progressBar_1.raise_()
        self.pushButton_2.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_9.raise_()
        self.dateEdit_1.raise_()
        self.dateEdit_2.raise_()
        self.groupBox_8.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(290, 230, 118, 23))
        self.progressBar_2.setStyleSheet("")
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 0, 401, 221))
        self.groupBox_4.setStyleSheet("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 161, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 30, 31, 20))
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 161, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 60, 31, 20))
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 90, 381, 121))
        self.groupBox_6.setObjectName("groupBox_6")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 35, 21, 21))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 80, 21, 21))
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(40, 42, 161, 21))
        self.label_6.setObjectName("label_6")
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(40, 87, 321, 21))
        self.label_14.setObjectName("label_14")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(40, 28, 171, 21))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(40, 73, 161, 20))
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(430, 0, 541, 61))
        self.groupBox_5.setStyleSheet("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 151, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 30, 31, 20))
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(270, 30, 81, 21))
        self.label_16.setObjectName("label_16")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 30, 81, 20))
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.graphicsView_2 = MplWidget(self.tab_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 280, 401, 261))
        self.graphicsView_2.setStyleSheet("background-color: #F7FBFD")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(880, 550, 75, 23))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 260, 401, 281))
        self.groupBox_10.setStyleSheet("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_11.setGeometry(QtCore.QRect(430, 70, 541, 471))
        self.groupBox_11.setStyleSheet("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 20, 221, 261))
        self.groupBox_12.setStyleSheet("\n"
"QGroupBox {\n"
"    font-weight: bold;\n"
"    border: 0px solid #DCDCDC;\n"
" }\n"
"")
        self.groupBox_12.setObjectName("groupBox_12")
        self.tableView_2 = QtWidgets.QTableView(self.groupBox_12)
        self.tableView_2.setGeometry(QtCore.QRect(10, 30, 201, 221))
        self.tableView_2.setStyleSheet("")
        self.tableView_2.setObjectName("tableView_2")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_13.setGeometry(QtCore.QRect(240, 20, 291, 261))
        self.groupBox_13.setStyleSheet("\n"
"QGroupBox {\n"
"    font-weight: bold;\n"
"    border: 0px solid #DCDCDC;\n"
" }\n"
"")
        self.groupBox_13.setObjectName("groupBox_13")
        self.tableView_4 = QtWidgets.QTableView(self.groupBox_13)
        self.tableView_4.setGeometry(QtCore.QRect(10, 30, 271, 221))
        self.tableView_4.setStyleSheet("")
        self.tableView_4.setObjectName("tableView_4")
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_11)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 280, 521, 181))
        self.groupBox_14.setStyleSheet("\n"
"QGroupBox {\n"
"    font-weight: bold;\n"
"    border: 0px solid #DCDCDC;\n"
" }\n"
"")
        self.groupBox_14.setObjectName("groupBox_14")
        self.tableView_3 = QtWidgets.QTableView(self.groupBox_14)
        self.tableView_3.setGeometry(QtCore.QRect(10, 30, 501, 141))
        self.tableView_3.setStyleSheet("")
        self.tableView_3.setObjectName("tableView_3")
        self.groupBox_13.raise_()
        self.groupBox_12.raise_()
        self.groupBox_14.raise_()
        self.groupBox_11.raise_()
        self.groupBox_10.raise_()
        self.progressBar_2.raise_()
        self.groupBox_4.raise_()
        self.pushButton_3.raise_()
        self.groupBox_5.raise_()
        self.graphicsView_2.raise_()
        self.pushButton_4.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 0, 991, 61))
        self.groupBox_7.setStyleSheet("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.pushButton_1.setStyleSheet("/* QPushButton -------------------------------------------------------------- */\n"
"\n"
"QPushButton {\n"
"    background-color: #E1E1E1;\n"
"    border: 1px solid #ADADAD;\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #0078D7;\n"
"    background-color: #E5F1FB;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #CCE4F7;\n"
"    border: 1px solid #00559B;\n"
"    color: #000000;\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_1.setGeometry(QtCore.QRect(90, 30, 301, 21))
        self.lineEdit_1.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    border-style: solid; /* without this border reverts for disabled */\n"
"    border: 1px solid #7A7A7A;\n"
"    color: #000000;\n"
"    border-radius: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 1px solid #000000;\n"
"    background-color: #FFFFFF;\n"
"    color: #000000;\n"
"}\n"
"")
        self.lineEdit_1.setReadOnly(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_1.setGeometry(QtCore.QRect(580, 30, 91, 17))
        self.checkBox_1.setStyleSheet("border: none\n"
"")
        self.checkBox_1.setObjectName("checkBox_1")
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_1.setGeometry(QtCore.QRect(420, 28, 131, 22))
        self.comboBox_1.setStyleSheet("")
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.lineEdit_1)
        MainWindow.setTabOrder(self.lineEdit_1, self.dateEdit_1)
        MainWindow.setTabOrder(self.dateEdit_1, self.dateEdit_2)
        MainWindow.setTabOrder(self.dateEdit_2, self.radioButton_1)
        MainWindow.setTabOrder(self.radioButton_1, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton_3)
        MainWindow.setTabOrder(self.radioButton_3, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.tableView_1)
        MainWindow.setTabOrder(self.tableView_1, self.radioButton_5)
        MainWindow.setTabOrder(self.radioButton_5, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.tableView_2)
        MainWindow.setTabOrder(self.tableView_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.lineEdit_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Methodologies DP&R"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate"))
        self.groupBox.setTitle(_translate("MainWindow", "Inputs"))
        self.label_1.setText(_translate("MainWindow", "Service Date Range Begin:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Date of Intervention (DOI) Optimization Options"))
        self.radioButton_1.setText(_translate("MainWindow", "Maximize 1 month prior to DOI"))
        self.radioButton_2.setText(_translate("MainWindow", "Maximize 1 month difference  after DOI"))
        self.radioButton_3.setText(_translate("MainWindow", "Maximize 12 month difference after DOI"))
        self.label_2.setText(_translate("MainWindow", "Service Date Range End:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Outputs"))
        self.label.setText(_translate("MainWindow", "Optimal DOI:"))
        self.label_8.setText(_translate("MainWindow", "Amount:"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Chart"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "   Data Points   "))
        self.groupBox_4.setTitle(_translate("MainWindow", "Inputs"))
        self.label_3.setText(_translate("MainWindow", "Maximum Number of Segments:"))
        self.label_4.setText(_translate("MainWindow", "Maximum Number of Iterations:"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Explanatory Variable (Time) Recode Options"))
        self.label_6.setText(_translate("MainWindow", "All independent variables vary"))
        self.label_14.setText(_translate("MainWindow", "One independent variable varies while all others held constant"))
        self.label_5.setText(_translate("MainWindow", "Continuous without Discretization"))
        self.label_9.setText(_translate("MainWindow", "Continuous with Discretization"))
        self.pushButton_3.setText(_translate("MainWindow", "Calculate"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Outputs"))
        self.label_7.setText(_translate("MainWindow", "Optimal Number of Segments:"))
        self.label_16.setText(_translate("MainWindow", "Function value:"))
        self.pushButton_4.setText(_translate("MainWindow", "Export"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Chart"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Tables"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Summary"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Parameters"))
        self.groupBox_14.setTitle(_translate("MainWindow", "ANOVA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "   Regression   "))
        self.groupBox_7.setTitle(_translate("MainWindow", "Data"))
        self.pushButton_1.setText(_translate("MainWindow", "Select File"))
        self.checkBox_1.setText(_translate("MainWindow", "Has Headers"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "Tab Delimited"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Comma Delimited"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "Pipe Delimited"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

