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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Cylinder_View(object):
    def setupUi(self, Cylinder_View):
        if not Cylinder_View.objectName():
            Cylinder_View.setObjectName(u"Cylinder_View")
        Cylinder_View.resize(290, 290)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Cylinder_View.sizePolicy().hasHeightForWidth())
        Cylinder_View.setSizePolicy(sizePolicy)
        Cylinder_View.setMinimumSize(QSize(290, 290))
        Cylinder_View.setMaximumSize(QSize(16777215, 600))
        Cylinder_View.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.verticalLayout = QVBoxLayout(Cylinder_View)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Cylinder_View)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinbox_diameter = QDoubleSpinBox(Cylinder_View)
        self.spinbox_diameter.setObjectName(u"spinbox_diameter")
        self.spinbox_diameter.setMinimumSize(QSize(135, 0))
        self.spinbox_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.spinbox_diameter.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinbox_diameter)

        self.label_2 = QLabel(Cylinder_View)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spinbox_length = QSpinBox(Cylinder_View)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setMinimumSize(QSize(135, 0))
        self.spinbox_length.setMaximumSize(QSize(16777215, 16777215))
        self.spinbox_length.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinbox_length.setMinimum(60)
        self.spinbox_length.setMaximum(300)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinbox_length)

        self.label_3 = QLabel(Cylinder_View)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.cb_add_base = QCheckBox(Cylinder_View)
        self.cb_add_base.setObjectName(u"cb_add_base")
        self.cb_add_base.setMaximumSize(QSize(1000, 16777215))
        self.cb_add_base.setLayoutDirection(Qt.RightToLeft)
        self.cb_add_base.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.cb_add_base.setIconSize(QSize(16, 16))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_add_base)


        self.verticalLayout.addLayout(self.formLayout)

        self.btn_apply_settings = QPushButton(Cylinder_View)
        self.btn_apply_settings.setObjectName(u"btn_apply_settings")
        self.btn_apply_settings.setMinimumSize(QSize(240, 33))
        self.btn_apply_settings.setMaximumSize(QSize(1000, 16777215))
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

        self.verticalLayout.addWidget(self.btn_apply_settings)

        self.verticalSpacer = QSpacerItem(265, 270, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.spinbox_diameter)
        self.label_2.setBuddy(self.spinbox_length)
        self.label_3.setBuddy(self.cb_add_base)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Cylinder_View)

        QMetaObject.connectSlotsByName(Cylinder_View)
    # setupUi

    def retranslateUi(self, Cylinder_View):
        Cylinder_View.setWindowTitle(QCoreApplication.translate("Cylinder_View", u"Form", None))
        self.label.setText(QCoreApplication.translate("Cylinder_View", u"Cylinder diameter", None))
        self.spinbox_diameter.setSuffix(QCoreApplication.translate("Cylinder_View", u" mm", None))
        self.label_2.setText(QCoreApplication.translate("Cylinder_View", u"Cylinder length", None))
        self.spinbox_length.setSuffix(QCoreApplication.translate("Cylinder_View", u" mm", None))
        self.label_3.setText(QCoreApplication.translate("Cylinder_View", u"Add Base", None))
        self.cb_add_base.setText("")
        self.btn_apply_settings.setText(QCoreApplication.translate("Cylinder_View", u"Apply Settings", None))
    # retranslateUi

