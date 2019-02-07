from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import pyqtgraph as pg
import GCS_updateUI
import sys
import csv
import random
import numpy as np


class MainWindow(GCS_updateUI.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # changing background color (from image)
        self.centralwidget.setStyleSheet(".QWidget#centralwidget {background-image:url(\"background.png\"); background-position: center; }")
        # self.leftMenu.setStyleSheet("background-color:rgba(255,0,0,0.0); ")

        self.setWindowFlags(Qt.FramelessWindowHint)


        # setting icon pictures
        self.temp_img.setPixmap(QPixmap("icons/temp.png"))
        self.pres_img.setPixmap(QPixmap("icons/pressure.png"))
        self.gps_lat_img.setPixmap(QPixmap("icons/gps.png"))
        self.bot_img.setPixmap(QPixmap("icons/battery.png"))
        self.spin_img.setPixmap(QPixmap("icons/spin.png"))
        self.pitch_img.setPixmap(QPixmap("icons/pitch.png"))
        self.roll_img.setPixmap(QPixmap("icons/roll.png"))
        # self.logo.setPixmap(QPixmap("icons/logo.png"))

    #     # adding plot panel
    #
    #     # 1) getting plot items
    #     self.plt_tmp = self.pltPanel_tmp.getPlotItem()
    #     self.plt_pres = self.pltPanel_pres.getPlotItem()
    #     self.plt_gps = self.pltPanel_gps.getPlotItem()
    #     self.plt_bot = self.pltPanel_bot.getPlotItem()
    #     self.plt_spin = self.pltPanel_spin.getPlotItem()
    #     self.plt_pitchRoll = self.pltPanel_pitchRoll.getPlotItem()
    #
    #     # 2) adding curves to plots
    #     # self.curve_tmp = self.plt_tmp.plot()
    #     self.curve_tmp = pg.ScatterPlotItem(size=5, pen=pg.mkPen(255, 255, 255))  # todo scatter
    #     self.plt_tmp.addItem(self.curve_tmp)  # todo scatter
    #     self.curve_pres = self.plt_pres.plot()
    #     self.curve_gps = self.plt_gps.plot()
    #     self.curve_bot = self.plt_bot.plot()
    #     self.curve_spin = self.plt_spin.plot()
    #     self.curve_pitch = self.plt_pitchRoll.scatterPlot()
    #     self.curve_roll = self.plt_pitchRoll.scatterPlot()
    #     self.curve_pitch.setPen(pg.mkPen('y', width=3))
    #     self.curve_roll.setPen(pg.mkPen('r', width=3, style=Qt.DotLine))
    #     # 3) initializing plots
    #     zeroList = []
    #     for i in range(100):
    #         zeroList.append(0)
    #
    #     self.data_tmp = np.array(zeroList)
    #     self.data_pres = np.array(zeroList)
    #     self.data_gps = np.array(zeroList)
    #     self.data_bot = np.array(zeroList)
    #     self.data_spin = np.array(zeroList)
    #     self.data_pitch = np.array(zeroList)
    #     self.data_roll = np.array(zeroList)
    #
    #     # self.curve_tmp.setData(self.data_tmp)
    #     self.curve_tmp.addPoints(range(self.data_tmp.size), self.data_tmp)  # todo scatter
    #
    #     self.curve_pres.setData(self.data_pres)
    #     self.curve_gps.setData(self.data_gps)
    #     self.curve_bot.setData(self.data_bot)
    #     self.curve_spin.setData(self.data_spin)
    #     self.curve_pitch.setData(self.data_pitch)
    #     self.curve_roll.setData(self.data_roll)
    #
    #     # adding webPageView
    #     self.webView = QWebEngineView(self.map)
    #     self.webView.setUrl(QUrl('https://www.google.com/maps'))
    #     self.webView.setMinimumSize(300, 300)  # TODO
    #
    #     # connecting buttons signals
    #     self.resBtn.clicked.connect(self.randomGen)
    #
    #     self.i = 0  # todo scatter
    #
    # @pyqtSlot()
    # def randomGen(self):
    #     randomArray = np.random.randint(low=1, high=100, size=7)
    #     self.temp.setText(str(randomArray[0]) + ' °C')
    #     self.pres.setText(str(randomArray[1]) + ' Pa')
    #     self.gps.setText(str(randomArray[2]) + ' ')
    #     self.bot.setText(str(randomArray[3]) + ' V')
    #     self.spin.setText(str(randomArray[4]) + ' rpm')
    #     self.pitch.setText(str(randomArray[5]) + ' °')
    #     self.roll.setText(str(randomArray[6]) + ' °')
    #
    #     self.data_tmp[:-1] = self.data_tmp[1:]
    #     self.data_tmp[-1] = randomArray[0]
    #     self.data_pres[:-1] = self.data_pres[1:]
    #     self.data_pres[-1] = randomArray[1]
    #     self.data_gps[:-1] = self.data_gps[1:]
    #     self.data_gps[-1] = randomArray[2]
    #     self.data_bot[:-1] = self.data_bot[1:]
    #     self.data_bot[-1] = randomArray[3]
    #     self.data_spin[:-1] = self.data_spin[1:]
    #     self.data_spin[-1] = randomArray[4]
    #     self.data_pitch[:-1] = self.data_pitch[1:]
    #     self.data_pitch[-1] = randomArray[5]
    #     self.data_roll[:-1] = self.data_roll[1:]
    #     self.data_roll[-1] = randomArray[6]
    #
    #     # self.curve_tmp.setData(self.data_tmp)
    #     self.curve_tmp.addPoints([100 + self.i], [randomArray[0]])  # todo scatter
    #     self.i += 1  # todo scatter
    #     self.curve_pres.setData(self.data_pres)
    #     self.curve_gps.setData(self.data_gps)
    #     self.curve_bot.setData(self.data_bot)
    #     self.curve_spin.setData(self.data_spin)
    #     self.curve_pitch.setData(self.data_pitch)
    #     self.curve_roll.setData(self.data_roll)
    #
    #     with open('foo.csv', 'a') as csvFile:
    #         csvFile.write("\n")
    #         np.savetxt(csvFile, randomArray, fmt='%.1f', newline=',')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
