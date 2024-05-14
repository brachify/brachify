# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_view.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Export_View(object):
    def setupUi(self, Export_View):
        if not Export_View.objectName():
            Export_View.setObjectName(u"Export_View")
        Export_View.resize(271, 411)
        Export_View.setStyleSheet(u"background-color: rgb(230, 235, 240);")
        self.label_3 = QLabel(Export_View)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 271, 411))
        self.label_3.setMinimumSize(QSize(0, 411))
        self.label_3.setMaximumSize(QSize(271, 411))
        self.label_3.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.formLayoutWidget = QWidget(Export_View)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 241, 39))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.sb_needle_length = QDoubleSpinBox(self.formLayoutWidget)
        self.sb_needle_length.setObjectName(u"sb_needle_length")
        self.sb_needle_length.setStyleSheet(u"background-color: rgb(230, 235, 240);")
        self.sb_needle_length.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sb_needle_length.setMaximum(350.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sb_needle_length)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(230, 235, 240);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(230, 235, 240);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.cb_tandem_shown = QCheckBox(self.formLayoutWidget)
        self.cb_tandem_shown.setObjectName(u"cb_tandem_shown")
        self.cb_tandem_shown.setLayoutDirection(Qt.RightToLeft)
        self.cb_tandem_shown.setStyleSheet(u"QCheckBox {\n"
"	background-color: rgb(230, 235, 240);\n"
"}")
        self.cb_tandem_shown.setChecked(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cb_tandem_shown)

        self.top_menu_bar = QWidget(Export_View)
        self.top_menu_bar.setObjectName(u"top_menu_bar")
        self.top_menu_bar.setGeometry(QRect(0, 50, 270, 135))
        self.top_menu_bar.setMinimumSize(QSize(270, 100))
        self.top_menu_bar.setMaximumSize(QSize(16777215, 135))
        self.top_menu_bar.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.btn_export_mesh = QPushButton(self.top_menu_bar)
        self.btn_export_mesh.setObjectName(u"btn_export_mesh")
        self.btn_export_mesh.setGeometry(QRect(10, 0, 240, 33))
        self.btn_export_mesh.setMinimumSize(QSize(240, 33))
        self.btn_export_mesh.setMaximumSize(QSize(240, 33))
        self.btn_export_mesh.setStyleSheet(u"QPushButton {\n"
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
        self.btn_export_shapes = QPushButton(self.top_menu_bar)
        self.btn_export_shapes.setObjectName(u"btn_export_shapes")
        self.btn_export_shapes.setGeometry(QRect(10, 30, 240, 33))
        self.btn_export_shapes.setMinimumSize(QSize(240, 33))
        self.btn_export_shapes.setMaximumSize(QSize(240, 33))
        self.btn_export_shapes.setStyleSheet(u"QPushButton {\n"
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
        self.btn_export_template_reference = QPushButton(self.top_menu_bar)
        self.btn_export_template_reference.setObjectName(u"btn_export_template_reference")
        self.btn_export_template_reference.setGeometry(QRect(10, 60, 240, 33))
        self.btn_export_template_reference.setMinimumSize(QSize(240, 33))
        self.btn_export_template_reference.setMaximumSize(QSize(240, 33))
        self.btn_export_template_reference.setStyleSheet(u"QPushButton {\n"
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
        self.btn_import_folder_2 = QPushButton(self.top_menu_bar)
        self.btn_import_folder_2.setObjectName(u"btn_import_folder_2")
        self.btn_import_folder_2.setGeometry(QRect(10, 90, 240, 33))
        self.btn_import_folder_2.setMinimumSize(QSize(240, 33))
        self.btn_import_folder_2.setMaximumSize(QSize(240, 33))
        self.btn_import_folder_2.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Export_View)

        QMetaObject.connectSlotsByName(Export_View)
    # setupUi

    def retranslateUi(self, Export_View):
        Export_View.setWindowTitle(QCoreApplication.translate("Export_View", u"Form", None))
        Export_View.setWindowFilePath("")
        self.label_3.setText("")
        self.sb_needle_length.setSuffix(QCoreApplication.translate("Export_View", u" mm", None))
        self.label.setText(QCoreApplication.translate("Export_View", u"Needle Length", None))
        self.label_2.setText(QCoreApplication.translate("Export_View", u"Show Tandem", None))
        self.cb_tandem_shown.setText("")
        self.btn_export_mesh.setText(QCoreApplication.translate("Export_View", u"Export Mesh", None))
        self.btn_export_shapes.setText(QCoreApplication.translate("Export_View", u"Export Shape(s)", None))
        self.btn_export_template_reference.setText(QCoreApplication.translate("Export_View", u"Export Template Reference Sheet", None))
        self.btn_import_folder_2.setText(QCoreApplication.translate("Export_View", u"Export Current Config File", None))
    # retranslateUi

