from math import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import numpy as np
import os
import shutil


def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class SolvingSystem:

    def __init__(self, programm_window):
        self.win = programm_window


    def receive_input_data(self):
        self.a = float(self.win.a_label.text())
        self.b = float(self.win.b_label.text())
        self.c = float(self.win.c_label.text())
        self.d = float(self.win.d_label.text())
        self.f = float(self.win.f_label.text())
        self.g = float(self.win.g_label.text())
        self.e = float(self.win.precision_label.text())
        self.x1 = float(self.win.x1_label.text())
        self.x2 = float(self.win.x2_label.text())
        self.index_eq = self.win.choose_equation.currentIndex()
        self.index_method = self.win.choose_method.currentIndex()


    def solve_system_of_equations(self):
        itterations_text =""
        self.quantity = 0
        it = 1

        try:
            if self.win.choose_equation.currentIndex() == 1:
                itterations_text += "Алгебраїчна система\n"
                itterations_text += f"{self.a}x₁³ - {self.b}x₂³ + {self.c} = 0\n"
                itterations_text += f"{self.d}x₁² - {self.f}x₂² + {self.g} = 0\n"

            if self.win.choose_equation.currentIndex() == 3:
                itterations_text += "Трансцедентна система\n"
                itterations_text += f"logₓ₁({self.a}x₁ + {self.b}x₂) = {self.c}\n"
                itterations_text += f"logₓ₂({self.d}x₁ + {self.f}x₂) = {self.g}\n"

            if self.win.choose_method.currentIndex() == 1:
                itterations_text += "Метод Якобі\n\n"
            if self.win.choose_method.currentIndex() == 2:
                itterations_text += "Метод Гауса-Зейделя\n\n"


            while it <= 1000:
                prev_var = [self.x1, self.x2]
                if self.index_method == 1:
                    if self.index_eq == 1:
                        self.x1 = cbrt((self.b * (prev_var[1] ** 3) - self.c) / self.a)
                        self.x2 = sqrt(abs((self.d * (prev_var[0] ** 2) + self.g) / self.f))
                    if self.index_eq == 2:
                        self.x1 = atan(cbrt( (-self.b*cos(self.c*prev_var[1]))/self.a ) )
                        self.x2 = atan((self.d * sin(self.f*prev_var[0])) / self.g)
                    if self.index_eq == 3:
                        k: int
                        if self.a * prev_var[0] + self.b * prev_var[1] < 0:
                            k = -1
                        else:
                            k = 1
                        self.x1 = ((self.a * prev_var[0] + self.b * prev_var[1]) * k) ** (1 / self.c)
                        if self.d * prev_var[0] + self.f * prev_var[1] < 0:
                            k = -1
                        else:
                            k = 1
                        self.x2 = ((self.d * prev_var[0] + self.f * prev_var[1]) * k) ** (1 / self.g)
                elif self.index_method == 2:
                    if self.index_eq == 1:
                        self.x1 = cbrt((self.b * (self.x2 ** 3) - self.c) / self.a)
                        self.x2 = sqrt(abs((self.d * (self.x1 ** 2) + self.g) / self.f))
                    if self.index_eq == 2:
                        self.x1 = atan(cbrt((-self.b * cos(self.c * self.x2)) / self.a))
                        self.x2 = atan((self.d * sin(self.f * self.x1)) / self.g)
                    if self.index_eq == 3:
                        if self.a * self.x1 + self.b * self.x2 < 0:
                            k = -1
                        else:
                            k = 1
                        self.x1 = ((self.a * self.x1 + self.b * self.x2) * k) ** (1 / self.c)
                        if self.d * self.x1 + self.f * self.x2 < 0:
                            k = -1
                        else:
                            k = 1
                        self.x2 = ((self.d * self.x1 + self.f * self.x2) * k) ** (1 / self.g)

                itterations_text += f"Ітерація №{it}\n"
                itterations_text += f"x1 = {self.x1}\n"
                itterations_text += f"x2 = {self.x2}\n\n"

                it += 1
                self.quantity = it
                curr = [self.x1, self.x2]

                if abs(norm_of_vector(curr) - norm_of_vector(prev_var)) <= self.e:
                    itterations_text += f"Кінцевий результат\n"
                    itterations_text += f"x1 = {self.x1}\n"
                    itterations_text += f"x2 = {self.x2}\n\n"
                    break
            if it > 1000:
                self.win.iterations_list.label.setText("Система не збіжна")
                QMessageBox.warning(self.win, "Увага!",
                                    "Метод не збіжний для системи.\nСпробуйте інакші коефіцієнти")
            else:
                if self.index_eq == 1:
                    if int(self.a * (self.x1 ** 3) - self.b * (self.x2 ** 3) + self.c) == 0 and int(
                            self.d * (self.x1 ** 2) - self.f * (self.x2 ** 2) + self.g) == 0:
                        self.win.iterations_list.label.setText(itterations_text)
                        self.draw_graph()
                        self.win.btn_write_to_file.setVisible(True)
                    else:
                        message_text = ""
                        message_text += "Система рівнянь розв'язків не має\n"
                        self.win.iterations_list.label.setText(message_text)
                        QMessageBox.warning(self.win, "Увага", f"Система не має розв'язків\n{int(self.a * (self.x1 ** 3) - self.b * (self.x2 ** 3) + self.c)} != 0\n"
                                                               f"{int(self.d * (self.x1 ** 2) - self.f * (self.x2 ** 2) + self.g)} != 0")
                        self.win.graphics.setVisible(False)
                if self.index_eq == 2:
                    if int(self.a * (tan(self.x1))**3 + self.b * cos(self.c*self.x2)) == 0 and int(self.d * sin(self.f * self.x1) - self.g * tan(self.x2)) == 0:
                        self.win.iterations_list.label.setText(itterations_text)
                        self.draw_graph()
                        self.win.btn_write_to_file.setVisible(True)
                    else:
                        self.win.graphics.setVisible(False)
                        message_text = ""
                        message_text += "Система рівнянь розв'язків не має\n"
                        self.win.iterations_list.label.setText(message_text)
                        QMessageBox.warning(self.win, "Увага", "Система рівнянь не має розв'язків")
                if self.index_eq == 3:
                    if int(log((self.a * self.x1 + self.b * self.x2), self.x1)) == self.c and int(log((self.d*self.x1 + self.f*self.x2), self.x2)) == self.g:
                        self.win.iterations_list.label.setText(itterations_text)
                        self.draw_graph()
                        self.win.btn_write_to_file.setVisible(True)
                    else:
                        message_text = ""
                        message_text += "Система рівнянь розв'язків не має\n"
                        self.win.iterations_list.label.setText(message_text)
                        QMessageBox.warning(self.win, "Увага", "Система розв'язків не має")

        except ZeroDivisionError:
            self.win.iterations_list.label.setText("")
            self.win.equation_solving.setVisible(False)
            QMessageBox.warning(self.win, "Помилка", "Ділення на нуль. Введіть інші значення коефіцієнтів.")
        except (MemoryError, OverflowError):
            self.win.iterations_list.label.setText("")
            self.win.equation_solving.setVisible(False)
            QMessageBox.warning(self.win, "Помилка", "Помилка переповнення. Спробуйте змінити значення. Метод не є збіжним")
        except ArithmeticError:
            self.win.iterations_list.label.setText("")
            self.win.equation_solving.setVisible(False)
            QMessageBox.warning(self.win, "Помилка", "Спробуйте змінити значення. Метод не збіжний для системи")
        except ValueError:
            self.win.iterations_list.label.setText("")
            self.win.equation_solving.setVisible(False)
            QMessageBox.warning(self.win, "Помилка", "Спробуйте змінити значення")


    def unique_solution(self):
        self.need_itteration_procces = True
        self.is_solved = False
        try:
            if self.a == 0 and self.b != 0:
                if self.d == 0 and self.f == 0:
                    if self.index_eq == 1:
                        self.need_itteration_procces = False
                        QMessageBox.warning(self.win, "Помилка", "Система рівнянь не має розв'язків")

                else:
                    if self.index_eq == 1:
                        self.x2 = cbrt(self.c / self.b)
                        self.x1 = sqrt((self.f * (self.x2 ** 2) - self.g) / self.d)
                        self.win.iterations_list.label.setText(
                            f"Система рівнянь розв'язане окремо від ітераційного процесу\nx₁ = {self.x1}\nx₂ = {self.x2}\n")
                        self.need_itteration_procces = False
                        self.is_solved = True

            if self.b == 0 and self.a != 0:
                if self.d == 0 and self.f == 0:
                    if self.index_eq == 1:
                        self.need_itteration_procces = False
                        QMessageBox.warning(self.win, "Помилка", "Система рівнянь не має розв'язків")

                else:
                    if self.index_eq == 1:
                        self.x1 = cbrt(self.c/self.a * (-1))
                        self.x2 = sqrt((self.d * (self.x1 ** 2) + self.g)/self.f)
                        self.win.iterations_list.label.setText(
                            f"Система рівнянь розв'язане окремо від ітераційного процесу\nx₁ = {self.x1}\nx₂ = {self.x2}\n")
                        self.need_itteration_procces = False
                        self.is_solved = True

            if self.d == 0 and self.f != 0:
                if self.a == 0 and self.b == 0:
                    if self.index_eq == 1:
                        self.need_itteration_procces = False
                        QMessageBox.warning(self.win, "Помилка", "Система рівнянь не має розв'язків")

                else:
                    if self.index_eq == 1:
                        self.x2 = sqrt(self.g/self.f)
                        self.x1 = cbrt((self.b * (self.x2**3) - self.c)/self.a)
                        self.win.iterations_list.label.setText(
                            f"Система рівнянь розв'язане окремо від ітераційного процесу\nx₁ = {self.x1}\nx₂ = {self.x2}\n")
                        self.need_itteration_procces = False
                        self.is_solved = True

            if self.f == 0 and self.d != 0:
                if self.a == 0 and self.b == 0:
                    if self.index_eq == 1:
                        self.need_itteration_procces = False
                        QMessageBox.warning(self.win, "Помилка", "Система рівнянь не має розв'язків")

                else:
                    if self.index_eq == 1:
                        self.x1 = sqrt(-self.g/self.d)
                        self.x2 = cbrt((self.a*(self.x1**3)+self.c)/self.b)
                        self.need_itteration_procces = False
                        self.is_solved = True
                        self.win.iterations_list.label.setText(
                            f"Система рівнянь розв'язане окремо від ітераційного процесу\nx₁ = {self.x1}\nx₂ = {self.x2}\n")

            if not self.need_itteration_procces and self.is_solved:
                self.draw_graph()

            if self.need_itteration_procces:
                self.solve_system_of_equations()

        except (ZeroDivisionError, ArithmeticError, ValueError):
            QMessageBox.warning(self.win, "Помилка", "Спробуйте інакші значення")




    def draw_graph(self):
        self.win.graphics.setVisible(True)
        self.win.plot_widget.clear()
        self.win.plot_widget.autoRange()
        max_size = 50000
        if self.index_eq == 1:
            if self.need_itteration_procces is True:
                first_y = np.linspace(-100, 100, max_size)
                first_x = np.cbrt((self.b * (first_y ** 3) - self.c) / self.a)

                second_x_1 = np.linspace(-100, 0, max_size)
                second_y_1 = np.sqrt((self.d * (second_x_1 ** 2) + self.g) / self.f)

                second_x_2 = np.linspace(0, 100, max_size)
                second_y_2 = np.sqrt((self.d * (second_x_2 ** 2) + self.g) / self.f)

                second_x_3 = np.linspace(-100, 0, max_size)
                second_y_3 = -np.sqrt((self.d * (second_x_3 ** 2) + self.g) / self.f)

                second_x_4 = np.linspace(0, 100, max_size)
                second_y_4 = -np.sqrt((self.d * (second_x_4 ** 2) + self.g) / self.f)

                self.win.plot_widget.plot(first_x, first_y, pen={'color': 'yellow', 'width': 2})
                self.win.plot_widget.plot(second_x_1, second_y_1, pen={'color': 'purple', 'width': 2})
                self.win.plot_widget.plot(second_x_2, second_y_2, pen={'color': 'purple', 'width': 2})
                self.win.plot_widget.plot(second_x_3, second_y_3, pen={'color': 'purple', 'width': 2})
                self.win.plot_widget.plot(second_x_4, second_y_4, pen={'color': 'purple', 'width': 2})
            else:
                if self.a == 0:
                    second_x_1 = np.linspace(-100, 0, max_size)
                    second_y_1 = np.sqrt((self.d * (second_x_1 ** 2) + self.g) / self.f)

                    second_x_2 = np.linspace(0, 100, max_size)
                    second_y_2 = np.sqrt((self.d * (second_x_2 ** 2) + self.g) / self.f)

                    second_x_3 = np.linspace(-100, 0, max_size)
                    second_y_3 = -np.sqrt((self.d * (second_x_3 ** 2) + self.g) / self.f)

                    second_x_4 = np.linspace(0, 100, max_size)
                    second_y_4 = -np.sqrt((self.d * (second_x_4 ** 2) + self.g) / self.f)

                    first_x = np.linspace(-100, 100, max_size)
                    first_y = [self.x2 for i in first_x]

                    self.win.plot_widget.plot(first_x, first_y, pen={'color': 'yellow', 'width': 2})
                    self.win.plot_widget.plot(second_x_1, second_y_1, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_2, second_y_2, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_3, second_y_3, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_4, second_y_4, pen={'color': 'purple', 'width': 2})
                if self.b == 0:
                    second_x_1 = np.linspace(-100, 0, max_size)
                    second_y_1 = np.sqrt((self.d * (second_x_1 ** 2) + self.g) / self.f)

                    second_x_2 = np.linspace(0, 100, max_size)
                    second_y_2 = np.sqrt((self.d * (second_x_2 ** 2) + self.g) / self.f)

                    second_x_3 = np.linspace(-100, 0, max_size)
                    second_y_3 = -np.sqrt((self.d * (second_x_3 ** 2) + self.g) / self.f)

                    second_x_4 = np.linspace(0, 100, max_size)
                    second_y_4 = -np.sqrt((self.d * (second_x_4 ** 2) + self.g) / self.f)

                    first_y = np.linspace(-100, 100, max_size)
                    first_x = [self.x1 for i in first_y]

                    self.win.plot_widget.plot(first_x, first_y, pen={'color': 'yellow', 'width': 2})
                    self.win.plot_widget.plot(second_x_1, second_y_1, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_2, second_y_2, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_3, second_y_3, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_4, second_y_4, pen={'color': 'purple', 'width': 2})
                if self.d == 0:
                    first_y = np.linspace(-100, 100, max_size)
                    first_x = np.cbrt((self.b * (first_y ** 3) - self.c) / self.a)

                    second_x_1 = np.linspace(-100, 0, max_size)
                    second_y_1 = [self.x2 for i in second_x_1]

                    second_x_2 = np.linspace(0, 100, max_size)
                    second_y_2 = [self.x2 for i in second_x_2]

                    second_x_3 = np.linspace(-100, 0, max_size)
                    second_y_3 = [-self.x2 for i in second_x_3]

                    second_x_4 = np.linspace(0, 100, max_size)
                    second_y_4 = [-self.x2 for i in second_x_4]

                    self.win.plot_widget.plot(first_x, first_y, pen={'color': 'yellow', 'width': 2})
                    self.win.plot_widget.plot(second_x_1, second_y_1, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_2, second_y_2, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_3, second_y_3, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_4, second_y_4, pen={'color': 'purple', 'width': 2})

                if self.f == 0:
                    first_y = np.linspace(-100, 100, max_size)
                    first_x = np.cbrt((self.b * (first_y ** 3) - self.c) / self.a)

                    second_y_1 = np.linspace(-100, 0, 100)
                    second_x_1 = [self.x1 for i in second_y_1]

                    second_y_2 = np.linspace(0, 100, 100)
                    second_x_2 = [self.x1 for i in second_y_1]

                    second_y_3 = np.linspace(-100, 0, 100)
                    second_x_3 = [-self.x1 for i in second_y_1]

                    second_y_4 = np.linspace(0, 100, 100)
                    second_x_4 = [-self.x1 for i in second_y_1]

                    self.win.plot_widget.plot(first_x, first_y, pen={'color': 'yellow', 'width': 2})
                    self.win.plot_widget.plot(second_x_1, second_y_1, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_2, second_y_2, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_3, second_y_3, pen={'color': 'purple', 'width': 2})
                    self.win.plot_widget.plot(second_x_4, second_y_4, pen={'color': 'purple', 'width': 2})


            solve_point = pg.ScatterPlotItem()
            solve_point.addPoints([{'pos': (self.x1, self.x2), 'symbol': 'o', 'pen': 'b', 'brush': 'g'}])

            self.win.plot_widget.addItem(solve_point)

            self.win.plot_widget.addLegend()
        if self.index_eq == 2:
            first_y = np.linspace(-100, 100, max_size)
            first_x = np.arctan(np.cbrt((-self.b * np.cos(self.c * first_y))/self.a))

            second_x = np.linspace(-100, 100, max_size)
            second_y = np.arctan((self.d * np.sin(self.f * second_x))/self.g)

            solve_point = pg.ScatterPlotItem()
            solve_point.addPoints([{'pos': (self.x1, self.x2), 'symbol': 'o', 'pen': 'b', 'brush': 'g'}])

            self.win.plot_widget.plot(first_x, first_y, pen ={'color': 'yellow', 'width':2})
            self.win.plot_widget.plot(second_x, second_y, pen ={'color': 'purple', 'width':2})

            self.win.plot_widget.addItem(solve_point)

        if self.index_eq == 3:

            first_x_neg = np.linspace(-100, 0, max_size)
            first_x_pos = np.linspace(0, 100, max_size)
            first_y_neg = (first_x_neg**self.c - first_x_neg*self.a)/self.b
            first_y_pos = (first_x_pos**self.c - first_x_pos*self.a)/self.b

            second_y_neg = np.linspace(-100, 0, max_size)
            second_y_pos = np.linspace(0, 100, max_size)
            second_x_neg = ((second_y_neg**self.g - second_y_neg*self.f)/self.d)
            second_x_pos = ((second_y_pos**self.g - second_y_pos*self.f)/self.d)


            self.win.plot_widget.plot(first_x_neg, first_y_neg, pen ={'color': '#FFC400', 'width':2})
            self.win.plot_widget.plot(first_x_pos, first_y_pos, pen ={'color': '#FFC400', 'width':2})
            self.win.plot_widget.plot(second_x_neg, second_y_neg, pen ={'color': '#CC2FDE', 'width':2})
            self.win.plot_widget.plot(second_x_pos, second_y_pos, pen ={'color': '#CC2FDE', 'width':2})

            solve_point = pg.ScatterPlotItem()
            solve_point.addPoints([{'pos': (self.x1, self.x2), 'symbol': 'o', 'pen': 'b', 'brush': 'g'}])
            self.win.plot_widget.addItem(solve_point)
            self.win.plot_widget.setClipToView(True)

        self.win.plot_widget.setClipToView(True)


    def write_to_file(self):
        file = open("Розв'язок.txt", "w")
        if self.index_eq == 1:
            file.write("Алгебраїчна система рівнянь\n")
            file.write(f"\t{self.a} * (x1)^3 - {self.b} * (x2)^3 + {self.c} = 0\n")
            file.write(f"\t{self.d} * (x1)^2 - {self.f} * (x2)^2 + {self.g} = 0\n\n")
        if self.index_eq == 2:
            file.write("Тригонометрична система рівнянь\n")
            file.write(f"\t{self.a} * tg^3(x1) + {self.b} * cos({self.c} * x2) = 0\n")
            file.write(f"\t{self.d} * sin({self.f} * x1) - {self.g} * tg(x2) = 0\n")
        if self.index_eq == 3:
            file.write("Трансцедентна система рівнянь\n")
            file.write(f"\tlog({self.a} * x1 + {self.b} * x2) = {self.c}\n")
            file.write(f"\tlog({self.d} * x1 + {self.f} * x2) = {self.g}\n")
        file.write("Розв'язок системи: \n")
        file.write(f"\tx1 = {self.x1}\n")
        file.write(f"\tx2 = {self.x2}\n")
        file.write(f"\nОбчислення виконані з точністю\ne = {self.e}\nЗа {self.quantity} ітерацій\n")
        if self.index_method == 1:
            file.write("\nСистему розв'язано методом Якобі(простої ітерації)\n")
        if self.index_method == 2:
            file.write("\nСистему розв'язано методом Гауса-Зейделя")
        file.close()


def norm_of_vector(vector:list):
    res = 0
    for i in range(0, len(vector)):
        res += vector[i]**2
    return sqrt(res)