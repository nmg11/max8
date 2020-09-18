import sys

from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication


class Label(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.p = None

    def setPixmap(self, p):
        self.p = p

    def paintEvent(self, event):
        if self.p:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            painter.drawPixmap(self.rect(), self.p)


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        lay = QVBoxLayout(self)
        lb = Label(self)
        lb.setPixmap(QPixmap("jack.jpg"))
        lay.addWidget(lb)


app = QApplication(sys.argv)
w = Widget()
w.show()
sys.exit(app.exec_())