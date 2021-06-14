import sys
import numpy as np
import gui
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    gui = gui.ChaosWindow(init_points=np.array([[-1., -1.], [1., -1., ], [0., 1.]]))
    sys.exit(app.exec())