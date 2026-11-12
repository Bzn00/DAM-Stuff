# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(428, 463)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.campoIntroducirTarea = QLineEdit(self.centralwidget)
        self.campoIntroducirTarea.setObjectName(u"campoIntroducirTarea")

        self.gridLayout.addWidget(self.campoIntroducirTarea, 0, 0, 1, 1)

        self.botonIntroducirTarea = QPushButton(self.centralwidget)
        self.botonIntroducirTarea.setObjectName(u"botonIntroducirTarea")

        self.gridLayout.addWidget(self.botonIntroducirTarea, 1, 0, 1, 1)

        self.listaTareas = QListWidget(self.centralwidget)
        self.listaTareas.setObjectName(u"listaTareas")

        self.gridLayout.addWidget(self.listaTareas, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.botonIntroducirTarea.setText(QCoreApplication.translate("MainWindow", u"Introducir", None))
    # retranslateUi

