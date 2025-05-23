# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginPage(object):
    def setupUi(self, page_login):
        if not page_login.objectName():
            page_login.setObjectName(u"page_login")
        self.page_login_layout = QVBoxLayout(page_login)
        self.page_login_layout.setSpacing(5)
        self.page_login_layout.setObjectName(u"page_login_layout")
        self.page_login_layout.setContentsMargins(5, 5, 5, 5)
        self.login_base = QFrame(page_login)
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


        self.page_login_layout.addWidget(self.login_base, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(page_login)

        QMetaObject.connectSlotsByName(page_login)
    # setupUi

    def retranslateUi(self, page_login):
        self.labelTitle.setText(QCoreApplication.translate("LoginPage", u"RPA iGate", None))
        self.labelDesc.setText(QCoreApplication.translate("LoginPage", u"H\u1ec7 th\u1ed1ng t\u1ef1 \u0111\u1ed9ng ho\u00e1 thao t\u00e1c \u1ee9ng d\u1ee5ng", None))
        self.editUsername.setPlaceholderText(QCoreApplication.translate("LoginPage", u"T\u00ean \u0111\u0103ng nh\u1eadp (*)", None))
        self.editPassword.setPlaceholderText(QCoreApplication.translate("LoginPage", u"M\u1eadt kh\u1ea9u (*)", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginPage", u"\u0110\u0103ng nh\u1eadp", None))
        self.btnSSO.setText(QCoreApplication.translate("LoginPage", u"\u0110\u0103ng nh\u1eadp SSO", None))
        self.labelForgot.setText(QCoreApplication.translate("LoginPage", u"B\u1ea1n kh\u00f4ng nh\u1edb m\u1eadt kh\u1ea9u?", None))
        self.labelReset.setText(QCoreApplication.translate("LoginPage", u"<a href='#' style='color:#2583f5'>Qu\u00ean m\u1eadt kh\u1ea9u</a>", None))
        pass
    # retranslateUi

