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
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Channels_View(object):
    def setupUi(self, Channels_View):
        if not Channels_View.objectName():
            Channels_View.setObjectName(u"Channels_View")
        Channels_View.resize(270, 5000)
        Channels_View.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_5 = QLabel(Channels_View)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, -10, 261, 411))
        self.label_5.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.groupBox_3 = QGroupBox(Channels_View)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 271, 5000))
        self.groupBox_3.setMinimumSize(QSize(271, 411))
        self.groupBox_3.setMaximumSize(QSize(271, 16777215))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listwidget_channels = QListWidget(self.groupBox_3)
        self.listwidget_channels.setObjectName(u"listwidget_channels")
        self.listwidget_channels.setMinimumSize(QSize(251, 200))
        self.listwidget_channels.setMaximumSize(QSize(251, 200))
        self.listwidget_channels.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.gridLayout.addWidget(self.listwidget_channels, 4, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.top_menu_bar = QWidget(self.groupBox_3)
        self.top_menu_bar.setObjectName(u"top_menu_bar")
        self.top_menu_bar.setMinimumSize(QSize(270, 70))
        self.top_menu_bar.setMaximumSize(QSize(16777215, 70))
        self.top_menu_bar.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.btn_enable = QPushButton(self.top_menu_bar)
        self.btn_enable.setObjectName(u"btn_enable")
        self.btn_enable.setGeometry(QRect(0, 0, 251, 33))
        self.btn_enable.setMinimumSize(QSize(240, 33))
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
        self.btn_set_tandem = QPushButton(self.top_menu_bar)
        self.btn_set_tandem.setObjectName(u"btn_set_tandem")
        self.btn_set_tandem.setGeometry(QRect(0, 30, 251, 33))
        self.btn_set_tandem.setMinimumSize(QSize(240, 33))
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

        self.gridLayout.addWidget(self.top_menu_bar, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(228, 35, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(108, 0))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.horizontalLayout.addWidget(self.label_9)

        self.spinbox_diameter = QDoubleSpinBox(self.frame)
        self.spinbox_diameter.setObjectName(u"spinbox_diameter")
        self.spinbox_diameter.setMinimumSize(QSize(20, 0))
        self.spinbox_diameter.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.spinbox_diameter)

        self.btn_apply_settings = QPushButton(self.frame)
        self.btn_apply_settings.setObjectName(u"btn_apply_settings")
        self.btn_apply_settings.setMinimumSize(QSize(45, 20))
        self.btn_apply_settings.setMaximumSize(QSize(45, 16777215))
        self.btn_apply_settings.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_apply_settings)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.horizontalLayout_3.addWidget(self.label)

        self.sb_needle_length = QDoubleSpinBox(self.groupBox_3)
        self.sb_needle_length.setObjectName(u"sb_needle_length")
        self.sb_needle_length.setMinimumSize(QSize(135, 18))
        self.sb_needle_length.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_needle_length.setMaximum(350.000000000000000)

        self.horizontalLayout_3.addWidget(self.sb_needle_length)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.retranslateUi(Channels_View)

        QMetaObject.connectSlotsByName(Channels_View)
    # setupUi

    def retranslateUi(self, Channels_View):
        Channels_View.setWindowTitle(QCoreApplication.translate("Channels_View", u"Form", None))
        self.label_5.setText("")
        self.groupBox_3.setTitle("")
        self.label_10.setText(QCoreApplication.translate("Channels_View", u"Channels", None))
        self.btn_enable.setText(QCoreApplication.translate("Channels_View", u"Disable", None))
        self.btn_set_tandem.setText(QCoreApplication.translate("Channels_View", u"Set as Tandem", None))
        self.label_9.setText(QCoreApplication.translate("Channels_View", u"Channels Diameter", None))
        self.btn_apply_settings.setText(QCoreApplication.translate("Channels_View", u"Apply", None))
        self.label.setText(QCoreApplication.translate("Channels_View", u"Needle Length", None))
        self.sb_needle_length.setSuffix(QCoreApplication.translate("Channels_View", u" mm", None))
    # retranslateUi

