# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ivan/Documents/__skripsi/buGis/ui_bugis.ui'
#
# Created: Thu Jan 30 02:13:21 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_buGis(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(385, 435)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.radioMapcanvas = QtGui.QRadioButton(self.groupBox)
        self.radioMapcanvas.setObjectName(_fromUtf8("radioMapcanvas"))
        self.gridLayout_2.addWidget(self.radioMapcanvas, 0, 0, 1, 2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.comboInput1 = QtGui.QComboBox(self.groupBox)
        self.comboInput1.setObjectName(_fromUtf8("comboInput1"))
        self.gridLayout_2.addWidget(self.comboInput1, 1, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.comboInput2 = QtGui.QComboBox(self.groupBox)
        self.comboInput2.setObjectName(_fromUtf8("comboInput2"))
        self.gridLayout_2.addWidget(self.comboInput2, 2, 1, 1, 2)
        self.radioBrowse = QtGui.QRadioButton(self.groupBox)
        self.radioBrowse.setObjectName(_fromUtf8("radioBrowse"))
        self.gridLayout_2.addWidget(self.radioBrowse, 3, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineBrowseIn1 = QtGui.QLineEdit(self.groupBox)
        self.lineBrowseIn1.setObjectName(_fromUtf8("lineBrowseIn1"))
        self.gridLayout_2.addWidget(self.lineBrowseIn1, 4, 1, 1, 1)
        self.pushBrowseIn1 = QtGui.QPushButton(self.groupBox)
        self.pushBrowseIn1.setObjectName(_fromUtf8("pushBrowseIn1"))
        self.gridLayout_2.addWidget(self.pushBrowseIn1, 4, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.lineBrowseIn2 = QtGui.QLineEdit(self.groupBox)
        self.lineBrowseIn2.setObjectName(_fromUtf8("lineBrowseIn2"))
        self.gridLayout_2.addWidget(self.lineBrowseIn2, 5, 1, 1, 1)
        self.pushBrowseIn2 = QtGui.QPushButton(self.groupBox)
        self.pushBrowseIn2.setObjectName(_fromUtf8("pushBrowseIn2"))
        self.gridLayout_2.addWidget(self.pushBrowseIn2, 5, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioTemp = QtGui.QRadioButton(self.groupBox_2)
        self.radioTemp.setObjectName(_fromUtf8("radioTemp"))
        self.gridLayout.addWidget(self.radioTemp, 0, 0, 1, 2)
        self.radioTofile = QtGui.QRadioButton(self.groupBox_2)
        self.radioTofile.setObjectName(_fromUtf8("radioTofile"))
        self.gridLayout.addWidget(self.radioTofile, 1, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineTofile = QtGui.QLineEdit(self.groupBox_2)
        self.lineTofile.setObjectName(_fromUtf8("lineTofile"))
        self.gridLayout.addWidget(self.lineTofile, 2, 1, 1, 1)
        self.pushBrowseOut = QtGui.QPushButton(self.groupBox_2)
        self.pushBrowseOut.setObjectName(_fromUtf8("pushBrowseOut"))
        self.gridLayout.addWidget(self.pushBrowseOut, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Input", None))
        self.radioMapcanvas.setText(_translate("Dialog", "From Map Canvas", None))
        self.label.setText(_translate("Dialog", "1st shp", None))
        self.label_2.setText(_translate("Dialog", "2nd shp", None))
        self.radioBrowse.setText(_translate("Dialog", "Browse for files", None))
        self.label_3.setText(_translate("Dialog", "1st shp", None))
        self.pushBrowseIn1.setText(_translate("Dialog", "Browse ...", None))
        self.label_4.setText(_translate("Dialog", "2nd shp", None))
        self.pushBrowseIn2.setText(_translate("Dialog", "Browse ...", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Output", None))
        self.radioTemp.setText(_translate("Dialog", "to temporary file", None))
        self.radioTofile.setText(_translate("Dialog", "to shp file", None))
        self.label_5.setText(_translate("Dialog", "Save to", None))
        self.pushBrowseOut.setText(_translate("Dialog", "Browse ...", None))

