from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout

import pyqtgraph as pg
import numpy as np


class ChaosWindow(QMainWindow):

    def __init__(self, init_points, n_new_points=10000, speed=10):
        super().__init__()

        self.freq = 1000 // speed
        self.init_points = init_points
        self.n_points = 0
        self.n_new_points = n_new_points

        # Add Timer for displaying and saving data
        self.displayTimer = QtCore.QTimer()
        self.displayTimer.timeout.connect(self.update_plot)

        # setting title
        self.setWindowTitle("Game of Chaos")

        # setting geometry
        self.setGeometry(100, 100, 800, 800)

        # icon
        icon = QIcon("fern_icon.png")

        # setting icon to the window
        self.setWindowIcon(icon)

        # initialising plot
        self.init_points = init_points
        self.scatter = self.init_plot(init_points=self.init_points)

        # showing all the widgets
        self.show()

        # start the display timer
        self.displayTimer.start(self.freq)

    def init_plot(self, init_points):
        # creating a widget object
        widget = QWidget()

        # creating a label
        label = QLabel("Triangle start")
        label.setWordWrap(True)
        label.setMinimumWidth(130)

        # creating a plot window
        plot = pg.plot()
        plot.getPlotItem().hideAxis('left')
        plot.getPlotItem().hideAxis('bottom')

        # creating a scatter plot item
        scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(0, 255, 0, 255))

        # adding points to the scatter plot
        points = [{'pos': init_points[i, :], 'data': 1} for i in range(len(init_points))]
        self.n_points = len(init_points)

        scatter.addPoints(points)
        plot.addItem(scatter)
        plot.setXRange(-1., 1., padding=0.2)
        plot.setYRange(-1., 1., padding=0.2)

        # Creating a grid layout
        layout = QGridLayout()
        widget.setLayout(layout)

        layout.addWidget(label, 1, 0)
        layout.addWidget(plot, 0, 1, 3, 1)

        # setting this widget as central widget of the main widow
        self.setCentralWidget(widget)

        return scatter

    def update_plot(self):
        new_point = np.random.uniform(low=-1., high=1., size=(2,))  # TODO: replace that with loop and logic for chaos game
        self.scatter.addPoints([{'pos': new_point, 'data': 1}])
        self.n_points += 1

        return
