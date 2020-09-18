import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication,
                             QLabel, QLineEdit, QMessageBox, QDesktopWidget,
                             QMainWindow, QAction, qApp, QGridLayout, QDialog)
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QImage
from PyQt5.uic.properties import QtCore
import random

identifikator_dict = {}
record_dict = {}


# main class
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # VARIABLE
        x = open('user list.txt')
        for line in x:
            user = line.strip().split(':')
            identifikator_dict[ user[ 0 ] ] = user[ 1 ]
        x.close()
        x = open('record list.txt')
        for line in x:
            user = line.strip().split(':')
            record_dict[ user[ 0 ] ] = user[ 1 ]
        x.close()
        self.username = ''
        login_label = QLabel('Login')
        self.login_edit = QLineEdit()
        self.push_button = QPushButton("LOG IN!")
        self.push_button_regisration = QPushButton('REGISTRATION')
        password_label = QLabel('Password')
        self.password_edit = QLineEdit()
        self.button_user = QPushButton('all users')
        self.button_record = QPushButton('Records')
        # true image
        image_label = QLabel()
        image = QPixmap('1.jpg')
        image_label.setPixmap(image)
        image_label.heightForWidth(20)

        # stile
        stile_font = QFont('SanSerif', 12)
        login_label.setFont(stile_font)
        self.push_button.setFont(stile_font)
        password_label.setFont(stile_font)

        # test image
        self.button = QPushButton(self)
        self.button.setIconSize(QSize(200, 200))
        self.button.setGeometry(0, 0, 40, 40)
        self.button.setIcon(QIcon(QPixmap("exit.png")))

        # LOGIN elements
        horizontal_layout_login = QVBoxLayout()
        horizontal_layout_login.addStretch(1)
        horizontal_layout_login.addWidget(login_label)
        horizontal_layout_login.addWidget(self.login_edit)
        horizontal_layout_login.addStretch(1)
        # PASSWORD elements
        horizontal_layout_password = QVBoxLayout()
        horizontal_layout_password.addStretch(1)
        horizontal_layout_password.addWidget(password_label)
        horizontal_layout_password.addWidget(self.password_edit)
        horizontal_layout_password.addStretch(1)
        # BUTTON elements
        horizontal_layout_button = QHBoxLayout()
        horizontal_layout_button.addWidget(self.push_button)
        horizontal_layout_button.addWidget(self.button_user)
        horizontal_layout_button.addWidget(self.button_record)
        horizontal_layout_button.addWidget(self.push_button_regisration)
        # VERTICAL LAYOUT elements
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.button)
        vertical_layout.addLayout(horizontal_layout_login)
        vertical_layout.addLayout(horizontal_layout_password)
        vertical_layout.addLayout(horizontal_layout_button)
        # HORIZONTAL LAYOUT MAIN elements
        horizontal_layout_main = QHBoxLayout()
        horizontal_layout_main.addStretch(1)
        horizontal_layout_main.addLayout(vertical_layout)
        horizontal_layout_main.addStretch(1)
        self.setLayout(horizontal_layout_main)
        # LOGIC_VAR
        self.push_button.pressed.connect(self.login)
        self.push_button_regisration.pressed.connect(self.registration)
        self.button_user.pressed.connect(self.show_user)
        self.button_record.pressed.connect(self.record)
        # show
        self.setWindowTitle('MyProgramm PyQt')
        self.show()

        # LOGIC_DEF
    def login(self):
        msb = QMessageBox()
        msb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if self.login_edit.text() in identifikator_dict:
            if identifikator_dict[ self.login_edit.text() ] == self.password_edit.text():
                username = self.login_edit.text()
                start = StartGame(self, username)
            else:
                msb.setDetailedText("login or password is not valid")
                msb.setText('you a NOT TRUE')
                msb.exec()
        else:
            msb.setDetailedText("login or password is not valid")
            msb.setText('you a NOT TRUE')
            msb.exec()

    def record(self):
        self.rec = record(self)
        self.rec.show()

    def registration(self):
        self.reg = registration_user(self)
        self.reg.show()


    def show_user(self):
        self.ul = user_list(self)

class record(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Window)
        self.init_record()
    def init_record(self):
        grid_user = QGridLayout()
        numb = 0
        for i in record_dict:
            grid_user.addWidget(QLabel(i), numb, 0)
            grid_user.addWidget(QLabel(record_dict[ i ]), numb, 1)
            numb += 1
            self.setLayout(grid_user)
            self.show()

class user_list(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Window)
        self.init_user_list()
    def init_user_list(self):
        grid_user = QGridLayout()
        numb = 0
        for i in identifikator_dict:
            grid_user.addWidget(QLabel(i), numb, 0)
            grid_user.addWidget(QLabel(identifikator_dict[ i ]), numb, 1)
            numb += 1
            self.setLayout(grid_user)
            self.show()


