# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pov_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1397, 800)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.panZoomToolButton = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panZoomToolButton.sizePolicy().hasHeightForWidth())
        self.panZoomToolButton.setSizePolicy(sizePolicy)
        self.panZoomToolButton.setMinimumSize(QtCore.QSize(0, 0))
        self.panZoomToolButton.setCheckable(True)
        self.panZoomToolButton.setChecked(True)
        self.panZoomToolButton.setAutoExclusive(False)
        self.panZoomToolButton.setAutoRaise(False)
        self.panZoomToolButton.setObjectName(_fromUtf8("panZoomToolButton"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.panZoomToolButton)
        self.horizontalLayout_2.addWidget(self.panZoomToolButton)
        self.pointSelectButton = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointSelectButton.sizePolicy().hasHeightForWidth())
        self.pointSelectButton.setSizePolicy(sizePolicy)
        self.pointSelectButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pointSelectButton.setCheckable(True)
        self.pointSelectButton.setObjectName(_fromUtf8("pointSelectButton"))
        self.buttonGroup.addButton(self.pointSelectButton)
        self.horizontalLayout_2.addWidget(self.pointSelectButton)
        self.regionSelectButton = QtGui.QToolButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regionSelectButton.sizePolicy().hasHeightForWidth())
        self.regionSelectButton.setSizePolicy(sizePolicy)
        self.regionSelectButton.setCheckable(True)
        self.regionSelectButton.setObjectName(_fromUtf8("regionSelectButton"))
        self.buttonGroup.addButton(self.regionSelectButton)
        self.horizontalLayout_2.addWidget(self.regionSelectButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cursorProbeLocation = QtGui.QLabel(self.centralwidget)
        self.cursorProbeLocation.setMinimumSize(QtCore.QSize(280, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.cursorProbeLocation.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andale Mono"))
        font.setPointSize(14)
        self.cursorProbeLocation.setFont(font)
        self.cursorProbeLocation.setObjectName(_fromUtf8("cursorProbeLocation"))
        self.horizontalLayout_2.addWidget(self.cursorProbeLocation)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.cursorProbeText = QtGui.QLabel(self.centralwidget)
        self.cursorProbeText.setMinimumSize(QtCore.QSize(280, 0))
        self.cursorProbeText.setMaximumSize(QtCore.QSize(256, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 71, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.cursorProbeText.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andale Mono"))
        font.setPointSize(14)
        self.cursorProbeText.setFont(font)
        self.cursorProbeText.setObjectName(_fromUtf8("cursorProbeText"))
        self.horizontalLayout_2.addWidget(self.cursorProbeText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.mainWidgets = QtGui.QTabWidget(self.centralwidget)
        self.mainWidgets.setObjectName(_fromUtf8("mainWidgets"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.mainWidgets.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.mainWidgets.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mainWidgets)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.progressText = QtGui.QLabel(self.groupBox)
        self.progressText.setMinimumSize(QtCore.QSize(240, 0))
        self.progressText.setMaximumSize(QtCore.QSize(256, 16777215))
        self.progressText.setAlignment(QtCore.Qt.AlignCenter)
        self.progressText.setObjectName(_fromUtf8("progressText"))
        self.verticalLayout_10.addWidget(self.progressText)
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setMaximumSize(QtCore.QSize(256, 16777215))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_10.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.animationLabel = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andale Mono"))
        font.setPointSize(14)
        self.animationLabel.setFont(font)
        self.animationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.animationLabel.setObjectName(_fromUtf8("animationLabel"))
        self.verticalLayout_11.addWidget(self.animationLabel)
        self.animationSlider = QtGui.QSlider(self.groupBox)
        self.animationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.animationSlider.setObjectName(_fromUtf8("animationSlider"))
        self.verticalLayout_11.addWidget(self.animationSlider)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.animBack = QtGui.QToolButton(self.groupBox)
        self.animBack.setToolTip(_fromUtf8(""))
        self.animBack.setObjectName(_fromUtf8("animBack"))
        self.horizontalLayout.addWidget(self.animBack)
        self.animPlayPause = QtGui.QToolButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Andale Mono"))
        font.setPointSize(18)
        font.setItalic(False)
        self.animPlayPause.setFont(font)
        self.animPlayPause.setObjectName(_fromUtf8("animPlayPause"))
        self.horizontalLayout.addWidget(self.animPlayPause)
        self.animForward = QtGui.QToolButton(self.groupBox)
        self.animForward.setObjectName(_fromUtf8("animForward"))
        self.horizontalLayout.addWidget(self.animForward)
        self.verticalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1397, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.areaProbePane = QtGui.QDockWidget(MainWindow)
        self.areaProbePane.setObjectName(_fromUtf8("areaProbePane"))
        self.probeWidget = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probeWidget.sizePolicy().hasHeightForWidth())
        self.probeWidget.setSizePolicy(sizePolicy)
        self.probeWidget.setObjectName(_fromUtf8("probeWidget"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.probeWidget)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.probeTabWidget = QtGui.QTabWidget(self.probeWidget)
        self.probeTabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.probeTabWidget.setObjectName(_fromUtf8("probeTabWidget"))
        self.tab_plus = QtGui.QWidget()
        self.tab_plus.setObjectName(_fromUtf8("tab_plus"))
        self.probeTabWidget.addTab(self.tab_plus, _fromUtf8(""))
        self.verticalLayout_12.addWidget(self.probeTabWidget)
        self.areaProbePane.setWidget(self.probeWidget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.areaProbePane)
        self.layersPane = QtGui.QDockWidget(MainWindow)
        self.layersPane.setObjectName(_fromUtf8("layersPane"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.layerSetTabs = QtGui.QTabWidget(self.dockWidgetContents_5)
        self.layerSetTabs.setMinimumSize(QtCore.QSize(160, 0))
        self.layerSetTabs.setObjectName(_fromUtf8("layerSetTabs"))
        self.tab_plusL = QtGui.QWidget()
        self.tab_plusL.setObjectName(_fromUtf8("tab_plusL"))
        self.layerSetTabs.addTab(self.tab_plusL, _fromUtf8(""))
        self.verticalLayout.addWidget(self.layerSetTabs)
        self.layersPane.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.layersPane)
        self.layerConfigPane = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerConfigPane.sizePolicy().hasHeightForWidth())
        self.layerConfigPane.setSizePolicy(sizePolicy)
        self.layerConfigPane.setObjectName(_fromUtf8("layerConfigPane"))
        self.layerInfoContents = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerInfoContents.sizePolicy().hasHeightForWidth())
        self.layerInfoContents.setSizePolicy(sizePolicy)
        self.layerInfoContents.setObjectName(_fromUtf8("layerInfoContents"))
        self.layerConfigPane.setWidget(self.layerInfoContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.layerConfigPane)

        self.retranslateUi(MainWindow)
        self.mainWidgets.setCurrentIndex(0)
        self.probeTabWidget.setCurrentIndex(0)
        self.layerSetTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SIFT Beta 0.7.4", None))
        self.panZoomToolButton.setToolTip(_translate("MainWindow", "Pan/Zoom Tool", None))
        self.panZoomToolButton.setStatusTip(_translate("MainWindow", "Left mouse click and drag pans the scene", None))
        self.panZoomToolButton.setText(_translate("MainWindow", "Pan/Zoom", None))
        self.pointSelectButton.setToolTip(_translate("MainWindow", "Point Probe Tool", None))
        self.pointSelectButton.setStatusTip(_translate("MainWindow", "Left mouse click probes a single point in the scene", None))
        self.pointSelectButton.setText(_translate("MainWindow", "Point", None))
        self.regionSelectButton.setToolTip(_translate("MainWindow", "Region Probe Tool", None))
        self.regionSelectButton.setStatusTip(_translate("MainWindow", "Left mouse click creates a polygon vertex (click initial vertex to complete)", None))
        self.regionSelectButton.setText(_translate("MainWindow", "Region", None))
        self.cursorProbeLocation.setToolTip(_translate("MainWindow", "Longitude/Latitude location of point probe", None))
        self.cursorProbeLocation.setStatusTip(_translate("MainWindow", "Longitude/Latitude coordinates under point probe", None))
        self.cursorProbeLocation.setText(_translate("MainWindow", "Probe Location: ", None))
        self.cursorProbeText.setToolTip(_translate("MainWindow", "Value under cursor", None))
        self.cursorProbeText.setStatusTip(_translate("MainWindow", "Top layer data value under point probe", None))
        self.cursorProbeText.setText(_translate("MainWindow", "Probe Value:", None))
        self.mainWidgets.setTabText(self.mainWidgets.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.mainWidgets.setTabText(self.mainWidgets.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.progressText.setText(_translate("MainWindow", "idle", None))
        self.progressBar.setToolTip(_translate("MainWindow", "Activity Progress", None))
        self.animationLabel.setText(_translate("MainWindow", "HH:MM", None))
        self.animBack.setStatusTip(_translate("MainWindow", "Step backward", None))
        self.animBack.setText(_translate("MainWindow", "|◀", None))
        self.animPlayPause.setStatusTip(_translate("MainWindow", "Start or stop animation", None))
        self.animPlayPause.setText(_translate("MainWindow", "▶", None))
        self.animForward.setStatusTip(_translate("MainWindow", "Step forward", None))
        self.animForward.setText(_translate("MainWindow", "▶|", None))
        self.areaProbePane.setWindowTitle(_translate("MainWindow", "Area Probe Graphs", None))
        self.probeTabWidget.setTabText(self.probeTabWidget.indexOf(self.tab_plus), _translate("MainWindow", "+", None))
        self.layersPane.setWindowTitle(_translate("MainWindow", "Layers", None))
        self.layerSetTabs.setToolTip(_translate("MainWindow", "Alternate layer sets", None))
        self.layerSetTabs.setStatusTip(_translate("MainWindow", "Select alternate layer set", None))
        self.layerSetTabs.setTabText(self.layerSetTabs.indexOf(self.tab_plusL), _translate("MainWindow", "+", None))
        self.layerConfigPane.setStatusTip(_translate("MainWindow", "Selected layer information", None))
        self.layerConfigPane.setWindowTitle(_translate("MainWindow", "Layer Details", None))

