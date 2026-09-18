# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'giaodien.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lcd_truck = QLCDNumber(self.groupBox)
        self.lcd_truck.setObjectName(u"lcd_truck")

        self.gridLayout.addWidget(self.lcd_truck, 4, 1, 1, 1)

        self.lcd_bus = QLCDNumber(self.groupBox)
        self.lcd_bus.setObjectName(u"lcd_bus")

        self.gridLayout.addWidget(self.lcd_bus, 3, 1, 1, 1)

        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.lbl_motor = QLabel(self.splitter)
        self.lbl_motor.setObjectName(u"lbl_motor")
        self.splitter.addWidget(self.lbl_motor)
        self.lbl_car = QLabel(self.splitter)
        self.lbl_car.setObjectName(u"lbl_car")
        self.splitter.addWidget(self.lbl_car)
        self.lbl_bus = QLabel(self.splitter)
        self.lbl_bus.setObjectName(u"lbl_bus")
        self.splitter.addWidget(self.lbl_bus)
        self.lbl_truck = QLabel(self.splitter)
        self.lbl_truck.setObjectName(u"lbl_truck")
        self.splitter.addWidget(self.lbl_truck)
        self.lbl_total = QLabel(self.splitter)
        self.lbl_total.setObjectName(u"lbl_total")
        self.splitter.addWidget(self.lbl_total)

        self.gridLayout.addWidget(self.splitter, 0, 0, 6, 1)

        self.lcd_car = QLCDNumber(self.groupBox)
        self.lcd_car.setObjectName(u"lcd_car")

        self.gridLayout.addWidget(self.lcd_car, 2, 1, 1, 1)

        self.lcd_total = QLCDNumber(self.groupBox)
        self.lcd_total.setObjectName(u"lcd_total")

        self.gridLayout.addWidget(self.lcd_total, 5, 1, 1, 1)

        self.lcd_motor = QLCDNumber(self.groupBox)
        self.lcd_motor.setObjectName(u"lcd_motor")

        self.gridLayout.addWidget(self.lcd_motor, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName(u"lbl_status")
        font = QFont()
        font.setPointSize(14)
        self.lbl_status.setFont(font)

        self.verticalLayout.addWidget(self.lbl_status)

        self.prog_wti = QProgressBar(self.centralwidget)
        self.prog_wti.setObjectName(u"prog_wti")
        self.prog_wti.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #555;\n"
"    border-radius: 5px;\n"
"    text-align: center;        /* \u00c9p ch\u1eef s\u1ed1 % v\u00e0o gi\u1eefa thanh */\n"
"    color: white;              \n"
"    font-weight: bold;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #ff9800; /* Ph\u1ea7n ch\u1ea1y m\u00e0u cam c\u1ea3nh b\u00e1o */\n"
"    width: 20px;\n"
"}")
        self.prog_wti.setValue(24)

        self.verticalLayout.addWidget(self.prog_wti)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.LabelRole, self.verticalLayout)

        self.lbl_camera = QLabel(self.centralwidget)
        self.lbl_camera.setObjectName(u"lbl_camera")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_camera.sizePolicy().hasHeightForWidth())
        self.lbl_camera.setSizePolicy(sizePolicy)
        self.lbl_camera.setFrameShape(QFrame.Shape.Box)
        self.lbl_camera.setTextFormat(Qt.TextFormat.AutoText)
        self.lbl_camera.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_camera.setWordWrap(False)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lbl_camera)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_start = QPushButton(self.centralwidget)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setStyleSheet(u"QPushButton {\n"
"    background-color: #28a745; /* M\u00e0u xanh l\u00e1 */\n"
"    color: white;              /* Ch\u1eef m\u00e0u tr\u1eafng */\n"
"    font-weight: bold;\n"
"    border-radius: 5px;        /* Bo g\u00f3c */\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #218838; /* \u0110\u1ed5i m\u00e0u xanh \u0111\u1eadm h\u01a1n khi r\u00ea chu\u1ed9t */\n"
"}")

        self.horizontalLayout.addWidget(self.btn_start)

        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setStyleSheet(u"QPushButton {\n"
"    background-color: #dc3545; /* M\u00e0u \u0111\u1ecf */\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #c82333; /* \u0110\u1ed5i m\u00e0u \u0111\u1ecf \u0111\u1eadm h\u01a1n khi r\u00ea chu\u1ed9t */\n"
"}")

        self.horizontalLayout.addWidget(self.btn_stop)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Th\u1ed1ng k\u00ea ph\u01b0\u01a1ng ti\u1ec7n", None))
        self.lbl_motor.setText(QCoreApplication.translate("MainWindow", u"Xe m\u00e1y:", None))
        self.lbl_car.setText(QCoreApplication.translate("MainWindow", u"\u00d4 t\u00f4:", None))
        self.lbl_bus.setText(QCoreApplication.translate("MainWindow", u"Xe bu\u00fdt:", None))
        self.lbl_truck.setText(QCoreApplication.translate("MainWindow", u"Xe t\u1ea3i:", None))
        self.lbl_total.setText(QCoreApplication.translate("MainWindow", u"T\u1ed5ng c\u1ed9ng:", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i: \u0110ang ch\u1edd", None))
        self.lbl_camera.setText(QCoreApplication.translate("MainWindow", u"KHUNG HI\u1ec2N TH\u1eca CAMERA", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Kh\u1edfi \u0111\u1ed9ng camera", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"D\u1eebng h\u1ec7 th\u1ed1ng", None))
    # retranslateUi

