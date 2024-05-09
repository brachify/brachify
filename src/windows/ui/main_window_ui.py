# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(965, 724)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.bodywidget = QWidget(self.centralwidget)
        self.bodywidget.setObjectName(u"bodywidget")
        self.verticalLayout_5 = QVBoxLayout(self.bodywidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.display_view_widget = QWidget(self.bodywidget)
        self.display_view_widget.setObjectName(u"display_view_widget")
        self.display_view_widget.setMinimumSize(QSize(600, 540))
        self.gridLayout = QGridLayout(self.display_view_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.display_view_widget)


        self.gridLayout_2.addWidget(self.bodywidget, 0, 1, 1, 1)

        self.left_menu_bar = QWidget(self.centralwidget)
        self.left_menu_bar.setObjectName(u"left_menu_bar")
        self.left_menu_bar.setMinimumSize(QSize(250, 0))
        self.left_menu_bar.setMaximumSize(QSize(260, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.left_menu_bar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_menu_bar_2 = QWidget(self.left_menu_bar)
        self.top_menu_bar_2.setObjectName(u"top_menu_bar_2")
        self.top_menu_bar_2.setMinimumSize(QSize(0, 241))
        self.top_menu_bar_2.setMaximumSize(QSize(250, 16777215))
        self.btn_import_view = QPushButton(self.top_menu_bar_2)
        self.btn_import_view.setObjectName(u"btn_import_view")
        self.btn_import_view.setGeometry(QRect(0, 0, 250, 40))
        self.btn_import_view.setMinimumSize(QSize(0, 40))
        self.btn_import_view.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 0, 250);\n"
"}")
        self.btn_channels_view = QPushButton(self.top_menu_bar_2)
        self.btn_channels_view.setObjectName(u"btn_channels_view")
        self.btn_channels_view.setGeometry(QRect(0, 40, 250, 40))
        self.btn_channels_view.setMinimumSize(QSize(0, 40))
        self.btn_channels_view.setStyleSheet(u"QPushButton {\n"
"	color: rgb(250, 0, 0);\n"
"	background-color: rgb(250, 250, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(250, 250, 0);\n"
"}")
        self.btn_cylinder_view = QPushButton(self.top_menu_bar_2)
        self.btn_cylinder_view.setObjectName(u"btn_cylinder_view")
        self.btn_cylinder_view.setGeometry(QRect(0, 80, 250, 40))
        self.btn_cylinder_view.setMinimumSize(QSize(0, 40))
        self.btn_cylinder_view.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 0, 0);\n"
"}")
        self.btn_tandem_view = QPushButton(self.top_menu_bar_2)
        self.btn_tandem_view.setObjectName(u"btn_tandem_view")
        self.btn_tandem_view.setGeometry(QRect(0, 120, 250, 40))
        self.btn_tandem_view.setMinimumSize(QSize(0, 40))
        self.btn_tandem_view.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 0, 0);\n"
"}")
        self.btn_export_view = QPushButton(self.top_menu_bar_2)
        self.btn_export_view.setObjectName(u"btn_export_view")
        self.btn_export_view.setGeometry(QRect(0, 160, 250, 40))
        self.btn_export_view.setMinimumSize(QSize(0, 40))
        self.btn_export_view.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 0, 0);\n"
"}")
        self.btn_settings = QPushButton(self.top_menu_bar_2)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(0, 200, 250, 40))
        self.btn_settings.setMinimumSize(QSize(0, 40))
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 0, 0);\n"
"}")
        self.viewswidget = QStackedWidget(self.top_menu_bar_2)
        self.viewswidget.setObjectName(u"viewswidget")
        self.viewswidget.setGeometry(QRect(0, 246, 251, 461))
        self.page_import = QWidget()
        self.page_import.setObjectName(u"page_import")
        self.verticalLayout_18 = QVBoxLayout(self.page_import)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(4, 4, 4, 4)
        self.viewswidget.addWidget(self.page_import)
        self.page_cylinder = QWidget()
        self.page_cylinder.setObjectName(u"page_cylinder")
        self.verticalLayout_19 = QVBoxLayout(self.page_cylinder)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(4, 4, 4, 4)
        self.viewswidget.addWidget(self.page_cylinder)
        self.page_channels = QWidget()
        self.page_channels.setObjectName(u"page_channels")
        self.verticalLayout_20 = QVBoxLayout(self.page_channels)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_channels)
        self.page_tandem = QWidget()
        self.page_tandem.setObjectName(u"page_tandem")
        self.verticalLayout_21 = QVBoxLayout(self.page_tandem)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_tandem)
        self.page_export = QWidget()
        self.page_export.setObjectName(u"page_export")
        self.verticalLayout_22 = QVBoxLayout(self.page_export)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_export)

        self.verticalLayout_2.addWidget(self.top_menu_bar_2)


        self.gridLayout_2.addWidget(self.left_menu_bar, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.viewswidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"brachify", None))
        self.btn_import_view.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.btn_channels_view.setText(QCoreApplication.translate("MainWindow", u"Channels", None))
        self.btn_cylinder_view.setText(QCoreApplication.translate("MainWindow", u"Cylinder", None))
        self.btn_tandem_view.setText(QCoreApplication.translate("MainWindow", u"Tandem", None))
        self.btn_export_view.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

