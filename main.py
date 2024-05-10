
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets
from windows.LoginPage import Ui_Form

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec())
