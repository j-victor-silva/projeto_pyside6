# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesgzsPvx.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(581, 423)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_home = QFrame(self.page_1)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(400, 70))
        self.frame_home.setMaximumSize(QSize(400, 70))
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_home)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_home)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"jetbrains mono"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 700 14pt \"jetbrains mono\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.frame_home)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	font: 8pt \"Segoe UI\";\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_home)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	font: 700 8pt \"Segoe UI\";\n"
"	background-color: #44475a;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #4f5368;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #282a36;\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame_home, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        StackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        StackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        StackedWidget.addWidget(self.page_3)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"Ola...", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("StackedWidget", u"Escreva o seu nome", None))
        self.pushButton.setText(QCoreApplication.translate("StackedWidget", u"Alterar Texto", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"P\u00e1gina 2", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"P\u00e1gina 3", None))
    # retranslateUi

