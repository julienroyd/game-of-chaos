from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout
from chaos import sample_point

import pyqtgraph as pg
import numpy as np

INIT_POINTS_COLLECTION = {
    "triangle": np.array([[-1., -1.], [1., -1., ], [0., 1.]]),
    "square": np.array([[-1., -1.], [1., -1., ], [-1., 1.], [1., 1.]]),
    "diamond": np.array([[-1., 0.], [1., 0., ], [0., 1.], [0., -1.]]),
}


class ChaosWindow(QMainWindow):

    def __init__(self, start_shape="triangle", n_new_points=10000, speed=1000):
        super().__init__()

        self.freq = 1000 // speed
        self.init_points = INIT_POINTS_COLLECTION[start_shape]
        self.last_point = self.init_points[0]
        self.n_points = 0
        self.n_new_points = n_new_points

        # Add Timer for displaying and saving data
        self.displayTimer = QtCore.QTimer()
        self.displayTimer.timeout.connect(self.update_plot)

        # Setting up the graphical user interface
        self.set_up_gui()

        # initialising plot
        self.init_plot(init_points=np.concatenate([self.init_points, np.expand_dims(self.last_point, axis=0)], axis=0))

        # start the display timer
        self.displayTimer.start(self.freq)

    def set_up_gui(self):
        # setting title
        self.setWindowTitle("Game of Chaos")

        # setting geometry
        self.setGeometry(100, 100, 800, 800)

        # setting icon to the window
        icon = QIcon("fern_icon.png")
        self.setWindowIcon(icon)

        # creating a widget object
        self.central_widget = QWidget()

        # creating a label
        self.label = QLabel("")
        self.label.setWordWrap(True)
        self.label.setMinimumWidth(130)

        # creating a plot window
        self.plot = pg.plot()
        self.plot.getPlotItem().hideAxis('left')
        self.plot.getPlotItem().hideAxis('bottom')

        # creating a scatter plot item
        self.scatter = pg.ScatterPlotItem(size=4, brush=pg.mkBrush(0, 255, 0, 255))
        self.plot.addItem(self.scatter)
        self.plot.setXRange(-1., 1., padding=0.2)
        self.plot.setYRange(-1., 1., padding=0.2)

        # Creating a grid layout
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.layout.addWidget(self.label, 1, 0)
        self.layout.addWidget(self.plot, 0, 1, 3, 1)

        # setting this widget as central widget of the main widow
        self.setCentralWidget(self.central_widget)

        # displaying the interface
        self.show()

    def init_plot(self, init_points):
        # setting text to inital shape title
        self.label.setText("Triangle start")

        # adding points to the scatter plot
        self.scatter.clear()
        points = [{'pos': init_points[i, :], 'data': 1} for i in range(len(init_points))]
        self.n_points = len(init_points)
        self.scatter.addPoints(points)

    def update_plot(self):
        new_point = sample_point(init_points=self.init_points, last_point=self.last_point)
        self.last_point = new_point
        self.scatter.addPoints([{'pos': new_point, 'data': 1}])
        self.n_points += 1

        return
