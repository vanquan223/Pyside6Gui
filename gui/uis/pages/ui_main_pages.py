# -*- coding: utf-8 -*-
from gui.uis.pages.login_page_ui import Ui_LoginPage
from qt_core import *


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
        self.pages.addWidget(self.page_login)
        
        self.main_pages_layout.addWidget(self.pages)

        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
    # retranslateUi
