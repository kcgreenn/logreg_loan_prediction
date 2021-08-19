import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from View import main_screen

def foo(exctype, value, tb):
    print('My Error Information')
    print('Type:', exctype)
    print('Value:', value)
    print('Traceback:', tb)

sys.excepthook = foo

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a dialog window
    app = QApplication(sys.argv)
    window = QMainWindow()
    main_scrn = main_screen.Ui_MainWindow()
    main_scrn.setupUi(window)
    window.show()
    main_scrn.load_data()

    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
