# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MDIMain_Layout.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        brush = QtGui.QBrush(QtGui.QColor(110, 115, 202))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1173, 19))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuReports = QtWidgets.QMenu(self.menuBar)
        self.menuReports.setObjectName("menuReports")
        self.menuWindows = QtWidgets.QMenu(self.menuBar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuMap = QtWidgets.QMenu(self.menuBar)
        self.menuMap.setObjectName("menuMap")
        self.menuLists = QtWidgets.QMenu(self.menuBar)
        self.menuLists.setObjectName("menuLists")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dckFilter = QtWidgets.QDockWidget(MainWindow)
        self.dckFilter.setMinimumSize(QtCore.QSize(86, 108))
        self.dckFilter.setBaseSize(QtCore.QSize(0, 0))
        self.dckFilter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dckFilter.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dckFilter.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dckFilter.setObjectName("dckFilter")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrFilter = QtWidgets.QScrollArea(self.dockWidgetContents)
        self.scrFilter.setMinimumSize(QtCore.QSize(0, 0))
        self.scrFilter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrFilter.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrFilter.setWidgetResizable(True)
        self.scrFilter.setObjectName("scrFilter")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 183, 865))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frmFilter = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frmFilter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmFilter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmFilter.setObjectName("frmFilter")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frmFilter)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblCountries = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCountries.setFont(font)
        self.lblCountries.setObjectName("lblCountries")
        self.verticalLayout.addWidget(self.lblCountries)
        self.cboCountries = QtWidgets.QComboBox(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboCountries.sizePolicy().hasHeightForWidth())
        self.cboCountries.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cboCountries.setFont(font)
        self.cboCountries.setObjectName("cboCountries")
        self.verticalLayout.addWidget(self.cboCountries)
        self.lblStates = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblStates.setFont(font)
        self.lblStates.setObjectName("lblStates")
        self.verticalLayout.addWidget(self.lblStates)
        self.cboStates = QtWidgets.QComboBox(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboStates.sizePolicy().hasHeightForWidth())
        self.cboStates.setSizePolicy(sizePolicy)
        self.cboStates.setObjectName("cboStates")
        self.verticalLayout.addWidget(self.cboStates)
        self.lblCounties = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCounties.setFont(font)
        self.lblCounties.setObjectName("lblCounties")
        self.verticalLayout.addWidget(self.lblCounties)
        self.cboCounties = QtWidgets.QComboBox(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboCounties.sizePolicy().hasHeightForWidth())
        self.cboCounties.setSizePolicy(sizePolicy)
        self.cboCounties.setObjectName("cboCounties")
        self.verticalLayout.addWidget(self.cboCounties)
        self.lblLocations = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLocations.setFont(font)
        self.lblLocations.setObjectName("lblLocations")
        self.verticalLayout.addWidget(self.lblLocations)
        self.cboLocations = QtWidgets.QComboBox(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboLocations.sizePolicy().hasHeightForWidth())
        self.cboLocations.setSizePolicy(sizePolicy)
        self.cboLocations.setObjectName("cboLocations")
        self.verticalLayout.addWidget(self.cboLocations)
        self.lblFamilies = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblFamilies.setFont(font)
        self.lblFamilies.setObjectName("lblFamilies")
        self.verticalLayout.addWidget(self.lblFamilies)
        self.cboFamilies = QtWidgets.QComboBox(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboFamilies.sizePolicy().hasHeightForWidth())
        self.cboFamilies.setSizePolicy(sizePolicy)
        self.cboFamilies.setObjectName("cboFamilies")
        self.verticalLayout.addWidget(self.cboFamilies)
        self.lblSpecies = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSpecies.setFont(font)
        self.lblSpecies.setObjectName("lblSpecies")
        self.verticalLayout.addWidget(self.lblSpecies)
        self.cboSpecies = QtWidgets.QComboBox(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboSpecies.sizePolicy().hasHeightForWidth())
        self.cboSpecies.setSizePolicy(sizePolicy)
        self.cboSpecies.setObjectName("cboSpecies")
        self.verticalLayout.addWidget(self.cboSpecies)
        self.lblEndSeasonalRange_2 = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblEndSeasonalRange_2.setFont(font)
        self.lblEndSeasonalRange_2.setObjectName("lblEndSeasonalRange_2")
        self.verticalLayout.addWidget(self.lblEndSeasonalRange_2)
        self.cboDateOptions = QtWidgets.QComboBox(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboDateOptions.sizePolicy().hasHeightForWidth())
        self.cboDateOptions.setSizePolicy(sizePolicy)
        self.cboDateOptions.setObjectName("cboDateOptions")
        self.verticalLayout.addWidget(self.cboDateOptions)
        self.lblStartDate = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblStartDate.setFont(font)
        self.lblStartDate.setObjectName("lblStartDate")
        self.verticalLayout.addWidget(self.lblStartDate)
        self.calStartDate = QtWidgets.QDateTimeEdit(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calStartDate.sizePolicy().hasHeightForWidth())
        self.calStartDate.setSizePolicy(sizePolicy)
        self.calStartDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 2, 1), QtCore.QTime(0, 0, 0)))
        self.calStartDate.setCalendarPopup(True)
        self.calStartDate.setObjectName("calStartDate")
        self.verticalLayout.addWidget(self.calStartDate)
        self.lblEndDate = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblEndDate.setFont(font)
        self.lblEndDate.setObjectName("lblEndDate")
        self.verticalLayout.addWidget(self.lblEndDate)
        self.calEndDate = QtWidgets.QDateTimeEdit(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calEndDate.sizePolicy().hasHeightForWidth())
        self.calEndDate.setSizePolicy(sizePolicy)
        self.calEndDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 2, 1), QtCore.QTime(0, 0, 0)))
        self.calEndDate.setCalendarPopup(True)
        self.calEndDate.setObjectName("calEndDate")
        self.verticalLayout.addWidget(self.calEndDate)
        self.lblEndSeasonalRange_3 = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblEndSeasonalRange_3.setFont(font)
        self.lblEndSeasonalRange_3.setObjectName("lblEndSeasonalRange_3")
        self.verticalLayout.addWidget(self.lblEndSeasonalRange_3)
        self.cboSeasonalRangeOptions = QtWidgets.QComboBox(self.frmFilter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboSeasonalRangeOptions.sizePolicy().hasHeightForWidth())
        self.cboSeasonalRangeOptions.setSizePolicy(sizePolicy)
        self.cboSeasonalRangeOptions.setObjectName("cboSeasonalRangeOptions")
        self.verticalLayout.addWidget(self.cboSeasonalRangeOptions)
        self.lblStartSeasonalRange = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblStartSeasonalRange.setFont(font)
        self.lblStartSeasonalRange.setObjectName("lblStartSeasonalRange")
        self.verticalLayout.addWidget(self.lblStartSeasonalRange)
        self.frmStartSeasonalRange = QtWidgets.QFrame(self.frmFilter)
        self.frmStartSeasonalRange.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmStartSeasonalRange.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmStartSeasonalRange.setLineWidth(0)
        self.frmStartSeasonalRange.setObjectName("frmStartSeasonalRange")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frmStartSeasonalRange)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cboStartSeasonalRangeMonth = QtWidgets.QComboBox(self.frmStartSeasonalRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboStartSeasonalRangeMonth.sizePolicy().hasHeightForWidth())
        self.cboStartSeasonalRangeMonth.setSizePolicy(sizePolicy)
        self.cboStartSeasonalRangeMonth.setObjectName("cboStartSeasonalRangeMonth")
        self.horizontalLayout.addWidget(self.cboStartSeasonalRangeMonth)
        self.cboStartSeasonalRangeDate = QtWidgets.QComboBox(self.frmStartSeasonalRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboStartSeasonalRangeDate.sizePolicy().hasHeightForWidth())
        self.cboStartSeasonalRangeDate.setSizePolicy(sizePolicy)
        self.cboStartSeasonalRangeDate.setObjectName("cboStartSeasonalRangeDate")
        self.horizontalLayout.addWidget(self.cboStartSeasonalRangeDate)
        self.verticalLayout.addWidget(self.frmStartSeasonalRange)
        self.lblEndSeasonalRange = QtWidgets.QLabel(self.frmFilter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblEndSeasonalRange.setFont(font)
        self.lblEndSeasonalRange.setObjectName("lblEndSeasonalRange")
        self.verticalLayout.addWidget(self.lblEndSeasonalRange)
        self.frmEndSeasonalRange = QtWidgets.QFrame(self.frmFilter)
        self.frmEndSeasonalRange.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmEndSeasonalRange.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frmEndSeasonalRange.setLineWidth(0)
        self.frmEndSeasonalRange.setObjectName("frmEndSeasonalRange")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frmEndSeasonalRange)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cboEndSeasonalRangeMonth = QtWidgets.QComboBox(self.frmEndSeasonalRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboEndSeasonalRangeMonth.sizePolicy().hasHeightForWidth())
        self.cboEndSeasonalRangeMonth.setSizePolicy(sizePolicy)
        self.cboEndSeasonalRangeMonth.setObjectName("cboEndSeasonalRangeMonth")
        self.horizontalLayout_2.addWidget(self.cboEndSeasonalRangeMonth)
        self.cboEndSeasonalRangeDate = QtWidgets.QComboBox(self.frmEndSeasonalRange)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboEndSeasonalRangeDate.sizePolicy().hasHeightForWidth())
        self.cboEndSeasonalRangeDate.setSizePolicy(sizePolicy)
        self.cboEndSeasonalRangeDate.setObjectName("cboEndSeasonalRangeDate")
        self.horizontalLayout_2.addWidget(self.cboEndSeasonalRangeDate)
        self.verticalLayout.addWidget(self.frmEndSeasonalRange)
        self.verticalLayout_2.addWidget(self.frmFilter)
        self.scrFilter.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrFilter)
        self.dckFilter.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dckFilter)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDateTotals = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon_datetotals.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDateTotals.setIcon(icon1)
        self.actionDateTotals.setObjectName("actionDateTotals")
        self.actionLocationTotals = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon_locationtotals.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLocationTotals.setIcon(icon2)
        self.actionLocationTotals.setObjectName("actionLocationTotals")
        self.actionCascadeWindows = QtWidgets.QAction(MainWindow)
        self.actionCascadeWindows.setObjectName("actionCascadeWindows")
        self.actionTileWindows = QtWidgets.QAction(MainWindow)
        self.actionTileWindows.setObjectName("actionTileWindows")
        self.actionCloseAllWindows = QtWidgets.QAction(MainWindow)
        self.actionCloseAllWindows.setObjectName("actionCloseAllWindows")
        self.actionCompareLists = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon_compare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompareLists.setIcon(icon3)
        self.actionCompareLists.setObjectName("actionCompareLists")
        self.actionCascade = QtWidgets.QAction(MainWindow)
        self.actionCascade.setObjectName("actionCascade")
        self.actionSpecies = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon_bird.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSpecies.setIcon(icon4)
        self.actionSpecies.setObjectName("actionSpecies")
        self.actionLocations = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon_location.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLocations.setIcon(icon5)
        self.actionLocations.setObjectName("actionLocations")
        self.actionChecklists = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon_checklists.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChecklists.setIcon(icon6)
        self.actionChecklists.setObjectName("actionChecklists")
        self.actionBigReport = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon_tripreport.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBigReport.setIcon(icon7)
        self.actionBigReport.setObjectName("actionBigReport")
        self.actionFind = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon_find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon8)
        self.actionFind.setObjectName("actionFind")
        self.actionFamilies = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon_families.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFamilies.setIcon(icon9)
        self.actionFamilies.setObjectName("actionFamilies")
        self.actionMap = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon_map.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMap.setIcon(icon10)
        self.actionMap.setObjectName("actionMap")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuReports.addAction(self.actionDateTotals)
        self.menuReports.addAction(self.actionLocationTotals)
        self.menuReports.addAction(self.actionCompareLists)
        self.menuReports.addAction(self.actionBigReport)
        self.menuWindows.addAction(self.actionTileWindows)
        self.menuWindows.addAction(self.actionCascade)
        self.menuWindows.addAction(self.actionCloseAllWindows)
        self.menuMap.addAction(self.actionMap)
        self.menuLists.addAction(self.actionSpecies)
        self.menuLists.addAction(self.actionLocations)
        self.menuLists.addAction(self.actionChecklists)
        self.menuLists.addAction(self.actionFamilies)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuLists.menuAction())
        self.menuBar.addAction(self.menuMap.menuAction())
        self.menuBar.addAction(self.menuReports.menuAction())
        self.menuBar.addAction(self.menuWindows.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSpecies)
        self.toolBar.addAction(self.actionLocations)
        self.toolBar.addAction(self.actionChecklists)
        self.toolBar.addAction(self.actionMap)
        self.toolBar.addAction(self.actionFamilies)
        self.toolBar.addAction(self.actionDateTotals)
        self.toolBar.addAction(self.actionLocationTotals)
        self.toolBar.addAction(self.actionCompareLists)
        self.toolBar.addAction(self.actionBigReport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFind)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "eBird Analyzer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuReports.setTitle(_translate("MainWindow", "Reports"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuMap.setTitle(_translate("MainWindow", "Map"))
        self.menuLists.setTitle(_translate("MainWindow", "Lists"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.dckFilter.setWindowTitle(_translate("MainWindow", "Filter"))
        self.lblCountries.setText(_translate("MainWindow", "Countries"))
        self.lblStates.setText(_translate("MainWindow", "States"))
        self.lblCounties.setText(_translate("MainWindow", "Counties"))
        self.lblLocations.setText(_translate("MainWindow", "Locations"))
        self.lblFamilies.setText(_translate("MainWindow", "Families"))
        self.lblSpecies.setText(_translate("MainWindow", "Species"))
        self.lblEndSeasonalRange_2.setText(_translate("MainWindow", "Date Options"))
        self.lblStartDate.setText(_translate("MainWindow", "Start Date"))
        self.calStartDate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.lblEndDate.setText(_translate("MainWindow", "End Date"))
        self.calEndDate.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.lblEndSeasonalRange_3.setText(_translate("MainWindow", "Seasonal Range Options"))
        self.lblStartSeasonalRange.setText(_translate("MainWindow", "Start Seasonal Range"))
        self.lblEndSeasonalRange.setText(_translate("MainWindow", "End Seasonal Range"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDateTotals.setText(_translate("MainWindow", "Date Totals"))
        self.actionLocationTotals.setText(_translate("MainWindow", "Location Totals"))
        self.actionCascadeWindows.setText(_translate("MainWindow", "Cascade Windows"))
        self.actionTileWindows.setText(_translate("MainWindow", "Tile Windows"))
        self.actionCloseAllWindows.setText(_translate("MainWindow", "Close All Windows"))
        self.actionCompareLists.setText(_translate("MainWindow", "Compare Lists"))
        self.actionCascade.setText(_translate("MainWindow", "Cascade Windows"))
        self.actionSpecies.setText(_translate("MainWindow", "Species"))
        self.actionLocations.setText(_translate("MainWindow", "Locations"))
        self.actionChecklists.setText(_translate("MainWindow", "Checklists"))
        self.actionBigReport.setText(_translate("MainWindow", "Big Report"))
        self.actionBigReport.setToolTip(_translate("MainWindow", "Big Report"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFamilies.setText(_translate("MainWindow", "Families"))
        self.actionMap.setText(_translate("MainWindow", "Map"))

import icons_rc