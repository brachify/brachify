# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tandem_view.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Tandem_View(object):
    def setupUi(self, Tandem_View):
        if not Tandem_View.objectName():
            Tandem_View.setObjectName(u"Tandem_View")
        Tandem_View.resize(271, 2174)
        Tandem_View.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.label_3 = QLabel(Tandem_View)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 271, 411))
        self.label_3.setStyleSheet(u"background-color: rgb(240, 245, 250)")
        self.verticalLayoutWidget_2 = QWidget(Tandem_View)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 271, 2181))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ab_1 = QTabWidget(self.verticalLayoutWidget_2)
        self.ab_1.setObjectName(u"ab_1")
        self.Import_2 = QWidget()
        self.Import_2.setObjectName(u"Import_2")
        self.verticalLayoutWidget_3 = QWidget(self.Import_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 271, 391))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(70, 25))

        self.horizontalLayout.addWidget(self.label_4)

        self.sb_height_offset = QDoubleSpinBox(self.verticalLayoutWidget_3)
        self.sb_height_offset.setObjectName(u"sb_height_offset")
        self.sb_height_offset.setMinimumSize(QSize(0, 20))
        self.sb_height_offset.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.sb_height_offset.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_height_offset.setMinimum(-100.000000000000000)
        self.sb_height_offset.setMaximum(100.000000000000000)

        self.horizontalLayout.addWidget(self.sb_height_offset)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_import = QPushButton(self.verticalLayoutWidget_3)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(50, 25))
        self.btn_import.setMaximumSize(QSize(70, 16777215))
        self.btn_import.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_import)

        self.btn_clear_import = QPushButton(self.verticalLayoutWidget_3)
        self.btn_clear_import.setObjectName(u"btn_clear_import")
        self.btn_clear_import.setMinimumSize(QSize(100, 25))
        self.btn_clear_import.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_clear_import)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.ab_1.addTab(self.Import_2, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_4 = QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, -1, 271, 2171))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(6)
        self.sb_tandem_height = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.sb_tandem_height.setObjectName(u"sb_tandem_height")
        self.sb_tandem_height.setStyleSheet(u"background-color: rgb(255, 255, 250)")
        self.sb_tandem_height.setMinimum(10.000000000000000)
        self.sb_tandem_height.setMaximum(500.000000000000000)
        self.sb_tandem_height.setValue(129.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.sb_tandem_height)

        self.sp_channel_diameter = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.sp_channel_diameter.setObjectName(u"sp_channel_diameter")
        self.sp_channel_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.sp_channel_diameter.setStyleSheet(u"background-color: rgb(255, 255, 250)")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.sp_channel_diameter)

        self.sp_stopper_diameter = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.sp_stopper_diameter.setObjectName(u"sp_stopper_diameter")
        self.sp_stopper_diameter.setStyleSheet(u"background-color: rgb(255, 255, 250)")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.sp_stopper_diameter)

        self.sp_bend_angle = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.sp_bend_angle.setObjectName(u"sp_bend_angle")
        self.sp_bend_angle.setStyleSheet(u"background-color: rgb(255, 255, 250)")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.sp_bend_angle)

        self.sb_bend_radius = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.sb_bend_radius.setObjectName(u"sb_bend_radius")
        self.sb_bend_radius.setStyleSheet(u"background-color: rgb(255, 255, 250)")
        self.sb_bend_radius.setMinimum(10.000000000000000)
        self.sb_bend_radius.setMaximum(1000.000000000000000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.sb_bend_radius)

        self.label_7 = QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_10 = QLabel(self.verticalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.verticalLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.verticalLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_12)


        self.verticalLayout_5.addLayout(self.formLayout_2)

        self.btn_apply = QPushButton(self.verticalLayoutWidget_4)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setMinimumSize(QSize(240, 33))
        self.btn_apply.setMaximumSize(QSize(245, 16777215))
        self.btn_apply.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_5.addWidget(self.btn_apply)

        self.btn_clear_generate = QPushButton(self.verticalLayoutWidget_4)
        self.btn_clear_generate.setObjectName(u"btn_clear_generate")
        self.btn_clear_generate.setMinimumSize(QSize(240, 33))
        self.btn_clear_generate.setMaximumSize(QSize(245, 16777215))
        self.btn_clear_generate.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_5.addWidget(self.btn_clear_generate)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.ab_1.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.ab_1)


        self.retranslateUi(Tandem_View)

        self.ab_1.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Tandem_View)
    # setupUi

    def retranslateUi(self, Tandem_View):
        Tandem_View.setWindowTitle(QCoreApplication.translate("Tandem_View", u"Form", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Tandem_View", u"Height Offset", None))
        self.sb_height_offset.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.btn_import.setText(QCoreApplication.translate("Tandem_View", u"Import", None))
        self.btn_clear_import.setText(QCoreApplication.translate("Tandem_View", u"Clear", None))
        self.label_5.setText(QCoreApplication.translate("Tandem_View", u"Model Filepath: None", None))
        self.ab_1.setTabText(self.ab_1.indexOf(self.Import_2), QCoreApplication.translate("Tandem_View", u"Import", None))
        self.sb_tandem_height.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.sp_channel_diameter.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.sp_stopper_diameter.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.sp_bend_angle.setSuffix(QCoreApplication.translate("Tandem_View", u" deg", None))
        self.sb_bend_radius.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.label_7.setText(QCoreApplication.translate("Tandem_View", u"Tandem Height", None))
        self.label_8.setText(QCoreApplication.translate("Tandem_View", u"Channel Diameter", None))
        self.label_10.setText(QCoreApplication.translate("Tandem_View", u"Stopper Diameter", None))
        self.label_11.setText(QCoreApplication.translate("Tandem_View", u"Bend Angle", None))
        self.label_12.setText(QCoreApplication.translate("Tandem_View", u"Bend Radius", None))
        self.btn_apply.setText(QCoreApplication.translate("Tandem_View", u"apply", None))
        self.btn_clear_generate.setText(QCoreApplication.translate("Tandem_View", u"clear", None))
        self.ab_1.setTabText(self.ab_1.indexOf(self.tab_2), QCoreApplication.translate("Tandem_View", u"Generate", None))
    # retranslateUi

