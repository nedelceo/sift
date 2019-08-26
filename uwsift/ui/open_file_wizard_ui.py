# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_file_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_openFileWizard(object):
    def setupUi(self, openFileWizard):
        openFileWizard.setObjectName("openFileWizard")
        openFileWizard.resize(599, 461)
        openFileWizard.setSizeGripEnabled(True)
        openFileWizard.setModal(True)
        openFileWizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        openFileWizard.setOptions(QtWidgets.QWizard.CancelButtonOnLeft)
        openFileWizard.setTitleFormat(QtCore.Qt.AutoText)
        openFileWizard.setSubTitleFormat(QtCore.Qt.AutoText)
        self.fileSelectionPage = AnyWizardPage()
        self.fileSelectionPage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fileSelectionPage.setObjectName("fileSelectionPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fileSelectionPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.readerLabel = QtWidgets.QLabel(self.fileSelectionPage)
        self.readerLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.readerLabel.setObjectName("readerLabel")
        self.horizontalLayout_3.addWidget(self.readerLabel)
        self.readerComboBox = QtWidgets.QComboBox(self.fileSelectionPage)
        self.readerComboBox.setObjectName("readerComboBox")
        self.horizontalLayout_3.addWidget(self.readerComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.inputFilesLabel = QtWidgets.QLabel(self.fileSelectionPage)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.inputFilesLabel.setFont(font)
        self.inputFilesLabel.setObjectName("inputFilesLabel")
        self.verticalLayout_3.addWidget(self.inputFilesLabel)
        self.fileList = QtWidgets.QListWidget(self.fileSelectionPage)
        self.fileList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.fileList.setObjectName("fileList")
        self.verticalLayout_3.addWidget(self.fileList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.fileSelectionPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(25, 25))
        self.addButton.setMaximumSize(QtCore.QSize(25, 25))
        self.addButton.setCheckable(False)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.removeButton = QtWidgets.QPushButton(self.fileSelectionPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setMinimumSize(QtCore.QSize(25, 25))
        self.removeButton.setMaximumSize(QtCore.QSize(25, 25))
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout.addWidget(self.removeButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        openFileWizard.addPage(self.fileSelectionPage)
        self.productSelectionPage = AnyWizardPage()
        self.productSelectionPage.setObjectName("productSelectionPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.productSelectionPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectIDTable = QtWidgets.QTableWidget(self.productSelectionPage)
        self.selectIDTable.setDragEnabled(False)
        self.selectIDTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.selectIDTable.setObjectName("selectIDTable")
        self.selectIDTable.setColumnCount(0)
        self.selectIDTable.setRowCount(0)
        self.verticalLayout.addWidget(self.selectIDTable)
        openFileWizard.addPage(self.productSelectionPage)

        self.retranslateUi(openFileWizard)
        QtCore.QMetaObject.connectSlotsByName(openFileWizard)

    def retranslateUi(self, openFileWizard):
        _translate = QtCore.QCoreApplication.translate
        openFileWizard.setWindowTitle(_translate("openFileWizard", "Open File Wizard"))
        self.fileSelectionPage.setTitle(_translate("openFileWizard", "Select Files"))
        self.fileSelectionPage.setSubTitle(_translate("openFileWizard", "Add data files to be opened"))
        self.readerLabel.setText(_translate("openFileWizard", "Reader:"))
        self.inputFilesLabel.setText(_translate("openFileWizard", "Input Files"))
        self.fileList.setSortingEnabled(True)
        self.addButton.setToolTip(_translate("openFileWizard", "Add files/dirs to list"))
        self.addButton.setText(_translate("openFileWizard", "+"))
        self.removeButton.setToolTip(_translate("openFileWizard", "Remove file from list"))
        self.removeButton.setText(_translate("openFileWizard", "-"))
        self.productSelectionPage.setTitle(_translate("openFileWizard", "Select Products"))
        self.productSelectionPage.setSubTitle(_translate("openFileWizard", "Select products to add"))
        self.selectIDTable.setSortingEnabled(False)

from uwsift.ui.custom_widgets import AnyWizardPage
