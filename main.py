import sys
import numpy as np
import gui
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    gui = gui.ChaosWindow(init_points=np.array([[0., 1.], [-1., 0., ], [1., 0.]]))
    sys.exit(app.exec())