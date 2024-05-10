# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'channels_view.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Channels_View(object):
    def setupUi(self, Channels_View):
        if not Channels_View.objectName():
            Channels_View.setObjectName(u"Channels_View")
        Channels_View.resize(270, 400)
        Channels_View.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_5 = QLabel(Channels_View)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, -10, 261, 411))
        self.groupBox_3 = QGroupBox(Channels_View)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 271, 411))
        self.groupBox_3.setMinimumSize(QSize(261, 411))
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.listwidget_channels = QListWidget(self.groupBox_3)
        self.listwidget_channels.setObjectName(u"listwidget_channels")
        self.listwidget_channels.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 219, 237);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(48, 88, 162);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(28, 44, 81);\n"
"}")

        self.gridLayout.addWidget(self.listwidget_channels, 2, 0, 1, 1)

        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.label_9)

        self.spinbox_diameter = QDoubleSpinBox(self.frame)
        self.spinbox_diameter.setObjectName(u"spinbox_diameter")

        self.horizontalLayout.addWidget(self.spinbox_diameter)

        self.btn_apply_diameter = QPushButton(self.frame)
        self.btn_apply_diameter.setObjectName(u"btn_apply_diameter")
        self.btn_apply_diameter.setMinimumSize(QSize(60, 25))
        self.btn_apply_diameter.setMaximumSize(QSize(45, 16777215))
        self.btn_apply_diameter.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 219, 237);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(48, 88, 162);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(28, 44, 81);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_apply_diameter)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(212, 0))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_enable = QPushButton(self.groupBox)
        self.btn_enable.setObjectName(u"btn_enable")
        self.btn_enable.setMinimumSize(QSize(0, 25))
        self.btn_enable.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 219, 237);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(48, 88, 162);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(28, 44, 81);\n"
"}")

        self.verticalLayout.addWidget(self.btn_enable)

        self.btn_set_tandem = QPushButton(self.groupBox)
        self.btn_set_tandem.setObjectName(u"btn_set_tandem")
        self.btn_set_tandem.setMinimumSize(QSize(0, 25))
        self.btn_set_tandem.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(199, 219, 237);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(48, 88, 162);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(28, 44, 81);\n"
"}")

        self.verticalLayout.addWidget(self.btn_set_tandem)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)


        self.retranslateUi(Channels_View)

        QMetaObject.connectSlotsByName(Channels_View)
    # setupUi

    def retranslateUi(self, Channels_View):
        Channels_View.setWindowTitle(QCoreApplication.translate("Channels_View", u"Form", None))
        self.label_5.setText("")
        self.groupBox_3.setTitle("")
        self.label_10.setText(QCoreApplication.translate("Channels_View", u"Channels", None))
        self.label_9.setText(QCoreApplication.translate("Channels_View", u"channels diameter", None))
        self.btn_apply_diameter.setText(QCoreApplication.translate("Channels_View", u"Apply", None))
        self.groupBox.setTitle(QCoreApplication.translate("Channels_View", u"Channel Details", None))
        self.btn_enable.setText(QCoreApplication.translate("Channels_View", u"Disable", None))
        self.btn_set_tandem.setText(QCoreApplication.translate("Channels_View", u"Set as Tandem", None))
    # retranslateUi

