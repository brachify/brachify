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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Channels_View(object):
    def setupUi(self, Channels_View):
        if not Channels_View.objectName():
            Channels_View.setObjectName(u"Channels_View")
        Channels_View.resize(290, 4095)
        Channels_View.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.verticalLayout = QVBoxLayout(Channels_View)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(Channels_View)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QSize(290, 411))
        self.groupBox.setMaximumSize(QSize(290, 16777215))
        self.groupBox.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listwidget_channels = QListWidget(self.groupBox)
        self.listwidget_channels.setObjectName(u"listwidget_channels")
        self.listwidget_channels.setMinimumSize(QSize(251, 200))
        self.listwidget_channels.setMaximumSize(QSize(16777215, 16777215))
        self.listwidget_channels.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.gridLayout.addWidget(self.listwidget_channels, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(228, 400000000, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(6)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(108, 18))
        self.label_4.setMaximumSize(QSize(16777215, 18))
        self.label_4.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.spinbox_diameter = QDoubleSpinBox(self.groupBox)
        self.spinbox_diameter.setObjectName(u"spinbox_diameter")
        self.spinbox_diameter.setMinimumSize(QSize(20, 0))
        self.spinbox_diameter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinbox_diameter.setMinimum(0.300000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinbox_diameter)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 18))
        self.label.setMaximumSize(QSize(16777215, 18))
        self.label.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.sb_needle_length = QDoubleSpinBox(self.groupBox)
        self.sb_needle_length.setObjectName(u"sb_needle_length")
        self.sb_needle_length.setMinimumSize(QSize(20, 0))
        self.sb_needle_length.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_needle_length.setMaximum(350.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sb_needle_length)

        self.sb_threading_dept = QDoubleSpinBox(self.groupBox)
        self.sb_threading_dept.setObjectName(u"sb_threading_dept")
        self.sb_threading_dept.setMinimumSize(QSize(20, 0))
        self.sb_threading_dept.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_threading_dept.setMaximum(350.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sb_threading_dept)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 18))
        self.label_2.setMaximumSize(QSize(16777215, 18))
        self.label_2.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 18))
        self.label_3.setMaximumSize(QSize(16777215, 18))
        self.label_3.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.sb_threading_diameter = QDoubleSpinBox(self.groupBox)
        self.sb_threading_diameter.setObjectName(u"sb_threading_diameter")
        self.sb_threading_diameter.setMinimumSize(QSize(20, 0))
        self.sb_threading_diameter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_threading_diameter.setMaximum(350.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sb_threading_diameter)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_enable = QPushButton(self.groupBox)
        self.btn_enable.setObjectName(u"btn_enable")
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

        self.verticalLayout_2.addWidget(self.btn_enable)

        self.btn_set_tandem = QPushButton(self.groupBox)
        self.btn_set_tandem.setObjectName(u"btn_set_tandem")
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

        self.verticalLayout_2.addWidget(self.btn_set_tandem)


        self.gridLayout.addLayout(self.verticalLayout_2, 5, 0, 1, 1)

        self.btn_apply_settings = QPushButton(self.groupBox)
        self.btn_apply_settings.setObjectName(u"btn_apply_settings")
        self.btn_apply_settings.setMinimumSize(QSize(240, 33))
        self.btn_apply_settings.setMaximumSize(QSize(16777215, 16777215))
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

        self.gridLayout.addWidget(self.btn_apply_settings, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Channels_View)

        QMetaObject.connectSlotsByName(Channels_View)
    # setupUi

    def retranslateUi(self, Channels_View):
        Channels_View.setWindowTitle(QCoreApplication.translate("Channels_View", u"Form", None))
        self.groupBox.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Channels_View", u"Channels Diameter", None))
        self.spinbox_diameter.setSuffix(QCoreApplication.translate("Channels_View", u"mm", None))
        self.label.setText(QCoreApplication.translate("Channels_View", u"Needle Length", None))
        self.sb_needle_length.setSuffix(QCoreApplication.translate("Channels_View", u" mm", None))
        self.sb_threading_dept.setSuffix(QCoreApplication.translate("Channels_View", u" mm", None))
        self.label_2.setText(QCoreApplication.translate("Channels_View", u"Threading Depth", None))
        self.label_3.setText(QCoreApplication.translate("Channels_View", u"Threading diameter", None))
        self.sb_threading_diameter.setSuffix(QCoreApplication.translate("Channels_View", u" mm", None))
        self.label_5.setText(QCoreApplication.translate("Channels_View", u"Channels", None))
        self.btn_enable.setText(QCoreApplication.translate("Channels_View", u"Disable", None))
        self.btn_set_tandem.setText(QCoreApplication.translate("Channels_View", u"Set as Tandem", None))
        self.btn_apply_settings.setText(QCoreApplication.translate("Channels_View", u"Apply", None))
    # retranslateUi

