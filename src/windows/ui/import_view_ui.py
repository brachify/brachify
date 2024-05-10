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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Import_View(object):
    def setupUi(self, Import_View):
        if not Import_View.objectName():
            Import_View.setObjectName(u"Import_View")
        Import_View.resize(270, 400)
        Import_View.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label = QLabel(Import_View)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 271, 401))
        self.groupBox_3 = QGroupBox(Import_View)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 271, 411))
        self.groupBox_3.setMinimumSize(QSize(271, 411))
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.btn_import_folder = QPushButton(self.groupBox_3)
        self.btn_import_folder.setObjectName(u"btn_import_folder")
        self.btn_import_folder.setMinimumSize(QSize(220, 25))
        self.btn_import_folder.setMaximumSize(QSize(16777215, 16777215))
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

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.btn_import_folder)

        self.label_file_info = QLabel(self.groupBox_3)
        self.label_file_info.setObjectName(u"label_file_info")
        self.label_file_info.setMinimumSize(QSize(220, 0))
        self.label_file_info.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_file_info)


        self.retranslateUi(Import_View)

        QMetaObject.connectSlotsByName(Import_View)
    # setupUi

    def retranslateUi(self, Import_View):
        Import_View.setWindowTitle(QCoreApplication.translate("Import_View", u"Form", None))
        self.label.setText("")
        self.groupBox_3.setTitle("")
        self.btn_import_folder.setText(QCoreApplication.translate("Import_View", u"import dicom folder", None))
        self.label_file_info.setText(QCoreApplication.translate("Import_View", u"No model(s) loaded", None))
    # retranslateUi

