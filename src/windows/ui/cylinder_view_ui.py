# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cylinder_view.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_Cylinder_View(object):
    def setupUi(self, Cylinder_View):
        if not Cylinder_View.objectName():
            Cylinder_View.setObjectName(u"Cylinder_View")
        Cylinder_View.resize(270, 400)
        Cylinder_View.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.label_4 = QLabel(Cylinder_View)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 271, 401))
        self.groupBox_3 = QGroupBox(Cylinder_View)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 271, 411))
        self.groupBox_3.setMinimumSize(QSize(271, 411))
        self.groupBox_3.setMaximumSize(QSize(250, 16777215))
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinbox_length = QSpinBox(self.groupBox_3)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setMinimumSize(QSize(135, 0))
        self.spinbox_length.setMaximumSize(QSize(16777215, 16777215))
        self.spinbox_length.setMinimum(60)
        self.spinbox_length.setMaximum(300)

        self.gridLayout.addWidget(self.spinbox_length, 1, 1, 1, 1)

        self.spinbox_diameter = QDoubleSpinBox(self.groupBox_3)
        self.spinbox_diameter.setObjectName(u"spinbox_diameter")
        self.spinbox_diameter.setMinimumSize(QSize(135, 0))
        self.spinbox_diameter.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.spinbox_diameter, 0, 1, 1, 1)

        self.btn_apply_settings = QPushButton(self.groupBox_3)
        self.btn_apply_settings.setObjectName(u"btn_apply_settings")
        self.btn_apply_settings.setMinimumSize(QSize(220, 25))
        self.btn_apply_settings.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.btn_apply_settings, 3, 0, 1, 3)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cb_add_base = QCheckBox(self.groupBox_3)
        self.cb_add_base.setObjectName(u"cb_add_base")
        self.cb_add_base.setMaximumSize(QSize(20, 16777215))
        self.cb_add_base.setLayoutDirection(Qt.RightToLeft)
        self.cb_add_base.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.cb_add_base, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_5.setBuddy(self.cb_add_base)
        self.label_3.setBuddy(self.spinbox_length)
        self.label.setBuddy(self.spinbox_diameter)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Cylinder_View)

        QMetaObject.connectSlotsByName(Cylinder_View)
    # setupUi

    def retranslateUi(self, Cylinder_View):
        Cylinder_View.setWindowTitle(QCoreApplication.translate("Cylinder_View", u"Form", None))
        self.label_4.setText("")
        self.groupBox_3.setTitle("")
        self.spinbox_length.setSuffix(QCoreApplication.translate("Cylinder_View", u" mm", None))
        self.btn_apply_settings.setText(QCoreApplication.translate("Cylinder_View", u"apply settings", None))
        self.label_5.setText(QCoreApplication.translate("Cylinder_View", u"add base", None))
        self.label_3.setText(QCoreApplication.translate("Cylinder_View", u"cylinder length", None))
        self.label.setText(QCoreApplication.translate("Cylinder_View", u"cylinder diameter", None))
        self.cb_add_base.setText("")
    # retranslateUi

