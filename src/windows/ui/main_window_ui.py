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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 607)
        icon = QIcon()
        icon.addFile(u":/Icon/Icon/brachify_splash-ico.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(155,189,220);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.display_view_widget = QWidget(self.centralwidget)
        self.display_view_widget.setObjectName(u"display_view_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_view_widget.sizePolicy().hasHeightForWidth())
        self.display_view_widget.setSizePolicy(sizePolicy)
        self.display_view_widget.setMinimumSize(QSize(425, 470))
        self.display_view_widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.display_view_widget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.display_view_widget)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.top_menu_bar = QWidget(self.centralwidget)
        self.top_menu_bar.setObjectName(u"top_menu_bar")
        self.top_menu_bar.setMinimumSize(QSize(290, 180))
        self.top_menu_bar.setMaximumSize(QSize(290, 180))
        self.verticalLayout_31 = QVBoxLayout(self.top_menu_bar)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 20)
        self.btn_import_view = QPushButton(self.top_menu_bar)
        self.btn_import_view.setObjectName(u"btn_import_view")
        self.btn_import_view.setMinimumSize(QSize(290, 33))
        self.btn_import_view.setMaximumSize(QSize(290, 33))
        self.btn_import_view.setStyleSheet(u"QPushButton {\n"
"	color: rgb(250,250,250);\n"
"	background-color: rgb(28, 44, 81);\n"
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

        self.verticalLayout_31.addWidget(self.btn_import_view)

        self.btn_cylinder_view = QPushButton(self.top_menu_bar)
        self.btn_cylinder_view.setObjectName(u"btn_cylinder_view")
        self.btn_cylinder_view.setMinimumSize(QSize(290, 33))
        self.btn_cylinder_view.setMaximumSize(QSize(290, 33))
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

        self.verticalLayout_31.addWidget(self.btn_cylinder_view)

        self.btn_channels_view = QPushButton(self.top_menu_bar)
        self.btn_channels_view.setObjectName(u"btn_channels_view")
        self.btn_channels_view.setMinimumSize(QSize(290, 33))
        self.btn_channels_view.setMaximumSize(QSize(290, 33))
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

        self.verticalLayout_31.addWidget(self.btn_channels_view)

        self.btn_tandem_view = QPushButton(self.top_menu_bar)
        self.btn_tandem_view.setObjectName(u"btn_tandem_view")
        self.btn_tandem_view.setMinimumSize(QSize(290, 33))
        self.btn_tandem_view.setMaximumSize(QSize(290, 33))
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

        self.verticalLayout_31.addWidget(self.btn_tandem_view)

        self.btn_export_view = QPushButton(self.top_menu_bar)
        self.btn_export_view.setObjectName(u"btn_export_view")
        self.btn_export_view.setMinimumSize(QSize(290, 33))
        self.btn_export_view.setMaximumSize(QSize(290, 33))
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

        self.verticalLayout_31.addWidget(self.btn_export_view)


        self.verticalLayout.addWidget(self.top_menu_bar)

        self.viewswidget = QStackedWidget(self.centralwidget)
        self.viewswidget.setObjectName(u"viewswidget")
        self.viewswidget.setMinimumSize(QSize(290, 100))
        self.viewswidget.setMaximumSize(QSize(290, 16777215))
        self.viewswidget.setStyleSheet(u"color: rgba(240, 245, 250);\n"
"\n"
"selection-background-color: rgb(0, 0, 255);\n"
"background-color: rgb(240, 245, 250);")
        self.page_import = QWidget()
        self.page_import.setObjectName(u"page_import")
        self.page_import.setStyleSheet(u"color: rgba(240, 245, 250);")
        self.verticalLayout_32 = QVBoxLayout(self.page_import)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_import)
        self.page_cylinder = QWidget()
        self.page_cylinder.setObjectName(u"page_cylinder")
        self.page_cylinder.setStyleSheet(u"color: rgba(240, 245, 250);")
        self.verticalLayout_33 = QVBoxLayout(self.page_cylinder)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_cylinder)
        self.page_channels = QWidget()
        self.page_channels.setObjectName(u"page_channels")
        self.page_channels.setStyleSheet(u"color: rgba(240, 245, 250);")
        self.verticalLayout_35 = QVBoxLayout(self.page_channels)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_channels)
        self.page_tandem = QWidget()
        self.page_tandem.setObjectName(u"page_tandem")
        self.page_tandem.setStyleSheet(u"color: rgba(240, 245, 250);")
        self.verticalLayout_36 = QVBoxLayout(self.page_tandem)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_tandem)
        self.page_export = QWidget()
        self.page_export.setObjectName(u"page_export")
        self.page_export.setStyleSheet(u"color: rgba(240, 245, 250);")
        self.verticalLayout_37 = QVBoxLayout(self.page_export)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.viewswidget.addWidget(self.page_export)

        self.verticalLayout.addWidget(self.viewswidget)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.viewswidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"brachify", None))
        self.btn_import_view.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.btn_cylinder_view.setText(QCoreApplication.translate("MainWindow", u"Cylinder", None))
        self.btn_channels_view.setText(QCoreApplication.translate("MainWindow", u"Channels", None))
        self.btn_tandem_view.setText(QCoreApplication.translate("MainWindow", u"Tandem", None))
        self.btn_export_view.setText(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

