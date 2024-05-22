# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_view.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Import_View(object):
    def setupUi(self, Import_View):
        if not Import_View.objectName():
            Import_View.setObjectName(u"Import_View")
        Import_View.resize(271, 5000)
        Import_View.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.verticalLayoutWidget = QWidget(Import_View)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 271, 5000))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.btn_import_folder = QPushButton(self.verticalLayoutWidget)
        self.btn_import_folder.setObjectName(u"btn_import_folder")
        self.btn_import_folder.setMinimumSize(QSize(240, 33))
        self.btn_import_folder.setMaximumSize(QSize(271, 33))
        self.btn_import_folder.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_import_folder)

        self.btn_config_file = QPushButton(self.verticalLayoutWidget)
        self.btn_config_file.setObjectName(u"btn_config_file")
        self.btn_config_file.setMinimumSize(QSize(240, 33))
        self.btn_config_file.setMaximumSize(QSize(271, 33))
        self.btn_config_file.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.btn_config_file)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_file_info = QLabel(self.verticalLayoutWidget)
        self.label_file_info.setObjectName(u"label_file_info")
        self.label_file_info.setMaximumSize(QSize(271, 16777215))
        self.label_file_info.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.label_file_info.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_file_info)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Import_View)

        QMetaObject.connectSlotsByName(Import_View)
    # setupUi

    def retranslateUi(self, Import_View):
        Import_View.setWindowTitle(QCoreApplication.translate("Import_View", u"Form", None))
        self.btn_import_folder.setText(QCoreApplication.translate("Import_View", u"Import Dicom", None))
        self.btn_config_file.setText(QCoreApplication.translate("Import_View", u"Import Config File", None))
        self.label_file_info.setText(QCoreApplication.translate("Import_View", u"No Model(s) Loaded", None))
    # retranslateUi

