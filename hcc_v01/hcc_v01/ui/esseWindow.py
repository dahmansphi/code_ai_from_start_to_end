
from PySide6.QtWidgets import QMainWindow, QFileDialog
from .ui_window import *

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set the main window to frameless and tranperent background
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

         # activate the close and min button from the customized title bar
        self.ui.close_window_btn.clicked.connect(lambda:self.close())
        self.ui.min_window_btn.clicked.connect(lambda:self.showMinimized())


        # now set the btns to QstackedWidget two pages Add and View case
        self.ui.view_case_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.view_case_page))
        self.ui.add_case_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.add_case_page))


        self.show()