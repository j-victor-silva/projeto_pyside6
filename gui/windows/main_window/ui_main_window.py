# IMPORT QT CORE
from qt_core import *

# IMPORT PAGES
from gui.pages.ui_pages import Ui_StackedWidget

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

# MAIN WINDOW
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName('MainWindow')
        
        # ///////////////////////////////////////////////////////////////////    
        # SET INITIAL PARAMETERS
        parent.resize(960, 540)
        parent.setMinimumSize(960, 540)
        
        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        
        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        # ///////////////////////////////////////////////////////////////////    
        
        # ///////////////////////////////////////////////////////////////////
        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet('background-color: #44475a')
        self.left_menu.setMinimumWidth(50)
        self.left_menu.setMaximumWidth(50)
        
        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        # ///////////////////////////////////////////////////////////////////
        
        # ///////////////////////////////////////////////////////////////////
        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName('left_menu_top_frame')
        self.left_menu_top_frame.setStyleSheet('#left_menu_top_frame { background-color: red; }')
        
        # TOP BTNS
        self.toggle_btn = PyPushButton(
            text='Ocultar Menu',
            icon_path='icon_menu.svg',
        )
        self.btn_1 = PyPushButton(
            text='Página Inicial',
            icon_path='pagina_inicial.svg',
            is_active=True
        )
        self.btn_2 = PyPushButton(
            text='Página 2',
            icon_path='pagina_2.svg'
        )
        
        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)
        
        # ADD BTNS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_btn)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        # ///////////////////////////////////////////////////////////////////
        
        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # ///////////////////////////////////////////////////////////////////
        # BOT FRAME MENU
        self.left_menu_bot_frame = QFrame()
        self.left_menu_bot_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName('left_menu_bot_frame')
        self.left_menu_bot_frame.setStyleSheet('#left_menu_bot_frame { background-color: red; }')
        
        # BOT BTNS
        self.settings = PyPushButton(
            text='Settings',
            icon_path='settings.svg'
        )
        
        # BOT FRAME LAYOUT
        self.left_menu_bot_layout = QVBoxLayout(self.left_menu_bot_frame)
        self.left_menu_bot_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bot_layout.setSpacing(0)
        
        # ADD BTNS TO LAYOUT
        self.left_menu_bot_layout.addWidget(self.settings)
        
        # LABEL VERSION
        self.left_menu_label_version = QLabel('v1.0.0')
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet('background-color: #3c3f50; color: #c3ccdf')
        
        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bot_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        # ///////////////////////////////////////////////////////////////////
        
        # ///////////////////////////////////////////////////////////////////
        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet('background-color: #282a36')
        
        # TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet('background-color: #21232d; color: #6272a4')
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)
        
        # LEFT LABEL
        self.top_label_left = QLabel('Essa é minha primeira aplicação com PySide6')
        
        # TOP SPACER
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # RIGHT LABEL
        self.top_label_right = QLabel('Página Inicial')
        self.top_label_right.setStyleSheet('font: 700 9pt "Segoe UI"')
        
        # ADD TO LAYOUT
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)
        # ///////////////////////////////////////////////////////////////////
        
        # ///////////////////////////////////////////////////////////////////
        # APPLICATION PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet('font: 700; font-size: 12pt; color: #f8f8f2')
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)
        # ///////////////////////////////////////////////////////////////////
        
        # ///////////////////////////////////////////////////////////////////
        # BOTTOM BAR
        self.bot_bar = QFrame()
        self.bot_bar.setMinimumHeight(30)
        self.bot_bar.setMaximumHeight(30)
        self.bot_bar.setStyleSheet('background-color: #21232d; color: #6272a4')
        self.bot_bar_layout = QHBoxLayout(self.bot_bar)
        self.bot_bar_layout.setContentsMargins(10,0,10,0)
        
        # LEFT LABEL
        self.bot_label_left = QLabel('Criado por: João V. da Silva')
        
        # BOT SPACER
        self.bot_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # RIGHT LABEL
        self.bot_label_right = QLabel('5 2022')
        self.bot_label_right.setStyleSheet('font: 700 9pt "Segoe UI"')
        
        # ADD TO LAYOUT
        self.bot_bar_layout.addWidget(self.bot_label_left)
        self.bot_bar_layout.addItem(self.bot_spacer)
        self.bot_bar_layout.addWidget(self.bot_label_right)
        # ///////////////////////////////////////////////////////////////////
        
        # ///////////////////////////////////////////////////////////////////
        # CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        
        # ADD TO CONTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bot_bar)
        # ///////////////////////////////////////////////////////////////////
        
        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # SET CENTRAL WIDGHET
        parent.setCentralWidget(self.central_frame)
        