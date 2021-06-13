import sys
import gui
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    gui = gui.ChaosWindow()
    sys.exit(app.exec())