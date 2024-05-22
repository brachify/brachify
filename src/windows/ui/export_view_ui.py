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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Export_View(object):
    def setupUi(self, Export_View):
        if not Export_View.objectName():
            Export_View.setObjectName(u"Export_View")
        Export_View.resize(271, 2172)
        Export_View.setStyleSheet(u"background-color: rgb(230, 235, 240);")
        self.label_3 = QLabel(Export_View)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 271, 2171))
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(271, 16777215))
        self.label_3.setStyleSheet(u"background-color: rgb(240, 245, 250)")
        self.verticalLayoutWidget = QWidget(Export_View)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 271, 2171))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cb_tandem_shown = QCheckBox(self.verticalLayoutWidget)
        self.cb_tandem_shown.setObjectName(u"cb_tandem_shown")
        self.cb_tandem_shown.setLayoutDirection(Qt.RightToLeft)
        self.cb_tandem_shown.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.cb_tandem_shown.setChecked(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cb_tandem_shown)


        self.verticalLayout.addLayout(self.formLayout)

        self.top_menu_bar = QWidget(self.verticalLayoutWidget)
        self.top_menu_bar.setObjectName(u"top_menu_bar")
        self.top_menu_bar.setMinimumSize(QSize(100, 80))
        self.top_menu_bar.setMaximumSize(QSize(16777215, 135))
        self.top_menu_bar.setStyleSheet(u"background-color: rgb(230, 235, 240)")
        self.verticalLayout_2 = QVBoxLayout(self.top_menu_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_export_mesh = QPushButton(self.top_menu_bar)
        self.btn_export_mesh.setObjectName(u"btn_export_mesh")
        self.btn_export_mesh.setMinimumSize(QSize(240, 33))
        self.btn_export_mesh.setMaximumSize(QSize(16777215, 33))
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

        self.verticalLayout_2.addWidget(self.btn_export_mesh)

        self.btn_export_template_reference = QPushButton(self.top_menu_bar)
        self.btn_export_template_reference.setObjectName(u"btn_export_template_reference")
        self.btn_export_template_reference.setMinimumSize(QSize(240, 33))
        self.btn_export_template_reference.setMaximumSize(QSize(16777215, 33))
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

        self.verticalLayout_2.addWidget(self.btn_export_template_reference)

        self.btn_export_shapes = QPushButton(self.top_menu_bar)
        self.btn_export_shapes.setObjectName(u"btn_export_shapes")
        self.btn_export_shapes.setMinimumSize(QSize(240, 33))
        self.btn_export_shapes.setMaximumSize(QSize(16777215, 33))
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

        self.verticalLayout_2.addWidget(self.btn_export_shapes)

        self.btn_export_current_config = QPushButton(self.top_menu_bar)
        self.btn_export_current_config.setObjectName(u"btn_export_current_config")
        self.btn_export_current_config.setMinimumSize(QSize(240, 33))
        self.btn_export_current_config.setMaximumSize(QSize(16777215, 33))
        self.btn_export_current_config.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_export_current_config)


        self.verticalLayout.addWidget(self.top_menu_bar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Export_View)

        QMetaObject.connectSlotsByName(Export_View)
    # setupUi

    def retranslateUi(self, Export_View):
        Export_View.setWindowTitle(QCoreApplication.translate("Export_View", u"Form", None))
        Export_View.setWindowFilePath("")
        self.label_3.setText("")
        self.verticalLayoutWidget.setStyleSheet(QCoreApplication.translate("Export_View", u"background-color: rgb(240, 245, 250);", None))
        self.label_2.setText(QCoreApplication.translate("Export_View", u"Show Tandem", None))
        self.cb_tandem_shown.setText("")
        self.btn_export_mesh.setText(QCoreApplication.translate("Export_View", u"Export Mesh", None))
        self.btn_export_template_reference.setText(QCoreApplication.translate("Export_View", u"Export Reference Sheet", None))
        self.btn_export_shapes.setText(QCoreApplication.translate("Export_View", u"Export Shape(s)", None))
        self.btn_export_current_config.setText(QCoreApplication.translate("Export_View", u"Export Current Settings as Config", None))
    # retranslateUi

