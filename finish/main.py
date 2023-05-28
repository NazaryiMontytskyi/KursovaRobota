from gui import *


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = ProgrammWindow()
    sys.exit(app.exec_())