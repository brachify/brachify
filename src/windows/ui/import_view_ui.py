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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Import_View(object):
    def setupUi(self, Import_View):
        if not Import_View.objectName():
            Import_View.setObjectName(u"Import_View")
        Import_View.resize(294, 290)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Import_View.sizePolicy().hasHeightForWidth())
        Import_View.setSizePolicy(sizePolicy)
        Import_View.setMinimumSize(QSize(0, 290))
        Import_View.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(Import_View)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.btn_import_folder = QPushButton(Import_View)
        self.btn_import_folder.setObjectName(u"btn_import_folder")
        self.btn_import_folder.setMinimumSize(QSize(240, 33))
        self.btn_import_folder.setMaximumSize(QSize(16777215, 33))
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

        self.verticalLayout_3.addWidget(self.btn_import_folder)

        self.btn_config_file = QPushButton(Import_View)
        self.btn_config_file.setObjectName(u"btn_config_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_config_file.sizePolicy().hasHeightForWidth())
        self.btn_config_file.setSizePolicy(sizePolicy1)
        self.btn_config_file.setMinimumSize(QSize(240, 33))
        self.btn_config_file.setMaximumSize(QSize(16777215, 33))
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

        self.verticalLayout_3.addWidget(self.btn_config_file)

        self.info_area = QTextEdit(Import_View)
        self.info_area.setObjectName(u"info_area")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.info_area.sizePolicy().hasHeightForWidth())
        self.info_area.setSizePolicy(sizePolicy2)
        self.info_area.setMinimumSize(QSize(268, 50))
        self.info_area.setMaximumSize(QSize(16777215, 16777215))
        self.info_area.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.info_area.setAcceptDrops(False)
        self.info_area.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.info_area.setInputMethodHints(Qt.ImhNone)
        self.info_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.info_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.info_area.setUndoRedoEnabled(False)
        self.info_area.setOverwriteMode(False)
        self.info_area.setAcceptRichText(False)
        self.info_area.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_3.addWidget(self.info_area)


        self.retranslateUi(Import_View)

        QMetaObject.connectSlotsByName(Import_View)
    # setupUi

    def retranslateUi(self, Import_View):
        Import_View.setWindowTitle(QCoreApplication.translate("Import_View", u"Form", None))
        self.btn_import_folder.setText(QCoreApplication.translate("Import_View", u"Import Dicom", None))
        self.btn_config_file.setText(QCoreApplication.translate("Import_View", u"Import Config File", None))
    # retranslateUi

