# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_report(object):
    def setupUi(self, report):
        if not report.objectName():
            report.setObjectName(u"report")
        report.resize(820, 527)
        self.home_layout = QVBoxLayout(report)
        self.home_layout.setObjectName(u"home_layout")
        self.reportLayout = QHBoxLayout()
        self.reportLayout.setObjectName(u"reportLayout")
        self.editReportLayout = QVBoxLayout()
        self.editReportLayout.setObjectName(u"editReportLayout")
        self.labelReport = QLabel(report)
        self.labelReport.setObjectName(u"labelReport")

        self.editReportLayout.addWidget(self.labelReport)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelAddReport = QLabel(report)
        self.labelAddReport.setObjectName(u"labelAddReport")

        self.horizontalLayout_3.addWidget(self.labelAddReport)

        self.addReportButton = QPushButton(report)
        self.addReportButton.setObjectName(u"addReportButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.addReportButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.addReportButton)

        self.labelIdReport = QLabel(report)
        self.labelIdReport.setObjectName(u"labelIdReport")

        self.horizontalLayout_3.addWidget(self.labelIdReport)


        self.horizontalLayout.addLayout(self.horizontalLayout_3)


        self.editReportLayout.addLayout(self.horizontalLayout)

        self.levelReport = QSpinBox(report)
        self.levelReport.setObjectName(u"levelReport")

        self.editReportLayout.addWidget(self.levelReport)

        self.procedureCode = QSpinBox(report)
        self.procedureCode.setObjectName(u"procedureCode")

        self.editReportLayout.addWidget(self.procedureCode)

        self.titleReport = QLineEdit(report)
        self.titleReport.setObjectName(u"titleReport")

        self.editReportLayout.addWidget(self.titleReport)

        self.descReport = QPlainTextEdit(report)
        self.descReport.setObjectName(u"descReport")

        self.editReportLayout.addWidget(self.descReport)

        self.addImageReport = QLineEdit(report)
        self.addImageReport.setObjectName(u"addImageReport")

        self.editReportLayout.addWidget(self.addImageReport)

        self.listImageReport = QListWidget(report)
        self.listImageReport.setObjectName(u"listImageReport")

        self.editReportLayout.addWidget(self.listImageReport)

        self.pushButton_3 = QPushButton(report)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.editReportLayout.addWidget(self.pushButton_3)


        self.reportLayout.addLayout(self.editReportLayout)

        self.listReportLayout = QVBoxLayout()
        self.listReportLayout.setObjectName(u"listReportLayout")
        self.label_4 = QLabel(report)
        self.label_4.setObjectName(u"label_4")

        self.listReportLayout.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(report)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.searchReportButton = QPushButton(report)
        self.searchReportButton.setObjectName(u"searchReportButton")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.searchReportButton.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.searchReportButton)


        self.listReportLayout.addLayout(self.horizontalLayout_4)

        self.listReport = QListView(report)
        self.listReport.setObjectName(u"listReport")

        self.listReportLayout.addWidget(self.listReport)


        self.reportLayout.addLayout(self.listReportLayout)


        self.home_layout.addLayout(self.reportLayout)


        self.retranslateUi(report)

        QMetaObject.connectSlotsByName(report)
    # setupUi

    def retranslateUi(self, report):
        self.labelReport.setText(QCoreApplication.translate("report", u"B\u00e1o l\u1ed7i", None))
        self.labelAddReport.setText(QCoreApplication.translate("report", u"G\u1eedi b\u00e1o l\u1ed7i \u0111\u1ec3 \u0111\u01b0\u1ee3c h\u1ed7 tr\u1ee3", None))
        self.addReportButton.setText("")
        self.labelIdReport.setText(QCoreApplication.translate("report", u"TextLabel", None))
        self.titleReport.setPlaceholderText(QCoreApplication.translate("report", u"Nh\u1eadp ti\u00eau \u0111\u1ec1 ng\u1eafn g\u1ecdn b\u00e1o l\u1ed7i", None))
        self.descReport.setPlaceholderText(QCoreApplication.translate("report", u"Nh\u1eadp chi ti\u1ebft b\u00e1o l\u1ed7i", None))
        self.addImageReport.setPlaceholderText(QCoreApplication.translate("report", u"Ch\u1ecdn \u1ea3nh ch\u1ee5p m\u00e0n h\u00ecnh l\u1ed7i v\u00e0o \u0111\u00e2y", None))
        self.pushButton_3.setText(QCoreApplication.translate("report", u"G\u1eedi", None))
        self.label_4.setText(QCoreApplication.translate("report", u"L\u1ecbch s\u1eed b\u00e1o l\u1ed7i", None))
        self.label_5.setText(QCoreApplication.translate("report", u"C\u00e1c b\u00e1o l\u1ed7i g\u1ea7n \u0111\u00e2y v\u00e0 tr\u1ea1ng th\u00e1i x\u1eed l\u00fd", None))
        self.searchReportButton.setText("")
        pass
    # retranslateUi

