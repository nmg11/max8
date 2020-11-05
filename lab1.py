import sys
from PyQt5.QtCore import QSize, Qt, QTime, QTimer
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication,
                             QLabel, QLineEdit, QMessageBox, QDesktopWidget,
                             QMainWindow, QAction, qApp, QGridLayout, QDialog,
                             QToolButton, QCheckBox, QComboBox)
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QImage
from PyQt5.uic.properties import QtCore
import random

#словари для хранения логина\пароля и рекордов
identifikator_dict = {}
record_dict = {}
#диапазон чисел в игре
min_rand_number = -10
max_rand_number = 10

#основной класс
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #передача логинов\паролей в игру
        file_with_user_list = open('user list.txt')
        for line in file_with_user_list :
            user = line.strip().split(':')
            identifikator_dict[ user[ 0 ] ] = user[ 1 ]
        file_with_user_list.close()
        # передача рекордов в игру
        file_with_record_list = open('record list.txt')
        for line in file_with_record_list:
            user = line.strip().split(':')
            record_dict[ user[ 0 ] ] = user[ 1 ]
        file_with_record_list.close()

        self.username = ''
        #поля для ввода логина\пароля
        login_label = QLabel('Login')
        self.login_edit = QLineEdit()
        password_label = QLabel('Password')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        #кнопки для входа в игру, регистрации,
        #просмотра рекордов и всех существующих пользователей
        self.push_button = QPushButton("Log In!")
        self.push_button_regisration = QPushButton('Registration')
        self.button_user = QPushButton('All users')
        self.button_record = QPushButton('Records')

        #изменение шрифта
        stile_font = QFont('SanSerif', 10)
        login_label.setFont(stile_font)
        self.push_button.setFont(stile_font)
        password_label.setFont(stile_font)
        self.push_button_regisration.setFont(stile_font)
        self.button_user.setFont(stile_font)
        self.button_record.setFont(stile_font)

        #картинка в главном меню
        self.button = QPushButton(self)
        self.button.setIconSize(QSize(200, 200))
        self.button.setGeometry(0, 0, 40, 40)
        self.button.setIcon(QIcon(QPixmap("exit.png")))

        # элементы для полей логина
        horizontal_layout_login = QVBoxLayout()
        horizontal_layout_login.addStretch(1)
        horizontal_layout_login.addWidget(login_label)
        horizontal_layout_login.addWidget(self.login_edit)
        horizontal_layout_login.addStretch(1)
        # элементы для полей пароля
        horizontal_layout_password = QVBoxLayout()
        horizontal_layout_password.addStretch(1)
        horizontal_layout_password.addWidget(password_label)
        horizontal_layout_password.addWidget(self.password_edit)
        horizontal_layout_password.addStretch(1)
        # кнопки
        horizontal_layout_button = QHBoxLayout()
        horizontal_layout_button.addWidget(self.push_button)
        horizontal_layout_button.addWidget(self.button_user)
        horizontal_layout_button.addWidget(self.button_record)
        horizontal_layout_button.addWidget(self.push_button_regisration)
        # небольшая стилизация, добавление отступов по вертикали
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.button)
        vertical_layout.addLayout(horizontal_layout_login)
        vertical_layout.addLayout(horizontal_layout_password)
        vertical_layout.addLayout(horizontal_layout_button)
        # добавление отступов по горизонтали
        horizontal_layout_main = QHBoxLayout()
        horizontal_layout_main.addStretch(1)
        horizontal_layout_main.addLayout(vertical_layout)
        horizontal_layout_main.addStretch(1)
        self.setLayout(horizontal_layout_main)
        # функции для кнопок
        self.push_button.pressed.connect(self.login)
        self.push_button_regisration.pressed.connect(self.registration)
        self.button_user.pressed.connect(self.show_user)
        self.button_record.pressed.connect(self.record)

        self.setWindowTitle('MyProgramm PyQt')
        self.show()

        # функции кнопок
    def login(self):
        #аутентификация пользователя
        #проверка наличия введённых данных в словаре
        msb = QMessageBox()
        msb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if self.login_edit.text() in identifikator_dict:
            if identifikator_dict[ self.login_edit.text() ] == self.password_edit.text():
                username = self.login_edit.text()
                start = StartGame(self, username)
            else:
                msb.setDetailedText("enter existing data or go through registration")
                msb.setText('login or password is not valid')
                msb.exec()
        else:
            msb.setDetailedText("enter existing data or go through registration")
            msb.setText('login or password is not valid')
            msb.exec()

    def record(self):
        #открытие окна рекордов
        self.rec = record(self)
        self.rec.show()

    def registration(self):
        # открытие окна для регистрации
        self.reg = registration_user(self)
        self.reg.show()


    def show_user(self):
        # открытие окна просмотра логинов и паролей(временно) всех юзеров
        self.ul = user_list(self)