class registration_user(QWidget):
    def __init__(self, parent=None, ):
        super().__init__(parent, Qt.Window)
        self.init_reg()

    def init_reg(self):
        box = QVBoxLayout()
        hor_box = QHBoxLayout()
        # var
        name_label = QLabel('enter your name')
        self.name_edit = QLineEdit()
        pass_label = QLabel('your password')
        self.pass_edit = QLineEdit()
        self.regg = QPushButton('Registration')

        # build
        box.addWidget(name_label)
        box.addWidget(self.name_edit)
        box.addWidget(pass_label)
        box.addWidget(self.pass_edit)
        box.addWidget(self.regg)

        hor_box.addStretch(1)
        hor_box.addLayout(box)
        hor_box.addStretch(1)
        # logic var
        self.regg.pressed.connect(self.registr)
        #
        self.setLayout(hor_box)
        self.show()

    # Logic def
    def registr(self):
        push = QMessageBox()
        if self.name_edit.text() not in identifikator_dict:
            identifikator_dict[ self.name_edit.text() ] = self.pass_edit.text()
            push.setText('registration complited!')
            x = open('user list.txt', 'a')
            user = '\n' + self.name_edit.text() + ':' + self.pass_edit.text()
            x.write(user)
            x.close()
        else:
            push.setText('this name is already in use')
        push.setStandardButtons(QMessageBox.Ok)
        push.exec()


