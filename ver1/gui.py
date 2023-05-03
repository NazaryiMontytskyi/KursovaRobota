import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class ProgrammWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ітераційні методи систем нелінійних рівнянь")
        self.resize(1280, 650)

        self.main_labels = QHBoxLayout()

        self.welcome_label = QtWidgets.QLabel("Розв'яжіть систему рівнянь із заданими коефіцієнтами", self)
        self.welcome_label.setFont(QtGui.QFont("Arial", 11))
        self.welcome_label.setGeometry(10,10,400,30)

        self.windowFunction = ProgramFunctions(self)

        self.introduction_label = QtWidgets.QLabel("Необхідно обрати тип рівняння\nОбрати: ",self)
        self.introduction_label.setFont(QtGui.QFont("Arial", 11))
        self.introduction_label.setGeometry(10,35,300,35)

        self.btnClose = QtWidgets.QPushButton("Вийти з додатку", self)
        self.btnClose.setFont(QtGui.QFont("Arial", 11))
        self.btnClose.clicked.connect(self.close)
        self.btnClose.setGeometry(650,10,150,35)

        self.choose_equation_list = ["<Оберіть рівняння>", "Алгебраїчне", "Тригонометричне", "Трансцедентне"]
        self.choose_equation = QComboBox(self)
        self.choose_equation.addItems(self.choose_equation_list)
        self.choose_equation.setGeometry(10,75,170,25)
        self.choose_equation.setFont(QtGui.QFont("Arial",11))

        self.method_label = QtWidgets.QLabel("Необхідно обрати метод розв'язання\nОберіть метод:",self)
        self.method_label.setGeometry(10, 110, 300, 30)
        self.method_label.setFont(QtGui.QFont("Arial", 11))

        self.choose_method_list = ["<Обрати метод>", "Метод простої ітерації", "Метод Гаусса-Зейделя"]
        self.choose_method = QComboBox(self)
        self.choose_method.addItems(self.choose_method_list)
        self.choose_method.setGeometry(10, 145, 200, 25)
        self.choose_method.setFont(QtGui.QFont("Arial", 11))

        self.equation_list = QLabel(self)
        self.equation_list.setFont(QtGui.QFont("Arial", 11))
        self.equation_list.setGeometry(10, 185, 400, 65)
        self.choose_equation.currentIndexChanged.connect(self.windowFunction.show_equations)


        self.method_list = QLabel(self)
        self.method_list.setFont(QtGui.QFont("Arial", 11))
        self.method_list.setGeometry(10, 255, 300, 55)
        self.choose_method.currentIndexChanged.connect(self.windowFunction.show_method)






        self.show()




class ProgramFunctions:
    def __init__(self, received_window:ProgrammWindow):
        self.window = received_window

    def show_equations(self, index):
        text = "Система рівнянь:\n"
        if index == 0:
            text += "Система не задана\n"
            self.window.equation_list.setText(text)
            self.window.is_system_chosen = False
        if index == 1:
            text += "[a] * x₁³ - [b]*x₂³ + [c] = 0\n"
            text += "[d] * x₁² - [f]*x₂² + [g] = 0\n"
            self.window.equation_list.setText(text)
            self.window.is_system_chosen = True
        if index == 2:
            text += "[a] * cos(x₁) - [b]sin(x₂) + [c] = 0\n"
            text += "[d] * arcsin(x₁) + [f]arctg(x₂) - [g] = 0\n"
            self.window.equation_list.setText(text)
            self.window.is_system_chosen = True
        if index == 3:
            text += "[a] * ln(x₁) + [b]*e^(x₂) - [c] = 0\n"
            text += "[d] * arctg(x₁) - log[f](x₂) + [g] = 0\n"
            self.window.equation_list.setText(text)
            self.window.is_system_chosen = True


    def show_method(self, index):
        text = "Обраний метод розв'язання:\n"
        if index == 0:
            text += "Метод не задано\n"
            self.window.method_list.setText(text)
            self.window.is_method_chosen = False
        if index == 1:
            text += "Метод простої ітерації\n"
            self.window.method_list.setText(text)
            self.window.is_method_chosen = True
        if index == 2:
            text += "Метод Гаусса-Зейделя\n"
            self.window.method_list.setText(text)
            self.window.is_method_chosen = True


    







