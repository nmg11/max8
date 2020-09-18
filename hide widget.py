from PyQt5.Qt import *


def on_click():
    if btn.text() == 'Hide':
        w1.hide()
        btn.setText('Show')
    elif btn.text() == 'Show':
        w1.show()
        btn.setText('Hide')


app = QApplication([ ])
w = QWidget()
w1 = QWidget()
lbl1 = QLabel('lbl1')
lbl2 = QLabel('lbl2')
lbl3 = QLabel('lbl3')

lay1 = QVBoxLayout(w1)
lay1.addWidget(lbl1)
lay1.addWidget(lbl2)
lay1.addWidget(lbl3)

lay = QHBoxLayout(w)
btn = QPushButton('Hide')
btn.clicked.connect(on_click)
lay.addWidget(w1)
lay.addWidget(btn)
w.move(0, 0)
w.show()
app.exec_()