class StartGame(QWidget):
    def __init__(self, parent = None, username = 'player1'):

        super().__init__(parent, Qt.Window)
        self.init_start_game()
        self.username = username

    def init_start_game(self):
        # start widget

        level_label = QLabel('enter a quantity block')
        self.pb_3 = QPushButton('3x3')
        self.pb_4 = QPushButton('4x4')
        self.pb_5 = QPushButton('5x5')
        self.pb_6 = QPushButton('6x6')

        grid_buttons = QGridLayout()
        grid_buttons.addWidget(self.pb_3, 0, 0)
        grid_buttons.addWidget(self.pb_4, 0, 1)
        grid_buttons.addWidget(self.pb_5, 1, 0)
        grid_buttons.addWidget(self.pb_6, 1, 1)

        vertical_lay = QVBoxLayout()
        vertical_lay.addStretch(1)
        vertical_lay.addWidget(level_label)
        vertical_lay.addStretch(1)
        vertical_lay.addLayout(grid_buttons)

        self.widget = QWidget()
        self.horizontal_lay = QHBoxLayout(self.widget)
        self.horizontal_lay.addStretch(2)
        self.horizontal_lay.addLayout(vertical_lay)
        self.horizontal_lay.addStretch(2)

        for n in range(3, 7):
            getattr(self, 'pb_%s' % n).pressed.connect(lambda v=n: self.play_game(v))
        self.widget.show()

    def play_game(self, number):
        self.widget.hide()
        self.number = number
        # var
        self.step = 0
        self.player_1 = QLabel('player 1')
        self.player_1.setText(str(self.username))
        self.player_2 = QLabel('player 2')
        self.steps_over = QLabel('steps over')
        self.steps_everywhing = QLabel(str(number ** 2 - self.step))
        self.timer = QLabel('Time')
        self.timer.setStyleSheet('QLabel {background-color: white; color: black;}')
        self.player_1.setStyleSheet('background-color: white')
        self.player_2.setStyleSheet('background-color: white')
        self.timer.setText('step player 1')

        self.count_1 = QLabel('0')
        self.count_2 = QLabel('0')
        self.player_move = 1
        self.matrix_play = [ [ 1 for i in range(self.number) ] for j in range(self.number) ]
        self.matrix_play2 = [ list(x) for x in zip(*self.matrix_play) ]

        # layout grid button
        self.grid_play = QGridLayout()
        for i in range(number):
            for j in range(number):
                rand_number = str(random.randint(-100, 100))
                x = 'pushbuttongrid_%s' % i + '_%s' % j
                setattr(self, x, QPushButton(rand_number))
                getattr(self, x).setEnabled(False)
                getattr(self, x).setStyleSheet('QPushButton {background-color: white; color: black;}')
                self.grid_play.addWidget(getattr(self, x), i, j)
        for i in range(number):
            x = 'pushbuttongrid_%s' % i + '_0'
            if int(getattr(self, x).text()) > 0:
                getattr(self, x).setStyleSheet('QPushButton {background-color: green; color: black;}')
            else:
                getattr(self, x).setStyleSheet('QPushButton {background-color: orange; color: black;}')
            getattr(self, x).setEnabled(True)
        #logic button
        for i in range(number):
            for j in range(number):
                x = 'pushbuttongrid_%s' % i + '_%s' % j
                getattr(self, x).pressed.connect(lambda v=i, w=j: self.player_step(v, w))
        #layout game area
        horizontal_layout_label = QHBoxLayout()
        horizontal_layout_edit = QHBoxLayout()
        horizontal_layout_timer = QHBoxLayout()
        vertical_layout = QVBoxLayout()
        horizontal_layout_main = QHBoxLayout()

        horizontal_layout_label.addStretch(4)
        horizontal_layout_label.addWidget(self.player_1)
        horizontal_layout_label.addStretch(1)
        horizontal_layout_label.addWidget(self.steps_over)
        horizontal_layout_label.addStretch(1)
        horizontal_layout_label.addWidget(self.player_2)
        horizontal_layout_label.addStretch(4)

        horizontal_layout_edit.addStretch(1)
        horizontal_layout_edit.addWidget(self.count_1)
        horizontal_layout_edit.addStretch(1)
        horizontal_layout_edit.addWidget(self.steps_everywhing)
        horizontal_layout_edit.addStretch(1)
        horizontal_layout_edit.addWidget(self.count_2)
        horizontal_layout_edit.addStretch(1)

        horizontal_layout_timer.addStretch(4)
        horizontal_layout_timer.addWidget(self.timer)
        horizontal_layout_timer.addStretch(4)

        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout_label)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout_edit)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(self.grid_play)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout_timer)

        horizontal_layout_main.addStretch(1)
        horizontal_layout_main.addLayout(vertical_layout)
        horizontal_layout_main.addStretch(1)

        self.setLayout(horizontal_layout_main)
        self.show()

    def player_step(self, height=1, width=1):
        # delete abd hide button
        self.matrix_play[ height ][ width ] = 0
        self.matrix_play2[ width ][ height ] = 0
        self.steps_everywhing.setText(str(int(self.steps_everywhing.text()) - 1))
        x = 'pushbuttongrid_%s' % height + '_%s' % width
        getattr(self, x).setEnabled(False)
        self.grid_play.addWidget(QLabel(getattr(self, x).text()), height, width)
        getattr(self, x).hide()
        if self.player_move == 2:
            self.count_2.setText(str(int(self.count_2.text()) + int(getattr(self, x).text())))
            for i in range(self.number):
                y = 'pushbuttongrid_%s' % height + '_%s' % i
                getattr(self, y).setEnabled(False)
                getattr(self, y).setStyleSheet('QPushButton {background-color: white; color: black;}')
            if 1 in self.matrix_play2[ width ]:
                for i in range(self.number):
                    x = 'pushbuttongrid_%s' % i + '_%s' % width
                    if 1 in self.matrix_play2[ width ]:
                        getattr(self, x).setEnabled(True)
                        if int(getattr(self, x).text()) > 0:
                            getattr(self, x).setStyleSheet('QPushButton {background-color: green; color: black;}')
                        else:
                            getattr(self, x).setStyleSheet('QPushButton {background-color: orange; color: black;}')

                    self.player_1.setStyleSheet('QLabel {background-color: green; color: black;}')
                    self.player_2.setStyleSheet('QLabel {background-color: white; color: black;}')
                    self.timer.setText('step player 1')
                self.player_move = 1
            else:

                self.end_game = QMessageBox()
                self.end_game.setStandardButtons(QMessageBox.Ok)
                if int(self.count_1.text()) > int(self.count_2.text()):
                    winner = 'player 1'
                else:
                    winner = 'player 2'
                winner += ' wingame'
                self.end_game.setText(winner)
                self.end_game.exec()
        else:
            self.count_1.setText(str(int(self.count_1.text()) + int(getattr(self, x).text())))
            for i in range(self.number):
                y = 'pushbuttongrid_%s' % i + '_%s' % width
                getattr(self, y).setEnabled(False)
                getattr(self, y).setStyleSheet('QPushButton {background-color: white; color: black;}')
            if 1 in self.matrix_play[ height ]:
                for i in range(self.number):
                    y = 'pushbuttongrid_%s' % i + '_%s' % width
                    x = 'pushbuttongrid_%s' % height + '_%s' % i
                    getattr(self, x).setEnabled(True)
                    if int(getattr(self, x).text()) > 0:
                        getattr(self, x).setStyleSheet('QPushButton {background-color: green; color: black;}')
                    else:
                        getattr(self, x).setStyleSheet('QPushButton {background-color: orange; color: black;}')
                    getattr(self, y).setEnabled(False)
                    getattr(self, y).setStyleSheet('QPushButton {background-color: white; color: black;}')
                    self.player_2.setStyleSheet('QLabel {background-color: green; color: black;}')
                    self.player_1.setStyleSheet('QLabel {background-color: white; color: black;}')
                    self.timer.setText('step player 2')
                self.player_move = 2
            else:
                self.end_game = QMessageBox()
                self.end_game.setStandardButtons(QMessageBox.Ok)
                if int(self.count_1.text()) > int(self.count_2.text()):
                    winner = 'player 1'
                else:
                    winner = 'player 2'
                winner += ' wingame'
                self.end_game.setText(winner)
                self.end_game.exec()
    def record(self):
        #new record
        if self.username not in record_dict.keys():
            record_dict[self.username] = self.count_1.text()
            with open('record list.txt', 'a') as file:
                file.write(str(self.username + ':' + self.count_1.text()))
        #new user record
        else:
            if int(record_dict[self.username]) < int(self.count_1.text()):
                record_dict[self.username] = self.count_1.text()
                with open('record list.txt', 'a') as file:
                    for line in file:
                        string = line.strip().split(':')
                        if string[ 0 ] == self.username:
                            line = line.replace(str(string))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())