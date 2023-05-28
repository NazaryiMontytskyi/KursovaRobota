import sys
from PyQt5.QtWidgets import *


class FileManager:

    name = "Розв'язок.txt"

    def __init__(self, programm_window):
        self.win = programm_window

    def share_solution_to_file(self):

        dest = open(FileManager.name, "w")

        if self.win.solving_equation.index_eq == 1:
            dest.write("Алгебраїчна система рівнянь\n\n")
            dest.write(f"\t{self.win.solving_equation.a} * (x1)^3 - {self.win.solving_equation.b} * (x2)^3 + {self.win.solving_equation.c} = 0\n")
            dest.write(f"\t{self.win.solving_equation.d} * (x1)^2 - {self.win.solving_equation.f} * (x2)^2 + {self.win.solving_equation.g} = 0\n")
        if self.win.solving_equation.index_eq == 2:
            dest.write("Тригонометрична система рівнянь\n\n")
            dest.write(f"\t{self.win.solving_equation.a} * tg^3(x1) + {self.win.solving_equation.b} * cos({self.win.solving_equation.c} * x2) = 0\n")
            dest.write(f"\t{self.win.solving_equation.d} * sin({self.win.solving_equation.f} * x1) - {self.win.solving_equation.g} * tg(x2) = 0\n")
        if self.win.solving_equation.index_eq == 3:
            dest.write("Трансцедентна система рівнянь\n\n")
            dest.write(f"\tlog({self.win.solving_equation.a} * x1 + {self.win.solving_equation.b} * x2) = {self.win.solving_equation.c}\n")
            dest.write(f"\tlog({self.win.solving_equation.d} * x1 + {self.win.solving_equation.f} * x2) = {self.win.solving_equation.g}\n")

        dest.write("Розв'язок системи:\n")
        dest.write(f"\tx1 = {self.win.solving_equation.x1}\n")
        dest.write(f"\tx2 = {self.win.solving_equation.x2}\n")

        if self.win.solving_equation.need_itteration_procces:
            dest.write(f"\nРозв'язки виконані із точністю\n\te = {self.win.solving_equation.e}\n\tКількість ітерацій: {self.win.solving_equation.it - 1}\n")
            dest.write(f"\nРозв'язання виконане методом ")
            if self.win.solving_equation.index_method == 1:
                dest.write("Якобі(простої ітерації)\n")
            if self.win.solving_equation.index_method == 2:
                dest.write("Гауса-Зейделя")
        else:
            dest.write("\nСистема рівнянь розв'язна окремо від ітераційного процесу")

        dest.close()