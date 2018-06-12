from algorithms import Transposition as ts
from algorithms import affine as aff
from algorithms import RSA
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from key_generation import Ui_Dialog
import sys, random
from math import gcd


class Ui_Form(object):
    # --------------------------------GUI---------------------------
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(661, 645)
        self.dialog = QDialog()
        self.dialog.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.ui.OK.clicked.connect(self.generate_key)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/Python Projects/Security_projects/icons/key.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color:\"#2c3e50\";\n"
                           "color:\"#71BA51\"")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 110, 621, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.q = QtWidgets.QTabWidget(Form)
        self.q.setGeometry(QtCore.QRect(26, 139, 601, 501))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.q.setFont(font)
        self.q.setStyleSheet("\n"
                             "QTabWidget::pane { /* The tab widget frame */\n"
                             "    border-top: 1px solid #2c3e50;\n"
                             "    position: absolute;\n"
                             "    top: -0.5em;\n"
                             "}\n"
                             "\n"
                             "\n"
                             "/* Style the tab using the tab sub-control. Note that\n"
                             "    it reads QTabBar _not_ QTabWidget */\n"
                             "QTabBar::tab {\n"
                             "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                             "                                stop: 0 #2c3e50, stop: 0.4 #2c3e50,\n"
                             "                                stop: 0.5 #34495e, stop: 1.0 #34495e);\n"
                             "    border: 2px solid #2c3e50;\n"
                             "    border-bottom-color: #2c3e50; /* same as the pane color */\n"
                             "    border-top-left-radius: 4px;\n"
                             "    border-top-right-radius: 4px;\n"
                             "    min-width: 8ex;\n"
                             "    padding: 2px;\n"
                             "}\n"
                             "\n"
                             "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                             "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                             "                                stop: 0 #34495e, stop: 0.4 #2c3e50,\n"
                             "                                stop: 0.5 #2c3e50, stop: 1.0 #2c3e50);\n"
                             "}\n"
                             "\n"
                             "QTabBar::tab:selected {\n"
                             "    border-color: #3b6289;\n"
                             "    border-bottom-color: #3b6289; /* same as pane color */\n"
                             "}\n"
                             "color:\"#71BA51\"")
        self.q.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.q.setIconSize(QtCore.QSize(35, 25))
        self.q.setTabsClosable(False)
        self.q.setMovable(True)
        self.q.setTabBarAutoHide(True)
        self.q.setObjectName("q")
        self.tran = QtWidgets.QWidget()
        self.tran.setObjectName("tran")
        self.T_choose = QtWidgets.QComboBox(self.tran)
        self.T_choose.setGeometry(QtCore.QRect(330, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.T_choose.setFont(font)
        self.T_choose.setMouseTracking(False)
        self.T_choose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T_choose.setEditable(False)
        self.T_choose.setCurrentText("Encryption")
        self.T_choose.setObjectName("T_choose")
        self.T_choose.addItem("")
        self.T_choose.addItem("")
        self.label = QtWidgets.QLabel(self.tran)
        self.label.setGeometry(QtCore.QRect(10, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textLable = QtWidgets.QLabel(self.tran)
        self.textLable.setGeometry(QtCore.QRect(10, 110, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textLable.setFont(font)
        self.textLable.setObjectName("textLable")
        self.T_text = QtWidgets.QPlainTextEdit(self.tran)
        self.T_text.setGeometry(QtCore.QRect(180, 90, 391, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.T_text.setFont(font)
        self.T_text.setStyleSheet("background-color:\"#fff\";\n"
                                  "color:\"#000\"")
        self.T_text.setTabChangesFocus(True)
        self.T_text.setObjectName("T_text")
        self.label_3 = QtWidgets.QLabel(self.tran)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.T_key = QtWidgets.QLineEdit(self.tran)
        self.T_key.setGeometry(QtCore.QRect(180, 200, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.T_key.setFont(font)
        self.T_key.setStyleSheet("background-color:\"#fff\";\n"
                                 "color:\"#000\"")
        self.T_key.setObjectName("T_key")
        self.T_result = QtWidgets.QTextBrowser(self.tran)
        self.T_result.setGeometry(QtCore.QRect(10, 310, 561, 121))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.T_result.setFont(font)
        self.T_result.setStyleSheet("background-color:\"#fff\";\n"
                                    "color:\"#000\"")
        self.T_result.setObjectName("T_result")
        self.resultLabel = QtWidgets.QLabel(self.tran)
        self.resultLabel.setGeometry(QtCore.QRect(10, 280, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.resultLabel.setFont(font)
        self.resultLabel.setObjectName("resultLabel")
        self.T_err = QtWidgets.QLabel(self.tran)
        self.T_err.setGeometry(QtCore.QRect(10, 440, 561, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.T_err.setFont(font)
        self.T_err.setStyleSheet("color:\"#EE543A\"")
        self.T_err.setWordWrap(True)
        self.T_err.setObjectName("T_err")
        self.T_go = QtWidgets.QPushButton(self.tran)
        self.T_go.setGeometry(QtCore.QRect(530, 250, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.T_go.setFont(font)
        self.T_go.setStyleSheet("background-color:\"#e74c3c\";\n"
                                "color:\"#fff\";\n"
                                "border-radius:20px")
        self.T_go.setObjectName("T_go")
        self.label_4 = QtWidgets.QLabel(self.tran)
        self.label_4.setGeometry(QtCore.QRect(10, 245, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.show_table = QtWidgets.QPushButton(self.tran)
        self.show_table.setEnabled(False)
        self.show_table.setGeometry(QtCore.QRect(430, 255, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_table.setFont(font)
        self.show_table.setStyleSheet("background-color:\"#71BA51\";\n"
                                      "color:\"#fff\";\n"
                                      "border-radius:3px")
        self.show_table.setObjectName("pushButton")
        self.show_table.clicked.connect(self.showTable)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/Python Projects/Security_projects/icons/T.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.q.addTab(self.tran, icon1, "")
        self.affine = QtWidgets.QWidget()
        self.affine.setObjectName("affine")
        self.label_13 = QtWidgets.QLabel(self.affine)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.A_choose = QtWidgets.QComboBox(self.affine)
        self.A_choose.setGeometry(QtCore.QRect(330, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.A_choose.setFont(font)
        self.A_choose.setMouseTracking(False)
        self.A_choose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.A_choose.setEditable(False)
        self.A_choose.setCurrentText("Encryption")
        self.A_choose.setObjectName("A_choose")
        self.A_choose.addItem("")
        self.A_choose.addItem("")
        self.label_14 = QtWidgets.QLabel(self.affine)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.A_alpha = QtWidgets.QPlainTextEdit(self.affine)
        self.A_alpha.setGeometry(QtCore.QRect(10, 90, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.A_alpha.setFont(font)
        self.A_alpha.setStyleSheet("background-color:\"#fff\";\n"
                                   "border radius:6px;\n"
                                   "color:\"#000\"")
        self.A_alpha.setTabChangesFocus(True)
        self.A_alpha.setObjectName("A_alpha")
        self.A_shf = QtWidgets.QSpinBox(self.affine)
        self.A_shf.setGeometry(QtCore.QRect(540, 160, 61, 31))
        font = QtGui.QFont()
        self.A_shf.setValue(1)
        font.setPointSize(12)
        self.A_shf.setFont(font)
        self.A_shf.setObjectName("A_shf")
        self.Lappp_2 = QtWidgets.QLabel(self.affine)
        self.Lappp_2.setGeometry(QtCore.QRect(320, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lappp_2.setFont(font)
        self.Lappp_2.setObjectName("Lappp_2")
        self.A_amp = QtWidgets.QSpinBox(self.affine)
        self.A_amp.setGeometry(QtCore.QRect(420, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.A_amp.setFont(font)
        self.A_amp.setValue(4)
        self.A_amp.setObjectName("A_amp")
        self.label_15 = QtWidgets.QLabel(self.affine)
        self.label_15.setGeometry(QtCore.QRect(490, 160, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.affine)
        self.label_16.setGeometry(QtCore.QRect(10, 160, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.affine)
        self.label_17.setGeometry(QtCore.QRect(10, 220, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.A_text = QtWidgets.QPlainTextEdit(self.affine)
        self.A_text.setGeometry(QtCore.QRect(270, 200, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.A_text.setFont(font)
        self.A_text.setStyleSheet("background-color:\"#fff\";\n"
                                  "border radius:6px;\n"
                                  "color:\"#000\"")
        self.A_text.setTabChangesFocus(True)
        self.A_text.setObjectName("A_text")
        self.label_19 = QtWidgets.QLabel(self.affine)
        self.label_19.setGeometry(QtCore.QRect(10, 280, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_18 = QtWidgets.QLabel(self.affine)
        self.label_18.setGeometry(QtCore.QRect(10, 310, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.A_result = QtWidgets.QTextBrowser(self.affine)
        self.A_result.setGeometry(QtCore.QRect(10, 340, 601, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.A_result.setFont(font)
        self.A_result.setStyleSheet("background-color:\"#fff\";\n"
                                    "border radius:6px;\n"
                                    "color:\"#000\"")
        self.A_result.setObjectName("A_result")
        self.A_err = QtWidgets.QLabel(self.affine)
        self.A_err.setGeometry(QtCore.QRect(10, 450, 591, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.A_err.setFont(font)
        self.A_err.setStyleSheet("color:\"#EE543A\"")
        self.A_err.setObjectName("A_err")
        self.A_go = QtWidgets.QPushButton(self.affine)
        self.A_go.setGeometry(QtCore.QRect(550, 290, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.A_go.setFont(font)
        self.A_go.setStyleSheet("background-color:\"#e74c3c\";\n"
                                "color:\"#fff\";\n"
                                "border-radius:20px")
        self.A_go.setObjectName("A_go")
        self.label_13.raise_()
        self.A_choose.raise_()
        self.label_14.raise_()
        self.A_alpha.raise_()
        self.A_shf.raise_()
        self.Lappp_2.raise_()
        self.A_amp.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_17.raise_()
        self.A_text.raise_()
        self.label_19.raise_()
        self.label_18.raise_()
        self.A_result.raise_()
        self.A_err.raise_()
        self.A_go.raise_()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("F:/Python Projects/Security_projects/icons/A.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.q.addTab(self.affine, icon2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.R_choose = QtWidgets.QComboBox(self.tab)
        self.R_choose.setGeometry(QtCore.QRect(320, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.R_choose.setFont(font)
        self.R_choose.setObjectName("R_choose")
        self.R_choose.addItem("")
        self.R_choose.addItem("")
        self.R_alpha = QtWidgets.QPlainTextEdit(self.tab)
        self.R_alpha.setGeometry(QtCore.QRect(10, 90, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_alpha.setFont(font)
        self.R_alpha.setStyleSheet("background-color:\"#fff\";\n"
                                   "border radius:6px;\n"
                                   "color:\"#000\"")
        self.R_alpha.setTabChangesFocus(True)
        self.R_alpha.setObjectName("R_alpha")
        self.R_text = QtWidgets.QPlainTextEdit(self.tab)
        self.R_text.setGeometry(QtCore.QRect(260, 190, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_text.setFont(font)
        self.R_text.setStyleSheet("background-color:\"#fff\";\n"
                                  "border radius:6px;\n"
                                  "color:\"#000\"")
        self.R_text.setTabChangesFocus(True)
        self.R_text.setPlainText("")
        self.R_text.setOverwriteMode(False)
        self.R_text.setObjectName("R_text")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 160, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Lappp = QtWidgets.QLabel(self.tab)
        self.Lappp.setGeometry(QtCore.QRect(400, 160, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Lappp.setFont(font)
        self.Lappp.setObjectName("Lappp")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(507, 160, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.R_q = QtWidgets.QSpinBox(self.tab)
        self.R_q.setMaximum(40000)
        self.R_q.setGeometry(QtCore.QRect(537, 160, 62, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.R_q.setFont(font)
        self.R_q.setObjectName("R_q")
        self.R_q.setSpecialValueText("0")
        self.R_p = QtWidgets.QSpinBox(self.tab)
        self.R_p.setMaximum(40000)
        self.R_p.setGeometry(QtCore.QRect(430, 160, 62, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.R_p.setFont(font)
        self.R_p.setSpecialValueText("0")
        self.R_p.setObjectName("R_p")
        self.R_result = QtWidgets.QTextBrowser(self.tab)
        self.R_result.setGeometry(QtCore.QRect(0, 330, 601, 111))
        self.R_result.setStyleSheet("background-color:\"#fff\";\n"
                                    "border radius:6px;\n"
                                    "color:\"#000\"")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.R_result.setFont(font)
        self.R_result.setObjectName("R_result")
        self.R_err = QtWidgets.QLabel(self.tab)
        self.R_err.setGeometry(QtCore.QRect(10, 450, 591, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.R_err.setFont(font)
        self.R_err.setStyleSheet("color:\"#EE543A\"")
        self.R_err.setObjectName("R_err")
        self.R_go = QtWidgets.QPushButton(self.tab)
        self.R_go.setGeometry(QtCore.QRect(540, 280, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.R_go.setFont(font)
        self.R_go.setStyleSheet("background-color:\"#e74c3c\";\n"
                                "color:\"#fff\";\n"
                                "border-radius:20px")
        self.R_go.setObjectName("R_go")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 270, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(10, 300, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(430, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:\"#71BA51\";\n"
                                      "color:\"#fff\";\n"
                                      "border-radius:3px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generate_key)
        self.p_q_keys = QtWidgets.QPushButton(self.tab)
        self.p_q_keys.setGeometry(QtCore.QRect(330, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_q_keys.setFont(font)
        self.p_q_keys.setStyleSheet("background-color:\"#71BA51\";\n"
                                    "color:\"#fff\";\n"
                                    "border-radius:3px")
        self.p_q_keys.setObjectName("pushButton")
        self.p_q_keys.clicked.connect(self.show_p_q)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("F:/Python Projects/Security_projects/icons/R.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.q.addTab(self.tab, icon3, "")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 621, 80))
        self.widget.setStyleSheet("background-color:\"#71BA51\"\n"
                                  ";color:\"#fff\";\n"
                                  "border-radius:5px")
        self.widget.setObjectName("widget")
        self.chLable = QtWidgets.QLabel(self.widget)
        self.chLable.setGeometry(QtCore.QRect(20, 50, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.chLable.setFont(font)
        self.chLable.setObjectName("chLable")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(230, 20, 31, 21))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        self.q.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cipher"))
        self.T_choose.setItemText(0, _translate("Form", "Encryption"))
        self.T_choose.setItemText(1, _translate("Form", "Decryption"))
        self.T_choose.currentIndexChanged.connect(self.Trans_change)
        self.label.setText(_translate("Form", "Choose encryption Or decryption  :"))
        self.textLable.setText(_translate("Form", "Enter your plain text:"))
        self.T_text.setPlaceholderText(_translate("Form", "WE NEED MORE SNOW NOW"))
        self.label_3.setText(_translate("Form", "Enter your key word :"))
        self.T_key.setPlaceholderText(_translate("Form", "SECTION"))
        self.resultLabel.setText(_translate("Form", "Your Result for encryption is :"))
        self.T_err.setText(_translate("Form", ""))
        self.T_go.setText(_translate("Form", "GO"))
        self.show_table.setText(_translate("Form", "Show table"))
        self.T_go.clicked.connect(self.Trans_go)
        self.label_4.setText(_translate("Form", "Please press GO to start encrypt :"))
        self.q.setTabText(self.q.indexOf(self.tran), _translate("Form", "Transposition"))
        self.label_13.setText(_translate("Form", "Choose encryption Or decryption  :"))
        self.A_choose.setItemText(0, _translate("Form", "Encryption"))
        self.A_choose.setItemText(1, _translate("Form", "Decryption"))
        self.A_choose.currentIndexChanged.connect(self.aff_change)
        self.label_14.setText(
            _translate("Form", "Enter the alphabet you wish to use Or keep it blank for 26 char alphabet : "))
        self.A_alpha.setPlaceholderText(_translate("Form", "ABCDEFG..."))
        self.Lappp_2.setText(_translate("Form", "Amplitude :"))
        self.Lappp_2.setToolTip(" M ")
        self.label_15.setText(_translate("Form", "Shift :"))
        self.label_15.setToolTip(" S ")
        self.label_16.setText(_translate("Form", "Enter your M and S [prime numbers] :"))
        self.label_17.setText(_translate("Form", "Enter your plain text :"))
        self.A_text.setPlaceholderText(_translate("Form", "WE NEED MORE SNOW NOW"))
        self.label_19.setText(_translate("Form", "Please press GO to start encrypt :"))
        self.label_18.setText(_translate("Form", "Your Result for encryption is :"))
        self.A_err.setText(_translate("Form", ""))
        self.A_go.setText(_translate("Form", "GO"))
        self.A_go.clicked.connect(self.aff_go)
        self.q.setTabText(self.q.indexOf(self.affine), _translate("Form", "    Affine    "))
        self.label_6.setText(
            _translate("Form", "Enter the alphabet you wish to use Or keep it blank for 26 char alphabet : "))
        self.label_7.setText(_translate("Form", "Choose encryption Or decryption :"))
        self.R_choose.setItemText(0, _translate("Form", "Encryption"))
        self.R_choose.setItemText(1, _translate("Form", "Decryption"))
        self.R_choose.currentIndexChanged.connect(self.rsa_change)
        self.R_alpha.setPlaceholderText(_translate("Form", "ABCDEFG..."))
        self.R_text.setPlaceholderText(_translate("Form", "WE NEED MORE SNOW NOW"))
        self.label_8.setText(_translate("Form", "Enter your text :"))
        self.label_9.setText(_translate("Form", "Enter your E and N [public key] :"))
        self.Lappp.setText(_translate("Form", "E :"))
        self.label_11.setText(_translate("Form", "N :"))
        self.R_err.setText(_translate("Form", ""))
        self.R_go.setText(_translate("Form", "GO"))
        self.R_go.clicked.connect(self.rsa_go)
        self.label_10.setText(_translate("Form", "Please press GO to start encrypt :"))
        self.label_12.setText(_translate("Form", "Your Result for encryption is :"))
        self.pushButton.setText(_translate("Form", "Generate keys"))
        self.p_q_keys.setText(_translate("Form", "Set p AND q"))
        self.pushButton.setToolTip("Use two prime numbers [P,Q] to gentries the public and private keys")
        self.q.setTabText(self.q.indexOf(self.tab), _translate("Form", "   R.S.A   "))
        self.chLable.setText(_translate("Form", "Please choose the encryption or decryption technique : "))
        self.label_2.setText(_translate("Form", "Welcome To cipher"))
        self.label_5.setText(
            _translate("Form",
                       "<html><head/><body><p><img src=\"F:/Python Projects/Security_projects/icons/key.png\"/></p></body></html>"))

    # -------------------------transposition-----------------------
    def Trans_go(self):
        choose = self.T_choose.currentIndex()
        if self.T_text.toPlainText() == "":
            self.T_err.setText("Please fill the plan text field first to start")

        elif self.T_key.text() == "":
            self.T_err.setText("Please fill the key text field first to start")

        else:
            if choose == 0:
                self.Trans_encryption()
                self.show_table.setEnabled(True)
            elif choose == 1:
                self.Trans_decryption()
                self.show_table.setEnabled(True)

    def Trans_encryption(self):
        self.textLable.setText("Enter your plan text :")
        self.T_err.setText("")
        plan = str(self.T_text.toPlainText())
        key = str(self.T_key.text())
        self.keyy = list(key)
        if not plan.isalpha() and not key.isalpha():
            self.T_err.setText("Please plan text and key shouldn't be all numbers")
        else:
            # check key word uniqueness
            if ts.unique_chars_set(key):
                cipher_text, self.en_table = ts.encryption(key, plan)
                self.T_result.setText(cipher_text)
            else:
                self.T_err.setText("chars in the key should be unique for avoid conflict ")

    def Trans_decryption(self):
        self.textLable.setText("Enter your cipher text :")
        cipher = str(self.T_text.toPlainText())
        key = str(self.T_key.text())

        # check key word uniqueness
        if ts.unique_chars_set(key):
            plan_text, self.de_table = ts.decryption(key, cipher)
            self.T_result.setText(plan_text)
            # self.T_result.append(
            # "Since the matrix doesn’t hold spaces you’ll have to realize the text meaning your self")
            # self.T_result.append("for example > "+ str(plan_text.upper()))
            # self.T_result.append("with letters [ABCD] >> doesn’t hold meaning so that must have completed missing cells")
        else:
            self.T_err.setText("chars in the key should be unique for avoid conflict ")

    def Trans_change(self):
        if self.T_choose.currentIndex() == 0:
            self.textLable.setText("Enter your plain text:")
            self.label_4.setText("Please press GO to start encrypt :")
            self.resultLabel.setText("Your Result for encryption is :")
        else:
            self.textLable.setText("Enter your cipher text :")
            self.label_4.setText("Please press GO to start decrypt :")
            self.resultLabel.setText("Your Result for decryption is :")

    def showTable(self):
        try:
            if self.T_choose.currentIndex() == 0:
                if self.show_table.isEnabled():
                    self.T_result.setText(str(self.keyy))
                    for xx in self.en_table:
                        self.T_result.append(str(xx))
                    self.show_table.setEnabled(False)
                else:
                    self.T_err.setText("Sorry, you must encrypt some thing to see it's table")
            else:
                if self.show_table.isEnabled():
                    self.T_result.setText(str(self.keyy))
                    for xx in self.de_table:
                        self.T_result.append(str(xx))
                    self.show_table.setEnabled(False)
                else:
                    self.T_err.setText("Sorry, you must encrypt some thing to see it's table")
        except Exception:
            self.T_err.setText("Un expected error occurs ")

    # ------------------------Affine-------------------------------
    def aff_go(self):
        choose = self.A_choose.currentIndex()
        self.A_err.setText("")
        if self.A_text.toPlainText() == "":
            self.A_err.setText("Please fill the plan text field first to start")

        elif self.A_amp.text() == "":
            self.A_err.setText("Please fill the Amplitude number  first to start")
        elif self.A_shf.text() == "":
            self.A_err.setText("Please fill the shift number first to start")

        else:
            if choose == 0:
                self.aff_encryption()
                # self.A_alpha.setPlainText("")
            elif choose == 1:
                self.aff_decryption()
                # self.A_alpha.setPlainText("")

    def aff_encryption(self):
        if self.A_alpha.toPlainText() == "":
            if self.A_text.toPlainText().islower():
                alpha = "abcdefghijklmnopqrstuvwxyz"
                self.A_alpha.setPlainText(" abcdefghijklmnopqrstuvwxyz")

            else:
                alpha = "  ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                self.A_alpha.setPlainText(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        a = int(self.A_amp.text())
        s = int(self.A_shf.text())
        alpha = str(self.A_alpha.toPlainText())
        # if not alpha.isalpha():
        #     self.A_err.setText("Please put an alphabet chars")
        # else:
        if gcd(a, len(alpha)) != 1:
            self.A_err.setText("Please change the Amplitude number [GCD] err")
        else:
            plan_text = str(self.A_text.toPlainText())
            in_alpha = True
            for char in plan_text:
                if char not in alpha:
                    in_alpha = False

            if in_alpha:
                cipher_text = aff.encryption(plan_text, a, s, alpha)
                self.A_result.setText(cipher_text)
            else:
                self.A_err.setText("The plain text chars is not in your entered alphabet change it ")

    def aff_decryption(self):
        if self.A_alpha.toPlainText() == "":
            if self.A_text.toPlainText().islower():
                alpha = "abcdefghijklmnopqrstuvwxyz "
                self.A_alpha.setPlainText(" abcdefghijklmnopqrstuvwxyz")
            else:
                alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                self.A_alpha.setPlainText(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        a = int(self.A_amp.text())
        s = int(self.A_shf.text())
        alpha = str(self.A_alpha.toPlainText())
        # if not alpha.isalpha():
        #     self.A_err.setText("Please put an alphabet chars")
        # else:
        if gcd(a, len(alpha)) != 1:
            self.A_err.setText("Please change the Amplitude number [GCD] err")
        else:
            cipher_text = str(self.A_text.toPlainText())
            in_alpha = True
            for char in cipher_text:
                if char not in alpha:
                    in_alpha = False

            if in_alpha:
                plain_text = aff.decryption(a, s, cipher_text, alpha)
                if plain_text == False:
                    self.A_err.setText("Please choose another amplitude ")
                else:
                    self.A_result.setText(plain_text)
            else:
                self.A_err.setText("The plain text chars is not in your entered alphabet !")

    def aff_change(self):
        if self.A_choose.currentIndex() == 0:
            self.label_17.setText("Enter your plain text :")
            self.label_19.setText("Please press GO to start encrypt :")
            self.label_18.setText("Your Result for encryption is :")
        else:
            self.label_17.setText("Enter your cipher text :")
            self.label_19.setText("Please press GO to start decrypt :")
            self.label_18.setText("Your Result for decryption is :")

    # -------------------------RSA--------------------------------
    def rsa_go(self):
        choose = self.R_choose.currentIndex()
        self.R_err.setText("")
        if self.R_text.toPlainText() == "":
            self.R_err.setText("Please fill the plan text field first to start")

        elif self.R_p.text() == "0":
            self.R_err.setText("Please fill the [E] number  first to start")
        elif self.R_q.text() == "0":
            self.R_err.setText("Please fill the [N] number first to start")

        else:
            if choose == 0:
                self.rsa_encryption()
            elif choose == 1:
                self.rsa_decryption()

    def get_prime(self):
        p = random.randrange(1, 50)
        q = random.randrange(1, 50)
        if (RSA.is_prime(p) and RSA.is_prime(q)) and q != p:
            return p, q
        else:
            return self.get_prime()

    def show_p_q(self):
        self.dialog.ui.spinBox.setValue(0)
        self.dialog.ui.spinBox_2.setValue(0)
        self.dialog.show()

    def generate_key(self):
        q_dialog = self.dialog.ui.spinBox.value()
        p_dialog = self.dialog.ui.spinBox_2.value()
        if p_dialog == 0 and q_dialog == 0:
            p, q = self.get_prime()
        else:

            p = p_dialog
            q = q_dialog
        try:
            self.ee, self.dd, self.nn = RSA.generate_keys(p, q)
            self.R_result.setText(
                "This values  (E =" + str(self.ee) + ", N =" + str(self.nn) + ") used for Encryption ")
            self.R_result.append(
                "\nThis values  (D =" + str(self.dd) + ", N =" + str(self.nn) + ") used for Decryption")
            self.R_result.append(
                "\nThe two prime numbers used are (P =" + str(p) + ", Q =" + str(q) + ")")
            self.R_q.setValue(self.nn)
            self.R_p.setValue(self.ee)
            self.R_err.setText("")
        except Exception:
            self.R_err.setText("Sorry, your entered numbers are not valid please change it ")

    def rsa_encryption(self):
        if self.R_alpha.toPlainText() == "":
            if self.R_text.toPlainText().islower():
                alpha = " abcdefghijklmnopqrstuvwxyz"
                self.R_alpha.setPlainText(" abcdefghijklmnopqrstuvwxyz")

            else:
                alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                self.R_alpha.setPlainText(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        plan = str(self.R_text.toPlainText())
        e = int(self.R_p.text())
        n = int(self.R_q.text())

        alpha = list(str(self.R_alpha.toPlainText()))
        in_alpha = True
        for char in plan:
            if char not in alpha:
                in_alpha = False

        if in_alpha:

            # apply encryption
            cipher = RSA.encryption(plan_text=plan, E=e, N=n, alpha=alpha)
            cipher = ", ".join(str(x) for x in cipher)
            self.R_result.setText(cipher)
        else:
            self.R_err.setText("The plain text chars is not in your entered alphabet  change it")

    def rsa_decryption(self):
        cipher = []
        try:
            c = str(self.R_text.toPlainText()).replace(" ", "").split(',')
            for i in c:
                cipher.append(int(i))

            d = int(self.R_p.text())
            n = int(self.R_q.text())

            alpha = list(str(self.R_alpha.toPlainText()))
            # apply decryption
            plan = RSA.decryption(cipher, D=d, N=n, alpha=alpha)
            self.R_result.setText(plan)
        except Exception:
            self.R_err.setText(
                "Please put your cipher in this format [1,2,3,4,..] Or check entered [D] and [N]")

    def rsa_change(self):
        if self.R_choose.currentIndex() == 0:
            self.label_8.setText("Enter your plain text :")
            self.label_9.setText("Enter your E and N [public key] :")
            self.Lappp.setText("E :")
            self.label_11.setText("N :")
            self.label_10.setText("Please press GO to start encrypt :")
            self.label_12.setText("Your Result for encryption is :")
            try:
                self.R_q.setValue(self.nn)
                self.R_p.setValue(self.ee)
            except Exception:
                self.R_q.setValue(0)
                self.R_p.setValue(0)

        else:

            self.label_8.setText("Enter your cipher text :")
            self.label_9.setText("Enter your D and N [Private key] :")
            self.Lappp.setText("D :")
            self.label_11.setText("N :")
            self.label_10.setText("Please press GO to start decrypt :")
            self.label_12.setText("Your Result for decryption is :")
            try:
                self.R_q.setValue(self.nn)
                self.R_p.setValue(self.dd)
            except Exception:
                self.R_q.setValue(0)
                self.R_p.setValue(0)


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
