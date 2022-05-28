# IMPORT MODULES
import sys
import os
from gui.widgets.py_push_button import PyPushButton

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import Ui_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Curso de Python e PySide6')
        
        # SETUP MAIN WINDOW
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        
        # TOGGLE BUTTON
        self.ui.toggle_btn.clicked.connect(self.toggle_button)
        
        # BTN HOME
        self.ui.btn_1.clicked.connect(self.show_page_1)
        
        # BTN PAGE 2
        self.ui.btn_2.clicked.connect(self.show_page_2)
        
        # BTN SETTINGS
        self.ui.settings.clicked.connect(self.show_page_3)
        
        # BTN CHANGE LABEL
        self.ui.ui_pages.pushButton.clicked.connect(self.change_button)
        
        # EXIBE A APLICAÇÃO
        self.show()
        
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
        
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)
        
    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)
        
    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings.set_active(True)
        
    def toggle_button(self):
        # GET MENU WIDTH
        menu_width = self.ui.left_menu.width()
        
        # CHECK WIDTH
        width = 50
        if menu_width == 50:
            width = 240
        
        # START ANIMATION
        self.animation = QPropertyAnimation(self.ui.left_menu, b'minimumWidth')
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(250)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()
        
    def change_button(self):
        # GET TEXT OF LINEEDIT
        text = self.ui.ui_pages.lineEdit.text()
        if text == '':
            return
        
        # SET TEXT IN LABEL
        self.ui.ui_pages.label_3.setText(text)
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
        
