# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GCS.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1080, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        mainWindow.setMaximumSize(QtCore.QSize(1086, 721))
        font = QtGui.QFont()
        font.setFamily("Arial")
        mainWindow.setFont(font)
        mainWindow.setMouseTracking(False)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet("\n"
"QWidget#centralwidget{\n"
"    background-color: rgb(17, 41, 79);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgba(17, 41, 79,0.5);\n"
"    color: rgb(238,238,238)\n"
"}")
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temp_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp_img.sizePolicy().hasHeightForWidth())
        self.temp_img.setSizePolicy(sizePolicy)
        self.temp_img.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.temp_img.setFont(font)
        self.temp_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.temp_img.setObjectName("temp_img")
        self.horizontalLayout.addWidget(self.temp_img)
        self.temp = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp.sizePolicy().hasHeightForWidth())
        self.temp.setSizePolicy(sizePolicy)
        self.temp.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.temp.setFont(font)
        self.temp.setStyleSheet("color: rgb(238, 238, 238);")
        self.temp.setTextFormat(QtCore.Qt.AutoText)
        self.temp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.temp.setObjectName("temp")
        self.horizontalLayout.addWidget(self.temp)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pres_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pres_img.sizePolicy().hasHeightForWidth())
        self.pres_img.setSizePolicy(sizePolicy)
        self.pres_img.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pres_img.setFont(font)
        self.pres_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pres_img.setObjectName("pres_img")
        self.horizontalLayout_3.addWidget(self.pres_img)
        self.pres = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pres.sizePolicy().hasHeightForWidth())
        self.pres.setSizePolicy(sizePolicy)
        self.pres.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pres.setFont(font)
        self.pres.setStyleSheet("color: rgb(238, 238, 238);")
        self.pres.setTextFormat(QtCore.Qt.AutoText)
        self.pres.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pres.setObjectName("pres")
        self.horizontalLayout_3.addWidget(self.pres)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gps_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gps_img.sizePolicy().hasHeightForWidth())
        self.gps_img.setSizePolicy(sizePolicy)
        self.gps_img.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gps_img.setFont(font)
        self.gps_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gps_img.setObjectName("gps_img")
        self.horizontalLayout_5.addWidget(self.gps_img)
        self.gps = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gps.sizePolicy().hasHeightForWidth())
        self.gps.setSizePolicy(sizePolicy)
        self.gps.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.gps.setFont(font)
        self.gps.setStyleSheet("color: rgb(238, 238, 238);")
        self.gps.setTextFormat(QtCore.Qt.AutoText)
        self.gps.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gps.setObjectName("gps")
        self.horizontalLayout_5.addWidget(self.gps)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bot_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_img.sizePolicy().hasHeightForWidth())
        self.bot_img.setSizePolicy(sizePolicy)
        self.bot_img.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bot_img.setFont(font)
        self.bot_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bot_img.setObjectName("bot_img")
        self.horizontalLayout_6.addWidget(self.bot_img)
        self.bot = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot.sizePolicy().hasHeightForWidth())
        self.bot.setSizePolicy(sizePolicy)
        self.bot.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.bot.setFont(font)
        self.bot.setStyleSheet("color: rgb(238, 238, 238);")
        self.bot.setTextFormat(QtCore.Qt.AutoText)
        self.bot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bot.setObjectName("bot")
        self.horizontalLayout_6.addWidget(self.bot)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.spin_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_img.sizePolicy().hasHeightForWidth())
        self.spin_img.setSizePolicy(sizePolicy)
        self.spin_img.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spin_img.setFont(font)
        self.spin_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spin_img.setObjectName("spin_img")
        self.horizontalLayout_7.addWidget(self.spin_img)
        self.spin = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin.sizePolicy().hasHeightForWidth())
        self.spin.setSizePolicy(sizePolicy)
        self.spin.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.spin.setFont(font)
        self.spin.setStyleSheet("color: rgb(238, 238, 238);")
        self.spin.setTextFormat(QtCore.Qt.AutoText)
        self.spin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spin.setObjectName("spin")
        self.horizontalLayout_7.addWidget(self.spin)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pitch_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pitch_img.sizePolicy().hasHeightForWidth())
        self.pitch_img.setSizePolicy(sizePolicy)
        self.pitch_img.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pitch_img.setFont(font)
        self.pitch_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pitch_img.setObjectName("pitch_img")
        self.horizontalLayout_8.addWidget(self.pitch_img)
        self.pitch = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pitch.sizePolicy().hasHeightForWidth())
        self.pitch.setSizePolicy(sizePolicy)
        self.pitch.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pitch.setFont(font)
        self.pitch.setStyleSheet("color: rgb(238, 238, 238);")
        self.pitch.setTextFormat(QtCore.Qt.AutoText)
        self.pitch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pitch.setObjectName("pitch")
        self.horizontalLayout_8.addWidget(self.pitch)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.roll_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roll_img.sizePolicy().hasHeightForWidth())
        self.roll_img.setSizePolicy(sizePolicy)
        self.roll_img.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.roll_img.setFont(font)
        self.roll_img.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.roll_img.setObjectName("roll_img")
        self.horizontalLayout_4.addWidget(self.roll_img)
        self.roll = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roll.sizePolicy().hasHeightForWidth())
        self.roll.setSizePolicy(sizePolicy)
        self.roll.setMinimumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.roll.setFont(font)
        self.roll.setStyleSheet("color: rgb(238, 238, 238);")
        self.roll.setTextFormat(QtCore.Qt.AutoText)
        self.roll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.roll.setObjectName("roll")
        self.horizontalLayout_4.addWidget(self.roll)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(200, 120))
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(700, 560))
        self.tabWidget.setObjectName("tabWidget")
        self.plots = QtWidgets.QWidget()
        self.plots.setObjectName("plots")
        self.layoutWidget = QtWidgets.QWidget(self.plots)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 691, 532))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pltPanel_tmp = PlotWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(233)
        sizePolicy.setVerticalStretch(186)
        sizePolicy.setHeightForWidth(self.pltPanel_tmp.sizePolicy().hasHeightForWidth())
        self.pltPanel_tmp.setSizePolicy(sizePolicy)
        self.pltPanel_tmp.setMinimumSize(QtCore.QSize(233, 170))
        self.pltPanel_tmp.setObjectName("pltPanel_tmp")
        self.gridLayout.addWidget(self.pltPanel_tmp, 0, 0, 1, 1)
        self.pltPanel_pitchRoll = PlotWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(233)
        sizePolicy.setVerticalStretch(186)
        sizePolicy.setHeightForWidth(self.pltPanel_pitchRoll.sizePolicy().hasHeightForWidth())
        self.pltPanel_pitchRoll.setSizePolicy(sizePolicy)
        self.pltPanel_pitchRoll.setMinimumSize(QtCore.QSize(233, 170))
        self.pltPanel_pitchRoll.setObjectName("pltPanel_pitchRoll")
        self.gridLayout.addWidget(self.pltPanel_pitchRoll, 2, 0, 1, 1)
        self.pltPanel_gps = PlotWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(233)
        sizePolicy.setVerticalStretch(186)
        sizePolicy.setHeightForWidth(self.pltPanel_gps.sizePolicy().hasHeightForWidth())
        self.pltPanel_gps.setSizePolicy(sizePolicy)
        self.pltPanel_gps.setMinimumSize(QtCore.QSize(233, 170))
        self.pltPanel_gps.setObjectName("pltPanel_gps")
        self.gridLayout.addWidget(self.pltPanel_gps, 1, 0, 1, 1)
        self.pltPanel_spin = PlotWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(233)
        sizePolicy.setVerticalStretch(186)
        sizePolicy.setHeightForWidth(self.pltPanel_spin.sizePolicy().hasHeightForWidth())
        self.pltPanel_spin.setSizePolicy(sizePolicy)
        self.pltPanel_spin.setMinimumSize(QtCore.QSize(233, 170))
        self.pltPanel_spin.setObjectName("pltPanel_spin")
        self.gridLayout.addWidget(self.pltPanel_spin, 2, 1, 1, 1)
        self.pltPanel_bot = PlotWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(233)
        sizePolicy.setVerticalStretch(186)
        sizePolicy.setHeightForWidth(self.pltPanel_bot.sizePolicy().hasHeightForWidth())
        self.pltPanel_bot.setSizePolicy(sizePolicy)
        self.pltPanel_bot.setMinimumSize(QtCore.QSize(233, 170))
        self.pltPanel_bot.setObjectName("pltPanel_bot")
        self.gridLayout.addWidget(self.pltPanel_bot, 1, 1, 1, 1)
        self.pltPanel_pres = PlotWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(233)
        sizePolicy.setVerticalStretch(186)
        sizePolicy.setHeightForWidth(self.pltPanel_pres.sizePolicy().hasHeightForWidth())
        self.pltPanel_pres.setSizePolicy(sizePolicy)
        self.pltPanel_pres.setMinimumSize(QtCore.QSize(233, 170))
        self.pltPanel_pres.setObjectName("pltPanel_pres")
        self.gridLayout.addWidget(self.pltPanel_pres, 0, 1, 1, 1)
        self.tabWidget.addTab(self.plots, "")
        self.map = QtWidgets.QWidget()
        self.map.setObjectName("map")
        self.tabWidget.addTab(self.map, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.brate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.brate.setFont(font)
        self.brate.setStyleSheet("color: rgb(238, 238, 238);")
        self.brate.setObjectName("brate")
        self.horizontalLayout_9.addWidget(self.brate)
        self.brate_input = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.brate_input.setFont(font)
        self.brate_input.setObjectName("brate_input")
        self.horizontalLayout_9.addWidget(self.brate_input)
        self.cnctBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cnctBtn.setObjectName("cnctBtn")
        self.horizontalLayout_9.addWidget(self.cnctBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem8)
        self.resBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resBtn.sizePolicy().hasHeightForWidth())
        self.resBtn.setSizePolicy(sizePolicy)
        self.resBtn.setMinimumSize(QtCore.QSize(140, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.resBtn.setFont(font)
        self.resBtn.setObjectName("resBtn")
        self.verticalLayout_3.addWidget(self.resBtn)
        self.calBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calBtn.sizePolicy().hasHeightForWidth())
        self.calBtn.setSizePolicy(sizePolicy)
        self.calBtn.setMinimumSize(QtCore.QSize(140, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.calBtn.setFont(font)
        self.calBtn.setObjectName("calBtn")
        self.verticalLayout_3.addWidget(self.calBtn)
        self.parBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parBtn.sizePolicy().hasHeightForWidth())
        self.parBtn.setSizePolicy(sizePolicy)
        self.parBtn.setMinimumSize(QtCore.QSize(140, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.parBtn.setFont(font)
        self.parBtn.setObjectName("parBtn")
        self.verticalLayout_3.addWidget(self.parBtn)
        self.alarmBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alarmBtn.sizePolicy().hasHeightForWidth())
        self.alarmBtn.setSizePolicy(sizePolicy)
        self.alarmBtn.setMinimumSize(QtCore.QSize(140, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.alarmBtn.setFont(font)
        self.alarmBtn.setObjectName("alarmBtn")
        self.verticalLayout_3.addWidget(self.alarmBtn)
        self.relBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.relBtn.sizePolicy().hasHeightForWidth())
        self.relBtn.setSizePolicy(sizePolicy)
        self.relBtn.setMinimumSize(QtCore.QSize(140, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.relBtn.setFont(font)
        self.relBtn.setObjectName("relBtn")
        self.verticalLayout_3.addWidget(self.relBtn)
        spacerItem9 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem9)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "SATAUT Ground Station"))
        self.temp_img.setText(_translate("mainWindow", "0"))
        self.temp.setText(_translate("mainWindow", "0"))
        self.pres_img.setText(_translate("mainWindow", "0"))
        self.pres.setText(_translate("mainWindow", "0"))
        self.gps_img.setText(_translate("mainWindow", "0"))
        self.gps.setText(_translate("mainWindow", "0"))
        self.bot_img.setText(_translate("mainWindow", "0"))
        self.bot.setText(_translate("mainWindow", "0"))
        self.spin_img.setText(_translate("mainWindow", "0"))
        self.spin.setText(_translate("mainWindow", "0"))
        self.pitch_img.setText(_translate("mainWindow", "0"))
        self.pitch.setText(_translate("mainWindow", "0"))
        self.roll_img.setText(_translate("mainWindow", "0"))
        self.roll.setText(_translate("mainWindow", "0"))
        self.logo.setText(_translate("mainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plots), _translate("mainWindow", "Plots"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.map), _translate("mainWindow", "Map"))
        self.brate.setText(_translate("mainWindow", "B-rate:"))
        self.cnctBtn.setText(_translate("mainWindow", "Connect"))
        self.resBtn.setText(_translate("mainWindow", "Reset"))
        self.calBtn.setText(_translate("mainWindow", "Calibrate"))
        self.parBtn.setText(_translate("mainWindow", "Parachute"))
        self.alarmBtn.setText(_translate("mainWindow", "Alarm"))
        self.relBtn.setText(_translate("mainWindow", "Release"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

