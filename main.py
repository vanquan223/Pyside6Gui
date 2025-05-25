# -*- coding: utf-8 -*-
import os
import sys

from gui.core.json_settings import Settings
from gui.uis.pages.home_ui import Ui_home
from gui.uis.pages.page_1_ui import Ui_Page1
from gui.uis.pages.page_3_ui import Ui_Page3
from gui.uis.windows.main import *
from gui.uis.windows.main.functions_main_window import *
from gui.uis.windows.page1.setup_page1 import SetupPage1
from gui.widgets import *
from qt_core import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        
        # HOME BTN
        if btn.objectName() == "btn_home":
            self.ui.left_menu.select_only_one(btn.objectName())
            
            self.ui.load_pages.home = QWidget()
            self.ui.load_pages.home_ui = Ui_home()
            self.ui.load_pages.home_ui.setupUi(self.ui.load_pages.home)
            self.ui.load_pages.pages.addWidget(self.ui.load_pages.home)
            MainFunctions.set_page(self, self.ui.load_pages.home)
            
            # MainFunctions.set_page(self, self.ui.load_pages.home)
        
        # Home BTN
        if btn.objectName() == "btn_widgets":
            self.ui.left_menu.select_only_one(btn.objectName())
            
            self.ui.load_pages.page_1 = QWidget()
            self.ui.load_pages.page1_ui = Ui_Page1()
            self.ui.load_pages.page1_ui.setupUi(self.ui.load_pages.page_1)
            self.ui.load_pages.pages.addWidget(self.ui.load_pages.page_1)
            MainFunctions.set_page(self, self.ui.load_pages.page_1)
            
            SetupPage1(self.ui)

        # LOAD USER PAGE
        if btn.objectName() == "btn_add_user":
            self.ui.left_menu.select_only_one(btn.objectName())
            
            self.ui.load_pages.page_3 = QWidget()
            self.ui.load_pages.page3_ui = Ui_Page3()
            self.ui.load_pages.page3_ui.setupUi(self.ui.load_pages.page_3)
            self.ui.load_pages.pages.addWidget(self.ui.load_pages.page_3)
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
        
        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////          

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
        
    
    def handle_login(self):
        username = self.ui.load_pages.login_ui.editUsername.text()
        password = self.ui.load_pages.login_ui.editPassword.text()
        # Kiểm tra tài khoản (ví dụ: admin/admin)
        if username == "" and password == "":
            # Chuyển sang home
            self.ui.load_pages.home = QWidget()
            self.ui.load_pages.home_ui = Ui_home()
            self.ui.load_pages.home_ui.setupUi(self.ui.load_pages.home)
            self.ui.load_pages.pages.addWidget(self.ui.load_pages.home)
            
            MainFunctions.set_page(self, self.ui.load_pages.home)
            # Hiện left menu
            self.ui.left_menu_frame.setVisible(True)
        else:
            QMessageBox.warning(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())