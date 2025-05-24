# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_home(object):
    def setupUi(self, home):
        if not home.objectName():
            home.setObjectName(u"home")
        home.resize(630, 424)
        self.home_layout = QVBoxLayout(home)
        self.home_layout.setObjectName(u"home_layout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.statisticsLayout = QHBoxLayout()
        self.statisticsLayout.setObjectName(u"statisticsLayout")

        self.verticalLayout.addLayout(self.statisticsLayout)

        self.chartLayout = QVBoxLayout()
        self.chartLayout.setObjectName(u"chartLayout")

        self.verticalLayout.addLayout(self.chartLayout)


        self.home_layout.addLayout(self.verticalLayout)


        self.retranslateUi(home)

        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        pass
    # retranslateUi

