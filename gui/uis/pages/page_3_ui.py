# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_3.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Page3(object):
    def setupUi(self, page_3):
        if not page_3.objectName():
            page_3.setObjectName(u"page_3")
        self.page_3_layout = QVBoxLayout(page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        font = QFont()
        font.setPointSize(16)
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)


        self.retranslateUi(page_3)

        QMetaObject.connectSlotsByName(page_3)
    # setupUi

    def retranslateUi(self, page_3):
        self.empty_page_label.setText(QCoreApplication.translate("Page3", u"Empty Page 3", None))
        pass
    # retranslateUi

