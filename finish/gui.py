import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph as pg
from mathematic import *
from PyQt5.QtMultimedia import QSoundEffect
from messages import *
from managing_file import *


class ProgrammWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Система нелінійних рівнянь")
        self.setGeometry(100, 100, 1200, 600)

        self.setWindowIcon(QIcon("venv\Scripts\main_icon.png"))
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile("venv\Scripts\clicked_mouth.wav"))

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(120, 171, 230))
        self.setPalette(palette)

        self.main_title = QLabel(self)
        self.main_title.setGeometry(10, 10, 180, 20)
        self.main_title.setText("Система нелінійних рівнянь")
        self.main_title.setFont(QtGui.QFont("Calibri", 11))

        self.btn_info = QPushButton(self)
        self.btn_info.setGeometry(270, 10 , 100, 25)
        self.btn_info.setText("Довідка")
        self.btn_info.clicked.connect(self.show_info)
        self.btn_info.setStyleSheet("QPushButton {border-radius: 7px; background-color: #cbcdff; color: #333333; font-size: 14px;}")

        self.btn_exit = QPushButton(self)
        self.btn_exit.setGeometry(375, 10, 100, 25)
        self.btn_exit.setText("Вихід")
        self.btn_exit.clicked.connect(self.close)
        self.btn_exit.setStyleSheet("QPushButton {border-radius: 7px; background-color: #cbcdff; color: #333333; font-size: 14px;}")

        self.choose_equation_title = QLabel(self)
        self.choose_equation_title.setText("Оберіть систему рівнянь:")
        self.choose_equation_title.setGeometry(10, 35, 180, 20)
        self.choose_equation_title.setFont(QtGui.QFont("Calibri", 11))

        self.choose_equation = QComboBox(self)
        self.choose_equation.addItems(["Оберіть систему", "Алгебраїчна", "Тригонометрична", "Трансцедентна"])
        self.choose_equation.setGeometry(10, 55, 180, 20)
        self.choose_equation.setFont(QtGui.QFont("Calibri", 11))

        self.equation_content = QLabel(self)
        self.equation_content.setText("Систему не обрано")
        self.equation_content.setGeometry(10, 80, 205, 53)
        self.choose_equation.activated.connect(self.show_systems)
        self.choose_equation.activated.connect(self.updateVisible)
        self.equation_content.setFont(QtGui.QFont("Calibri", 11))

        self.choose_method_title = QLabel(self)
        self.choose_method_title.setText("Оберіть метод:")
        self.choose_method_title.setGeometry(10, 129, 120, 25)
        self.choose_method_title.setFont(QtGui.QFont("Calibri", 11))

        self.choose_method = QComboBox(self)
        self.choose_method.addItems(["Оберіть метод:", "Метод Якобі", "Метод Гауса-Зейделя"])
        self.choose_method.setGeometry(10, 150, 180, 20)
        self.choose_method.setFont(QtGui.QFont("Calibri", 11))

        self.method_content = QLabel(self)
        self.method_content.setGeometry(10, 165, 140, 45)
        self.method_content.setText("Метод не обрано")
        self.choose_method.activated.connect(self.show_methods)
        self.choose_method.activated.connect(self.updateVisible)
        self.method_content.setFont(QtGui.QFont("Calibri", 11))

        self.input_group = QGroupBox(self)
        self.input_group.setGeometry(10,215,250,260)

        self.coef_input_fields = QVBoxLayout()

        self.input_coef_text_box = QHBoxLayout()
        self.input_coef_text = QLabel("Введіть коефіцієнти")
        self.input_coef_text.setFont(QtGui.QFont("Calibri", 11))
        self.input_coef_text_box.addWidget(self.input_coef_text)

        self.first_eq_input = QHBoxLayout()
        self.a_ch = QLabel("a: ")
        self.a_ch.setFont(QtGui.QFont("Calibri", 11))
        self.b_ch = QLabel("b: ")
        self.b_ch.setFont(QtGui.QFont("Calibri", 11))
        self.c_ch = QLabel("c: ")
        self.c_ch.setFont(QtGui.QFont("Calibri", 11))
        self.a_label = QLineEdit()
        self.b_label = QLineEdit()
        self.c_label = QLineEdit()
        self.a_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.b_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.c_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.first_eq_input.addWidget(self.a_ch)
        self.first_eq_input.addWidget(self.a_label)
        self.first_eq_input.addWidget(self.b_ch)
        self.first_eq_input.addWidget(self.b_label)
        self.first_eq_input.addWidget(self.c_ch)
        self.first_eq_input.addWidget(self.c_label)

        self.second_equation_input = QHBoxLayout()
        self.d_ch = QLabel("d: ")
        self.d_ch.setFont(QtGui.QFont("Calibri", 11))
        self.f_ch = QLabel("f: ")
        self.f_ch.setFont(QtGui.QFont("Calibri", 11))
        self.g_ch = QLabel("g: ")
        self.g_ch.setFont(QtGui.QFont("Calibri", 11))
        self.d_label = QLineEdit()
        self.f_label = QLineEdit()
        self.g_label = QLineEdit()
        self.d_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.f_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.g_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.second_equation_input.addWidget(self.d_ch)
        self.second_equation_input.addWidget(self.d_label)
        self.second_equation_input.addWidget(self.f_ch)
        self.second_equation_input.addWidget(self.f_label)
        self.second_equation_input.addWidget(self.g_ch)
        self.second_equation_input.addWidget(self.g_label)

        self.start_vector_box = QVBoxLayout()
        self.start_vector_text = QLabel("Введіть вектор початкового наближення: ")
        self.start_vector_text.setFont(QtGui.QFont("Calibri", 9))


        self.vector_box = QHBoxLayout()
        self.x1_ch = QLabel("x1: ")
        self.x2_ch = QLabel("x2: ")
        self.x1_label = QLineEdit()
        self.x2_label = QLineEdit()
        self.x1_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.x2_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.vector_box.addWidget(self.x1_ch)
        self.vector_box.addWidget(self.x1_label)
        self.vector_box.addWidget(self.x2_ch)
        self.vector_box.addWidget(self.x2_label)

        self.start_vector_box.addWidget(self.start_vector_text)

        self.precision_text = QVBoxLayout()
        self.precision = QLabel("Введіть точність: ")
        self.precision_text.addWidget(self.precision)
        self.precision.setFont(QtGui.QFont("Calibri", 11))

        self.precision_input = QHBoxLayout()
        self.precision_ch = QLabel("e: ")
        self.precision_label = QLineEdit()
        self.precision_label.setStyleSheet("QLineEdit {border-radius: 7px;}")
        self.precision_ch.setFont(QtGui.QFont("Calibri", 11))
        self.precision_input.addWidget(self.precision_ch)
        self.precision_input.addWidget(self.precision_label)


        self.btn_logic_box = QVBoxLayout()
        self.btn_clear = QPushButton()
        self.btn_clear.setText("Очистити ввід")
        self.btn_clear.setStyleSheet("QPushButton {border-radius: 7px; background-color: #cbcdff; color: #333333; font-size: 14px;}")
        self.btn_clear.setFont(QtGui.QFont("Calibri", 11))
        self.btn_clear.clicked.connect(self.clear_input_fields)

        self.btn_solve = QPushButton()
        self.btn_solve.setText("Розв'язати систему")
        self.btn_solve.setStyleSheet("QPushButton {border-radius: 7px; background-color: #cbcdff; color: #333333; font-size: 14px;}")
        self.btn_solve.setFont(QtGui.QFont("Calibri", 11))
        self.btn_solve.clicked.connect(self.solve_system)

        self.btn_logic_box.addWidget(self.btn_clear)
        self.btn_logic_box.addWidget(self.btn_solve)

        self.coef_input_fields.addLayout(self.input_coef_text_box)
        self.coef_input_fields.addLayout(self.first_eq_input)
        self.coef_input_fields.addLayout(self.second_equation_input)
        self.coef_input_fields.addLayout(self.start_vector_box)
        self.coef_input_fields.addLayout(self.vector_box)
        self.coef_input_fields.addLayout(self.precision_text)
        self.coef_input_fields.addLayout(self.precision_input)
        self.coef_input_fields.addLayout(self.btn_logic_box)

        self.input_group.setLayout(self.coef_input_fields)

        self.input_group.setVisible(False)

        self.solving_equation = SolvingSystem(self)
        self.equation_solving = QGroupBox(self)
        self.equation_solving.setGeometry(270, 50, 300, 425)
        self.iterations_box = QVBoxLayout()
        self.iterations_list = ScrollLabel()
        self.iterations_list.label.setFont(QtGui.QFont("Calibri", 11))
        self.iteration_label = QLabel("Хід розв'язання\nСписок ітерацій: ")
        self.iteration_label.setFont(QtGui.QFont("Calibri", 11))
        self.iterations_box.addWidget(self.iteration_label)
        self.iterations_box.addWidget(self.iterations_list)
        self.equation_solving.setLayout(self.iterations_box)
        self.equation_solving.setVisible(False)

        self.graphics = QGroupBox(self)
        self.plot_box = QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget()
        self.graph_label = QLabel("Графічне зображення розв'язання")
        self.graph_label.setFont(QtGui.QFont("Calibri Bold", 11))
        self.plot_box.addWidget(self.graph_label)
        self.plot_box.addWidget(self.plot_widget)
        self.graphics.setLayout(self.plot_box)
        self.graphics.setGeometry(600, 50, 500, 500)
        self.graphics.setVisible(False)

        self.btn_write_to_file = QPushButton(self)
        self.btn_write_to_file.setText("Записати розв'язок у файл")
        self.btn_write_to_file.setGeometry(900,550,200, 30)
        self.btn_write_to_file.clicked.connect(self.write_sol_to_file)
        self.btn_write_to_file.setStyleSheet("QPushButton {border-radius: 7px; background-color: #cbcdff; color: #333333; font-size: 14px;}")
        self.btn_write_to_file.setFont(QtGui.QFont("Calibri", 11))
        self.btn_write_to_file.setVisible(False)

        self.message_class = WinMessages(self)
        self.file_class = FileManager(self)

        self.show()


    def show_systems(self, index):
        text = "Система не задана"
        if index == 0:
            self.sound_effect.play()
            text = "Система не задана"
            self.equation_content.setText(text)
        if index == 1:
            text = "Система рівнянь:\n"
            text += "[a] * x₁³ - [b] * x₂³ + [c] = 0\n"
            text += "[d] * x₁² - [f] * x₂² + [g] = 0\n"
            self.equation_content.setText(text)
            self.sound_effect.play()
        if index == 2:
            text = "Система рівнянь:\n"
            text += "[a] * tg³(x₁) + [b] * cos([c] * x₂) = 0\n"
            text += "[d] * sin([f] * x₁) - [g] * tg(x₂) = 0\n"
            self.equation_content.setText(text)
            self.sound_effect.play()
        if index == 3:
            text = "Система рівнянь:\n"
            text += "logₓ₁([a] * x₁ + [b] * x₂)=c\n"
            text += "logₓ₂([d] * x₁ + [f] * x₂)=g\n"
            self.equation_content.setText(text)
            self.sound_effect.play()


    def show_methods(self, index):
        text = "Метод не обрано"
        if index == 0:
            text = "Метод не обрано"
            self.method_content.setText(text)
            self.sound_effect.play()
        if index == 1:
            text = "Обраний метод\n"
            text += "Метод Якобі"
            self.method_content.setText(text)
            self.sound_effect.play()
        if index == 2:
            text = "Обраний метод\n"
            text += "Метод Гауса-Зейделя"
            self.method_content.setText(text)
            self.sound_effect.play()


    def updateVisible(self):
        if self.choose_equation.currentIndex() == 0:
            if self.choose_method.currentIndex() == 1 or self.choose_method.currentIndex() == 2:
                self.input_group.setVisible(False)
        if self.choose_method.currentIndex() == 0:
            if self.choose_equation.currentIndex() == 1 or self.choose_equation.currentIndex() == 2 or self.choose_equation.currentIndex() == 3:
                self.input_group.setVisible(False)
        if self.choose_equation.currentIndex() == 1:
            if self.choose_method.currentIndex() == 1 or self.choose_method.currentIndex() == 2:
                self.input_group.setVisible(True)
        if self.choose_equation.currentIndex() == 2:
            if self.choose_method.currentIndex() == 1 or self.choose_method.currentIndex() == 2:
                self.input_group.setVisible(True)
        if self.choose_equation.currentIndex() == 3:
            if self.choose_method.currentIndex() == 1 or self.choose_method.currentIndex() == 2:
                self.input_group.setVisible(True)


    def clear_input_fields(self):
        self.sound_effect.play()
        self.a_label.clear()
        self.b_label.clear()
        self.c_label.clear()
        self.d_label.clear()
        self.f_label.clear()
        self.g_label.clear()
        self.x2_label.clear()
        self.x1_label.clear()
        self.precision_label.clear()
        self.btn_write_to_file.setVisible(False)
        self.equation_solving.setVisible(False)
        self.graphics.setVisible(False)



    def show_info(self):
        self.sound_effect.play()
        msg_info = QMessageBox()
        msg_info.setWindowTitle("Довідка")
        msg_info.setText("Даний додаток розв'язує системи нелінійних рівнянь двома ітераційними методами: Якобі та Гауса-Зейделя. Для взаємодії"
                         "з додатком оберіть тип системи та метод розв'язання. Введіть коефіцієнти, вектор початкового наближення та точність розв'язання."
                         "Після введення усіх необхідних даних натисність на кнопку 'Розв'язати систему' після чого ви побачите хід ітераційного процесу та"
                         "графічне розв'язання системи.\n\n"
                         "Метод Якобі: ітераційний метод, який полягає у виражені кожної змінної з кожного рівняння та обранні вектора початкового наближення."
                         "На кожній ітерації новому значенню змінних присвоюється значення обчислене з кожного рівняння, де використовуються обчислення виконанні "
                         "на попередній ітерації.\n\n"
                         "Метод Гауса-Зейделя майже ідентичний до попереднього, проте різниця полягає у підстановці значень отриманих уже на поточній ітерації.\n")
        msg_info.setFont(QtGui.QFont("Times New Roman", 11))
        msg_info.setStandardButtons(QMessageBox.Close)
        msg_info.exec_()


    def checkValidation(self):
        input_a = self.a_label.text()
        input_b = self.b_label.text()
        input_c = self.c_label.text()
        input_d = self.d_label.text()
        input_f = self.f_label.text()
        input_g = self.g_label.text()
        input_x1 = self.x1_label.text()
        input_x2 = self.x2_label.text()
        input_e = self.precision_label.text()

        if isFloat(input_a) and \
            isFloat(input_b) and \
            isFloat(input_c) and \
            isFloat(input_d) and \
            isFloat(input_f) and \
            isFloat(input_g) and \
            isFloat(input_x1) and \
            isFloat(input_x2) and \
            isFloat(input_e):
                return True
        else:
            QMessageBox.warning(self, "Помилка", "Числа введені не правильно. Введіть числа у вигляді цілих або дробових із роздільником у вигляді крапки")
            self.clear_input_fields()
            return False


    def solve_system(self):
        self.sound_effect.play()
        if self.checkValidation() == True:
            self.solving_equation.receive_input_data()
            if self.solving_equation.check_borders_of_values():
                self.equation_solving.setVisible(True)
                self.solving_equation.unique_solution()
            else:
                self.message_class.value_out_of_range()
        else:
            self.equation_solving.setVisible(False)


    def write_sol_to_file(self):
        self.sound_effect.play()
        self.file_class.share_solution_to_file()
        QMessageBox.information(self, "Увага", "Розв'язок вашої системи рівнянь записано у файл")


class ScrollLabel(QScrollArea):

    def __init__(self):
        QScrollArea.__init__(self)

        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)

        self.label = QLabel(content)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
