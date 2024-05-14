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
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 584)
        icon = QIcon()
        icon.addFile(u":/Icon/Icon/brachify_splash-ico.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(155,189,220);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.top_menu_bar = QWidget(self.centralwidget)
        self.top_menu_bar.setObjectName(u"top_menu_bar")
        self.top_menu_bar.setMinimumSize(QSize(270, 180))
        self.top_menu_bar.setMaximumSize(QSize(16777215, 180))
        self.btn_export_view = QPushButton(self.top_menu_bar)
        self.btn_export_view.setObjectName(u"btn_export_view")
        self.btn_export_view.setGeometry(QRect(0, 130, 270, 33))
        self.btn_export_view.setMinimumSize(QSize(270, 33))
        self.btn_export_view.setMaximumSize(QSize(16777215, 20))
        self.btn_export_view.setStyleSheet(u"QPushButton {\n"
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
        self.btn_import_view = QPushButton(self.top_menu_bar)
        self.btn_import_view.setObjectName(u"btn_import_view")
        self.btn_import_view.setGeometry(QRect(0, 10, 270, 33))
        self.btn_import_view.setMinimumSize(QSize(270, 33))
        self.btn_import_view.setMaximumSize(QSize(16777215, 20))
        self.btn_import_view.setStyleSheet(u"QPushButton {\n"
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
        self.btn_cylinder_view = QPushButton(self.top_menu_bar)
        self.btn_cylinder_view.setObjectName(u"btn_cylinder_view")
        self.btn_cylinder_view.setGeometry(QRect(0, 40, 270, 33))
        self.btn_cylinder_view.setMinimumSize(QSize(270, 33))
        self.btn_cylinder_view.setMaximumSize(QSize(16777215, 20))
        self.btn_cylinder_view.setStyleSheet(u"QPushButton {\n"
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
        self.btn_channels_view = QPushButton(self.top_menu_bar)
        self.btn_channels_view.setObjectName(u"btn_channels_view")
        self.btn_channels_view.setGeometry(QRect(0, 70, 270, 33))
        self.btn_channels_view.setMinimumSize(QSize(270, 33))
        self.btn_channels_view.setMaximumSize(QSize(16777215, 20))
        self.btn_channels_view.setStyleSheet(u"QPushButton {\n"
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
        self.btn_tandem_view = QPushButton(self.top_menu_bar)
        self.btn_tandem_view.setObjectName(u"btn_tandem_view")
        self.btn_tandem_view.setGeometry(QRect(0, 100, 270, 33))
        self.btn_tandem_view.setMinimumSize(QSize(270, 33))
        self.btn_tandem_view.setMaximumSize(QSize(16777215, 20))
        self.btn_tandem_view.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.top_menu_bar, 0, 0, 1, 1)

        self.left_menu_bar = QWidget(self.centralwidget)
        self.left_menu_bar.setObjectName(u"left_menu_bar")
        self.left_menu_bar.setMinimumSize(QSize(270, 0))
        self.left_menu_bar.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.left_menu_bar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.viewswidget = QStackedWidget(self.left_menu_bar)
        self.viewswidget.setObjectName(u"viewswidget")
        self.viewswidget.setMinimumSize(QSize(100, 380))
        self.viewswidget.setMaximumSize(QSize(270, 16777215))
        self.page_import = QWidget()
        self.page_import.setObjectName(u"page_import")
        self.verticalLayout_7 = QVBoxLayout(self.page_import)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.viewswidget.addWidget(self.page_import)
        self.page_cylinder = QWidget()
        self.page_cylinder.setObjectName(u"page_cylinder")
        self.verticalLayout = QVBoxLayout(self.page_cylinder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.viewswidget.addWidget(self.page_cylinder)
        self.page_channels = QWidget()
        self.page_channels.setObjectName(u"page_channels")
        self.verticalLayout_3 = QVBoxLayout(self.page_channels)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_channels)
        self.page_tandem = QWidget()
        self.page_tandem.setObjectName(u"page_tandem")
        self.verticalLayout_4 = QVBoxLayout(self.page_tandem)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_tandem)
        self.page_export = QWidget()
        self.page_export.setObjectName(u"page_export")
        self.verticalLayout_8 = QVBoxLayout(self.page_export)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_export)

        self.verticalLayout_2.addWidget(self.viewswidget)


        self.gridLayout_2.addWidget(self.left_menu_bar, 1, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(679, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.display_view_widget = QWidget(self.centralwidget)
        self.display_view_widget.setObjectName(u"display_view_widget")
        self.display_view_widget.setMinimumSize(QSize(600, 540))
        self.gridLayout_3 = QGridLayout(self.display_view_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.display_view_widget)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.viewswidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"brachify", None))
        self.btn_export_view.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.btn_import_view.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.btn_cylinder_view.setText(QCoreApplication.translate("MainWindow", u"Cylinder", None))
        self.btn_channels_view.setText(QCoreApplication.translate("MainWindow", u"Channels", None))
        self.btn_tandem_view.setText(QCoreApplication.translate("MainWindow", u"Tandem", None))
    # retranslateUi

