# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'displayfile.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fileDialog(object):
    def setupUi(self, fileDialog):
        fileDialog.setObjectName("fileDialog")
        fileDialog.resize(816, 657)
        self.verticalLayout = QtWidgets.QVBoxLayout(fileDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileName = QtWidgets.QLabel(fileDialog)
        self.fileName.setObjectName("fileName")
        self.verticalLayout.addWidget(self.fileName)
        self.tabWidget = QtWidgets.QTabWidget(fileDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabWidgetPage1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hexDump = QtWidgets.QTextEdit(self.tabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono")
        font.setPointSize(10)
        self.hexDump.setFont(font)
        self.hexDump.setReadOnly(True)
        self.hexDump.setObjectName("hexDump")
        self.horizontalLayout_3.addWidget(self.hexDump)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.basicText = QtWidgets.QTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono")
        font.setPointSize(10)
        self.basicText.setFont(font)
        self.basicText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.basicText.setReadOnly(True)
        self.basicText.setObjectName("basicText")
        self.horizontalLayout_4.addWidget(self.basicText)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainText = QtWidgets.QTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono")
        self.plainText.setFont(font)
        self.plainText.setObjectName("plainText")
        self.horizontalLayout.addWidget(self.plainText)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previousButton = QtWidgets.QPushButton(fileDialog)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_2.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(fileDialog)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_2.addWidget(self.nextButton)
        self.closeButton = QtWidgets.QPushButton(fileDialog)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(fileDialog)
        self.tabWidget.setCurrentIndex(2)
        self.closeButton.clicked.connect(fileDialog.accept)
        self.nextButton.clicked.connect(fileDialog.next)
        QtCore.QMetaObject.connectSlotsByName(fileDialog)

    def retranslateUi(self, fileDialog):
        _translate = QtCore.QCoreApplication.translate
        fileDialog.setWindowTitle(_translate("fileDialog", "Dialog"))
        self.fileName.setText(_translate("fileDialog", "FileName"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("fileDialog", "Hex Dump"))
        self.basicText.setHtml(_translate("fileDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans Mono\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Droid Sans Mono\';\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("fileDialog", "Basic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("fileDialog", "Text"))
        self.previousButton.setToolTip(_translate("fileDialog", "Previous Item"))
        self.previousButton.setText(_translate("fileDialog", "<<"))
        self.nextButton.setToolTip(_translate("fileDialog", "Next Item"))
        self.nextButton.setText(_translate("fileDialog", ">>"))
        self.closeButton.setText(_translate("fileDialog", "Close"))
