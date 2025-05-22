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
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.login_base = QFrame(self.page_1)
        self.login_base.setObjectName(u"login_base")
        self.login_base.setMinimumSize(QSize(500, 380))
        self.login_base.setMaximumSize(QSize(500, 380))
        self.login_base.setStyleSheet(u"background: #fff; border-radius: 24px;")
        self.login_base.setFrameShape(QFrame.Shape.NoFrame)
        self.login_base.setFrameShadow(QFrame.Shadow.Raised)
        self.center_page_layout = QVBoxLayout(self.login_base)
        self.center_page_layout.setSpacing(0)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 15, 0, 15)
        self.labelTitle = QLabel(self.login_base)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setMinimumSize(QSize(400, 40))
        self.labelTitle.setMaximumSize(QSize(400, 40))
        self.labelTitle.setStyleSheet(u"font-size: 28px; color: #2583f5; font-weight: 500;")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.center_page_layout.addWidget(self.labelTitle, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelDesc = QLabel(self.login_base)
        self.labelDesc.setObjectName(u"labelDesc")
        self.labelDesc.setMinimumSize(QSize(400, 30))
        self.labelDesc.setMaximumSize(QSize(400, 30))
        self.labelDesc.setStyleSheet(u"font-size: 16px; color: #222;")
        self.labelDesc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.center_page_layout.addWidget(self.labelDesc, 0, Qt.AlignmentFlag.AlignHCenter)

        self.editUsername = QLineEdit(self.login_base)
        self.editUsername.setObjectName(u"editUsername")
        self.editUsername.setMinimumSize(QSize(400, 40))
        self.editUsername.setMaximumSize(QSize(400, 40))
        self.editUsername.setStyleSheet(u"font-size: 16px; border: 1px solid #e0e0e0; border-radius: 8px; padding-left: 12px; background: #fafbfc;")

        self.center_page_layout.addWidget(self.editUsername, 0, Qt.AlignmentFlag.AlignHCenter)

        self.editPassword = QLineEdit(self.login_base)
        self.editPassword.setObjectName(u"editPassword")
        self.editPassword.setMinimumSize(QSize(400, 40))
        self.editPassword.setMaximumSize(QSize(400, 40))
        self.editPassword.setStyleSheet(u"font-size: 16px; border: 1px solid #e0e0e0; border-radius: 8px; padding-left: 12px; background: #fafbfc;")
        self.editPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.center_page_layout.addWidget(self.editPassword, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnLogin = QPushButton(self.login_base)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setEnabled(True)
        self.btnLogin.setMinimumSize(QSize(400, 40))
        self.btnLogin.setMaximumSize(QSize(400, 40))
        self.btnLogin.setStyleSheet(u"font-size: 18px; background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #bdbdbd, stop:1 #e0e0e0); color: #fff; border-radius: 8px;")

        self.center_page_layout.addWidget(self.btnLogin, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btnSSO = QPushButton(self.login_base)
        self.btnSSO.setObjectName(u"btnSSO")
        self.btnSSO.setMinimumSize(QSize(400, 40))
        self.btnSSO.setMaximumSize(QSize(400, 40))
        self.btnSSO.setStyleSheet(u"font-size: 18px; background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2583f5, stop:1 #1a6be0); color: #fff; border-radius: 8px;")

        self.center_page_layout.addWidget(self.btnSSO, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame = QFrame(self.login_base)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 30))
        self.frame.setMaximumSize(QSize(400, 30))
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.labelForgot = QLabel(self.frame)
        self.labelForgot.setObjectName(u"labelForgot")
        self.labelForgot.setMinimumSize(QSize(0, 30))
        self.labelForgot.setMaximumSize(QSize(16777215, 30))
        self.labelForgot.setStyleSheet(u"font-size: 13px; color: #444;")
        self.labelForgot.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelForgot)

        self.labelReset = QLabel(self.frame)
        self.labelReset.setObjectName(u"labelReset")
        self.labelReset.setMinimumSize(QSize(0, 30))
        self.labelReset.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.labelReset.setAutoFillBackground(False)
        self.labelReset.setStyleSheet(u"font-size: 13px; color: #2583f5;")
        self.labelReset.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.labelReset.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.labelReset)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.center_page_layout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter)


        self.page_1_layout.addWidget(self.login_base, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 215, 266))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.labelTitle.setText(QCoreApplication.translate("MainPages", u"RPA iGate", None))
        self.labelDesc.setText(QCoreApplication.translate("MainPages", u"H\u1ec7 th\u1ed1ng t\u1ef1 \u0111\u1ed9ng ho\u00e1 thao t\u00e1c \u1ee9ng d\u1ee5ng", None))
        self.editUsername.setPlaceholderText(QCoreApplication.translate("MainPages", u"T\u00ean \u0111\u0103ng nh\u1eadp (*)", None))
        self.editPassword.setPlaceholderText(QCoreApplication.translate("MainPages", u"M\u1eadt kh\u1ea9u (*)", None))
        self.btnLogin.setText(QCoreApplication.translate("MainPages", u"\u0110\u0103ng nh\u1eadp", None))
        self.btnSSO.setText(QCoreApplication.translate("MainPages", u"\u0110\u0103ng nh\u1eadp SSO", None))
        self.labelForgot.setText(QCoreApplication.translate("MainPages", u"B\u1ea1n kh\u00f4ng nh\u1edb m\u1eadt kh\u1ea9u?", None))
        self.labelReset.setText(QCoreApplication.translate("MainPages", u"<a href='#' style='color:#2583f5'>Qu\u00ean m\u1eadt kh\u1ea9u</a>", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi
