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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Channels_View(object):
    def setupUi(self, Channels_View):
        if not Channels_View.objectName():
            Channels_View.setObjectName(u"Channels_View")
        Channels_View.resize(290, 290)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Channels_View.sizePolicy().hasHeightForWidth())
        Channels_View.setSizePolicy(sizePolicy)
        Channels_View.setMinimumSize(QSize(290, 290))
        Channels_View.setMaximumSize(QSize(290, 16777215))
        Channels_View.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Channels_View)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(Channels_View)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(108, 18))
        self.label_4.setMaximumSize(QSize(16777215, 18))
        self.label_4.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.spinbox_diameter = QDoubleSpinBox(Channels_View)
        self.spinbox_diameter.setObjectName(u"spinbox_diameter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinbox_diameter.sizePolicy().hasHeightForWidth())
        self.spinbox_diameter.setSizePolicy(sizePolicy2)
        self.spinbox_diameter.setMinimumSize(QSize(20, 0))
        self.spinbox_diameter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinbox_diameter.setMinimum(0.300000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinbox_diameter)

        self.label = QLabel(Channels_View)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 18))
        self.label.setMaximumSize(QSize(16777215, 18))
        self.label.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.sb_needle_length = QDoubleSpinBox(Channels_View)
        self.sb_needle_length.setObjectName(u"sb_needle_length")
        sizePolicy2.setHeightForWidth(self.sb_needle_length.sizePolicy().hasHeightForWidth())
        self.sb_needle_length.setSizePolicy(sizePolicy2)
        self.sb_needle_length.setMinimumSize(QSize(20, 0))
        self.sb_needle_length.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_needle_length.setMaximum(350.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sb_needle_length)

        self.label_2 = QLabel(Channels_View)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 18))
        self.label_2.setMaximumSize(QSize(16777215, 18))
        self.label_2.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.sb_threading_dept = QDoubleSpinBox(Channels_View)
        self.sb_threading_dept.setObjectName(u"sb_threading_dept")
        sizePolicy2.setHeightForWidth(self.sb_threading_dept.sizePolicy().hasHeightForWidth())
        self.sb_threading_dept.setSizePolicy(sizePolicy2)
        self.sb_threading_dept.setMinimumSize(QSize(20, 0))
        self.sb_threading_dept.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_threading_dept.setMaximum(350.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sb_threading_dept)

        self.label_3 = QLabel(Channels_View)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 18))
        self.label_3.setMaximumSize(QSize(16777215, 18))
        self.label_3.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.sb_threading_diameter = QDoubleSpinBox(Channels_View)
        self.sb_threading_diameter.setObjectName(u"sb_threading_diameter")
        sizePolicy2.setHeightForWidth(self.sb_threading_diameter.sizePolicy().hasHeightForWidth())
        self.sb_threading_diameter.setSizePolicy(sizePolicy2)
        self.sb_threading_diameter.setMinimumSize(QSize(20, 0))
        self.sb_threading_diameter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_threading_diameter.setMaximum(350.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.sb_threading_diameter)


        self.verticalLayout.addLayout(self.formLayout)

        self.btn_apply_settings = QPushButton(Channels_View)
        self.btn_apply_settings.setObjectName(u"btn_apply_settings")
        self.btn_apply_settings.setMinimumSize(QSize(20, 33))
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

        self.verticalLayout.addWidget(self.btn_apply_settings)

        self.label_5 = QLabel(Channels_View)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMinimumSize(QSize(10, 13))
        self.label_5.setMaximumSize(QSize(270, 13))

        self.verticalLayout.addWidget(self.label_5)

        self.listwidget_channels = QListWidget(Channels_View)
        self.listwidget_channels.setObjectName(u"listwidget_channels")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listwidget_channels.sizePolicy().hasHeightForWidth())
        self.listwidget_channels.setSizePolicy(sizePolicy3)
        self.listwidget_channels.setMinimumSize(QSize(251, 50))
        self.listwidget_channels.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(8)
        self.listwidget_channels.setFont(font)
        self.listwidget_channels.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.listwidget_channels.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.listwidget_channels)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.btn_set_tandem = QPushButton(Channels_View)
        self.btn_set_tandem.setObjectName(u"btn_set_tandem")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_set_tandem.sizePolicy().hasHeightForWidth())
        self.btn_set_tandem.setSizePolicy(sizePolicy4)
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

        self.verticalLayout_4.addWidget(self.btn_set_tandem)

        self.btn_enable = QPushButton(Channels_View)
        self.btn_enable.setObjectName(u"btn_enable")
        sizePolicy4.setHeightForWidth(self.btn_enable.sizePolicy().hasHeightForWidth())
        self.btn_enable.setSizePolicy(sizePolicy4)
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

        self.verticalLayout_4.addWidget(self.btn_enable)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(Channels_View)

        QMetaObject.connectSlotsByName(Channels_View)
    # setupUi

    def retranslateUi(self, Channels_View):
        Channels_View.setWindowTitle(QCoreApplication.translate("Channels_View", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Channels_View", u"Channels Diameter", None))
        self.spinbox_diameter.setSuffix(QCoreApplication.translate("Channels_View", u" mm", None))
        self.label.setText(QCoreApplication.translate("Channels_View", u"Needle Length", None))
        self.sb_needle_length.setSuffix(QCoreApplication.translate("Channels_View", u" mm", None))
        self.label_2.setText(QCoreApplication.translate("Channels_View", u"Threading Depth", None))
        self.sb_threading_dept.setSuffix(QCoreApplication.translate("Channels_View", u" mm", None))
        self.label_3.setText(QCoreApplication.translate("Channels_View", u"Threading Diameter", None))
        self.sb_threading_diameter.setSuffix(QCoreApplication.translate("Channels_View", u" mm", None))
        self.btn_apply_settings.setText(QCoreApplication.translate("Channels_View", u"Apply", None))
        self.label_5.setText(QCoreApplication.translate("Channels_View", u"Channels", None))
        self.btn_set_tandem.setText(QCoreApplication.translate("Channels_View", u"Set as Tandem", None))
        self.btn_enable.setText(QCoreApplication.translate("Channels_View", u"Disable", None))
    # retranslateUi

