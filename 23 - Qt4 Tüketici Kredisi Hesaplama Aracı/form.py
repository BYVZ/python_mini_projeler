# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(20, 60, 481, 211))
        self.tab_widget.setObjectName("tab_widget")
        self.tab_ihtiyac = QtWidgets.QWidget()
        self.tab_ihtiyac.setObjectName("tab_ihtiyac")
        self.widget_calculator = QtWidgets.QWidget(self.tab_ihtiyac)
        self.widget_calculator.setGeometry(QtCore.QRect(90, 10, 311, 161))
        self.widget_calculator.setObjectName("widget_calculator")
        self.sb_amount = QtWidgets.QDoubleSpinBox(self.widget_calculator)
        self.sb_amount.setGeometry(QtCore.QRect(120, 20, 181, 30))
        self.sb_amount.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_amount.setMinimum(1000.0)
        self.sb_amount.setMaximum(99999999.99)
        self.sb_amount.setSingleStep(100.0)
        self.sb_amount.setObjectName("sb_amount")
        self.cb_maturity = QtWidgets.QComboBox(self.widget_calculator)
        self.cb_maturity.setGeometry(QtCore.QRect(120, 60, 181, 28))
        self.cb_maturity.setEditable(True)
        self.cb_maturity.setObjectName("cb_maturity")
        self.btn_calculate = QtWidgets.QPushButton(self.widget_calculator)
        self.btn_calculate.setGeometry(QtCore.QRect(10, 110, 291, 30))
        self.btn_calculate.setObjectName("btn_calculate")
        self.lbl_amount = QtWidgets.QLabel(self.widget_calculator)
        self.lbl_amount.setGeometry(QtCore.QRect(10, 20, 111, 30))
        self.lbl_amount.setObjectName("lbl_amount")
        self.lbl_maturity = QtWidgets.QLabel(self.widget_calculator)
        self.lbl_maturity.setGeometry(QtCore.QRect(10, 60, 111, 28))
        self.lbl_maturity.setObjectName("lbl_maturity")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/ihtiyac.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_widget.addTab(self.tab_ihtiyac, icon, "")
        self.tab_konut = QtWidgets.QWidget()
        self.tab_konut.setObjectName("tab_konut")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/konut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_widget.addTab(self.tab_konut, icon1, "")
        self.tab_tasit = QtWidgets.QWidget()
        self.tab_tasit.setObjectName("tab_tasit")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/tasit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_widget.addTab(self.tab_tasit, icon2, "")
        self.tab_kobi = QtWidgets.QWidget()
        self.tab_kobi.setObjectName("tab_kobi")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/kobi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_widget.addTab(self.tab_kobi, icon3, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lw_result = QtWidgets.QListWidget(self.centralwidget)
        self.lw_result.setGeometry(QtCore.QRect(20, 274, 481, 281))
        self.lw_result.setObjectName("lw_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kredi Hesaplama"))
        self.sb_amount.setSuffix(_translate("MainWindow", " TL"))
        self.btn_calculate.setText(_translate("MainWindow", "Kredi Hesapla"))
        self.lbl_amount.setText(_translate("MainWindow", "Kredi Tutarı"))
        self.lbl_maturity.setText(_translate("MainWindow", "Vade (ay)"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_ihtiyac), _translate("MainWindow", "İhtiyaç Kredisi"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_konut), _translate("MainWindow", "Konut Kredisi"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_tasit), _translate("MainWindow", "Taşıt Kredisi"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_kobi), _translate("MainWindow", "Kobi Kredisi"))
        self.label.setText(_translate("MainWindow", "Kredi Hesaplama"))
