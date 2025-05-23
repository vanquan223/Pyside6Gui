# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from gui.uis.pages.login_page_ui import Ui_LoginPage
from gui.uis.pages.page_1_ui import Ui_Page1
from gui.uis.pages.page_2_ui import Ui_Page2
from gui.uis.pages.page_3_ui import Ui_Page3

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        
        # Login Page
        self.page_login = QWidget()
        self.login_ui = Ui_LoginPage()
        self.login_ui.setupUi(self.page_login)

        # Page 1
        self.page_1 = QWidget()
        self.page1_ui = Ui_Page1()
        self.page1_ui.setupUi(self.page_1)

        # Page 2
        self.page_2 = QWidget()
        self.page2_ui = Ui_Page2()
        self.page2_ui.setupUi(self.page_2)

        # Page 3
        self.page_3 = QWidget()
        self.page3_ui = Ui_Page3()
        self.page3_ui.setupUi(self.page_3)

        self.pages.addWidget(self.page_login)
        self.pages.addWidget(self.page_1)
        self.pages.addWidget(self.page_2)
        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
    # retranslateUi