class record(QWidget):
    #окно для вывода рекордов
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Window)
        self.init_record()

    def init_record(self):
        #вывод рекордов в таблице
        grid_user = QGridLayout()
        numb = 0
        for i in record_dict:
            grid_user.addWidget(QLabel(i), numb, 0)
            grid_user.addWidget(QLabel(record_dict[ i ]), numb, 1)
            numb += 1
            self.setLayout(grid_user)
            self.show()


class user_list(QWidget):
    #окно для показа списка пользователей
    # и, временно, паролей
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Window)
        self.init_user_list()

    def init_user_list(self):
        # вывод данных в таблице
        grid_user = QGridLayout()
        numb = 0
        for i in identifikator_dict:
            grid_user.addWidget(QLabel(i), numb, 0)
            grid_user.addWidget(QLabel(identifikator_dict[ i ]), numb, 1)
            numb += 1
            self.setLayout(grid_user)
            self.show()


class registration_user(QWidget):
    #окно для регистрации
    def __init__(self, parent=None, ):
        super().__init__(parent, Qt.Window)
        self.init_reg()

    def init_reg(self):

        box_for_registration = QVBoxLayout()
        hor_box = QHBoxLayout()
        # поля ввода логина\пароля
        name_label = QLabel('enter your name')
        self.name_edit = QLineEdit()
        pass_label = QLabel('your password')
        self.pass_edit = QLineEdit()
        self.regg = QPushButton('Registration')

        # build
        box_for_registration.addWidget(name_label)
        box_for_registration.addWidget(self.name_edit)
        box_for_registration.addWidget(pass_label)
        box_for_registration.addWidget(self.pass_edit)
        box_for_registration.addWidget(self.regg)

        hor_box.addStretch(1)
        hor_box.addLayout(box_for_registration)
        hor_box.addStretch(1)
        # функция для регистрации
        self.regg.pressed.connect(self.registr)
        #
        self.setLayout(hor_box)
        self.show()

    def registr(self):
        # регистрация
        # проверка на существования логина в базе
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
    #окошко для выбора размера поля
    #и создания элементов для игры
    def __init__(self, parent = None, username = 'player1'):
        super().__init__(parent, Qt.Window)
        self.init_start_game()
        self.username = username

    def init_start_game(self):
        text_quatity_label = QLabel('enter a quantity block')
        #enter area layout
        grid_buttons = QGridLayout() #для кнопок
        enemy_layout = QHBoxLayout()
        timer_layout = QHBoxLayout()
        #создание кнопок для выбора размеров поля
        for i in range(3,7):
            setattr(self, 'tool_button_%s' %i, QToolButton())
            getattr(self,'tool_button_%s'%i).setText(str(str(i) +' x '+str(i)))
        grid_buttons.addWidget(self.tool_button_3, 0, 0)
        grid_buttons.addWidget(self.tool_button_4, 0, 1)
        grid_buttons.addWidget(self.tool_button_5, 1, 0)
        grid_buttons.addWidget(self.tool_button_6, 1, 1)

        #создание итогового окна
        vertical_lay = QVBoxLayout()
        vertical_lay.addStretch(1)
        vertical_lay.addWidget(text_quatity_label)
        vertical_lay.addStretch(1)
        vertical_lay.addLayout(grid_buttons)
        vertical_lay.addStretch(1)
        self.widget_of_start_game = QWidget()
        self.horizontal_lay = QHBoxLayout(self.widget_of_start_game)
        self.horizontal_lay.addStretch(2)
        self.horizontal_lay.addLayout(vertical_lay)
        self.horizontal_lay.addStretch(2)
        # функции кнопок для создания размеров игрового поля
        for n in range(3, 7):
            getattr(self, 'tool_button_%s' % n).pressed.connect(lambda v=n: self.play_game(v))
        self.widget_of_start_game.show()

    def play_game(self, number):
        # создание поля игры
        self.widget_of_start_game.hide()
        self.field_size = number

        #количество шагов, имена пользователей, их счёт
        self.number_of_steps = 0
        self.player_1 = QLabel('player 1')
        self.player_1.setText(str(self.username))
        self.player_2 = QLabel('player 2')
        self.steps_over = QLabel('steps over')
        self.steps_everywhing = QLabel(str(self.field_size ** 2 - self.number_of_steps))
        self.whose_player_step = QLabel('Time')
        self.whose_player_step.setText('step player 1')
        #установка белого цвета на фон
        #далее меняется в зависимости от того, чей ход
        self.whose_player_step.setStyleSheet('QLabel {background-color: white; color: black;}')
        self.player_1.setStyleSheet('background-color: white')
        self.player_2.setStyleSheet('background-color: white')
        #счета игроков
        self.count_player_1 = QLabel('0')
        self.count_player_2 = QLabel('0')
        self.player_move = 1

        #создание единичных матриц, аналогичных полю игры
        #
        self.matrix_play = [ [ 1 for i in range(self.field_size ) ] for j in range(self.field_size ) ]
        self.matrix_play2 = [ list(x) for x in zip(*self.matrix_play) ]

        # построения поля для игры
        self.grid_play = QGridLayout()
        for i in range(self.field_size):
            for j in range(self.field_size):
                rand_number = str(random.randint(min_rand_number, max_rand_number))
                button_for_build_area_game = 'pushbuttongrid_%s' % i + '_%s' % j
                setattr(self, button_for_build_area_game, QPushButton(rand_number))
                getattr(self, button_for_build_area_game).setEnabled(False)
                getattr(self, button_for_build_area_game).setStyleSheet('QPushButton {background-color: white; color: black;}')
                self.grid_play.addWidget(getattr(self, button_for_build_area_game), i, j)
        #установка допустимых для нажатия кнопок в первом ходе
        for i in range(self.field_size):
            button_for_build_area_game = 'pushbuttongrid_%s' % i + '_0'
            getattr(self, button_for_build_area_game).setEnabled(True)
            if int(getattr(self, button_for_build_area_game).text()) > 0:
                getattr(self, button_for_build_area_game).setStyleSheet('QPushButton {background-color: green; color: black;}')
            else:
                getattr(self, button_for_build_area_game).setStyleSheet('QPushButton {background-color: orange; color: black;}')

        #установдение функций нажатия на кнопки поля
        for i in range(self.field_size):
            for j in range(self.field_size):
                button_for_build_area_game = 'pushbuttongrid_%s' % i + '_%s' % j
                getattr(self, button_for_build_area_game).pressed.connect(lambda v=i, w=j: self.player_step(v, w))
        #создание поля игры
        horizontal_layout_label = QHBoxLayout()
        horizontal_layout_edit = QHBoxLayout()
        horizontal_layout_whose_step = QHBoxLayout()
        vertical_layout = QVBoxLayout()
        horizontal_layout_main = QHBoxLayout()
        #создание элементов с именами игроков
        horizontal_layout_label.addStretch(4)
        horizontal_layout_label.addWidget(self.player_1)
        horizontal_layout_label.addStretch(1)
        horizontal_layout_label.addWidget(self.steps_over)
        horizontal_layout_label.addStretch(1)
        horizontal_layout_label.addWidget(self.player_2)
        horizontal_layout_label.addStretch(4)
        # создание элементов со счетами игроков и
        # оставшимся количеством ходов
        horizontal_layout_edit.addStretch(1)
        horizontal_layout_edit.addWidget(self.count_player_1)
        horizontal_layout_edit.addStretch(1)
        horizontal_layout_edit.addWidget(self.steps_everywhing)
        horizontal_layout_edit.addStretch(1)
        horizontal_layout_edit.addWidget(self.count_player_2)
        horizontal_layout_edit.addStretch(1)
        #создание для показа имени ходящего сейчас игрока
        horizontal_layout_whose_step.addStretch(4)
        horizontal_layout_whose_step.addWidget(self.whose_player_step)
        horizontal_layout_whose_step.addStretch(4)

        #сборка вышеописанных элементов
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout_label)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout_edit)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(self.grid_play)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout_whose_step)
        horizontal_layout_main.addStretch(1)
        horizontal_layout_main.addLayout(vertical_layout)
        horizontal_layout_main.addStretch(1)
        self.setLayout(horizontal_layout_main)
        self.show()

    def player_step(self, height=1, width=1):
        # функция с логикой нажатия нажатия на кнопку (1 шаг)
        # единичные матрицы, элементы которой зануляются аналогично
        # позиции нажатой кнопки на поле.
        # Нужно для правильной отрисовки и выбора ещё не нажатых клавиш
        self.matrix_play[ height ][ width ] = 0
        self.matrix_play2[ width ][ height ] = 0
        self.steps_everywhing.setText(str(int(self.steps_everywhing.text()) - 1))
        pressed_button_need_button = 'pushbuttongrid_%s' % height + '_%s' % width
        getattr(self, pressed_button_need_button).setEnabled(False)
        self.grid_play.addWidget(QLabel(getattr(self, pressed_button_need_button).text()), height, width)
        getattr(self, pressed_button_need_button).deleteLater()
        #  шаг игрока 1
        if self.player_move == 2:
            self.count_player_2.setText(str(int(self.count_player_2.text()) + int(getattr(self, pressed_button_need_button).text())))
            #убираем кликабельность кнопок
            for i in range(self.field_size ):
                button_wich_must_be_not_clicable = 'pushbuttongrid_%s' % height + '_%s' % i
                try:
                    getattr(self, button_wich_must_be_not_clicable).setEnabled(False)
                except RuntimeError:
                    pass
                else:
                    getattr(self, button_wich_must_be_not_clicable).setStyleSheet('QPushButton'
                                                                                  '{background-color: white; '
                                                                                  'color: black;}')
            #устанавливаем клакабельность кнопок
            if 1 in self.matrix_play2[ width ]:
                for i in range(self.field_size):
                    button_wich_must_be_clicable= 'pushbuttongrid_%s' % i + '_%s' % width
                    if 1 in self.matrix_play2[ width ]:
                        try:
                            getattr(self, button_wich_must_be_clicable).setEnabled(True)
                        except RuntimeError:
                            pass
                        else:
                            if int(getattr(self, button_wich_must_be_clicable).text()) > 0:
                                getattr(self, button_wich_must_be_clicable).setStyleSheet('QPushButton '
                                                                                        '{background-color: green; '
                                                                                        'color: black;}')
                            else:
                                getattr(self, button_wich_must_be_clicable).setStyleSheet('QPushButton '
                                                                                        '{background-color: '
                                                                                        'orange; color: black;}')
                        self.player_1.setStyleSheet('QLabel {background-color: green; color: black;}')
                        self.player_2.setStyleSheet('QLabel {background-color: white; color: black;}')
                        self.whose_player_step.setText('step player 1')
                self.player_move = 1
            #конец игры
            else:
                #если в матрице нет 1 - нет возможности хода
                self.end_game = QMessageBox()
                self.end_game.setStandardButtons(QMessageBox.Ok)
                if int(self.count_player_1.text()) > int(self.count_player_2.text()):
                    winner = 'player 1'
                    self.record()
                else:
                    winner = 'player 2'
                winner += ' wingame'
                self.end_game.setText(winner)
                self.end_game.exec()
        # шаг игрока 2
        else:
            self.count_player_1.setText(str(int(self.count_player_1.text()) + int(getattr(self, pressed_button_need_button).text())))
            for i in range(self.field_size ):
                # убираем кликабельность кнопок
                button_wich_must_be_not_clicable = 'pushbuttongrid_%s' % i + '_%s' % width
                try:
                    getattr(self, button_wich_must_be_not_clicable).setEnabled(False)
                except RuntimeError:
                    print('this button was deleted!')
                else:
                    getattr(self, button_wich_must_be_not_clicable).setStyleSheet('QPushButton {background-color: white; color: black;}')
            if 1 in self.matrix_play[ height ]:
                for i in range(self.field_size):
                    # устанавливаем клакабельность кнопок
                    button_wich_must_be_not_clicable = 'pushbuttongrid_%s' % i + '_%s' % width
                    button_wich_must_be_clicable = 'pushbuttongrid_%s' % height + '_%s' % i
                    try:
                        getattr(self, button_wich_must_be_clicable).setEnabled(True)
                    except RuntimeError:
                        pass
                    else:
                        if int(getattr(self, button_wich_must_be_clicable).text()) > 0:
                            getattr(self, button_wich_must_be_clicable).setStyleSheet('QPushButton {background-color: green; color: black;}')
                        else:
                            getattr(self, button_wich_must_be_clicable).setStyleSheet('QPushButton {background-color: orange; color: black;}')
                        try:
                            getattr(self, button_wich_must_be_clicable).setEnabled(False)
                        except RuntimeError:
                            pass
                        else:
                            getattr(self, button_wich_must_be_not_clicable).setStyleSheet('QPushButton {background-color: white; color: black;}')
                            self.player_2.setStyleSheet('QLabel {background-color: green; color: black;}')
                            self.player_1.setStyleSheet('QLabel {background-color: white; color: black;}')
                            self.whose_player_step.setText('step player 2')
                self.player_move = 2
            #конец игры
            else:
                # если в матрице нет 1 - нет возможности хода
                self.end_game = QMessageBox()
                self.end_game.setStandardButtons(QMessageBox.Ok)
                if int(self.count_player_1.text()) > int(self.count_player_2.text()):
                    winner = 'player 1'
                    self.record()
                else:
                    winner = 'player 2'
                winner += ' wingame'
                self.end_game.setText(winner)
                self.end_game.exec()

    def record(self):
        # запись рекорда нового пользователя
        if self.username not in record_dict.keys():
            record_dict[self.username] = self.count_player_1.text()
            with open('record list.txt', 'a') as file:
                file.write(str('\n' + self.username + ':' + self.count_player_1.text()))
        #перезапись рекорда
        else:
            if int(record_dict[self.username]) < int(self.count_player_1.text()):
                record_dict[self.username] = self.count_player_1.text()
                with open('record list.txt', 'w') as file:
                    for line in record_dict:
                        file.write(str('\n' + line + ':' + record_dict[line]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())