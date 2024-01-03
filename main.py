import sys
from PySide6.QtWidgets import QApplication
from fun2 import Ui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec()