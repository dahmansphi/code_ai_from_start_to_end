# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiview_fsp_v01.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
from . import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(762, 521)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;	\n"
"	background-color: rgb(6, 5, 5);\n"
"}\n"
"\n"
"QPushButton, QLabel, QListWidget,QLineEdit,QTextEdit\n"
"{\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit, QComboBox{\n"
"	\n"
"	background-color: rgb(7,8,7);\n"
"}\n"
"\n"
"QComboBox{\n"
"	color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: #699469;\n"
"	border: 1px solid #191f19;\n"
"    selection-background-color: #191f19;\n"
"}\n"
"\n"
"QListWidget::item:selected { selection-background-color: blue; }")
        MainWindow.setIconSize(QSize(80, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"*{background-color: rgb(7,8,7);}\n"
"\n"
"QFrame#header_frame{\n"
"	border: 1px solid rgb(11,13,11);\n"
"}")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(11, 0, 0, 0)
        self.pushButton = QPushButton(self.header_left_frame)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/iconsSVG/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/iconsSVG/laptop.svg"))
        self.label.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(7, 8, 7, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_2.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setAutoFillBackground(False)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setStyleSheet(u"#close_window_btn:hover,\n"
"#min_window_btn:hover,\n"
"#restor_window_btn:hover\n"
"{\n"
"\n"
"background:#0f120f;\n"
"\n"
"}\n"
"")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 8, 0)
        self.min_window_btn = QPushButton(self.header_right_frame)
        self.min_window_btn.setObjectName(u"min_window_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/iconsSVG/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_window_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.min_window_btn)

        self.close_window_btn = QPushButton(self.header_right_frame)
        self.close_window_btn.setObjectName(u"close_window_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/iconsSVG/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.close_window_btn)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.MB_frame_Menu = QFrame(self.main_body_frame)
        self.MB_frame_Menu.setObjectName(u"MB_frame_Menu")
        self.MB_frame_Menu.setStyleSheet(u"background-color: rgb(7,8,7);")
        self.MB_frame_Menu.setFrameShape(QFrame.StyledPanel)
        self.MB_frame_Menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MB_frame_Menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_items = QFrame(self.MB_frame_Menu)
        self.menu_items.setObjectName(u"menu_items")
        self.menu_items.setStyleSheet(u"")
        self.menu_items.setFrameShape(QFrame.StyledPanel)
        self.menu_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_items)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.view_case_frame = QFrame(self.menu_items)
        self.view_case_frame.setObjectName(u"view_case_frame")
        self.view_case_frame.setMaximumSize(QSize(16777215, 40))
        self.view_case_frame.setStyleSheet(u":hover{\n"
"\n"
"background:#0f120f;\n"
"\n"
"}\n"
"")
        self.view_case_frame.setFrameShape(QFrame.StyledPanel)
        self.view_case_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.view_case_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.view_sector_page_btn = QPushButton(self.view_case_frame)
        self.view_sector_page_btn.setObjectName(u"view_sector_page_btn")
        self.view_sector_page_btn.setMinimumSize(QSize(120, 0))
        self.view_sector_page_btn.setMaximumSize(QSize(100, 40))
        font2 = QFont()
        font2.setPointSize(10)
        self.view_sector_page_btn.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/icons/iconsSVG/list-view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.view_sector_page_btn.setIcon(icon3)
        self.view_sector_page_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.view_sector_page_btn, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.view_case_frame)

        self.add_case_frame = QFrame(self.menu_items)
        self.add_case_frame.setObjectName(u"add_case_frame")
        self.add_case_frame.setMaximumSize(QSize(16777215, 40))
        self.add_case_frame.setStyleSheet(u":hover{\n"
"\n"
"background:#0f120f;\n"
"\n"
"}\n"
"\n"
"")
        self.add_case_frame.setFrameShape(QFrame.StyledPanel)
        self.add_case_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.add_case_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.view_profile_page_btn = QPushButton(self.add_case_frame)
        self.view_profile_page_btn.setObjectName(u"view_profile_page_btn")
        self.view_profile_page_btn.setMinimumSize(QSize(120, 0))
        self.view_profile_page_btn.setMaximumSize(QSize(100, 40))
        self.view_profile_page_btn.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/icons/iconsSVG/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.view_profile_page_btn.setIcon(icon4)
        self.view_profile_page_btn.setIconSize(QSize(30, 30))
        self.view_profile_page_btn.setAutoDefault(False)

        self.horizontalLayout_10.addWidget(self.view_profile_page_btn, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.add_case_frame)


        self.verticalLayout_2.addWidget(self.menu_items, 0, Qt.AlignLeft)

        self.menu_break_line = QFrame(self.MB_frame_Menu)
        self.menu_break_line.setObjectName(u"menu_break_line")
        self.menu_break_line.setFrameShape(QFrame.StyledPanel)
        self.menu_break_line.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menu_break_line)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.line = QFrame(self.menu_break_line)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)


        self.verticalLayout_2.addWidget(self.menu_break_line, 0, Qt.AlignLeft)

        self.about = QFrame(self.MB_frame_Menu)
        self.about.setObjectName(u"about")
        self.about.setFrameShape(QFrame.StyledPanel)
        self.about.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.about)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.about_logo_frame = QFrame(self.about)
        self.about_logo_frame.setObjectName(u"about_logo_frame")
        self.about_logo_frame.setFrameShape(QFrame.StyledPanel)
        self.about_logo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.about_logo_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.logo_about = QLabel(self.about_logo_frame)
        self.logo_about.setObjectName(u"logo_about")
        self.logo_about.setMinimumSize(QSize(100, 40))
        self.logo_about.setMaximumSize(QSize(130, 40))
        self.logo_about.setPixmap(QPixmap(u":/icons/iconsSVG/logo-desgin-white.gif"))
        self.logo_about.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.logo_about, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.about_logo_frame, 0, Qt.AlignLeft)

        self.about_desc_frame = QFrame(self.about)
        self.about_desc_frame.setObjectName(u"about_desc_frame")
        font3 = QFont()
        font3.setPointSize(7)
        self.about_desc_frame.setFont(font3)
        self.about_desc_frame.setFrameShape(QFrame.StyledPanel)
        self.about_desc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.about_desc_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.about_desc_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 60))
        self.label_3.setMaximumSize(QSize(130, 60))
        self.label_3.setFont(font3)
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)

        self.horizontalLayout_9.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.about_desc_frame, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.about, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_7.addWidget(self.MB_frame_Menu, 0, Qt.AlignLeft)

        self.MB_frame_Main = QFrame(self.main_body_frame)
        self.MB_frame_Main.setObjectName(u"MB_frame_Main")
        self.MB_frame_Main.setFrameShape(QFrame.StyledPanel)
        self.MB_frame_Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.MB_frame_Main)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.MB_frame_Main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.view_profile_page = QWidget()
        self.view_profile_page.setObjectName(u"view_profile_page")
        self.view_profile_page.setStyleSheet(u"QFrame#addPT_patientData_frame,#addPB_patientIMG_frame{\n"
"	border: 1px solid rgb(11,13,11);\n"
"}")
        self.horizontalLayout_14 = QHBoxLayout(self.view_profile_page)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.add_page_left_frame = QFrame(self.view_profile_page)
        self.add_page_left_frame.setObjectName(u"add_page_left_frame")
        self.add_page_left_frame.setFrameShape(QFrame.StyledPanel)
        self.add_page_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.add_page_left_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.addPT_patientData_frame = QFrame(self.add_page_left_frame)
        self.addPT_patientData_frame.setObjectName(u"addPT_patientData_frame")
        self.addPT_patientData_frame.setFrameShape(QFrame.StyledPanel)
        self.addPT_patientData_frame.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.addPT_patientData_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 100, 20, 20))
        self.label_7.setMinimumSize(QSize(20, 20))
        self.label_7.setMaximumSize(QSize(20, 20))
        self.label_7.setPixmap(QPixmap(u":/icons/iconsSVG/code-alt.svg"))
        self.label_7.setScaledContents(True)
        self.add_age = QLineEdit(self.addPT_patientData_frame)
        self.add_age.setObjectName(u"add_age")
        self.add_age.setGeometry(QRect(200, 20, 106, 16))
        self.add_age.setMaxLength(2)
        self.add_age.setReadOnly(True)
        self.label_6 = QLabel(self.addPT_patientData_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 60, 20, 20))
        self.label_6.setMinimumSize(QSize(20, 20))
        self.label_6.setMaximumSize(QSize(20, 20))
        self.label_6.setPixmap(QPixmap(u":/icons/iconsSVG/sticker.svg"))
        self.label_6.setScaledContents(True)
        self.add_description = QLineEdit(self.addPT_patientData_frame)
        self.add_description.setObjectName(u"add_description")
        self.add_description.setGeometry(QRect(200, 60, 106, 16))
        self.add_description.setMaxLength(50)
        self.add_description.setReadOnly(True)
        self.label_5 = QLabel(self.addPT_patientData_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 20, 20))
        self.label_5.setMinimumSize(QSize(20, 20))
        self.label_5.setMaximumSize(QSize(20, 20))
        self.label_5.setPixmap(QPixmap(u":/icons/iconsSVG/lock-alt.svg"))
        self.label_5.setScaledContents(True)
        self.label_10 = QLabel(self.addPT_patientData_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 20, 121, 16))
        self.label_9 = QLabel(self.addPT_patientData_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 60, 91, 16))
        self.label_11 = QLabel(self.addPT_patientData_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 100, 101, 16))
        self.label_4 = QLabel(self.addPT_patientData_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 20, 20))
        self.label_4.setMinimumSize(QSize(20, 20))
        self.label_4.setMaximumSize(QSize(20, 20))
        self.label_4.setPixmap(QPixmap(u":/icons/iconsSVG/cart-add.svg"))
        self.label_4.setScaledContents(True)
        self.label_12 = QLabel(self.addPT_patientData_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(60, 140, 101, 16))
        self.lineEdit = QLineEdit(self.addPT_patientData_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 100, 113, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QLineEdit(self.addPT_patientData_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(200, 140, 113, 20))
        self.lineEdit_2.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.addPT_patientData_frame)

        self.addPB_patientIMG_frame = QFrame(self.add_page_left_frame)
        self.addPB_patientIMG_frame.setObjectName(u"addPB_patientIMG_frame")
        self.addPB_patientIMG_frame.setFrameShape(QFrame.StyledPanel)
        self.addPB_patientIMG_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.addPB_patientIMG_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.add_patient_img_btn = QFrame(self.addPB_patientIMG_frame)
        self.add_patient_img_btn.setObjectName(u"add_patient_img_btn")
        self.add_patient_img_btn.setFrameShape(QFrame.StyledPanel)
        self.add_patient_img_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.add_patient_img_btn)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.live_price_chart_btn = QPushButton(self.add_patient_img_btn)
        self.live_price_chart_btn.setObjectName(u"live_price_chart_btn")
        self.live_price_chart_btn.setStyleSheet(u":hover{\n"
"\n"
"background:#0f120f;\n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/iconsSVG/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.live_price_chart_btn.setIcon(icon5)

        self.horizontalLayout_16.addWidget(self.live_price_chart_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_15.addWidget(self.add_patient_img_btn)

        self.add_patient_img_frame = QFrame(self.addPB_patientIMG_frame)
        self.add_patient_img_frame.setObjectName(u"add_patient_img_frame")
        self.add_patient_img_frame.setStyleSheet(u"background-color: rgb(7,8,7);")
        self.add_patient_img_frame.setFrameShape(QFrame.StyledPanel)
        self.add_patient_img_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.add_patient_img_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.history_price_graph_frame = QLabel(self.add_patient_img_frame)
        self.history_price_graph_frame.setObjectName(u"history_price_graph_frame")
        self.history_price_graph_frame.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.history_price_graph_frame)


        self.horizontalLayout_15.addWidget(self.add_patient_img_frame)


        self.verticalLayout_9.addWidget(self.addPB_patientIMG_frame)


        self.horizontalLayout_14.addWidget(self.add_page_left_frame)

        self.add_page_right_frame = QFrame(self.view_profile_page)
        self.add_page_right_frame.setObjectName(u"add_page_right_frame")
        self.add_page_right_frame.setMinimumSize(QSize(180, 0))
        self.add_page_right_frame.setMaximumSize(QSize(180, 16777215))
        self.add_page_right_frame.setFrameShape(QFrame.StyledPanel)
        self.add_page_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.add_page_right_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.addPT_right_frame_lbl = QFrame(self.add_page_right_frame)
        self.addPT_right_frame_lbl.setObjectName(u"addPT_right_frame_lbl")
        self.addPT_right_frame_lbl.setFrameShape(QFrame.StyledPanel)
        self.addPT_right_frame_lbl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.addPT_right_frame_lbl)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_3 = QPushButton(self.addPT_right_frame_lbl)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/iconsSVG/language.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.pushButton_3)

        self.profile_list_widget = QListWidget(self.addPT_right_frame_lbl)
        self.profile_list_widget.setObjectName(u"profile_list_widget")

        self.verticalLayout_11.addWidget(self.profile_list_widget)

        self.label_8 = QLabel(self.addPT_right_frame_lbl)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/icons/iconsSVG/layers.svg"))

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.addPT_right_frame_lbl)

        self.addPB_right_frame_btnFrame = QFrame(self.add_page_right_frame)
        self.addPB_right_frame_btnFrame.setObjectName(u"addPB_right_frame_btnFrame")
        self.addPB_right_frame_btnFrame.setFrameShape(QFrame.StyledPanel)
        self.addPB_right_frame_btnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.addPB_right_frame_btnFrame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.check_fingerprint_btn = QPushButton(self.addPB_right_frame_btnFrame)
        self.check_fingerprint_btn.setObjectName(u"check_fingerprint_btn")
        font4 = QFont()
        font4.setPointSize(8)
        self.check_fingerprint_btn.setFont(font4)
        self.check_fingerprint_btn.setStyleSheet(u":hover{\n"
"\n"
"background:#0f120f;\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/iconsSVG/add-to-list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.check_fingerprint_btn.setIcon(icon7)
        self.check_fingerprint_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_18.addWidget(self.check_fingerprint_btn)


        self.verticalLayout_10.addWidget(self.addPB_right_frame_btnFrame)


        self.horizontalLayout_14.addWidget(self.add_page_right_frame)

        self.stackedWidget.addWidget(self.view_profile_page)
        self.view_sector_page = QWidget()
        self.view_sector_page.setObjectName(u"view_sector_page")
        self.view_sector_page.setStyleSheet(u"QFrame#viewPL_bottom_frame, #viewPL_upper_frame, #view_case_widget{\n"
"	border: 1px solid rgb(11,13,11);\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.view_sector_page)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.view_page_left_frame = QFrame(self.view_sector_page)
        self.view_page_left_frame.setObjectName(u"view_page_left_frame")
        self.view_page_left_frame.setStyleSheet(u"")
        self.view_page_left_frame.setFrameShape(QFrame.StyledPanel)
        self.view_page_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.view_page_left_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.viewPL_upper_frame = QFrame(self.view_page_left_frame)
        self.viewPL_upper_frame.setObjectName(u"viewPL_upper_frame")
        self.viewPL_upper_frame.setFrameShape(QFrame.StyledPanel)
        self.viewPL_upper_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.viewPL_upper_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.view_companies_widget = QListWidget(self.viewPL_upper_frame)
        self.view_companies_widget.setObjectName(u"view_companies_widget")

        self.horizontalLayout_13.addWidget(self.view_companies_widget)


        self.verticalLayout_7.addWidget(self.viewPL_upper_frame)


        self.horizontalLayout_12.addWidget(self.view_page_left_frame)

        self.view_page_right_frame = QFrame(self.view_sector_page)
        self.view_page_right_frame.setObjectName(u"view_page_right_frame")
        self.view_page_right_frame.setMinimumSize(QSize(240, 0))
        self.view_page_right_frame.setMaximumSize(QSize(240, 16777215))
        self.view_page_right_frame.setFrameShape(QFrame.StyledPanel)
        self.view_page_right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.view_page_right_frame)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 9, -1, -1)
        self.pushButton_2 = QPushButton(self.view_page_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/icons/iconsSVG/list-alt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon8)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.verticalLayout_8.addWidget(self.pushButton_2, 0, Qt.AlignLeft)

        self.view_sectors_widget = QListWidget(self.view_page_right_frame)
        self.view_sectors_widget.setObjectName(u"view_sectors_widget")
        self.view_sectors_widget.setStyleSheet(u"QListWidget::item:selected{}\n"
"background-color: rgb(255, 248, 35);")

        self.verticalLayout_8.addWidget(self.view_sectors_widget)

        self.del_case_frame = QFrame(self.view_page_right_frame)
        self.del_case_frame.setObjectName(u"del_case_frame")
        self.del_case_frame.setFrameShape(QFrame.StyledPanel)
        self.del_case_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.del_case_frame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.add_com_to_profile_btn = QPushButton(self.del_case_frame)
        self.add_com_to_profile_btn.setObjectName(u"add_com_to_profile_btn")
        self.add_com_to_profile_btn.setStyleSheet(u":hover{\n"
"\n"
"background:#0f120f;\n"
"\n"
"}")
        self.add_com_to_profile_btn.setIcon(icon7)

        self.horizontalLayout_19.addWidget(self.add_com_to_profile_btn)


        self.verticalLayout_8.addWidget(self.del_case_frame)


        self.horizontalLayout_12.addWidget(self.view_page_right_frame)

        self.stackedWidget.addWidget(self.view_sector_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.error_msg_lbl = QLabel(self.MB_frame_Main)
        self.error_msg_lbl.setObjectName(u"error_msg_lbl")
        self.error_msg_lbl.setMinimumSize(QSize(0, 25))
        self.error_msg_lbl.setMaximumSize(QSize(16777215, 25))
        self.error_msg_lbl.setStyleSheet(u"color: rgb(255, 85, 0);")

        self.verticalLayout_6.addWidget(self.error_msg_lbl)


        self.horizontalLayout_7.addWidget(self.MB_frame_Main)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(7,8,7);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.footer_copyright_label = QLabel(self.footer_left_frame)
        self.footer_copyright_label.setObjectName(u"footer_copyright_label")

        self.horizontalLayout_6.addWidget(self.footer_copyright_label, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame, 0, Qt.AlignBottom)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setMinimumSize(QSize(20, 20))
        self.footer_right_frame.setMaximumSize(QSize(20, 20))
        self.footer_right_frame.setStyleSheet(u"background-image: url(:/icons/iconsSVG/apps-alt.svg);")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.footer_right_frame, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.main_body_frame.raise_()
        self.footer_frame.raise_()
        self.header_frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HCC_V01", None))
        self.pushButton.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FSP_V01", None))
        self.min_window_btn.setText("")
        self.close_window_btn.setText("")
        self.view_sector_page_btn.setText(QCoreApplication.translate("MainWindow", u"View Sectors", None))
        self.view_profile_page_btn.setText(QCoreApplication.translate("MainWindow", u"View  Profile", None))
        self.logo_about.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"This is a trial software. It aims to create fingerprint for IST stock companies. Yet, helps to predict hourly price motion.", None))
        self.label_7.setText("")
        self.add_age.setText("")
        self.add_age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u20ba00.00", None))
        self.label_6.setText("")
        self.add_description.setText("")
        self.add_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u20ba00.00 - \u20ba00.00", None))
        self.label_5.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PREVIOUS CLOSE", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"DAY RANGE", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MARKET CAP", None))
        self.label_4.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"P/E RATIO", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.00 TRY", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00.00", None))
        self.live_price_chart_btn.setText(QCoreApplication.translate("MainWindow", u"Live Price Chart", None))
        self.history_price_graph_frame.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Your Profile", None))
        self.label_8.setText("")
        self.check_fingerprint_btn.setText(QCoreApplication.translate("MainWindow", u"Check The Fingerprint", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"List All Sectors", None))
        self.add_com_to_profile_btn.setText(QCoreApplication.translate("MainWindow", u"add the selected comp to profile", None))
        self.error_msg_lbl.setText("")
        self.footer_copyright_label.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright DAHMAN'S Phi", None))
    # retranslateUi

