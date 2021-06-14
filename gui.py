from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout

import pyqtgraph as pg
import numpy as np


class ChaosWindow(QMainWindow):

    def __init__(self, init_points):
        super().__init__()

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

        # TODO: replace that with loop and logic for chaos game
        self.scatter.addPoints([{'pos': [0., 0.5], 'data': 1}])

        # showing all the widgets
        self.show()

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

        scatter.addPoints(points)
        plot.addItem(scatter)

        # Creating a grid layout
        layout = QGridLayout()
        widget.setLayout(layout)

        layout.addWidget(label, 1, 0)
        layout.addWidget(plot, 0, 1, 3, 1)

        # setting this widget as central widget of the main widow
        self.setCentralWidget(widget)

        return scatter
