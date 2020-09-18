import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class SecondWindow(QWidget):
    def __init__(self, parent=None):
        # Передаём ссылку на родительский элемент и чтобы виджет
        # отображался как самостоятельное окно указываем тип окна
        super().__init__(parent, Qt.Window)
        self.build()

    def build(self):
        self.mainLayout = QVBoxLayout()

        self.buttons = [ ]
        for i in range(5):
            but = QPushButton('button {}'.format(i), self)
            self.mainLayout.addWidget(but)
            self.buttons.append(but)

        self.setLayout(self.mainLayout)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.secondWin = None
        self.build()

    def build(self):
        self.mainLayout = QVBoxLayout()

        self.lab = QLabel('simple text', self)
        self.mainLayout.addWidget(self.lab)

        self.but1 = QPushButton('open window', self)
        self.but1.clicked.connect(self.openWin)
        self.mainLayout.addWidget(self.but1)

        self.setLayout(self.mainLayout)

    def openWin(self):
        if not self.secondWin:
            self.secondWin = SecondWindow(self)
        self.secondWin.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
0