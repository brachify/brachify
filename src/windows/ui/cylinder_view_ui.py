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
    QGridLayout, QGroupBox, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_Cylinder_View(object):
    def setupUi(self, Cylinder_View):
        if not Cylinder_View.objectName():
            Cylinder_View.setObjectName(u"Cylinder_View")
        Cylinder_View.resize(271, 411)
        Cylinder_View.setStyleSheet(u"background-color: rgb(250,250,250);")
        self.groupBox = QGroupBox(Cylinder_View)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 271, 411))
        self.groupBox.setMinimumSize(QSize(271, 411))
        self.groupBox.setMaximumSize(QSize(271, 16777215))
        self.groupBox.setStyleSheet(u"background-color: rgb(240, 245, 250);")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinbox_diameter = QDoubleSpinBox(self.groupBox)
        self.spinbox_diameter.setObjectName(u"spinbox_diameter")
        self.spinbox_diameter.setMinimumSize(QSize(135, 0))
        self.spinbox_diameter.setMaximumSize(QSize(16777215, 16777215))
        self.spinbox_diameter.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinbox_diameter)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spinbox_length = QSpinBox(self.groupBox)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setMinimumSize(QSize(135, 0))
        self.spinbox_length.setMaximumSize(QSize(16777215, 16777215))
        self.spinbox_length.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.spinbox_length.setMinimum(60)
        self.spinbox_length.setMaximum(300)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinbox_length)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(240, 245, 250);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.cb_add_base = QCheckBox(self.groupBox)
        self.cb_add_base.setObjectName(u"cb_add_base")
        self.cb_add_base.setMaximumSize(QSize(1000, 16777215))
        self.cb_add_base.setLayoutDirection(Qt.RightToLeft)
        self.cb_add_base.setIconSize(QSize(16, 16))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_add_base)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.btn_apply_settings = QPushButton(self.groupBox)
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

        self.gridLayout_2.addWidget(self.btn_apply_settings, 1, 0, 1, 1)

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
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Cylinder_View", u"Cylinder diameter", None))
        self.label_2.setText(QCoreApplication.translate("Cylinder_View", u"Cylinder length", None))
        self.spinbox_length.setSuffix(QCoreApplication.translate("Cylinder_View", u" mm", None))
        self.label_3.setText(QCoreApplication.translate("Cylinder_View", u"Add Base", None))
        self.cb_add_base.setText("")
        self.btn_apply_settings.setText(QCoreApplication.translate("Cylinder_View", u"Apply Settings", None))
    # retranslateUi

