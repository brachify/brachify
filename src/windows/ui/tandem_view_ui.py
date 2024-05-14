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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_Tandem_View(object):
    def setupUi(self, Tandem_View):
        if not Tandem_View.objectName():
            Tandem_View.setObjectName(u"Tandem_View")
        Tandem_View.resize(271, 411)
        Tandem_View.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.label_3 = QLabel(Tandem_View)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 271, 411))
        self.label_3.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.formLayoutWidget = QWidget(Tandem_View)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 271, 411))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.formLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(260, 340))
        self.tabWidget.setMaximumSize(QSize(260, 340))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.tab_import = QWidget()
        self.tab_import.setObjectName(u"tab_import")
        self.tab_import.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.formLayout_2 = QFormLayout(self.tab_import)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_6 = QLabel(self.tab_import)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(230, 235, 240)")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.sb_height_offset = QDoubleSpinBox(self.tab_import)
        self.sb_height_offset.setObjectName(u"sb_height_offset")
        self.sb_height_offset.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.sb_height_offset.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_height_offset.setMinimum(-100.000000000000000)
        self.sb_height_offset.setMaximum(100.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.sb_height_offset)

        self.btn_import = QPushButton(self.tab_import)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(50, 25))
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

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.btn_import)

        self.btn_clear_import = QPushButton(self.tab_import)
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

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.btn_clear_import)

        self.label_5 = QLabel(self.tab_import)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(230, 235, 240)")

        self.formLayout_2.setWidget(2, QFormLayout.SpanningRole, self.label_5)

        self.tabWidget.addTab(self.tab_import, "")
        self.tab_generate = QWidget()
        self.tab_generate.setObjectName(u"tab_generate")
        self.label_8 = QLabel(self.tab_generate)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(9, 9, 72, 16))
        self.label_8.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.sb_tandem_height = QDoubleSpinBox(self.tab_generate)
        self.sb_tandem_height.setObjectName(u"sb_tandem_height")
        self.sb_tandem_height.setGeometry(QRect(100, 9, 135, 16))
        self.sb_tandem_height.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.sb_tandem_height.setMinimum(10.000000000000000)
        self.sb_tandem_height.setMaximum(500.000000000000000)
        self.sb_tandem_height.setValue(129.000000000000000)
        self.label = QLabel(self.tab_generate)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 31, 85, 16))
        self.label.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.sp_channel_diameter = QDoubleSpinBox(self.tab_generate)
        self.sp_channel_diameter.setObjectName(u"sp_channel_diameter")
        self.sp_channel_diameter.setGeometry(QRect(100, 31, 135, 16))
        self.sp_channel_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.sp_channel_diameter.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.label_2 = QLabel(self.tab_generate)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 53, 84, 16))
        self.label_2.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.sp_stopper_diameter = QDoubleSpinBox(self.tab_generate)
        self.sp_stopper_diameter.setObjectName(u"sp_stopper_diameter")
        self.sp_stopper_diameter.setGeometry(QRect(100, 53, 135, 16))
        self.sp_stopper_diameter.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.label_4 = QLabel(self.tab_generate)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(9, 74, 54, 16))
        self.label_4.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.sp_bend_angle = QDoubleSpinBox(self.tab_generate)
        self.sp_bend_angle.setObjectName(u"sp_bend_angle")
        self.sp_bend_angle.setGeometry(QRect(100, 74, 135, 16))
        self.sp_bend_angle.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.label_7 = QLabel(self.tab_generate)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(9, 96, 59, 16))
        self.label_7.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.sb_bend_radius = QDoubleSpinBox(self.tab_generate)
        self.sb_bend_radius.setObjectName(u"sb_bend_radius")
        self.sb_bend_radius.setGeometry(QRect(100, 96, 135, 16))
        self.sb_bend_radius.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.sb_bend_radius.setMinimum(10.000000000000000)
        self.sb_bend_radius.setMaximum(1000.000000000000000)
        self.btn_clear_generate = QPushButton(self.tab_generate)
        self.btn_clear_generate.setObjectName(u"btn_clear_generate")
        self.btn_clear_generate.setGeometry(QRect(0, 180, 245, 33))
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
        self.btn_apply = QPushButton(self.tab_generate)
        self.btn_apply.setObjectName(u"btn_apply")
        self.btn_apply.setGeometry(QRect(0, 150, 245, 33))
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
        self.tabWidget.addTab(self.tab_generate, "")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.tabWidget)

#if QT_CONFIG(shortcut)
        self.label_8.setBuddy(self.sb_tandem_height)
        self.label.setBuddy(self.sp_channel_diameter)
        self.label_2.setBuddy(self.sp_stopper_diameter)
        self.label_4.setBuddy(self.sp_bend_angle)
        self.label_7.setBuddy(self.sb_bend_radius)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Tandem_View)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Tandem_View)
    # setupUi

    def retranslateUi(self, Tandem_View):
        Tandem_View.setWindowTitle(QCoreApplication.translate("Tandem_View", u"Form", None))
        self.label_3.setText("")
        self.label_6.setText(QCoreApplication.translate("Tandem_View", u"Height Offse", None))
        self.sb_height_offset.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.btn_import.setText(QCoreApplication.translate("Tandem_View", u"Import", None))
        self.btn_clear_import.setText(QCoreApplication.translate("Tandem_View", u"Clear", None))
        self.label_5.setText(QCoreApplication.translate("Tandem_View", u"Model Details", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_import), QCoreApplication.translate("Tandem_View", u"import", None))
        self.label_8.setText(QCoreApplication.translate("Tandem_View", u"Tandem Height", None))
        self.sb_tandem_height.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.label.setText(QCoreApplication.translate("Tandem_View", u"Channel Diameter", None))
        self.sp_channel_diameter.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.label_2.setText(QCoreApplication.translate("Tandem_View", u"Stopper Diameter", None))
        self.sp_stopper_diameter.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.label_4.setText(QCoreApplication.translate("Tandem_View", u"Bend Angle", None))
        self.sp_bend_angle.setSuffix(QCoreApplication.translate("Tandem_View", u" deg", None))
        self.label_7.setText(QCoreApplication.translate("Tandem_View", u"Bend Radius", None))
        self.sb_bend_radius.setSuffix(QCoreApplication.translate("Tandem_View", u" mm", None))
        self.btn_clear_generate.setText(QCoreApplication.translate("Tandem_View", u"clear", None))
        self.btn_apply.setText(QCoreApplication.translate("Tandem_View", u"apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_generate), QCoreApplication.translate("Tandem_View", u"generate", None))
    # retranslateUi

