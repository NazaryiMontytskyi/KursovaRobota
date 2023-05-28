import sys
from PyQt5.QtWidgets import *


class WinMessages:

    def __init__(self, program_window):
        self.win = program_window


    def system_no_solutions(self):
        warning_message = "Неможливо знайти розв'язок системи. Спробуйте використати інші значення коефіцієнтів."
        self.win.btn_write_to_file.setVisible(False)
        self.win.iterations_list.label.setText(warning_message)
        self.win.graphics.setVisible(False)
        QMessageBox.warning(self.win, "Увага", "Неможливо знайти розв'язок системи")


    def system_value_error(self):
        warning_message = "При даних значеннях неможливо знайти розв'язок системи. Змініть значення коефіцієнтів"
        self.win.iterations_list.label.setText(warning_message)
        self.win.btn_write_to_file.setVisible(False)
        self.win.graphics.setVisible(False)
        QMessageBox.warning(self.win, "Помилка", warning_message)


    def system_endless_loop(self):
        warning_message = "Ітераційні методи не є збіжними для системи. Значення розбігаються. Спробуйте інші значення."
        self.win.iterations_list.label.setText(warning_message)
        self.win.btn_write_to_file.setVisible(False)
        self.win.graphics.setVisible(False)
        QMessageBox.warning(self.win, "Помилка", warning_message)


    def value_out_of_range(self):
        self.win.btn_write_to_file.setVisible(False)
        self.win.graphics.setVisible(False)
        QMessageBox.warning(self.win, "Помилка", "Завеликі значення, введіть значення параметрів у проміжку [-30; 30]\n")

