# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'modelo.ui'
##
# Created by: Qt User Interface Compiler version 6.7.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox,
                               QComboBox, QDateEdit, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QRadioButton, QScrollArea,
                               QSizePolicy, QSpacerItem, QSpinBox,
                               QStackedWidget, QTextBrowser, QTextEdit,
                               QTimeEdit, QToolButton, QVBoxLayout, QWidget)

import icon1_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1025, 700)
        MainWindow.setMinimumSize(QSize(1025, 700))
        MainWindow.setStyleSheet(u"background-color: rgb(254, 255, 238);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)

        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_cabecalho = QFrame(self.centralwidget)
        self.frame_cabecalho.setObjectName(u"frame_cabecalho")
        self.frame_cabecalho.setMaximumSize(QSize(16777215, 50))
        self.frame_cabecalho.setStyleSheet(
            u"background-color: #1F0B39; color: #fff;")
        self.frame_cabecalho.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_cabecalho.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_cabecalho)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_header_left = QFrame(self.frame_cabecalho)
        self.frame_header_left.setObjectName(u"frame_header_left")
        self.frame_header_left.setStyleSheet(u"border: none;\n"
                                             "background-color: rgb(97, 28, 152);")
        self.frame_header_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_header_left.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_header_left)

        self.frame_header_center = QFrame(self.frame_cabecalho)
        self.frame_header_center.setObjectName(u"frame_header_center")
        self.frame_header_center.setStyleSheet(u"border: none;\n"
                                               "background-color: rgb(97, 28, 152);")
        self.frame_header_center.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_header_center.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_header_center)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.header_titulo = QLabel(self.frame_header_center)
        self.header_titulo.setObjectName(u"header_titulo")

        self.gridLayout_2.addWidget(
            self.header_titulo, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.frame_header_center)

        self.frame_header_right = QFrame(self.frame_cabecalho)
        self.frame_header_right.setObjectName(u"frame_header_right")
        self.frame_header_right.setStyleSheet(u"border: none;\n"
                                              "background-color: rgb(97, 28, 152);")
        self.frame_header_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_header_right.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_header_right)

        self.gridLayout.addWidget(self.frame_cabecalho, 0, 0, 1, 2)

        self.frame_main_meio = QFrame(self.centralwidget)
        self.frame_main_meio.setObjectName(u"frame_main_meio")
        self.frame_main_meio.setStyleSheet(u"background-color: #fff;")
        self.frame_main_meio.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_3 = QGridLayout(self.frame_main_meio)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.abas = QStackedWidget(self.frame_main_meio)
        self.abas.setObjectName(u"abas")
        self.abas.setStyleSheet(u"")
        self.pg_PROVA = QWidget()
        self.pg_PROVA.setObjectName(u"pg_PROVA")
        self.pg_PROVA.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.verticalLayout_4 = QVBoxLayout(self.pg_PROVA)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pg_PROVA_frame_top = QFrame(self.pg_PROVA)
        self.pg_PROVA_frame_top.setObjectName(u"pg_PROVA_frame_top")
        self.pg_PROVA_frame_top.setMaximumSize(QSize(16777215, 50))
        self.pg_PROVA_frame_top.setStyleSheet(u"QFrame{\n"
                                              "	border: none;\n"
                                              "}")
        self.pg_PROVA_frame_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.pg_PROVA_frame_top.setFrameShadow(QFrame.Shadow.Raised)
        self.pg_PROVA_frame_top.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.pg_PROVA_frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.pg1_btn_novo = QPushButton(self.pg_PROVA_frame_top)
        self.pg1_btn_novo.setObjectName(u"pg1_btn_novo")
        palette = QPalette()
        brush = QBrush(QColor(63, 63, 63, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(204, 204, 204, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(63, 63, 63, 128))
        brush2.setStyle(Qt.SolidPattern)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
# endif
        self.pg1_btn_novo.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pg1_btn_novo.setFont(font)
        self.pg1_btn_novo.setCursor(QCursor(Qt.PointingHandCursor))
        self.pg1_btn_novo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pg1_btn_novo.setStyleSheet(u"QPushButton{\n"
                                        "  	width: 100%;\n"
                                        "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                        "    text-align: center;\n"
                                        "    padding: 10px;\n"
                                        "\n"
                                        "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                        "	background-color: rgb(204, 204, 204);\n"
                                        "	color: rgb(63, 63, 63);\n"
                                        "	\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::hover{\n"
                                        "	background-color: rgb(85, 39, 159);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed{\n"
                                        "	background-color: #611C98;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "")
        self.pg1_btn_novo.setText(u"NOVO")
        icon = QIcon()
        icon.addFile(u":/icon/plus-black.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pg1_btn_novo.setIcon(icon)
        self.pg1_btn_novo.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(
            self.pg1_btn_novo, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout_4.addWidget(self.pg_PROVA_frame_top)

        self.pg_PROVA_frame_center = QFrame(self.pg_PROVA)
        self.pg_PROVA_frame_center.setObjectName(u"pg_PROVA_frame_center")
        self.pg_PROVA_frame_center.setMaximumSize(QSize(16777215, 80))
        self.pg_PROVA_frame_center.setStyleSheet(u"QFrame{\n"
                                                 "	border: none;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit{\n"
                                                 "	background-color: rgb(210, 210, 210);\n"
                                                 "	font-size: 12pt;\n"
                                                 "}")
        self.pg_PROVA_frame_center.setFrameShape(QFrame.Shape.StyledPanel)
        self.pg_PROVA_frame_center.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.pg_PROVA_frame_center)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_filtro_titulo = QLineEdit(self.pg_PROVA_frame_center)
        self.lineEdit_filtro_titulo.setObjectName(u"lineEdit_filtro_titulo")
        self.lineEdit_filtro_titulo.setMinimumSize(QSize(0, 50))
        self.lineEdit_filtro_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_filtro_titulo)

        self.lineEdit_filtro_turma = QLineEdit(self.pg_PROVA_frame_center)
        self.lineEdit_filtro_turma.setObjectName(u"lineEdit_filtro_turma")
        self.lineEdit_filtro_turma.setMinimumSize(QSize(0, 50))
        self.lineEdit_filtro_turma.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_filtro_turma)

        self.lineEdit_filtro_grupo = QLineEdit(self.pg_PROVA_frame_center)
        self.lineEdit_filtro_grupo.setObjectName(u"lineEdit_filtro_grupo")
        self.lineEdit_filtro_grupo.setMinimumSize(QSize(0, 50))
        self.lineEdit_filtro_grupo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_filtro_grupo)

        self.lineEdit_filtro_data = QLineEdit(self.pg_PROVA_frame_center)
        self.lineEdit_filtro_data.setObjectName(u"lineEdit_filtro_data")
        self.lineEdit_filtro_data.setMinimumSize(QSize(0, 50))
        self.lineEdit_filtro_data.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_filtro_data)

        self.verticalLayout_4.addWidget(self.pg_PROVA_frame_center)

        self.pg_PROVA_frame_bottom = QFrame(self.pg_PROVA)
        self.pg_PROVA_frame_bottom.setObjectName(u"pg_PROVA_frame_bottom")
        self.pg_PROVA_frame_bottom.setStyleSheet(u"QFrame{\n"
                                                 "	border: none;\n"
                                                 "}\n"
                                                 "")
        self.pg_PROVA_frame_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.pg_PROVA_frame_bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.pg_PROVA_frame_bottom.setLineWidth(0)
        self.verticalLayout_14 = QVBoxLayout(self.pg_PROVA_frame_bottom)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.FP_header_info = QFrame(self.pg_PROVA_frame_bottom)
        self.FP_header_info.setObjectName(u"FP_header_info")
        self.FP_header_info.setMaximumSize(QSize(16777215, 30))
        self.FP_header_info.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
                                          "border: none;\n"
                                          "padding: 0px;\n"
                                          "color: #000;")
        self.FP_header_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_header_info.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.FP_header_info)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.FP_HEADER_INFO_titulo = QFrame(self.FP_header_info)
        self.FP_HEADER_INFO_titulo.setObjectName(u"FP_HEADER_INFO_titulo")
        self.FP_HEADER_INFO_titulo.setStyleSheet(u"color: #000;\n")
        self.FP_HEADER_INFO_titulo.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_HEADER_INFO_titulo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.FP_HEADER_INFO_titulo)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.FP_HEADER_INFO_titulo_label = QLabel(self.FP_HEADER_INFO_titulo)
        self.FP_HEADER_INFO_titulo_label.setObjectName(
            u"FP_HEADER_INFO_titulo_label")
        

        self.horizontalLayout_17.addWidget(
            self.FP_HEADER_INFO_titulo_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_16.addWidget(self.FP_HEADER_INFO_titulo)

        self.FP_HEADER_INFO_turma = QFrame(self.FP_header_info)
        self.FP_HEADER_INFO_turma.setObjectName(u"FP_HEADER_INFO_turma")
        self.FP_HEADER_INFO_turma.setStyleSheet(u"")
        self.FP_HEADER_INFO_turma.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_HEADER_INFO_turma.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.FP_HEADER_INFO_turma)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.FP_HEADER_INFO_turma_label = QLabel(self.FP_HEADER_INFO_turma)
        self.FP_HEADER_INFO_turma_label.setObjectName(
            u"FP_HEADER_INFO_turma_label")

        self.horizontalLayout_18.addWidget(
            self.FP_HEADER_INFO_turma_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_16.addWidget(self.FP_HEADER_INFO_turma)

        self.FP_HEADER_INFO_grupo = QFrame(self.FP_header_info)
        self.FP_HEADER_INFO_grupo.setObjectName(u"FP_HEADER_INFO_grupo")
        self.FP_HEADER_INFO_grupo.setStyleSheet(u"")
        self.FP_HEADER_INFO_grupo.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_HEADER_INFO_grupo.setFrameShadow(QFrame.Shadow.Raised)
        self.FP_HEADER_INFO_grupo.setLineWidth(0)
        self.horizontalLayout_19 = QHBoxLayout(self.FP_HEADER_INFO_grupo)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.FP_HEADER_INFO_grupo_label = QLabel(self.FP_HEADER_INFO_grupo)
        self.FP_HEADER_INFO_grupo_label.setObjectName(
            u"FP_HEADER_INFO_grupo_label")

        self.horizontalLayout_19.addWidget(
            self.FP_HEADER_INFO_grupo_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_16.addWidget(self.FP_HEADER_INFO_grupo)

        self.FP_HEADER_INFO_data_criacao = QFrame(self.FP_header_info)
        self.FP_HEADER_INFO_data_criacao.setObjectName(
            u"FP_HEADER_INFO_data_criacao")
        self.FP_HEADER_INFO_data_criacao.setStyleSheet(u"")
        self.FP_HEADER_INFO_data_criacao.setFrameShape(
            QFrame.Shape.StyledPanel)
        self.FP_HEADER_INFO_data_criacao.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(
            self.FP_HEADER_INFO_data_criacao)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.FP_HEADER_INFO_data_c_label = QLabel(
            self.FP_HEADER_INFO_data_criacao)
        self.FP_HEADER_INFO_data_c_label.setObjectName(
            u"FP_HEADER_INFO_data_c_label")

        self.horizontalLayout_20.addWidget(
            self.FP_HEADER_INFO_data_c_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_16.addWidget(self.FP_HEADER_INFO_data_criacao)

        self.FP_HEADER_INFO_hora_criacao = QFrame(self.FP_header_info)
        self.FP_HEADER_INFO_hora_criacao.setObjectName(
            u"FP_HEADER_INFO_hora_criacao")
        self.FP_HEADER_INFO_hora_criacao.setMaximumSize(QSize(120, 16777215))
        self.FP_HEADER_INFO_hora_criacao.setStyleSheet(u"")
        self.FP_HEADER_INFO_hora_criacao.setFrameShape(
            QFrame.Shape.StyledPanel)
        self.FP_HEADER_INFO_hora_criacao.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(
            self.FP_HEADER_INFO_hora_criacao)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.FP_HEADER_INFO_hora_label = QLabel(
            self.FP_HEADER_INFO_hora_criacao)
        self.FP_HEADER_INFO_hora_label.setObjectName(
            u"FP_HEADER_INFO_hora_label")

        self.horizontalLayout_21.addWidget(
            self.FP_HEADER_INFO_hora_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_16.addWidget(self.FP_HEADER_INFO_hora_criacao)

        self.FP_HEADER_INFO_acoes = QFrame(self.FP_header_info)
        self.FP_HEADER_INFO_acoes.setObjectName(u"FP_HEADER_INFO_acoes")
        self.FP_HEADER_INFO_acoes.setMaximumSize(QSize(150, 16777215))
        self.FP_HEADER_INFO_acoes.setStyleSheet(u"")
        self.FP_HEADER_INFO_acoes.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_HEADER_INFO_acoes.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.FP_HEADER_INFO_acoes)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(10, 10, 10, 10)
        self.FP_HEADER_INFO_acoes_label = QLabel(self.FP_HEADER_INFO_acoes)
        self.FP_HEADER_INFO_acoes_label.setObjectName(
            u"FP_HEADER_INFO_acoes_label")

        self.horizontalLayout_22.addWidget(
            self.FP_HEADER_INFO_acoes_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_16.addWidget(self.FP_HEADER_INFO_acoes)

        self.verticalLayout_14.addWidget(self.FP_header_info)

        self.scrollArea_provas = QScrollArea(self.pg_PROVA_frame_bottom)
        self.scrollArea_provas.setObjectName(u"scrollArea_provas")
        self.scrollArea_provas.setStyleSheet(u"QFrame{\n"
                                             "	border: none;\n"
                                             "}\n"
                                             "")
        self.scrollArea_provas.setWidgetResizable(True)
        self.scrollAreaWidgetContents_provas = QWidget()
        self.scrollAreaWidgetContents_provas.setObjectName(
            u"scrollAreaWidgetContents_provas")
        self.scrollAreaWidgetContents_provas.setGeometry(QRect(0, 0, 898, 110))
        self.verticalLayout_15 = QVBoxLayout(
            self.scrollAreaWidgetContents_provas)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.FP_1 = QFrame(self.scrollAreaWidgetContents_provas)
        self.FP_1.setObjectName(u"FP_1")
        self.FP_1.setMinimumSize(QSize(0, 40))
        self.FP_1.setMaximumSize(QSize(16777215, 40))
        self.FP_1.setStyleSheet(u"background-color: rgb(0, 85, 0);\n"
                                "background-color: rgb(85, 0, 127);\n"
                                "margin-bottom: 0px;\n"
                                "background-color: rgb(85, 0, 127);\n"
                                "height: 55px;\n"
                                "padding: 0px;\n"
                                "color: white;\n"

                                )
        self.FP_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.FP_1)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_23.setContentsMargins(0,0,0,0)
        self.FP_1_conteudo_titulo = QFrame(self.FP_1)
        self.FP_1_conteudo_titulo.setObjectName(u"FP_1_conteudo_titulo")
        self.FP_1_conteudo_titulo.setMinimumSize(QSize(150, 40))
        self.FP_1_conteudo_titulo.setMaximumSize(QSize(400, 40))
        self.FP_1_conteudo_titulo.setStyleSheet(u"")
        self.FP_1_conteudo_titulo.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_1_conteudo_titulo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.FP_1_conteudo_titulo)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(5, 0, 0, 0)
        self.FP_1_titulo = QLabel(self.FP_1_conteudo_titulo)
        self.FP_1_titulo.setObjectName(u"FP_1_titulo")
        self.FP_1_titulo.setStyleSheet(u"font: 12pt ;\n"
                                       "")

        self.horizontalLayout_36.addWidget(self.FP_1_titulo)

        self.horizontalLayout_23.addWidget(self.FP_1_conteudo_titulo)

        self.FP_1_conteudo_turma = QFrame(self.FP_1)
        self.FP_1_conteudo_turma.setObjectName(u"FP_1_conteudo_turma")
        self.FP_1_conteudo_turma.setMinimumSize(QSize(150, 40))
        self.FP_1_conteudo_turma.setMaximumSize(QSize(16777215, 40))
        self.FP_1_conteudo_turma.setStyleSheet(u"")
        self.FP_1_conteudo_turma.setInputMethodHints(
            Qt.InputMethodHint.ImhNone)
        self.FP_1_conteudo_turma.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_1_conteudo_turma.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.FP_1_conteudo_turma)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(10, 10, 10, 10)
        self.FP_1_bpx_turma = QComboBox(self.FP_1_conteudo_turma)
        self.FP_1_bpx_turma.addItem("")
        self.FP_1_bpx_turma.addItem("")
        self.FP_1_bpx_turma.setObjectName(u"FP_1_bpx_turma")
        self.FP_1_bpx_turma.setStyleSheet(u"QComboBox{\n"
                                          "	font: 12pt;\n"
                                          "}")

        self.horizontalLayout_34.addWidget(self.FP_1_bpx_turma)

        self.horizontalLayout_23.addWidget(self.FP_1_conteudo_turma)

        self.FP_1_conteudo_grupo = QFrame(self.FP_1)
        self.FP_1_conteudo_grupo.setObjectName(u"FP_1_conteudo_grupo")
        self.FP_1_conteudo_grupo.setMinimumSize(QSize(150, 40))
        self.FP_1_conteudo_grupo.setMaximumSize(QSize(16777215, 40))
        self.FP_1_conteudo_grupo.setStyleSheet(u"")
        self.FP_1_conteudo_grupo.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_1_conteudo_grupo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.FP_1_conteudo_grupo)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(10, 10, 10, 10)
        self.FP_1_box_grupo = QComboBox(self.FP_1_conteudo_grupo)
        self.FP_1_box_grupo.addItem("")
        self.FP_1_box_grupo.addItem("")
        self.FP_1_box_grupo.setObjectName(u"FP_1_box_grupo")
        self.FP_1_box_grupo.setStyleSheet(u"QComboBox{\n"
                                          "	font: 12pt;\n"
                                          "}")

        self.horizontalLayout_35.addWidget(self.FP_1_box_grupo)

        self.horizontalLayout_23.addWidget(self.FP_1_conteudo_grupo)

        self.FP_1_conteudo_data_criacao = QFrame(self.FP_1)
        self.FP_1_conteudo_data_criacao.setObjectName(
            u"FP_1_conteudo_data_criacao")
        self.FP_1_conteudo_data_criacao.setMinimumSize(QSize(145, 40))
        self.FP_1_conteudo_data_criacao.setMaximumSize(QSize(16777215, 40))
        self.FP_1_conteudo_data_criacao.setStyleSheet(u"")
        self.FP_1_conteudo_data_criacao.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_1_conteudo_data_criacao.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.FP_1_conteudo_data_criacao)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.FP_1_data_criacao = QDateEdit(self.FP_1_conteudo_data_criacao)
        self.FP_1_data_criacao.setObjectName(u"FP_1_data_criacao")
        self.FP_1_data_criacao.setMaximumSize(QSize(16777215, 150))
        self.FP_1_data_criacao.setStyleSheet(u"QDateEdit{\n"
                                             "	font: 12pt;\n"
                                             "}")

        self.horizontalLayout_32.addWidget(self.FP_1_data_criacao)

        self.horizontalLayout_23.addWidget(self.FP_1_conteudo_data_criacao)

        self.FP_1_conteudo_hora = QFrame(self.FP_1)
        self.FP_1_conteudo_hora.setObjectName(u"FP_1_conteudo_hora")
        self.FP_1_conteudo_hora.setMinimumSize(QSize(120, 40))
        self.FP_1_conteudo_hora.setMaximumSize(QSize(115, 40))
        self.FP_1_conteudo_hora.setStyleSheet(u"")
        self.FP_1_conteudo_hora.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_1_conteudo_hora.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.FP_1_conteudo_hora)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(10, 10, 10, 10)
        self.FP_1_hora_criacao = QTimeEdit(self.FP_1_conteudo_hora)
        self.FP_1_hora_criacao.setObjectName(u"FP_1_hora_criacao")
        self.FP_1_hora_criacao.setMaximumSize(QSize(16777215, 150))
        self.FP_1_hora_criacao.setStyleSheet(u"QTimeEdit{\n"
                                             "	font: 12pt;\n"
                                             "}")

        self.horizontalLayout_33.addWidget(self.FP_1_hora_criacao)

        self.horizontalLayout_23.addWidget(self.FP_1_conteudo_hora)

        self.FP_1_conteudo_acoes = QFrame(self.FP_1)
        self.FP_1_conteudo_acoes.setObjectName(u"FP_1_conteudo_acoes")
        self.FP_1_conteudo_acoes.setMinimumSize(QSize(135, 40))
        self.FP_1_conteudo_acoes.setMaximumSize(QSize(135, 40))
        self.FP_1_conteudo_acoes.setStyleSheet(u"")
        self.FP_1_conteudo_acoes.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_1_conteudo_acoes.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.FP_1_conteudo_acoes)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.FP_1_btn_delete = QPushButton(self.FP_1_conteudo_acoes)
        self.FP_1_btn_delete.setObjectName(u"FP_1_btn_delete")
        icon1 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.FP_1_btn_delete.setIcon(icon1)

        self.horizontalLayout_25.addWidget(self.FP_1_btn_delete)

        self.FP_1_btn_edit = QPushButton(self.FP_1_conteudo_acoes)
        self.FP_1_btn_edit.setObjectName(u"FP_1_btn_edit")
        self.FP_1_btn_edit.setStyleSheet(u"\n"
                                         "QToolButton{\n"
                                         "	padding-right: 15px;\n"
                                         "	margin-right: 5px;\n"
                                         "	background-color: rgb(107, 0, 0);\n"
                                         "\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton::hover{\n"
                                         "	background-color: rgb(200, 0, 0);\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton::pressed{\n"
                                         "	background-color: rgb(100, 0, 0);\n"
                                         "\n"
                                         "}")
        icon2 = QIcon(QIcon.fromTheme(u"mail-message-new"))
        self.FP_1_btn_edit.setIcon(icon2)

        self.horizontalLayout_25.addWidget(self.FP_1_btn_edit)

        self.horizontalLayout_23.addWidget(self.FP_1_conteudo_acoes)

        self.verticalLayout_15.addWidget(self.FP_1)

        self.FP_2 = QFrame(self.scrollAreaWidgetContents_provas)
        self.FP_2.setObjectName(u"FP_2")
        self.FP_2.setMinimumSize(QSize(0, 40))
        self.FP_2.setMaximumSize(QSize(16777215, 40))
        self.FP_2.setStyleSheet(u"background-color: rgb(85, 0, 127);\n"
                                "color: white;\n")
        
        self.FP_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.FP_2)
        self.horizontalLayout_44.setSpacing(6)
        # self.horizontalLayout_44.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.FP_2_conteudo_titulo = QFrame(self.FP_2)
        self.FP_2_conteudo_titulo.setObjectName(u"FP_2_conteudo_titulo")
        self.FP_2_conteudo_titulo.setMinimumSize(QSize(150, 40))
        self.FP_2_conteudo_titulo.setMaximumSize(QSize(400, 40))
        self.FP_2_conteudo_titulo.setStyleSheet(u"\n"
                                                "font: 12pt;")
        self.FP_2_conteudo_titulo.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_2_conteudo_titulo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.FP_2_conteudo_titulo)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(5, 0, 0, 0)
        self.FP_2_titulo = QLabel(self.FP_2_conteudo_titulo)
        self.FP_2_titulo.setObjectName(u"FP_2_titulo")

        self.horizontalLayout_45.addWidget(self.FP_2_titulo)

        self.horizontalLayout_44.addWidget(self.FP_2_conteudo_titulo)

        self.FP_2_conteudo_turma = QFrame(self.FP_2)
        self.FP_2_conteudo_turma.setObjectName(u"FP_2_conteudo_turma")
        self.FP_2_conteudo_turma.setMinimumSize(QSize(150, 40))
        self.FP_2_conteudo_turma.setMaximumSize(QSize(16777215, 40))
        self.FP_2_conteudo_turma.setStyleSheet(u"\n"
                                               "QFrame{\n"
                                               "	Margin: 0px;\n"
                                               "\n"
                                               "}")
        self.FP_2_conteudo_turma.setInputMethodHints(
            Qt.InputMethodHint.ImhNone)
        self.FP_2_conteudo_turma.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_2_conteudo_turma.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.FP_2_conteudo_turma)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(10, 10, 10, 10)
        self.FP_2_box_turma = QComboBox(self.FP_2_conteudo_turma)
        self.FP_2_box_turma.addItem("")
        self.FP_2_box_turma.addItem("")
        self.FP_2_box_turma.setObjectName(u"FP_2_box_turma")
        self.FP_2_box_turma.setStyleSheet(u"QComboBox{\n"
                                          "	font: 12pt;\n"
                                          "}")

        self.horizontalLayout_46.addWidget(self.FP_2_box_turma)

        self.horizontalLayout_44.addWidget(self.FP_2_conteudo_turma)

        self.FP_2_conteudo_grupo = QFrame(self.FP_2)
        self.FP_2_conteudo_grupo.setObjectName(u"FP_2_conteudo_grupo")
        self.FP_2_conteudo_grupo.setMinimumSize(QSize(150, 40))
        self.FP_2_conteudo_grupo.setMaximumSize(QSize(16777215, 40))
        self.FP_2_conteudo_grupo.setStyleSheet(u"")
        self.FP_2_conteudo_grupo.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_2_conteudo_grupo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.FP_2_conteudo_grupo)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(10, 10, 10, 10)
        self.FP_2_box_grupo = QComboBox(self.FP_2_conteudo_grupo)
        self.FP_2_box_grupo.addItem("")
        self.FP_2_box_grupo.addItem("")
        self.FP_2_box_grupo.setObjectName(u"FP_2_box_grupo")
        self.FP_2_box_grupo.setStyleSheet(u"QComboBox{\n"
                                          "	font: 12pt;\n"
                                          "}")

        self.horizontalLayout_47.addWidget(self.FP_2_box_grupo)

        self.horizontalLayout_44.addWidget(self.FP_2_conteudo_grupo)

        self.FP_2_conteudo_data_criacao = QFrame(self.FP_2)
        self.FP_2_conteudo_data_criacao.setObjectName(
            u"FP_2_conteudo_data_criacao")
        self.FP_2_conteudo_data_criacao.setMinimumSize(QSize(145, 40))
        self.FP_2_conteudo_data_criacao.setMaximumSize(QSize(16777215, 40))
        self.FP_2_conteudo_data_criacao.setStyleSheet(u"")
        self.FP_2_conteudo_data_criacao.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_2_conteudo_data_criacao.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.FP_2_conteudo_data_criacao)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(10, 10, 10, 10)
        self.FP_2_data_criacao = QDateEdit(self.FP_2_conteudo_data_criacao)
        self.FP_2_data_criacao.setObjectName(u"FP_2_data_criacao")
        self.FP_2_data_criacao.setMaximumSize(QSize(16777215, 150))
        self.FP_2_data_criacao.setStyleSheet(u"QDateEdit{\n"
                                             "	font: 12pt;\n"
                                             "}")

        self.horizontalLayout_48.addWidget(self.FP_2_data_criacao)

        self.horizontalLayout_44.addWidget(self.FP_2_conteudo_data_criacao)

        self.FP_2_conteudo_hora = QFrame(self.FP_2)
        self.FP_2_conteudo_hora.setObjectName(u"FP_2_conteudo_hora")
        self.FP_2_conteudo_hora.setMinimumSize(QSize(120, 40))
        self.FP_2_conteudo_hora.setMaximumSize(QSize(115, 40))
        self.FP_2_conteudo_hora.setStyleSheet(u"")
        self.FP_2_conteudo_hora.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_2_conteudo_hora.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.FP_2_conteudo_hora)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(10, 10, 10, 10)
        self.FP_2_hora_criacao = QTimeEdit(self.FP_2_conteudo_hora)
        self.FP_2_hora_criacao.setObjectName(u"FP_2_hora_criacao")
        self.FP_2_hora_criacao.setMaximumSize(QSize(16777215, 150))
        self.FP_2_hora_criacao.setStyleSheet(u"QTimeEdit{\n"
                                             "	font: 12pt;\n"
                                             "}")

        self.horizontalLayout_49.addWidget(self.FP_2_hora_criacao)

        self.horizontalLayout_44.addWidget(self.FP_2_conteudo_hora)

        self.FP_2_conteudo_acoes = QFrame(self.FP_2)
        self.FP_2_conteudo_acoes.setObjectName(u"FP_2_conteudo_acoes")
        self.FP_2_conteudo_acoes.setMinimumSize(QSize(135, 40))
        self.FP_2_conteudo_acoes.setMaximumSize(QSize(135, 40))
        self.FP_2_conteudo_acoes.setStyleSheet(u"")
        self.FP_2_conteudo_acoes.setFrameShape(QFrame.Shape.StyledPanel)
        self.FP_2_conteudo_acoes.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.FP_2_conteudo_acoes)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.FP_2_btn_delete = QPushButton(self.FP_2_conteudo_acoes)
        self.FP_2_btn_delete.setObjectName(u"FP_2_btn_delete")
        self.FP_2_btn_delete.setIcon(icon1)

        self.horizontalLayout_50.addWidget(self.FP_2_btn_delete)

        self.FP_2_btn_edit = QPushButton(self.FP_2_conteudo_acoes)
        self.FP_2_btn_edit.setObjectName(u"FP_2_btn_edit")
        self.FP_2_btn_edit.setStyleSheet(u"\n"
                                         "QToolButton{\n"
                                         "	padding-right: 15px;\n"
                                         "	margin-right: 5px;\n"
                                         "	background-color: rgb(107, 0, 0);\n"
                                         "\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton::hover{\n"
                                         "	background-color: rgb(200, 0, 0);\n"
                                         "}\n"
                                         "\n"
                                         "QToolButton::pressed{\n"
                                         "	background-color: rgb(100, 0, 0);\n"
                                         "\n"
                                         "}")
        self.FP_2_btn_edit.setIcon(icon2)

        self.horizontalLayout_50.addWidget(self.FP_2_btn_edit)

        self.horizontalLayout_44.addWidget(self.FP_2_conteudo_acoes)

        self.verticalLayout_15.addWidget(self.FP_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.scrollArea_provas.setWidget(self.scrollAreaWidgetContents_provas)

        self.verticalLayout_14.addWidget(self.scrollArea_provas)

        self.verticalLayout_4.addWidget(self.pg_PROVA_frame_bottom)

        self.abas.addWidget(self.pg_PROVA)
        self.pg_GRUPO = QWidget()
        self.pg_GRUPO.setObjectName(u"pg_GRUPO")
        self.pg_GRUPO.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.pg_GRUPO)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.frame_pg_GRUPO_top = QFrame(self.pg_GRUPO)
        self.frame_pg_GRUPO_top.setObjectName(u"frame_pg_GRUPO_top")
        self.frame_pg_GRUPO_top.setMinimumSize(QSize(0, 80))
        self.frame_pg_GRUPO_top.setMaximumSize(QSize(16777215, 80))
        self.frame_pg_GRUPO_top.setStyleSheet(u"QFrame{\n"
                                              "	border: none;\n"
                                              "}")
        self.frame_pg_GRUPO_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_GRUPO_top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_pg_GRUPO_top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_pg_GRUPO_top_left = QFrame(self.frame_pg_GRUPO_top)
        self.frame_pg_GRUPO_top_left.setObjectName(u"frame_pg_GRUPO_top_left")
        self.frame_pg_GRUPO_top_left.setStyleSheet(u"")
        self.frame_pg_GRUPO_top_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_GRUPO_top_left.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.frame_pg_GRUPO_top_left)

        self.frame_pg_GRUPO_top_center = QFrame(self.frame_pg_GRUPO_top)
        self.frame_pg_GRUPO_top_center.setObjectName(
            u"frame_pg_GRUPO_top_center")
        self.frame_pg_GRUPO_top_center.setStyleSheet(u"")
        self.frame_pg_GRUPO_top_center.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_GRUPO_top_center.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_pg_GRUPO_top_center)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.header_titulo_2 = QLabel(self.frame_pg_GRUPO_top_center)
        self.header_titulo_2.setObjectName(u"header_titulo_2")
        self.header_titulo_2.setStyleSheet(u"color: #000;")

        self.horizontalLayout_8.addWidget(
            self.header_titulo_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_4.addWidget(self.frame_pg_GRUPO_top_center)

        self.frame_pg_GRUPO_top_right = QFrame(self.frame_pg_GRUPO_top)
        self.frame_pg_GRUPO_top_right.setObjectName(
            u"frame_pg_GRUPO_top_right")
        self.frame_pg_GRUPO_top_right.setStyleSheet(u"")
        self.frame_pg_GRUPO_top_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_GRUPO_top_right.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_pg_GRUPO_top_right)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pg1_btn_cancelar = QPushButton(self.frame_pg_GRUPO_top_right)
        self.pg1_btn_cancelar.setObjectName(u"pg1_btn_cancelar")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush3 = QBrush(QColor(85, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
# endif
        self.pg1_btn_cancelar.setPalette(palette1)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.pg1_btn_cancelar.setFont(font1)
        self.pg1_btn_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pg1_btn_cancelar.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight)
        self.pg1_btn_cancelar.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: rgb(85, 0, 0);\n"
                                            "  	width: 100%;\n"
                                            "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                            "    text-align: center;\n"
                                            "    padding: 10px;\n"
                                            "    color: white;\n"
                                            "    border-radius: 10px;\n"
                                            "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                            "	color: white;\n"
                                            "	border-radius: 10px;\n"
                                            "\n"
                                            "\n"
                                            "	\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::hover{\n"
                                            "	background-color: rgb(116, 0, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::pressed{\n"
                                            "	background-color: rgb(57, 0, 0);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")
        self.pg1_btn_cancelar.setText(u"Cancelar")
        self.pg1_btn_cancelar.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(
            self.pg1_btn_cancelar, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_4.addWidget(self.frame_pg_GRUPO_top_right)

        self.verticalLayout_3.addWidget(self.frame_pg_GRUPO_top)

        self.frame_pg_GRUPO_center = QFrame(self.pg_GRUPO)
        self.frame_pg_GRUPO_center.setObjectName(u"frame_pg_GRUPO_center")
        self.frame_pg_GRUPO_center.setStyleSheet(u"QFrame{\n"
                                                 "	background-color: rgb(210, 210, 210);\n"
                                                 "	margin: 60px;\n"
                                                 "	border-radius: 12px;\n"
                                                 "}\n"
                                                 "")
        self.frame_pg_GRUPO_center.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_GRUPO_center.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pg_GRUPO_center)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_GRUPO_main = QFrame(self.frame_pg_GRUPO_center)
        self.frame_GRUPO_main.setObjectName(u"frame_GRUPO_main")
        self.frame_GRUPO_main.setStyleSheet(u"background-color: rgb(85, 0, 255);\n"
                                            "margin: 0;\n"
                                            "background-color: rgb(0, 85, 127);")
        self.frame_GRUPO_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_GRUPO_main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_GRUPO_main)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_pg_GRUPO_CAMPOS = QFrame(self.frame_GRUPO_main)
        self.frame_pg_GRUPO_CAMPOS.setObjectName(u"frame_pg_GRUPO_CAMPOS")
        self.frame_pg_GRUPO_CAMPOS.setMaximumSize(QSize(16777215, 16777215))
        self.frame_pg_GRUPO_CAMPOS.setStyleSheet(u"\n"
                                                 "margin: 0;\n"
                                                 "color: black;")
        self.frame_pg_GRUPO_CAMPOS.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_GRUPO_CAMPOS.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_pg_GRUPO_CAMPOS)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.GRUPO_label_descricao = QLabel(self.frame_pg_GRUPO_CAMPOS)
        self.GRUPO_label_descricao.setObjectName(u"GRUPO_label_descricao")

        self.verticalLayout_7.addWidget(self.GRUPO_label_descricao)

        self.GRUPO_LineEdit_descricao = QLineEdit(self.frame_pg_GRUPO_CAMPOS)
        self.GRUPO_LineEdit_descricao.setObjectName(
            u"GRUPO_LineEdit_descricao")
        self.GRUPO_LineEdit_descricao.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                    "padding: 10px;\n"
                                                    "margin-bottom: 20px;\n"
                                                    "font-size: 12pt;\n"
                                                    "border: none;\n"
                                                    "border-radius: 10px;")

        self.verticalLayout_7.addWidget(self.GRUPO_LineEdit_descricao)

        self.GRUPO_label_observacao = QLabel(self.frame_pg_GRUPO_CAMPOS)
        self.GRUPO_label_observacao.setObjectName(u"GRUPO_label_observacao")

        self.verticalLayout_7.addWidget(self.GRUPO_label_observacao)

        self.GRUPO_TextEdit_observacao = QTextEdit(self.frame_pg_GRUPO_CAMPOS)
        self.GRUPO_TextEdit_observacao.setObjectName(
            u"GRUPO_TextEdit_observacao")
        self.GRUPO_TextEdit_observacao.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                     "padding: 10px;\n"
                                                     "font-size: 12pt;")

        self.verticalLayout_7.addWidget(self.GRUPO_TextEdit_observacao)

        self.horizontalLayout_6.addWidget(self.frame_pg_GRUPO_CAMPOS)

        self.scrollArea_list_grupo = QScrollArea(self.frame_GRUPO_main)
        self.scrollArea_list_grupo.setObjectName(u"scrollArea_list_grupo")
        self.scrollArea_list_grupo.setMinimumSize(QSize(0, 0))
        self.scrollArea_list_grupo.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_list_grupo.setStyleSheet(u"\n"
                                                 "	background-color: rgb(210, 210, 210);\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.scrollArea_list_grupo.setWidgetResizable(True)
        self.scrollAreaWidget_GRUPO = QWidget()
        self.scrollAreaWidget_GRUPO.setObjectName(u"scrollAreaWidget_GRUPO")
        self.scrollAreaWidget_GRUPO.setGeometry(QRect(0, 0, 152, 48))
        self.scrollAreaWidget_GRUPO.setStyleSheet(
            u"background-color: rgb(0, 85, 127);")
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidget_GRUPO)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_lista = QFrame(self.scrollAreaWidget_GRUPO)
        self.frame_lista.setObjectName(u"frame_lista")
        self.frame_lista.setMinimumSize(QSize(0, 30))
        self.frame_lista.setMaximumSize(QSize(16777215, 30))
        self.frame_lista.setStyleSheet(u"background-color: rgb(85, 0, 127);")
        self.frame_lista.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lista.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_lista.setLineWidth(1)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_lista)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.label_name_grupo = QLabel(self.frame_lista)
        self.label_name_grupo.setObjectName(u"label_name_grupo")
        self.label_name_grupo.setMinimumSize(QSize(0, 0))
        self.label_name_grupo.setStyleSheet(u"margin-left: 10px;")

        self.horizontalLayout_9.addWidget(
            self.label_name_grupo, 0, Qt.AlignmentFlag.AlignLeft)

        self.toolButton_editar_grupo = QToolButton(self.frame_lista)
        self.toolButton_editar_grupo.setObjectName(u"toolButton_editar_grupo")
        self.toolButton_editar_grupo.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_editar_grupo.setStyleSheet(u"QToolButton{\n"
                                                   "	padding-right: 15px;\n"
                                                   "	margin-right: 2px;\n"
                                                   "}\n"
                                                   "")
        self.toolButton_editar_grupo.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.toolButton_editar_grupo)

        self.toolButton_excluir_grupo = QToolButton(self.frame_lista)
        self.toolButton_excluir_grupo.setObjectName(
            u"toolButton_excluir_grupo")
        self.toolButton_excluir_grupo.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_excluir_grupo.setStyleSheet(u"\n"
                                                    "QToolButton{\n"
                                                    "	padding-right: 15px;\n"
                                                    "	margin-right: 5px;\n"
                                                    "	background-color: rgb(107, 0, 0);\n"
                                                    "\n"
                                                    "\n"
                                                    "}\n"
                                                    "\n"
                                                    "QToolButton::hover{\n"
                                                    "	background-color: rgb(200, 0, 0);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QToolButton::pressed{\n"
                                                    "	background-color: rgb(100, 0, 0);\n"
                                                    "\n"
                                                    "}")
        icon3 = QIcon(QIcon.fromTheme(u"user-trash"))
        self.toolButton_excluir_grupo.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.toolButton_excluir_grupo)

        self.verticalLayout_8.addWidget(self.frame_lista)

        self.scrollArea_list_grupo.setWidget(self.scrollAreaWidget_GRUPO)

        self.horizontalLayout_6.addWidget(
            self.scrollArea_list_grupo, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_pg_GRUPO_DICA = QFrame(self.frame_GRUPO_main)
        self.frame_pg_GRUPO_DICA.setObjectName(u"frame_pg_GRUPO_DICA")
        self.frame_pg_GRUPO_DICA.setMaximumSize(QSize(300, 16777215))
        self.frame_pg_GRUPO_DICA.setStyleSheet(u"background-color: #ADAAAA;\n"
                                               "margin: 0;\n"
                                               "color: #000;")
        self.frame_pg_GRUPO_DICA.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_GRUPO_DICA.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_pg_GRUPO_DICA)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_grupos_dica = QLabel(self.frame_pg_GRUPO_DICA)
        self.label_grupos_dica.setObjectName(u"label_grupos_dica")

        self.verticalLayout_6.addWidget(
            self.label_grupos_dica, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.label_grupos_text = QTextBrowser(self.frame_pg_GRUPO_DICA)
        self.label_grupos_text.setObjectName(u"label_grupos_text")
        self.label_grupos_text.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.label_grupos_text.setReadOnly(True)

        self.verticalLayout_6.addWidget(
            self.label_grupos_text, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_6.addWidget(self.frame_pg_GRUPO_DICA)

        self.verticalLayout_5.addWidget(self.frame_GRUPO_main)

        self.frame_GRUPO_SALVAR = QFrame(self.frame_pg_GRUPO_center)
        self.frame_GRUPO_SALVAR.setObjectName(u"frame_GRUPO_SALVAR")
        self.frame_GRUPO_SALVAR.setMaximumSize(QSize(16777215, 80))
        self.frame_GRUPO_SALVAR.setStyleSheet(u"margin: 0;")
        self.frame_GRUPO_SALVAR.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_GRUPO_SALVAR.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_GRUPO_SALVAR)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pg_prova_btn_SALVAR = QPushButton(self.frame_GRUPO_SALVAR)
        self.pg_prova_btn_SALVAR.setObjectName(u"pg_prova_btn_SALVAR")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush4 = QBrush(QColor(84, 27, 156, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
# endif
        self.pg_prova_btn_SALVAR.setPalette(palette2)
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(False)
        self.pg_prova_btn_SALVAR.setFont(font2)
        self.pg_prova_btn_SALVAR.setCursor(QCursor(Qt.PointingHandCursor))
        self.pg_prova_btn_SALVAR.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight)
        self.pg_prova_btn_SALVAR.setStyleSheet(u"QPushButton{\n"
                                               "  	width: 100%;\n"
                                               "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                               "    text-align: center;\n"
                                               "    padding: 10px;\n"
                                               "    color: white;\n"
                                               "    border-radius: 10px;\n"
                                               "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                               "	color: white;\n"
                                               "	border-radius: 10px;\n"
                                               "	background: #541B9C;\n"
                                               "	font-size: 18pt;\n"
                                               "	border-radius: 12px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton::hover{\n"
                                               "	background-color: rgb(108, 35, 204);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton::pressed{\n"
                                               "	background-color: rgb(50, 16, 95);\n"
                                               "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #541B9C, stop: 1 #0d5ca6);\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "")
        self.pg_prova_btn_SALVAR.setText(u"Salvar")
        self.pg_prova_btn_SALVAR.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(
            self.pg_prova_btn_SALVAR, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_5.addWidget(self.frame_GRUPO_SALVAR)

        self.verticalLayout_3.addWidget(self.frame_pg_GRUPO_center)

        self.abas.addWidget(self.pg_GRUPO)
        self.pg_turma = QWidget()
        self.pg_turma.setObjectName(u"pg_turma")
        self.pg_turma.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.pg_turma)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_pg_TURMA_top = QFrame(self.pg_turma)
        self.frame_pg_TURMA_top.setObjectName(u"frame_pg_TURMA_top")
        self.frame_pg_TURMA_top.setMinimumSize(QSize(0, 80))
        self.frame_pg_TURMA_top.setMaximumSize(QSize(16777215, 80))
        self.frame_pg_TURMA_top.setStyleSheet(u"QFrame{\n"
                                              "	border: none;\n"
                                              "}")
        self.frame_pg_TURMA_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_TURMA_top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_pg_TURMA_top)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_pg_TURMA_top_LEFT = QFrame(self.frame_pg_TURMA_top)
        self.frame_pg_TURMA_top_LEFT.setObjectName(u"frame_pg_TURMA_top_LEFT")
        self.frame_pg_TURMA_top_LEFT.setStyleSheet(u"")
        self.frame_pg_TURMA_top_LEFT.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_TURMA_top_LEFT.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_10.addWidget(self.frame_pg_TURMA_top_LEFT)

        self.frame_pg_TURMA_top_CENTER = QFrame(self.frame_pg_TURMA_top)
        self.frame_pg_TURMA_top_CENTER.setObjectName(
            u"frame_pg_TURMA_top_CENTER")
        self.frame_pg_TURMA_top_CENTER.setStyleSheet(u"")
        self.frame_pg_TURMA_top_CENTER.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_TURMA_top_CENTER.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_pg_TURMA_top_CENTER)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.header_titulo_turma = QLabel(self.frame_pg_TURMA_top_CENTER)
        self.header_titulo_turma.setObjectName(u"header_titulo_turma")
        self.header_titulo_turma.setStyleSheet(u"color: #000;")

        self.horizontalLayout_11.addWidget(
            self.header_titulo_turma, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_10.addWidget(self.frame_pg_TURMA_top_CENTER)

        self.frame_pg_TURMA_top_HIGHT = QFrame(self.frame_pg_TURMA_top)
        self.frame_pg_TURMA_top_HIGHT.setObjectName(
            u"frame_pg_TURMA_top_HIGHT")
        self.frame_pg_TURMA_top_HIGHT.setStyleSheet(u"")
        self.frame_pg_TURMA_top_HIGHT.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_TURMA_top_HIGHT.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_pg_TURMA_top_HIGHT)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pg_TURMA_btn_cancelar = QPushButton(self.frame_pg_TURMA_top_HIGHT)
        self.pg_TURMA_btn_cancelar.setObjectName(u"pg_TURMA_btn_cancelar")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush3)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush3)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush3)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
# endif
        self.pg_TURMA_btn_cancelar.setPalette(palette3)
        self.pg_TURMA_btn_cancelar.setFont(font1)
        self.pg_TURMA_btn_cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pg_TURMA_btn_cancelar.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight)
        self.pg_TURMA_btn_cancelar.setStyleSheet(u"QPushButton{\n"
                                                 "\n"
                                                 "	background-color: rgb(85, 0, 0);\n"
                                                 "  	width: 100%;\n"
                                                 "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                                 "    text-align: center;\n"
                                                 "    padding: 10px;\n"
                                                 "    color: white;\n"
                                                 "    border-radius: 10px;\n"
                                                 "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                                 "	color: white;\n"
                                                 "	border-radius: 10px;\n"
                                                 "	\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton::hover{\n"
                                                 "	background-color: rgb(116, 0, 0);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton::pressed{\n"
                                                 "	background-color: rgb(57, 0, 0);\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.pg_TURMA_btn_cancelar.setText(u"Cancelar")
        self.pg_TURMA_btn_cancelar.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(
            self.pg_TURMA_btn_cancelar, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_10.addWidget(self.frame_pg_TURMA_top_HIGHT)

        self.verticalLayout_9.addWidget(self.frame_pg_TURMA_top)

        self.frame_pg_TURMA_center = QFrame(self.pg_turma)
        self.frame_pg_TURMA_center.setObjectName(u"frame_pg_TURMA_center")
        self.frame_pg_TURMA_center.setStyleSheet(u"QFrame{\n"
                                                 "	background-color: rgb(210, 210, 210);\n"
                                                 "	margin: 60px;\n"
                                                 "	border-radius: 12px;\n"
                                                 "}\n"
                                                 "")
        self.frame_pg_TURMA_center.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_TURMA_center.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_pg_TURMA_center)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_pg_TURMA_main = QFrame(self.frame_pg_TURMA_center)
        self.frame_pg_TURMA_main.setObjectName(u"frame_pg_TURMA_main")
        self.frame_pg_TURMA_main.setStyleSheet(u"QFrame{\n"
                                               "	background-color: rgb(204, 204, 204);\n"
                                               "	margin: 0px;\n"
                                               "	border-radius: 12px;\n"
                                               "}\n"
                                               "")
        self.frame_pg_TURMA_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_TURMA_main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_pg_TURMA_main)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_pg_TURMA_CAMPOS = QFrame(self.frame_pg_TURMA_main)
        self.frame_pg_TURMA_CAMPOS.setObjectName(u"frame_pg_TURMA_CAMPOS")
        self.frame_pg_TURMA_CAMPOS.setMaximumSize(QSize(16777215, 16777215))
        self.frame_pg_TURMA_CAMPOS.setStyleSheet(u"\n"
                                                 "margin: 0;\n"
                                                 "color: black;")
        self.frame_pg_TURMA_CAMPOS.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_TURMA_CAMPOS.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_pg_TURMA_CAMPOS)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.TURMA_label_descricao = QLabel(self.frame_pg_TURMA_CAMPOS)
        self.TURMA_label_descricao.setObjectName(u"TURMA_label_descricao")

        self.verticalLayout_13.addWidget(self.TURMA_label_descricao)

        self.turma_LineEdit_descricao = QLineEdit(self.frame_pg_TURMA_CAMPOS)
        self.turma_LineEdit_descricao.setObjectName(
            u"turma_LineEdit_descricao")
        self.turma_LineEdit_descricao.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                    "padding: 10px;\n"
                                                    "margin-bottom: 20px;\n"
                                                    "font-size: 12pt;\n"
                                                    "border: none;\n"
                                                    "border-radius: 10px;")

        self.verticalLayout_13.addWidget(self.turma_LineEdit_descricao)

        self.TURMA_label_observacao = QLabel(self.frame_pg_TURMA_CAMPOS)
        self.TURMA_label_observacao.setObjectName(u"TURMA_label_observacao")

        self.verticalLayout_13.addWidget(self.TURMA_label_observacao)

        self.TURMA_TextEdit_observacao = QTextEdit(self.frame_pg_TURMA_CAMPOS)
        self.TURMA_TextEdit_observacao.setObjectName(
            u"TURMA_TextEdit_observacao")
        self.TURMA_TextEdit_observacao.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                     "padding: 10px;\n"
                                                     "font-size: 12pt;")

        self.verticalLayout_13.addWidget(self.TURMA_TextEdit_observacao)

        self.horizontalLayout_15.addWidget(self.frame_pg_TURMA_CAMPOS)

        self.scrollArea_list_grupo_2 = QScrollArea(self.frame_pg_TURMA_main)
        self.scrollArea_list_grupo_2.setObjectName(u"scrollArea_list_grupo_2")
        self.scrollArea_list_grupo_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_list_grupo_2.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_list_grupo_2.setStyleSheet(u" background-color:  rgb(204, 204, 204);\n"
                                                   "\n"
                                                   "\n"
                                                   "")
        self.scrollArea_list_grupo_2.setWidgetResizable(True)
        self.scrollAreaWidget_TURMA = QWidget()
        self.scrollAreaWidget_TURMA.setObjectName(u"scrollAreaWidget_TURMA")
        self.scrollAreaWidget_TURMA.setGeometry(QRect(0, 0, 200, 69))
        self.scrollAreaWidget_TURMA.setStyleSheet(u"background-color: rgb(204, 204, 204);\n")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidget_TURMA)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_lista_TURMA = QFrame(self.scrollAreaWidget_TURMA)
        self.frame_lista_TURMA.setObjectName(u"frame_lista_TURMA")
        self.frame_lista_TURMA.setMinimumSize(QSize(0, 30))
        self.frame_lista_TURMA.setMaximumSize(QSize(16777215, 30))
        self.frame_lista_TURMA.setStyleSheet(
            u"background-color: rgb(85, 0, 127);")
        self.frame_lista_TURMA.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lista_TURMA.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_lista_TURMA.setLineWidth(1)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_lista_TURMA)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0,0,0,0)
        self.label_name_turma = QLabel(self.frame_lista_TURMA)
        self.label_name_turma.setObjectName(u"label_name_turma")
        self.label_name_turma.setMinimumSize(QSize(0, 0))
        self.label_name_turma.setStyleSheet(u"margin-left: 10px;")

        self.horizontalLayout_14.addWidget(
            self.label_name_turma, 0, Qt.AlignmentFlag.AlignLeft)

        self.toolButton_editar_turma = QToolButton(self.frame_lista_TURMA)
        self.toolButton_editar_turma.setObjectName(u"toolButton_editar_turma")
        self.toolButton_editar_turma.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_editar_turma.setStyleSheet(u"QToolButton{\n"
                                                   "	padding-right: 15px;\n"
                                                   "	margin-right: 2px;\n"
                                                   "}\n"
                                                   "")
        self.toolButton_editar_turma.setIcon(icon2)

        self.horizontalLayout_14.addWidget(self.toolButton_editar_turma)

        self.toolButton_excluir_turma = QToolButton(self.frame_lista_TURMA)
        self.toolButton_excluir_turma.setObjectName(
            u"toolButton_excluir_turma")
        self.toolButton_excluir_turma.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_excluir_turma.setStyleSheet(u"\n"
                                                    "QToolButton{\n"
                                                    "	padding-right: 15px;\n"
                                                    "	margin-right: 5px;\n"
                                                    "	background-color: rgb(107, 0, 0);\n"
                                                    "\n"
                                                    "\n"
                                                    "}\n"
                                                    "\n"
                                                    "QToolButton::hover{\n"
                                                    "	background-color: rgb(200, 0, 0);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QToolButton::pressed{\n"
                                                    "	background-color: rgb(100, 0, 0);\n"
                                                    "\n"
                                                    "}")
        self.toolButton_excluir_turma.setIcon(icon3)

        self.horizontalLayout_14.addWidget(self.toolButton_excluir_turma)

        self.verticalLayout_11.addWidget(self.frame_lista_TURMA)

        self.scrollArea_list_grupo_2.setWidget(self.scrollAreaWidget_TURMA)

        self.horizontalLayout_15.addWidget(
            self.scrollArea_list_grupo_2, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_pg_GRUPO_DICA_2 = QFrame(self.frame_pg_TURMA_main)
        self.frame_pg_GRUPO_DICA_2.setObjectName(u"frame_pg_GRUPO_DICA_2")
        self.frame_pg_GRUPO_DICA_2.setMaximumSize(QSize(300, 16777215))
        self.frame_pg_GRUPO_DICA_2.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                 "margin: 0;\n"
                                                 "color: #000;")
        self.frame_pg_GRUPO_DICA_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_GRUPO_DICA_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_pg_GRUPO_DICA_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_grupos_dica_2 = QLabel(self.frame_pg_GRUPO_DICA_2)
        self.label_grupos_dica_2.setObjectName(u"label_grupos_dica_2")

        self.verticalLayout_12.addWidget(
            self.label_grupos_dica_2, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.label_grupos_text_2 = QTextBrowser(self.frame_pg_GRUPO_DICA_2)
        self.label_grupos_text_2.setObjectName(u"label_grupos_text_2")
        self.label_grupos_text_2.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.label_grupos_text_2.setReadOnly(True)

        self.verticalLayout_12.addWidget(
            self.label_grupos_text_2, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_15.addWidget(self.frame_pg_GRUPO_DICA_2)

        self.verticalLayout_10.addWidget(self.frame_pg_TURMA_main)

        self.frame_pg_TURMA_SALVAR = QFrame(self.frame_pg_TURMA_center)
        self.frame_pg_TURMA_SALVAR.setObjectName(u"frame_pg_TURMA_SALVAR")
        self.frame_pg_TURMA_SALVAR.setMaximumSize(QSize(16777215, 80))
        self.frame_pg_TURMA_SALVAR.setStyleSheet(u"QFrame{\n"
                                                 "\n"
                                                 "	margin: 0px;\n"
                                                 "	border-radius: 12px;\n"
                                                 "}\n"
                                                 "")
        self.frame_pg_TURMA_SALVAR.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pg_TURMA_SALVAR.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_pg_TURMA_SALVAR)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pg_TURMA_btn_SALVAR = QPushButton(self.frame_pg_TURMA_SALVAR)
        self.pg_TURMA_btn_SALVAR.setObjectName(u"pg_TURMA_btn_SALVAR")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
# endif
        self.pg_TURMA_btn_SALVAR.setPalette(palette4)
        self.pg_TURMA_btn_SALVAR.setFont(font2)
        self.pg_TURMA_btn_SALVAR.setCursor(QCursor(Qt.PointingHandCursor))
        self.pg_TURMA_btn_SALVAR.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight)
        self.pg_TURMA_btn_SALVAR.setStyleSheet(u"QPushButton{\n"
                                               "  	width: 100%;\n"
                                               "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                               "    text-align: center;\n"
                                               "    padding: 10px;\n"
                                               "    color: white;\n"
                                               "    border-radius: 10px;\n"
                                               "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                               "	color: white;\n"
                                               "	border-radius: 10px;\n"
                                               "	background: #541B9C;\n"
                                               "	font-size: 18pt;\n"
                                               "	border-radius: 12px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton::hover{\n"
                                               "	background-color: rgb(108, 35, 204);\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton::pressed{\n"
                                               "	background-color: rgb(50, 16, 95);\n"
                                               "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #541B9C, stop: 1 #0d5ca6);\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "")
        self.pg_TURMA_btn_SALVAR.setText(u"Salvar")
        self.pg_TURMA_btn_SALVAR.setIconSize(QSize(20, 20))

        self.horizontalLayout_13.addWidget(
            self.pg_TURMA_btn_SALVAR, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_10.addWidget(self.frame_pg_TURMA_SALVAR)

        self.verticalLayout_9.addWidget(self.frame_pg_TURMA_center)

        self.abas.addWidget(self.pg_turma)
        self.pg_criar_provas = QWidget()
        self.pg_criar_provas.setObjectName(u"pg_criar_provas")
        self.verticalLayout_20 = QVBoxLayout(self.pg_criar_provas)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.FCP_Top = QFrame(self.pg_criar_provas)
        self.FCP_Top.setObjectName(u"FCP_Top")
        self.FCP_Top.setMinimumSize(QSize(0, 0))
        self.FCP_Top.setMaximumSize(QSize(16777215, 65))
        self.FCP_Top.setStyleSheet(u"border: none;")
        self.FCP_Top.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_Top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.FCP_Top)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.FCP_btn_gerar_pdf_dc_top_right = QPushButton(self.FCP_Top)
        self.FCP_btn_gerar_pdf_dc_top_right.setObjectName(
            u"FCP_btn_gerar_pdf_dc_top_right")
        font3 = QFont()
        font3.setPointSize(11)
        self.FCP_btn_gerar_pdf_dc_top_right.setFont(font3)
        self.FCP_btn_gerar_pdf_dc_top_right.setStyleSheet(u"QPushButton{\n"
                                                          "  width: 100%;\n"
                                                          "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                                          "    text-align: center;\n"
                                                          "    padding: 10px;\n"
                                                          "    color: white;\n"
                                                          "    border-radius: 10px;\n"
                                                          "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                                          "	color: white;\n"
                                                          "	border-radius: 10px;\n"
                                                          "	background-color: #9C1B59;\n"
                                                          "	\n"
                                                          "}\n"
                                                          "\n"
                                                          "QPushButton::hover{\n"
                                                          "	\n"
                                                          "	\n"
                                                          "	background-color: rgb(180, 31, 103);\n"
                                                          "}\n"
                                                          "\n"
                                                          "QPushButton::pressed{\n"
                                                          "	\n"
                                                          "\n"
                                                          "	background-color: rgb(117, 20, 67);\n"
                                                          "}\n"
                                                          "\n"
                                                          "\n"
                                                          "\n"
                                                          "\n"
                                                          "\n"
                                                          "\n"
                                                          "")

        self.horizontalLayout_26.addWidget(
            self.FCP_btn_gerar_pdf_dc_top_right, 0, Qt.AlignmentFlag.AlignRight)

        self.FCP_btn_cancelar_dc_top_right = QPushButton(self.FCP_Top)
        self.FCP_btn_cancelar_dc_top_right.setObjectName(
            u"FCP_btn_cancelar_dc_top_right")
        self.FCP_btn_cancelar_dc_top_right.setFont(font3)
        self.FCP_btn_cancelar_dc_top_right.setStyleSheet(u"QPushButton {\n"
                                                         "    width: 100%;\n"
                                                         "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                                         "    text-align: center;\n"
                                                         "    padding: 10px;\n"
                                                         "    background-color: rgb(85, 0, 0);\n"
                                                         "    color: white;\n"
                                                         "    border-radius: 10px;\n"
                                                         "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                                         "}\n"
                                                         "\n"
                                                         "QPushButton::hover{\n"
                                                         "	\n"
                                                         "	background-color: rgb(129, 0, 0);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QPushButton::pressed{\n"
                                                         "	\n"
                                                         "	background-color: rgb(65, 0, 0);\n"
                                                         "}\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "")

        self.horizontalLayout_26.addWidget(
            self.FCP_btn_cancelar_dc_top_right, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout_20.addWidget(
            self.FCP_Top, 0, Qt.AlignmentFlag.AlignRight)

        self.FCP_ct = QFrame(self.pg_criar_provas)
        self.FCP_ct.setObjectName(u"FCP_ct")
        self.FCP_ct.setStyleSheet(u"border: none;")
        self.FCP_ct.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_ct.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.FCP_ct)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.FCP_save_level = QFrame(self.FCP_ct)
        self.FCP_save_level.setObjectName(u"FCP_save_level")
        self.FCP_save_level.setMinimumSize(QSize(0, 50))
        self.FCP_save_level.setStyleSheet(u"background-color: #ccc;\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "border-radius: 10px;")
        self.FCP_save_level.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_save_level.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.FCP_save_level)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.FCP_checkBox_save_question = QCheckBox(self.FCP_save_level)
        self.FCP_checkBox_save_question.setObjectName(
            u"FCP_checkBox_save_question")
        self.FCP_checkBox_save_question.setStyleSheet(u"font: 12pt;")
        self.FCP_checkBox_save_question.setChecked(True)

        self.horizontalLayout_39.addWidget(self.FCP_checkBox_save_question)

        self.FCP_label_level_question = QLabel(self.FCP_save_level)
        self.FCP_label_level_question.setObjectName(
            u"FCP_label_level_question")
        self.FCP_label_level_question.setStyleSheet(u"font: 12pt;\n"
                                                    "color: rgb(0, 0, 0);")

        self.horizontalLayout_39.addWidget(self.FCP_label_level_question)

        self.FCP_comboBox_level_question = QComboBox(self.FCP_save_level)
        self.FCP_comboBox_level_question.addItem("")
        self.FCP_comboBox_level_question.addItem("")
        self.FCP_comboBox_level_question.addItem("")
        self.FCP_comboBox_level_question.setObjectName(
            u"FCP_comboBox_level_question")
        self.FCP_comboBox_level_question.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_39.addWidget(self.FCP_comboBox_level_question)

        self.label_qtd_pergunta = QLabel(self.FCP_save_level)
        self.label_qtd_pergunta.setObjectName(u"label_qtd_pergunta")
        self.label_qtd_pergunta.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_39.addWidget(
            self.label_qtd_pergunta, 0, Qt.AlignmentFlag.AlignRight)

        self.verticalLayout_21.addWidget(self.FCP_save_level)

        self.FCP_ct_center_top = QFrame(self.FCP_ct)
        self.FCP_ct_center_top.setObjectName(u"FCP_ct_center_top")
        self.FCP_ct_center_top.setMinimumSize(QSize(0, 0))
        self.FCP_ct_center_top.setMaximumSize(QSize(16777215, 150))
        self.FCP_ct_center_top.setStyleSheet(u"background-color: rgb(56, 0, 84);\n"
                                             "background-color: #ccc;\n"
                                             "color: #fff;\n"
                                             "color: #000;\n"
                                             "font: 10.5pt;\n"
                                             "border-radius: 12px;\n"
                                             "border: none;")
        self.FCP_ct_center_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_ct_center_top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.FCP_ct_center_top)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.FCP_center_top_left_modelo = QFrame(self.FCP_ct_center_top)
        self.FCP_center_top_left_modelo.setObjectName(
            u"FCP_center_top_left_modelo")
        self.FCP_center_top_left_modelo.setMinimumSize(QSize(200, 0))
        self.FCP_center_top_left_modelo.setMaximumSize(QSize(300, 16777215))
        self.FCP_center_top_left_modelo.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_center_top_left_modelo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.FCP_center_top_left_modelo)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_tipo_pergunta = QLabel(self.FCP_center_top_left_modelo)
        self.label_tipo_pergunta.setObjectName(u"label_tipo_pergunta")
        self.label_tipo_pergunta.setStyleSheet(u"font: 12pt;")

        self.verticalLayout_22.addWidget(
            self.label_tipo_pergunta, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.FCP_radioButton_dissertativa = QRadioButton(
            self.FCP_center_top_left_modelo)
        self.FCP_radioButton_dissertativa.setObjectName(
            u"FCP_radioButton_dissertativa")
        self.FCP_radioButton_dissertativa.setStyleSheet(u"")

        self.FCP_radioButton_dissertativa.setChecked(True)

        self.verticalLayout_22.addWidget(self.FCP_radioButton_dissertativa)

        self.FCP_radioButton_objetiva = QRadioButton(
            self.FCP_center_top_left_modelo)
        self.FCP_radioButton_objetiva.setObjectName(
            u"FCP_radioButton_objetiva")

        self.verticalLayout_22.addWidget(self.FCP_radioButton_objetiva)

        self.FCP_radioButton_true_or_false = QRadioButton(
            self.FCP_center_top_left_modelo)
        self.FCP_radioButton_true_or_false.setObjectName(
            u"FCP_radioButton_true_or_false")

        self.verticalLayout_22.addWidget(self.FCP_radioButton_true_or_false)

        self.horizontalLayout_37.addWidget(
            self.FCP_center_top_left_modelo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.FCP_center_top_hight_cabecalho = QFrame(self.FCP_ct_center_top)
        self.FCP_center_top_hight_cabecalho.setObjectName(
            u"FCP_center_top_hight_cabecalho")
        self.FCP_center_top_hight_cabecalho.setFrameShape(
            QFrame.Shape.StyledPanel)
        self.FCP_center_top_hight_cabecalho.setFrameShadow(
            QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(
            self.FCP_center_top_hight_cabecalho)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.FCP_label_cabecalho = QLabel(self.FCP_center_top_hight_cabecalho)
        self.FCP_label_cabecalho.setObjectName(u"FCP_label_cabecalho")
        self.FCP_label_cabecalho.setStyleSheet(u"font: 12pt;")



        self.verticalLayout_23.addWidget(
            self.FCP_label_cabecalho, 0, Qt.AlignmentFlag.AlignHCenter)

        

        self.FCP_QTextEdit_cabecalho = QTextEdit(
            self.FCP_center_top_hight_cabecalho)
        self.FCP_QTextEdit_cabecalho.setObjectName(u"FCP_QTextEdit_cabecalho")
        self.FCP_QTextEdit_cabecalho.setStyleSheet(
            u"background-color: rgb(177, 177, 177);")
        


        # self.FCP_QTextEdit_cabecalho_2 = QTextEdit(
        #     self.FCP_center_top_hight_cabecalho)
        # self.FCP_QTextEdit_cabecalho_2.setObjectName(
        #     u"FCP_QTextEdit_cabecalho")
        # self.FCP_QTextEdit_cabecalho_2.setStyleSheet(
        #     u"background-color: rgb(177, 177, 177);\n"
        #     "margin-top: 5px")
        
        # self.FCP_QTextEdit_cabecalho_2.setPlaceholderText('Digite aqui o titulo da prova')

        self.verticalLayout_23.addWidget(self.FCP_QTextEdit_cabecalho)
        # self.verticalLayout_23.addWidget(self.FCP_QTextEdit_cabecalho_2)

        self.horizontalLayout_37.addWidget(self.FCP_center_top_hight_cabecalho)

        self.verticalLayout_21.addWidget(self.FCP_ct_center_top)

        self.FCP_ct_2 = QFrame(self.FCP_ct)
        self.FCP_ct_2.setObjectName(u"FCP_ct_2")
        self.FCP_ct_2.setMinimumSize(QSize(0, 200))
        self.FCP_ct_2.setStyleSheet(u"border: none;")
        self.FCP_ct_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_ct_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.FCP_ct_2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.stackedWidget_FCP = QStackedWidget(self.FCP_ct_2)
        self.stackedWidget_FCP.setObjectName(u"stackedWidget_FCP")
        self.stackedWidget_FCP.setStyleSheet(u"")
        self.FCP_question_dissertativa = QWidget()
        self.FCP_question_dissertativa.setObjectName(
            u"FCP_question_dissertativa")
        self.FCP_question_dissertativa.setMinimumSize(QSize(800, 0))
        self.FCP_question_dissertativa.setMaximumSize(QSize(1000, 16777215))
        self.FCP_question_dissertativa.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.FCP_question_dissertativa)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.FCP_dissertativa_conteudo = QFrame(self.FCP_question_dissertativa)
        self.FCP_dissertativa_conteudo.setObjectName(
            u"FCP_dissertativa_conteudo")
        self.FCP_dissertativa_conteudo.setMaximumSize(QSize(16777215, 125))
        self.FCP_dissertativa_conteudo.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_dissertativa_conteudo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.FCP_dissertativa_conteudo)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.FCP_label_cabecalho_respost_correta = QLabel(
            self.FCP_dissertativa_conteudo)
        self.FCP_label_cabecalho_respost_correta.setObjectName(
            u"FCP_label_cabecalho_respost_correta")
        self.FCP_label_cabecalho_respost_correta.setStyleSheet(u"font: 12pt;\n"
                                                               "color: #000;")

        self.verticalLayout_26.addWidget(
            self.FCP_label_cabecalho_respost_correta)

        self.FCP_QTextEdit_respost_certa = QTextEdit(
            self.FCP_dissertativa_conteudo)
        self.FCP_QTextEdit_respost_certa.setObjectName(
            u"FCP_QTextEdit_respost_certa")
        self.FCP_QTextEdit_respost_certa.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
                                                       "background-color: rgb(177, 177, 177);\n"
                                                       "\n"
                                                       "border-radius: 10px;\n"
                                                       "color: #000;\n"
                                                       "font: 12pt ;")

        self.verticalLayout_26.addWidget(self.FCP_QTextEdit_respost_certa)

        self.verticalLayout_25.addWidget(self.FCP_dissertativa_conteudo)

        self.stackedWidget_FCP.addWidget(self.FCP_question_dissertativa)
        self.FCP_question_true_or_false = QWidget()
        self.FCP_question_true_or_false.setObjectName(
            u"FCP_question_true_or_false")
        self.FCP_question_true_or_false.setMinimumSize(QSize(800, 0))
        self.FCP_question_true_or_false.setMaximumSize(QSize(1000, 16777215))
        self.FCP_question_true_or_false.setStyleSheet(
            u"background-color: rgb(85, 85, 127);")
        self.horizontalLayout_53 = QHBoxLayout(self.FCP_question_true_or_false)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.FCP_ct_6 = QFrame(self.FCP_question_true_or_false)
        self.FCP_ct_6.setObjectName(u"FCP_ct_6")
        self.FCP_ct_6.setStyleSheet(u"background-color: rgb(177, 177, 177);\n"
                                    "color: rgb(0, 0, 0);")
        self.FCP_ct_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_ct_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.FCP_ct_6)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.FCP_objetiva_ct = QFrame(self.FCP_ct_6)
        self.FCP_objetiva_ct.setObjectName(u"FCP_objetiva_ct")
        self.FCP_objetiva_ct.setMinimumSize(QSize(50, 0))
        self.FCP_objetiva_ct.setMaximumSize(QSize(16777215, 50))
        self.FCP_objetiva_ct.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_objetiva_ct.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.FCP_objetiva_ct)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(10, 10, 10, 10)
        self.FCP_objetiva_ct_7 = QFrame(self.FCP_objetiva_ct)
        self.FCP_objetiva_ct_7.setObjectName(u"FCP_objetiva_ct_7")
        self.FCP_objetiva_ct_7.setMinimumSize(QSize(0, 50))
        self.FCP_objetiva_ct_7.setMaximumSize(QSize(16777215, 50))
        self.FCP_objetiva_ct_7.setStyleSheet(u"background-color: rgb(177, 177, 177);\n"
                                             "background-color: rgb(204, 204, 204);\n"
                                             "border-radius: 10px;")
        self.FCP_objetiva_ct_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_objetiva_ct_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.FCP_objetiva_ct_7)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.FCP_objetiva_label_tipo_pergunta_3 = QLabel(
            self.FCP_objetiva_ct_7)
        self.FCP_objetiva_label_tipo_pergunta_3.setObjectName(
            u"FCP_objetiva_label_tipo_pergunta_3")
        self.FCP_objetiva_label_tipo_pergunta_3.setStyleSheet(u"font: 12pt;\n"
                                                              "color: rgb(0, 0, 0);")

        self.horizontalLayout_54.addWidget(
            self.FCP_objetiva_label_tipo_pergunta_3)

        self.FCP_objetiva_spinBox_qtd_op_2 = QSpinBox(self.FCP_objetiva_ct_7)
        self.FCP_objetiva_spinBox_qtd_op_2.setObjectName(
            u"FCP_objetiva_spinBox_qtd_op_2")
        self.FCP_objetiva_spinBox_qtd_op_2.setStyleSheet(u"font: 12pt;\n"
                                                         "color: rgb(0, 0, 0);")

        self.horizontalLayout_54.addWidget(self.FCP_objetiva_spinBox_qtd_op_2)

        self.FCP_objetiva_btn_gerar_op_2 = QPushButton(self.FCP_objetiva_ct_7)
        self.FCP_objetiva_btn_gerar_op_2.setObjectName(
            u"FCP_objetiva_btn_gerar_op_2")
        self.FCP_objetiva_btn_gerar_op_2.setFont(font3)
        self.FCP_objetiva_btn_gerar_op_2.setStyleSheet(u"QPushButton{\n"
                                                       "  width: 100%;\n"
                                                       "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                                       "    text-align: center;\n"
                                                       "    frame_lista_TURMApx;\n"
                                                       "    color: white;\n"
                                                       "    border-radius: 10px;\n"
                                                       "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                                       "	color: white;\n"
                                                       "	background-color: rgb(0, 85, 0);\n"
                                                       "\n"
                                                       "\n"
                                                       "	\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton::hover{\n"
                                                       "	\n"
                                                       "	\n"
                                                       "	background-color: rgb(0, 121, 0);\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton::pressed{\n"
                                                       "	\n"
                                                       "\n"
                                                       "	background-color: rgb(0, 58, 0);\n"
                                                       "}\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "\n"
                                                       "")

        self.horizontalLayout_54.addWidget(self.FCP_objetiva_btn_gerar_op_2)

        self.horizontalLayout_55.addWidget(self.FCP_objetiva_ct_7)

        self.verticalLayout_32.addWidget(self.FCP_objetiva_ct)

        self.frame_2 = QFrame(self.FCP_ct_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_2)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.FCP_true_false_frame_op_A = QFrame(self.frame_2)
        self.FCP_true_false_frame_op_A.setObjectName(
            u"FCP_true_false_frame_op_A")
        self.FCP_true_false_frame_op_A.setMaximumSize(QSize(16777215, 50))
        self.FCP_true_false_frame_op_A.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_true_false_frame_op_A.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.FCP_true_false_frame_op_A)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(10, 10, 10, 10)
        self.FCP_true_false_checkBox_resposta_certa_A_V = QCheckBox(
            self.FCP_true_false_frame_op_A)
        self.FCP_true_false_checkBox_resposta_certa_A_V.setObjectName(
            u"FCP_true_false_checkBox_resposta_certa_A_V")
        self.FCP_true_false_checkBox_resposta_certa_A_V.setMinimumSize(
            QSize(50, 0))
        self.FCP_true_false_checkBox_resposta_certa_A_V.setMaximumSize(
            QSize(50, 16777215))

        self.horizontalLayout_56.addWidget(
            self.FCP_true_false_checkBox_resposta_certa_A_V)

        self.FCP_true_false_checkBox_resposta_certa_A_F = QCheckBox(
            self.FCP_true_false_frame_op_A)
        self.FCP_true_false_checkBox_resposta_certa_A_F.setObjectName(
            u"FCP_true_false_checkBox_resposta_certa_A_F")
        self.FCP_true_false_checkBox_resposta_certa_A_F.setMinimumSize(
            QSize(50, 0))
        self.FCP_true_false_checkBox_resposta_certa_A_F.setMaximumSize(
            QSize(50, 16777215))

        self.horizontalLayout_56.addWidget(
            self.FCP_true_false_checkBox_resposta_certa_A_F)

        self.FCP_true_false_parentese_A = QLabel(
            self.FCP_true_false_frame_op_A)
        self.FCP_true_false_parentese_A.setObjectName(
            u"FCP_true_false_parentese_A")
        self.FCP_true_false_parentese_A.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_56.addWidget(self.FCP_true_false_parentese_A)

        self.FCP_true_false_op_A = QLabel(self.FCP_true_false_frame_op_A)
        self.FCP_true_false_op_A.setObjectName(u"FCP_true_false_op_A")
        self.FCP_true_false_op_A.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_56.addWidget(self.FCP_true_false_op_A)

        self.FCP_true_false_lineEdit_text_op_A = QLineEdit(
            self.FCP_true_false_frame_op_A)
        self.FCP_true_false_lineEdit_text_op_A.setObjectName(
            u"FCP_true_false_lineEdit_text_op_A")
        self.FCP_true_false_lineEdit_text_op_A.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_56.addWidget(
            self.FCP_true_false_lineEdit_text_op_A)

        self.verticalLayout_33.addWidget(self.FCP_true_false_frame_op_A)

        self.FCP_true_false_frame_op_B = QFrame(self.frame_2)
        self.FCP_true_false_frame_op_B.setObjectName(
            u"FCP_true_false_frame_op_B")
        self.FCP_true_false_frame_op_B.setMaximumSize(QSize(16777215, 50))
        self.FCP_true_false_frame_op_B.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_true_false_frame_op_B.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.FCP_true_false_frame_op_B)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(10, 10, 10, 10)
        self.FCP_true_false_checkBox_resposta_certa_B_V = QCheckBox(
            self.FCP_true_false_frame_op_B)
        self.FCP_true_false_checkBox_resposta_certa_B_V.setObjectName(
            u"FCP_true_false_checkBox_resposta_certa_B_V")
        self.FCP_true_false_checkBox_resposta_certa_B_V.setMinimumSize(
            QSize(50, 0))
        self.FCP_true_false_checkBox_resposta_certa_B_V.setMaximumSize(
            QSize(50, 16777215))

        self.horizontalLayout_59.addWidget(
            self.FCP_true_false_checkBox_resposta_certa_B_V)

        self.FCP_true_false_checkBox_resposta_certa_B_F = QCheckBox(
            self.FCP_true_false_frame_op_B)
        self.FCP_true_false_checkBox_resposta_certa_B_F.setObjectName(
            u"FCP_true_false_checkBox_resposta_certa_B_F")
        self.FCP_true_false_checkBox_resposta_certa_B_F.setMinimumSize(
            QSize(50, 0))
        self.FCP_true_false_checkBox_resposta_certa_B_F.setMaximumSize(
            QSize(50, 16777215))

        self.horizontalLayout_59.addWidget(
            self.FCP_true_false_checkBox_resposta_certa_B_F)

        self.FCP_true_false_parentese_B = QLabel(
            self.FCP_true_false_frame_op_B)
        self.FCP_true_false_parentese_B.setObjectName(
            u"FCP_true_false_parentese_B")
        self.FCP_true_false_parentese_B.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_59.addWidget(self.FCP_true_false_parentese_B)

        self.FCP_true_false_op_B = QLabel(self.FCP_true_false_frame_op_B)
        self.FCP_true_false_op_B.setObjectName(u"FCP_true_false_op_B")
        self.FCP_true_false_op_B.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_59.addWidget(self.FCP_true_false_op_B)

        self.FCP_true_false_lineEdit_text_op_B = QLineEdit(
            self.FCP_true_false_frame_op_B)
        self.FCP_true_false_lineEdit_text_op_B.setObjectName(
            u"FCP_true_false_lineEdit_text_op_B")
        self.FCP_true_false_lineEdit_text_op_B.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_59.addWidget(
            self.FCP_true_false_lineEdit_text_op_B)

        self.verticalLayout_33.addWidget(self.FCP_true_false_frame_op_B)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_3)

        self.verticalLayout_32.addWidget(self.frame_2)

        self.horizontalLayout_53.addWidget(self.FCP_ct_6)

        self.FCP_true_false_frame_DICA = QFrame(
            self.FCP_question_true_or_false)
        self.FCP_true_false_frame_DICA.setObjectName(
            u"FCP_true_false_frame_DICA")
        self.FCP_true_false_frame_DICA.setMaximumSize(QSize(300, 16777215))
        self.FCP_true_false_frame_DICA.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                     "margin: 0;\n"
                                                     "color: #000;\n"
                                                     "border-radius: 10px;")
        self.FCP_true_false_frame_DICA.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_true_false_frame_DICA.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.FCP_true_false_frame_DICA)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.FCP_objetiva_label_dica = QLabel(self.FCP_true_false_frame_DICA)
        self.FCP_objetiva_label_dica.setObjectName(u"FCP_objetiva_label_dica")

        self.verticalLayout_30.addWidget(
            self.FCP_objetiva_label_dica, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.FCP_objetiva_label_dica_text = QTextBrowser(
            self.FCP_true_false_frame_DICA)
        self.FCP_objetiva_label_dica_text.setObjectName(
            u"FCP_objetiva_label_dica_text")
        self.FCP_objetiva_label_dica_text.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.FCP_objetiva_label_dica_text.setReadOnly(True)

        self.verticalLayout_30.addWidget(self.FCP_objetiva_label_dica_text)

        self.horizontalLayout_53.addWidget(self.FCP_true_false_frame_DICA)

        self.stackedWidget_FCP.addWidget(self.FCP_question_true_or_false)
        self.FCP_question_objetiva = QWidget()
        self.FCP_question_objetiva.setObjectName(u"FCP_question_objetiva")
        self.FCP_question_objetiva.setMinimumSize(QSize(800, 0))
        self.FCP_question_objetiva.setMaximumSize(QSize(1000, 16777215))
        self.FCP_question_objetiva.setStyleSheet(u"")
        self.horizontalLayout_40 = QHBoxLayout(self.FCP_question_objetiva)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.FCP_ct_3 = QFrame(self.FCP_question_objetiva)
        self.FCP_ct_3.setObjectName(u"FCP_ct_3")
        self.FCP_ct_3.setStyleSheet(u"background-color: rgb(177, 177, 177);\n"
                                    "border-radius: 10px;")
        self.FCP_ct_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_ct_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.FCP_ct_3)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.FCP_ct_5 = QFrame(self.FCP_ct_3)
        self.FCP_ct_5.setObjectName(u"FCP_ct_5")
        self.FCP_ct_5.setMinimumSize(QSize(0, 50))
        self.FCP_ct_5.setMaximumSize(QSize(16777215, 50))
        self.FCP_ct_5.setStyleSheet(u"background-color: rgb(177, 177, 177);\n"
                                    "background-color: rgb(204, 204, 204);\n"
                                    "border-radius: 10px;")
        self.FCP_ct_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_ct_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.FCP_ct_5)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.FCP_label_tipo_pergunta_2 = QLabel(self.FCP_ct_5)
        self.FCP_label_tipo_pergunta_2.setObjectName(
            u"FCP_label_tipo_pergunta_2")
        self.FCP_label_tipo_pergunta_2.setStyleSheet(u"font: 12pt;\n"
                                                     "color: rgb(0, 0, 0);")

        self.horizontalLayout_52.addWidget(self.FCP_label_tipo_pergunta_2)

        self.FCP_spinBox_qtd_op = QSpinBox(self.FCP_ct_5)
        self.FCP_spinBox_qtd_op.setObjectName(u"FCP_spinBox_qtd_op")
        self.FCP_spinBox_qtd_op.setStyleSheet(u"font: 12pt;\n"
                                              "color: rgb(0, 0, 0);")

        self.FCP_spinBox_qtd_op.setValue(4)

        self.horizontalLayout_52.addWidget(self.FCP_spinBox_qtd_op)

        self.FCP_btn_gerar_op = QPushButton(self.FCP_ct_5)
        self.FCP_btn_gerar_op.setObjectName(u"FCP_btn_gerar_op")
        self.FCP_btn_gerar_op.setFont(font3)
        self.FCP_btn_gerar_op.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: rgb(0, 85, 0);\n"
                                            "  	width: 100%;\n"
                                            "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                            "    text-align: center;\n"
                                            "    padding: 5px;\n"
                                            "    color: white;\n"
                                            "    border-radius: 10px;\n"
                                            "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                            "	color: white;\n"

                                            "\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::hover{\n"
                                            "	\n"
                                            "	\n"
                                            "	background-color: rgb(0, 121, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::pressed{\n"
                                            "	\n"
                                            "\n"
                                            "	background-color: rgb(0, 58, 0);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")

        self.horizontalLayout_52.addWidget(self.FCP_btn_gerar_op)

        self.verticalLayout_28.addWidget(self.FCP_ct_5)

        self.FCP_ct_4 = QFrame(self.FCP_ct_3)
        self.FCP_ct_4.setObjectName(u"FCP_ct_4")
        self.FCP_ct_4.setStyleSheet(u"background-color: rgb(177, 177, 177);\n"
                                    "color: rgb(0, 0, 0);")
        self.FCP_ct_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_ct_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.FCP_ct_4)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.FCP_objetiva_op_A = QFrame(self.FCP_ct_4)
        self.FCP_objetiva_op_A.setObjectName(u"FCP_objetiva_op_A")
        self.FCP_objetiva_op_A.setMaximumSize(QSize(16777215, 50))
        self.FCP_objetiva_op_A.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_objetiva_op_A.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.FCP_objetiva_op_A)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(10, 10, 10, 10)
        self.FCP_objetiva_checkBox_resposta_certa_A = QCheckBox(
            self.FCP_objetiva_op_A)
        self.FCP_objetiva_checkBox_resposta_certa_A.setObjectName(
            u"FCP_objetiva_checkBox_resposta_certa_A")
        self.FCP_objetiva_checkBox_resposta_certa_A.setMinimumSize(
            QSize(150, 0))
        self.FCP_objetiva_checkBox_resposta_certa_A.setMaximumSize(
            QSize(150, 16777215))

        self.horizontalLayout_41.addWidget(
            self.FCP_objetiva_checkBox_resposta_certa_A)

        self.FCP_objetiva_op_A_2 = QLabel(self.FCP_objetiva_op_A)
        self.FCP_objetiva_op_A_2.setObjectName(u"FCP_objetiva_op_A_2")
        self.FCP_objetiva_op_A_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_41.addWidget(self.FCP_objetiva_op_A_2)

        self.FCP_objetiva_lineEdit_text_op_A = QLineEdit(
            self.FCP_objetiva_op_A)
        self.FCP_objetiva_lineEdit_text_op_A.setObjectName(
            u"FCP_objetiva_lineEdit_text_op_A")
        self.FCP_objetiva_lineEdit_text_op_A.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_41.addWidget(
            self.FCP_objetiva_lineEdit_text_op_A)

        self.verticalLayout_29.addWidget(self.FCP_objetiva_op_A)

        self.FCP_objetiva_op_B = QFrame(self.FCP_ct_4)
        self.FCP_objetiva_op_B.setObjectName(u"FCP_objetiva_op_B")
        self.FCP_objetiva_op_B.setMaximumSize(QSize(16777215, 50))
        self.FCP_objetiva_op_B.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_objetiva_op_B.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.FCP_objetiva_op_B)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(10, 10, 10, 10)
        self.FCP_objetiva_checkBox_resposta_certa_B = QCheckBox(
            self.FCP_objetiva_op_B)
        self.FCP_objetiva_checkBox_resposta_certa_B.setObjectName(
            u"FCP_objetiva_checkBox_resposta_certa_B")
        self.FCP_objetiva_checkBox_resposta_certa_B.setMinimumSize(
            QSize(150, 0))
        self.FCP_objetiva_checkBox_resposta_certa_B.setMaximumSize(
            QSize(150, 16777215))

        self.horizontalLayout_42.addWidget(
            self.FCP_objetiva_checkBox_resposta_certa_B)

        self.FCP_objetiva_op_B_2 = QLabel(self.FCP_objetiva_op_B)
        self.FCP_objetiva_op_B_2.setObjectName(u"FCP_objetiva_op_B_2")
        self.FCP_objetiva_op_B_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_42.addWidget(self.FCP_objetiva_op_B_2)

        self.FCP_objetiva_lineEdit_text_op_B = QLineEdit(
            self.FCP_objetiva_op_B)
        self.FCP_objetiva_lineEdit_text_op_B.setObjectName(
            u"FCP_objetiva_lineEdit_text_op_B")
        self.FCP_objetiva_lineEdit_text_op_B.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_42.addWidget(
            self.FCP_objetiva_lineEdit_text_op_B)

        self.verticalLayout_29.addWidget(self.FCP_objetiva_op_B)

        self.FCP_objetiva_op_C = QFrame(self.FCP_ct_4)
        self.FCP_objetiva_op_C.setObjectName(u"FCP_objetiva_op_C")
        self.FCP_objetiva_op_C.setMaximumSize(QSize(16777215, 50))
        self.FCP_objetiva_op_C.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_objetiva_op_C.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.FCP_objetiva_op_C)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(10, 10, 10, 10)
        self.FCP_objetiva_checkBox_resposta_certa_C = QCheckBox(
            self.FCP_objetiva_op_C)
        self.FCP_objetiva_checkBox_resposta_certa_C.setObjectName(
            u"FCP_objetiva_checkBox_resposta_certa_C")
        self.FCP_objetiva_checkBox_resposta_certa_C.setMinimumSize(
            QSize(150, 0))
        self.FCP_objetiva_checkBox_resposta_certa_C.setMaximumSize(
            QSize(150, 16777215))

        self.horizontalLayout_51.addWidget(
            self.FCP_objetiva_checkBox_resposta_certa_C)

        self.FCP_objetiva_op_C_2 = QLabel(self.FCP_objetiva_op_C)
        self.FCP_objetiva_op_C_2.setObjectName(u"FCP_objetiva_op_C_2")
        self.FCP_objetiva_op_C_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_51.addWidget(self.FCP_objetiva_op_C_2)

        self.FCP_objetiva_lineEdit_text_op_C = QLineEdit(
            self.FCP_objetiva_op_C)
        self.FCP_objetiva_lineEdit_text_op_C.setObjectName(
            u"FCP_objetiva_lineEdit_text_op_C")
        self.FCP_objetiva_lineEdit_text_op_C.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_51.addWidget(
            self.FCP_objetiva_lineEdit_text_op_C)

        self.verticalLayout_29.addWidget(self.FCP_objetiva_op_C)

        self.FCP_objetiva_op_D = QFrame(self.FCP_ct_4)
        self.FCP_objetiva_op_D.setObjectName(u"FCP_objetiva_op_D")
        self.FCP_objetiva_op_D.setMaximumSize(QSize(16777215, 50))
        self.FCP_objetiva_op_D.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_objetiva_op_D.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.FCP_objetiva_op_D)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")

        self.FCP_objetiva_checkBox_resposta_certa_D = QCheckBox(
            self.FCP_objetiva_op_D)
        self.FCP_objetiva_checkBox_resposta_certa_D.setObjectName(
            u"FCP_objetiva_checkBox_resposta_certa_D")
        self.FCP_objetiva_checkBox_resposta_certa_D.setMinimumSize(
            QSize(150, 0))
        self.FCP_objetiva_checkBox_resposta_certa_D.setMaximumSize(
            QSize(150, 16777215))

        self.horizontalLayout_43.addWidget(
            self.FCP_objetiva_checkBox_resposta_certa_D)

        self.FCP_objetiva_op_D_2 = QLabel(self.FCP_objetiva_op_D)
        self.FCP_objetiva_op_D_2.setObjectName(u"FCP_objetiva_op_D_2")
        self.FCP_objetiva_op_D_2.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_43.addWidget(self.FCP_objetiva_op_D_2)

        self.FCP_objetiva_lineEdit_text_op_D = QLineEdit(
            self.FCP_objetiva_op_D)
        self.FCP_objetiva_lineEdit_text_op_D.setObjectName(
            u"FCP_objetiva_lineEdit_text_op_D")
        self.FCP_objetiva_lineEdit_text_op_D.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_43.addWidget(
            self.FCP_objetiva_lineEdit_text_op_D)

        self.verticalLayout_29.addWidget(self.FCP_objetiva_op_D)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_2)

        self.verticalLayout_28.addWidget(self.FCP_ct_4)

        self.horizontalLayout_40.addWidget(self.FCP_ct_3)

        self.FCP_frame_DICA = QFrame(self.FCP_question_objetiva)
        self.FCP_frame_DICA.setObjectName(u"FCP_frame_DICA")
        self.FCP_frame_DICA.setMaximumSize(QSize(300, 16777215))
        self.FCP_frame_DICA.setStyleSheet(u"background-color: #ADAAAA;\n"
                                          "margin: 0;\n"
                                          "color: #000;\n"
                                          "border-radius: 10px;")
        self.FCP_frame_DICA.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_frame_DICA.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.FCP_frame_DICA)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.FCP_label_dica = QLabel(self.FCP_frame_DICA)
        self.FCP_label_dica.setObjectName(u"FCP_label_dica")

        self.verticalLayout_27.addWidget(
            self.FCP_label_dica, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.FCP_label_dica_text = QTextBrowser(self.FCP_frame_DICA)
        self.FCP_label_dica_text.setObjectName(u"FCP_label_dica_text")
        self.FCP_label_dica_text.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.FCP_label_dica_text.setReadOnly(True)

        self.verticalLayout_27.addWidget(self.FCP_label_dica_text)

        self.horizontalLayout_40.addWidget(self.FCP_frame_DICA)

        self.stackedWidget_FCP.addWidget(self.FCP_question_objetiva)

        self.verticalLayout_24.addWidget(self.stackedWidget_FCP)

        self.FCP_bottom_btns = QFrame(self.FCP_ct_2)
        self.FCP_bottom_btns.setObjectName(u"FCP_bottom_btns")
        self.FCP_bottom_btns.setMaximumSize(QSize(16777215, 50))
        self.FCP_bottom_btns.setStyleSheet(u"")
        self.FCP_bottom_btns.setFrameShape(QFrame.Shape.StyledPanel)
        self.FCP_bottom_btns.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.FCP_bottom_btns)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.FCP_btn_anterior = QPushButton(self.FCP_bottom_btns)
        self.FCP_btn_anterior.setObjectName(u"FCP_btn_anterior")
        self.FCP_btn_anterior.setFont(font3)
        self.FCP_btn_anterior.setStyleSheet(u"QPushButton{\n"
                                            "	background-color: rgb(170, 85, 0);\n"
                                            "  	width: 100%;\n"
                                            "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                            "    text-align: center;\n"
                                            "    padding: 10px;\n"
                                            "    color: white;\n"
                                            "    border-radius: 10px;\n"
                                            "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                            "	color: white;\n"
                                            "	border-radius: 10px;\n"
                                            "	\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::hover{\n"
                                            "	\n"
                                            "	background-color: rgb(197, 99, 0);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton::pressed{\n"
                                            "	\n"
                                            "	background-color: rgb(112, 56, 0);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "\n"
                                            "")

        self.horizontalLayout_38.addWidget(
            self.FCP_btn_anterior, 0, Qt.AlignmentFlag.AlignHCenter)

        self.FCP_btn_proximo = QPushButton(self.FCP_bottom_btns)
        self.FCP_btn_proximo.setObjectName(u"FCP_btn_proximo")
        self.FCP_btn_proximo.setFont(font3)
        self.FCP_btn_proximo.setStyleSheet(u"QPushButton{\n"
                                           "  width: 100%;\n"
                                           "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                           "    text-align: center;\n"
                                           "    padding: 10px;\n"
                                           "    color: white;\n"
                                           "    border-radius: 10px;\n"
                                           "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                           "	color: white;\n"
                                           "	margin-left: 10px;\n"
                                           "	border-radius: 10px;\n"
                                           "\n"
                                           "	background-color: rgb(27, 110, 156);\n"
                                           "\n"
                                           "	\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton::hover{\n"
                                           "	\n"
                                           "	background-color: rgb(32, 132, 186);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton::pressed{\n"
                                           "	\n"
                                           "	background-color: rgb(20, 82, 115);\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "")

        self.horizontalLayout_38.addWidget(
            self.FCP_btn_proximo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_24.addWidget(
            self.FCP_bottom_btns, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_21.addWidget(self.FCP_ct_2)

        self.verticalLayout_20.addWidget(self.FCP_ct)

        self.abas.addWidget(self.pg_criar_provas)
        self.pg_docente = QWidget()
        self.pg_docente.setObjectName(u"pg_docente")
        self.verticalLayout_31 = QVBoxLayout(self.pg_docente)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_dc_top = QFrame(self.pg_docente)
        self.frame_dc_top.setObjectName(u"frame_dc_top")
        self.frame_dc_top.setMaximumSize(QSize(16777215, 60))
        self.frame_dc_top.setStyleSheet(u"QFrame{\n"
                                        "	border: none;\n"
                                        "}\n"
                                        "")
        self.frame_dc_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_dc_top)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")

        self.frame_dc_top_left = QFrame(self.frame_dc_top)
        self.frame_dc_top_left.setObjectName(u"frame_dc_top_left")
        self.frame_dc_top_left.setStyleSheet(u"QFrame{\n"
                                             "	border: none;\n"
                                             "}\n"
                                             "")
        self.frame_dc_top_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_top_left.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_27.addWidget(self.frame_dc_top_left)

        self.frame_dc_top_center = QFrame(self.frame_dc_top)
        self.frame_dc_top_center.setObjectName(u"frame_dc_top_center")
        self.frame_dc_top_center.setStyleSheet(u"QFrame{\n"
                                               "	border: none;\n"
                                               "}\n"
                                               "")
        self.frame_dc_top_center.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_top_center.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_dc_top_center)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_dc_top_center_label = QLabel(self.frame_dc_top_center)
        self.frame_dc_top_center_label.setObjectName(
            u"frame_dc_top_center_label")

        self.horizontalLayout_30.addWidget(
            self.frame_dc_top_center_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_27.addWidget(self.frame_dc_top_center)

        self.frame_dc_top_right = QFrame(self.frame_dc_top)
        self.frame_dc_top_right.setObjectName(u"frame_dc_top_right")
        self.frame_dc_top_right.setStyleSheet(u"QFrame{\n"
                                              "	border: none;\n"
                                              "}\n"
                                              "")
        self.frame_dc_top_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_top_right.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_dc_top_right)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.btn_cancelar_dc_top_right = QPushButton(self.frame_dc_top_right)
        self.btn_cancelar_dc_top_right.setObjectName(
            u"btn_cancelar_dc_top_right")
        self.btn_cancelar_dc_top_right.setFont(font3)
        self.btn_cancelar_dc_top_right.setStyleSheet(u"QPushButton{\n"
                                                     "  	width: 100%;\n"
                                                     "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                                     "    text-align: center;\n"
                                                     "    padding: 10px;\n"
                                                     "    color: white;\n"
                                                     "    border-radius: 10px;\n"
                                                     "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                                     "	color: white;\n"
                                                     "	border-radius: 10px;\n"
                                                     "	\n"
                                                     "	background-color: rgb(85, 0, 0);\n"
                                                     "\n"
                                                     "	\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton::hover{\n"
                                                     "	\n"
                                                     "	background-color: rgb(129, 0, 0);\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton::pressed{\n"
                                                     "	\n"
                                                     "	background-color: rgb(65, 0, 0);\n"
                                                     "}\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "\n"
                                                     "")

        self.horizontalLayout_29.addWidget(
            self.btn_cancelar_dc_top_right, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_27.addWidget(self.frame_dc_top_right)

        self.verticalLayout_31.addWidget(self.frame_dc_top)

        self.frame_dc_main = QFrame(self.pg_docente)
        self.frame_dc_main.setObjectName(u"frame_dc_main")
        self.frame_dc_main.setStyleSheet(u"QFrame{\n"
                                         "	border: none;\n"
                                         "}\n"
                                         "")
        self.frame_dc_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_main.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_dc_main)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.frame_dc_main_interna = QFrame(self.frame_dc_main)
        self.frame_dc_main_interna.setObjectName(u"frame_dc_main_interna")
        self.frame_dc_main_interna.setStyleSheet(u"background-color: rgb(85, 85, 127);\n"
                                                 "border-radius: 12px;")
        self.frame_dc_main_interna.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_main_interna.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_dc_main_interna)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_dc_main_ct = QFrame(self.frame_dc_main_interna)
        self.frame_dc_main_ct.setObjectName(u"frame_dc_main_ct")
        self.frame_dc_main_ct.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_main_ct.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_dc_main_ct)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_dc_main_ct_left = QFrame(self.frame_dc_main_ct)
        self.frame_dc_main_ct_left.setObjectName(u"frame_dc_main_ct_left")
        self.frame_dc_main_ct_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_main_ct_left.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_dc_main_ct_left)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")

        self.frame_dc_label_docente = QLabel(self.frame_dc_main_ct_left)
        self.frame_dc_label_docente.setObjectName(u"frame_dc_label_docente")
        self.frame_dc_label_docente.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_19.addWidget(self.frame_dc_label_docente)

        self.frame_dc_lineEdit_docente = QLineEdit(self.frame_dc_main_ct_left)
        self.frame_dc_lineEdit_docente.setObjectName(
            u"frame_dc_lineEdit_docente")
        self.frame_dc_lineEdit_docente.setMaximumSize(QSize(700, 16777215))
        self.frame_dc_lineEdit_docente.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                     "padding: 10px;\n"
                                                     "margin-bottom: 20px;\n"
                                                     "font-size: 12pt;\n"
                                                     "border: none;\n"
                                                     "border-radius: 10px;")

        self.verticalLayout_19.addWidget(self.frame_dc_lineEdit_docente)

        self.frame_dc_label_instituicao = QLabel(self.frame_dc_main_ct_left)
        self.frame_dc_label_instituicao.setObjectName(
            u"frame_dc_label_instituicao")
        self.frame_dc_label_instituicao.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_19.addWidget(self.frame_dc_label_instituicao)

        self.frame_dc_lineEdit_instituicao = QLineEdit(
            self.frame_dc_main_ct_left)
        self.frame_dc_lineEdit_instituicao.setObjectName(
            u"frame_dc_lineEdit_instituicao")
        self.frame_dc_lineEdit_instituicao.setMaximumSize(QSize(700, 16777215))
        self.frame_dc_lineEdit_instituicao.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                         "padding: 10px;\n"
                                                         "margin-bottom: 20px;\n"
                                                         "font-size: 12pt;\n"
                                                         "border: none;\n"
                                                         "border-radius: 10px;")

        self.verticalLayout_19.addWidget(self.frame_dc_lineEdit_instituicao)

        self.frame_dc_label_formacao = QLabel(self.frame_dc_main_ct_left)
        self.frame_dc_label_formacao.setObjectName(u"frame_dc_label_formacao")
        self.frame_dc_label_formacao.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_19.addWidget(self.frame_dc_label_formacao)

        self.frame_dc_lineEdit_formacao = QLineEdit(self.frame_dc_main_ct_left)
        self.frame_dc_lineEdit_formacao.setObjectName(
            u"frame_dc_lineEdit_formacao")
        self.frame_dc_lineEdit_formacao.setMaximumSize(QSize(700, 16777215))
        self.frame_dc_lineEdit_formacao.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                      "padding: 10px;\n"
                                                      "margin-bottom: 20px;\n"
                                                      "font-size: 12pt;\n"
                                                      "border: none;\n"
                                                      "border-radius: 10px;")

        self.verticalLayout_19.addWidget(self.frame_dc_lineEdit_formacao)

        self.frame_dc_label_disciplina = QLabel(self.frame_dc_main_ct_left)
        self.frame_dc_label_disciplina.setObjectName(
            u"frame_dc_label_disciplina")
        self.frame_dc_label_disciplina.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_19.addWidget(self.frame_dc_label_disciplina)

        self.frame_dc_lineEdit_disciplina = QLineEdit(
            self.frame_dc_main_ct_left)
        self.frame_dc_lineEdit_disciplina.setObjectName(
            u"frame_dc_lineEdit_disciplina")
        self.frame_dc_lineEdit_disciplina.setMaximumSize(QSize(700, 16777215))
        self.frame_dc_lineEdit_disciplina.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                        "padding: 10px;\n"
                                                        "margin-bottom: 20px;\n"
                                                        "font-size: 12pt;\n"
                                                        "border: none;\n"
                                                        "border-radius: 10px;")

        self.verticalLayout_19.addWidget(self.frame_dc_lineEdit_disciplina)

        self.frame_dc_label_logomarca = QLabel(self.frame_dc_main_ct_left)
        self.frame_dc_label_logomarca.setObjectName(
            u"frame_dc_label_logomarca")
        self.frame_dc_label_logomarca.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_19.addWidget(self.frame_dc_label_logomarca)

        self.frame_dc_lineEdit_logomarca = QLineEdit(
            self.frame_dc_main_ct_left)
        self.frame_dc_lineEdit_logomarca.setObjectName(
            u"frame_dc_lineEdit_logomarca")
        self.frame_dc_lineEdit_logomarca.setMaximumSize(QSize(700, 16777215))
        self.frame_dc_lineEdit_logomarca.setStyleSheet(u"background-color: #ADAAAA;\n"
                                                       "padding: 10px;\n"
                                                       "margin-bottom: 20px;\n"
                                                       "font-size: 12pt;\n"
                                                       "border: none;\n"
                                                       "border-radius: 10px;")

        self.verticalLayout_19.addWidget(self.frame_dc_lineEdit_logomarca)

        self.horizontalLayout_28.addWidget(self.frame_dc_main_ct_left)

        self.frame_dc_main_ct_right = QFrame(self.frame_dc_main_ct)
        self.frame_dc_main_ct_right.setObjectName(u"frame_dc_main_ct_right")
        self.frame_dc_main_ct_right.setMinimumSize(QSize(300, 0))
        self.frame_dc_main_ct_right.setStyleSheet(u"")
        self.frame_dc_main_ct_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_main_ct_right.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_dc_main_ct_right)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame = QFrame(self.frame_dc_main_ct_right)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_24.addWidget(
            self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_18.addWidget(self.frame)

        self.horizontalLayout_28.addWidget(
            self.frame_dc_main_ct_right, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_17.addWidget(self.frame_dc_main_ct)

        self.frame_dc_bottom = QFrame(self.frame_dc_main_interna)
        self.frame_dc_bottom.setObjectName(u"frame_dc_bottom")
        self.frame_dc_bottom.setMaximumSize(QSize(16777215, 60))
        self.frame_dc_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dc_bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_dc_bottom)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pg_prova_btn_SALVAR_2 = QPushButton(self.frame_dc_bottom)
        self.pg_prova_btn_SALVAR_2.setObjectName(u"pg_prova_btn_SALVAR_2")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
# endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
# endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush4)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
# endif
        self.pg_prova_btn_SALVAR_2.setPalette(palette5)
        self.pg_prova_btn_SALVAR_2.setFont(font2)
        self.pg_prova_btn_SALVAR_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pg_prova_btn_SALVAR_2.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight)
        self.pg_prova_btn_SALVAR_2.setStyleSheet(u"QPushButton{\n"
                                                 "  	width: 100%;\n"
                                                 "    /* Para centralizar o texto dentro do bot\u00e3o */\n"
                                                 "    text-align: center;\n"
                                                 "    padding: 10px;\n"
                                                 "    color: white;\n"
                                                 "    border-radius: 10px;\n"
                                                 "    border: none; /* Opcional: Remove bordas padr\u00e3o, se necess\u00e1rio */\n"
                                                 "	color: white;\n"
                                                 "	border-radius: 10px;\n"
                                                 "	background: #541B9C;\n"
                                                 "	font-size: 18pt;\n"
                                                 "	border-radius: 12px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton::hover{\n"
                                                 "	background-color: rgb(108, 35, 204);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton::pressed{\n"
                                                 "	background-color: rgb(50, 16, 95);\n"
                                                 "     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #541B9C, stop: 1 #0d5ca6);\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.pg_prova_btn_SALVAR_2.setText(u"Salvar")
        self.pg_prova_btn_SALVAR_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_31.addWidget(
            self.pg_prova_btn_SALVAR_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_17.addWidget(self.frame_dc_bottom)

        self.verticalLayout_16.addWidget(self.frame_dc_main_interna)

        self.verticalLayout_31.addWidget(self.frame_dc_main)

        self.abas.addWidget(self.pg_docente)

        self.gridLayout_3.addWidget(self.abas, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_main_meio, 1, 1, 2, 1)

        self.frame_sidebar = QFrame(self.centralwidget)
        self.frame_sidebar.setObjectName(u"frame_sidebar")
        self.frame_sidebar.setMinimumSize(QSize(65, 0))
        self.frame_sidebar.setMaximumSize(QSize(60, 16777215))
        self.frame_sidebar.setStyleSheet(
            u"background-color: #1F0B39; color: #fff;")
        self.frame_sidebar.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frame_sidebar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_sidebar_top = QFrame(self.frame_sidebar)
        self.frame_sidebar_top.setObjectName(u"frame_sidebar_top")
        self.frame_sidebar_top.setMinimumSize(QSize(0, 310))
        self.frame_sidebar_top.setStyleSheet(u"border: none;")
        self.frame_sidebar_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sidebar_top.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_sidebar_top)
        self.verticalLayout_2.setSpacing(0)

        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolButton_provas = QToolButton(self.frame_sidebar_top)
        self.toolButton_provas.setObjectName(u"toolButton_provas")
        self.toolButton_provas.setEnabled(True)
        self.toolButton_provas.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_provas.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight)
        self.toolButton_provas.setStyleSheet(u"\n"
                                             "QToolButton{\n"
                                             "	border: none;\n"
                                             "	width : 100%;\n"
                                             "\n"
                                             "	padding: 10px;\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton::hover{\n"
                                             "	border: none;\n"
                                             "	background-color: rgb(97, 28, 152);\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton::pressed{\n"
                                             "	border: none;\n"
                                             "	background-color: rgb(97, 80, 152);\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "")
        icon4 = QIcon()
        icon4.addFile(u":/icon/prova-white.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_provas.setIcon(icon4)
        self.toolButton_provas.setIconSize(QSize(30, 30))
        self.toolButton_provas.setAutoRepeat(False)
        self.toolButton_provas.setAutoExclusive(False)
        self.toolButton_provas.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_provas)

        self.toolButton_grupos = QToolButton(self.frame_sidebar_top)
        self.toolButton_grupos.setObjectName(u"toolButton_grupos")
        self.toolButton_grupos.setMaximumSize(QSize(16777215, 16777215))
        self.toolButton_grupos.setStyleSheet(u"\n"
                                             "QToolButton{\n"
                                             "	border: none;\n"
                                             "	width : 100%;\n"
                                             "\n"
                                             "	padding: 10px;\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton::hover{\n"
                                             "	border: none;\n"
                                             "	background-color: rgb(97, 28, 152);\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton::pressed{\n"
                                             "	border: none;\n"
                                             "	background-color: green;\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "")
        icon5 = QIcon()
        icon5.addFile(u":/icon/grupo-white.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_grupos.setIcon(icon5)
        self.toolButton_grupos.setIconSize(QSize(30, 30))
        self.toolButton_grupos.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_grupos)

        self.toolButton_turmas = QToolButton(self.frame_sidebar_top)
        self.toolButton_turmas.setObjectName(u"toolButton_turmas")
        self.toolButton_turmas.setStyleSheet(u"\n"
                                             "QToolButton{\n"
                                             "	border: none;\n"
                                             "	padding: 10px;\n"
                                             "	width : 100%;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton::hover{\n"
                                             "	border: none;\n"
                                             "background-color: rgb(97, 28, 152);\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton::pressed{\n"
                                             "	border: none;\n"
                                             "	background-color: green;\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "")
        icon6 = QIcon()
        icon6.addFile(u":/icon/turma-white.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_turmas.setIcon(icon6)
        self.toolButton_turmas.setIconSize(QSize(30, 30))
        self.toolButton_turmas.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_turmas)

        self.toolButton_docente = QToolButton(self.frame_sidebar_top)
        self.toolButton_docente.setObjectName(u"toolButton_docente")
        self.toolButton_docente.setStyleSheet(u"\n"
                                              "QToolButton{\n"
                                              "	border: none;\n"
                                              "	padding: 10px;\n"
                                              "	width : 100%;\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton::hover{\n"
                                              "	border: none;\n"
                                              "background-color: rgb(97, 28, 152);\n"
                                              "}\n"
                                              "\n"
                                              "QToolButton::pressed{\n"
                                              "	border: none;\n"
                                              "	background-color: green;\n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "")
        icon7 = QIcon()
        icon7.addFile(u":/icon/professor.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_docente.setIcon(icon7)
        self.toolButton_docente.setIconSize(QSize(30, 30))
        self.toolButton_docente.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.toolButton_docente)

        self.verticalLayout.addWidget(
            self.frame_sidebar_top, 0, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.frame_sidebar_center = QFrame(self.frame_sidebar)
        self.frame_sidebar_center.setObjectName(u"frame_sidebar_center")
        self.frame_sidebar_center.setStyleSheet(u"border: none;")
        self.frame_sidebar_center.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sidebar_center.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_sidebar_center)

        self.frame_sidebar_bottom = QFrame(self.frame_sidebar)
        self.frame_sidebar_bottom.setObjectName(u"frame_sidebar_bottom")
        self.frame_sidebar_bottom.setStyleSheet(u"border: none;")
        self.frame_sidebar_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sidebar_bottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_sidebar_bottom)

        self.gridLayout.addWidget(self.frame_sidebar, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.toolButton_provas, self.toolButton_grupos)
        QWidget.setTabOrder(self.toolButton_grupos, self.toolButton_turmas)
        QWidget.setTabOrder(self.toolButton_turmas, self.lineEdit_filtro_data)
        QWidget.setTabOrder(self.lineEdit_filtro_data, self.pg1_btn_novo)
        QWidget.setTabOrder(self.pg1_btn_novo, self.lineEdit_filtro_turma)
        QWidget.setTabOrder(self.lineEdit_filtro_turma,
                            self.lineEdit_filtro_grupo)
        QWidget.setTabOrder(self.lineEdit_filtro_grupo, self.pg1_btn_cancelar)
        QWidget.setTabOrder(self.pg1_btn_cancelar, self.pg_prova_btn_SALVAR)
        QWidget.setTabOrder(self.pg_prova_btn_SALVAR,
                            self.lineEdit_filtro_titulo)
        QWidget.setTabOrder(self.lineEdit_filtro_titulo,
                            self.GRUPO_LineEdit_descricao)
        QWidget.setTabOrder(self.GRUPO_LineEdit_descricao,
                            self.GRUPO_TextEdit_observacao)

        self.retranslateUi(MainWindow)

        self.abas.setCurrentIndex(3)
        self.stackedWidget_FCP.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.header_titulo.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">   Aooba Sistemas</span></p></body></html>", None))
# if QT_CONFIG(tooltip)
        self.pg_PROVA_frame_top.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.pg_PROVA_frame_top.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
# endif // QT_CONFIG(whatsthis)
# if QT_CONFIG(tooltip)
        self.pg_PROVA_frame_center.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.pg_PROVA_frame_center.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
# endif // QT_CONFIG(whatsthis)
        self.lineEdit_filtro_titulo.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Filtrar por t\u00edtulo", None))
        self.lineEdit_filtro_turma.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Filtrar por turma", None))
        self.lineEdit_filtro_grupo.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Filtrar por grupo", None))
        self.lineEdit_filtro_data.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Filtrar por data", None))
# if QT_CONFIG(tooltip)
        self.pg_PROVA_frame_bottom.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
# endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.pg_PROVA_frame_bottom.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
# endif // QT_CONFIG(whatsthis)
        self.FP_HEADER_INFO_titulo_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">T\u00ectulo</span></p></body></html>", None))
        self.FP_HEADER_INFO_turma_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Turma</span></p></body></html>", None))
        self.FP_HEADER_INFO_grupo_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Grupo</span></p></body></html>", None))
        self.FP_HEADER_INFO_data_c_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Data de cria\u00e7\u00e3o</span></p></body></html>", None))
        self.FP_HEADER_INFO_hora_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Hora</span></p></body></html>", None))
        self.FP_HEADER_INFO_acoes_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">A\u00e7\u00f5es</span></p></body></html>", None))
        self.FP_1_titulo.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Nome avalia\u00e7\u00e3o</p></body></html>", None))
        self.FP_1_bpx_turma.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Turma 1", None))
        self.FP_1_bpx_turma.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Turma 2", None))

        self.FP_1_box_grupo.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Turma 1", None))
        self.FP_1_box_grupo.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Turma 2", None))

        self.FP_1_btn_delete.setText("")
        self.FP_1_btn_edit.setText("")
        self.FP_2_titulo.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Nome avalia\u00e7\u00e3o</p></body></html>", None))
        self.FP_2_box_turma.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Turma 1", None))
        self.FP_2_box_turma.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Turma 2", None))

        self.FP_2_box_grupo.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Turma 1", None))
        self.FP_2_box_grupo.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Turma 2", None))

        self.FP_2_btn_delete.setText("")
        self.FP_2_btn_edit.setText("")
        self.header_titulo_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">GRUPOS</span></p></body></html>", None))
        self.GRUPO_label_descricao.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Descri\u00e7\u00e3o</span></p></body></html>", None))
        self.GRUPO_LineEdit_descricao.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Digite uma descri\u00e7\u00e3o", None))
        self.GRUPO_label_observacao.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Observa\u00e7\u00f5es</span></p></body></html>", None))
        self.GRUPO_TextEdit_observacao.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Digite aqui as observa\u00e7\u00f5es", None))
        self.label_name_grupo.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Alunos</span></p></body></html>", None))
        self.toolButton_editar_grupo.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_excluir_grupo.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.label_grupos_dica.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Dica de como usar</span></p></body></html>", None))
        self.label_grupos_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "hr { height: 1px; border-width: 0; }\n"
                                                                  "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                  "li.checked::marker { content: \"\\2612\"; }\n"
                                                                  "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">As vezes, uma ou mais provas podem ser do mesmo grupo, mas pertencer a disciplinas diferentes. </span></p>\n"
                                                                  "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Ex.: Uma prova de grupo matem\u00e1tica. De turmas diferentes.<br />"
                                                                  "<br />Use os grupos quando quiser categorizar as avalia\u00e7\u00f5es</span></p></body></html>", None))
        self.header_titulo_turma.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">TURMAS</span></p></body></html>", None))
        self.TURMA_label_descricao.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Descri\u00e7\u00e3o</span></p></body></html>", None))
        self.turma_LineEdit_descricao.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Digite uma descri\u00e7\u00e3o", None))
        self.TURMA_label_observacao.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Observa\u00e7\u00f5es</span></p></body></html>", None))
        self.TURMA_TextEdit_observacao.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Digite aqui as observa\u00e7\u00f5es", None))
        self.label_name_turma.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Turma 1</span></p></body></html>", None))
        self.toolButton_editar_turma.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_excluir_turma.setText(
            QCoreApplication.translate("MainWindow", u"...", None))
        self.label_grupos_dica_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Dica de como usar</span></p></body></html>", None))
        self.label_grupos_text_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "hr { height: 1px; border-width: 0; }\n"
                                                                    "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                    "li.checked::marker { content: \"\\2612\"; }\n"
                                                                    "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">As vezes, uma ou mais provas podem ser da mesma disciplina,<br />mas pertencer a turmas diferentes.<br /><br />Ex.: Uma prova de matem\u00e1tica. De turmas diferentes.<br /><br />Use as turmas quando quiser organizar as turmas lecionadas.</span></p></body></html>", None))
        self.FCP_btn_gerar_pdf_dc_top_right.setText(
            QCoreApplication.translate("MainWindow", u"Gerar PDF", None))
        self.FCP_btn_cancelar_dc_top_right.setText(
            QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.FCP_checkBox_save_question.setText(
            QCoreApplication.translate("MainWindow", u"Salvar pergunta!", None))
        self.FCP_label_level_question.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Nivel da pergunta:</span></p></body></html>", None))
        self.FCP_comboBox_level_question.setItemText(
            0, QCoreApplication.translate("MainWindow", u"F\u00e1cil", None))
        self.FCP_comboBox_level_question.setItemText(
            1, QCoreApplication.translate("MainWindow", u"M\u00e9dio", None))
        self.FCP_comboBox_level_question.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Dif\u00edcio", None))

        self.label_qtd_pergunta.setText(QCoreApplication.translate(
            "MainWindow", u"Pergunta: 1", None))
        self.label_tipo_pergunta.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Tipo de Pergunta</span></p></body></html>", None))
        self.FCP_radioButton_dissertativa.setText(
            QCoreApplication.translate("MainWindow", u"Dissertativa", None))
        self.FCP_radioButton_objetiva.setText(
            QCoreApplication.translate("MainWindow", u"Objetiva", None))
        self.FCP_radioButton_true_or_false.setText(
            QCoreApplication.translate("MainWindow", u"Verdade ou Falso", None))

        self.FCP_label_cabecalho.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Digite aqui a sua pergunta...</span></p></body></html>", None))

        self.FCP_label_cabecalho_respost_correta.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Resposta correta - Gabarito (opcional)</span></p></body></html>", None))

        self.FCP_objetiva_label_tipo_pergunta_3.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Numero de op\u00e7\u00f5es:</span></p></body></html>", None))
        self.FCP_objetiva_btn_gerar_op_2.setText(
            QCoreApplication.translate("MainWindow", u"Gerar", None))
        self.FCP_true_false_checkBox_resposta_certa_A_V.setText(
            QCoreApplication.translate("MainWindow", u"V", None))
        self.FCP_true_false_checkBox_resposta_certa_A_F.setText(
            QCoreApplication.translate("MainWindow", u"F", None))
        self.FCP_true_false_parentese_A.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">(  )</span></p></body></html>", None))
        self.FCP_true_false_op_A.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">A)</span></p></body></html>", None))
        self.FCP_true_false_lineEdit_text_op_A.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Digite aqui a resposta 1", None))
        self.FCP_true_false_checkBox_resposta_certa_B_V.setText(
            QCoreApplication.translate("MainWindow", u"V", None))
        self.FCP_true_false_checkBox_resposta_certa_B_F.setText(
            QCoreApplication.translate("MainWindow", u"F", None))
        self.FCP_true_false_parentese_B.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">(  )</span></p></body></html>", None))
        self.FCP_true_false_op_B.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">B)</span></p></body></html>", None))
        self.FCP_true_false_lineEdit_text_op_B.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Digite aqui a resposta 2", None))
        self.FCP_objetiva_label_dica.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Dica de como usar</span></p></body></html>", None))
        self.FCP_objetiva_label_dica_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                             "p, li { white-space: pre-wrap; }\n"
                                                                             "hr { height: 1px; border-width: 0; }\n"
                                                                             "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                             "li.checked::marker { content: \"\\2612\"; }\n"
                                                                             "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                             "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Cada op\u00e7\u00e3o tem uma CheckBox, que deve ser marcada caso a op\u00e7\u00e3o seja a correta!</span></p></body></html>", None))
        self.FCP_label_tipo_pergunta_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Numero de op\u00e7\u00f5es:</span></p></body></html>", None))
        self.FCP_btn_gerar_op.setText(
            QCoreApplication.translate("MainWindow", u"Gerar", None))
        self.FCP_objetiva_checkBox_resposta_certa_A.setText(
            QCoreApplication.translate("MainWindow", u"Resposta certa", None))
        self.FCP_objetiva_op_A_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">A)</span></p></body></html>", None))
        self.FCP_objetiva_lineEdit_text_op_A.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Digite aqui a resposta 1", None))
        self.FCP_objetiva_checkBox_resposta_certa_B.setText(
            QCoreApplication.translate("MainWindow", u"Resposta certa", None))
        self.FCP_objetiva_op_B_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">B)</span></p></body></html>", None))
        self.FCP_objetiva_lineEdit_text_op_B.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Digite aqui a resposta 2", None))
        self.FCP_objetiva_checkBox_resposta_certa_C.setText(
            QCoreApplication.translate("MainWindow", u"Resposta certa", None))
        self.FCP_objetiva_op_C_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">C)</span></p></body></html>", None))
        self.FCP_objetiva_lineEdit_text_op_C.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Digite aqui a resposta 3", None))
        self.FCP_objetiva_checkBox_resposta_certa_D.setText(
            QCoreApplication.translate("MainWindow", u"Resposta certa", None))
        self.FCP_objetiva_op_D_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">D)</span></p></body></html>", None))
        self.FCP_objetiva_lineEdit_text_op_D.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Digite aqui a resposta 4", None))
        self.FCP_label_dica.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Dica de como usar</span></p></body></html>", None))
        self.FCP_label_dica_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "hr { height: 1px; border-width: 0; }\n"
                                                                    "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                    "li.checked::marker { content: \"\\2612\"; }\n"
                                                                    "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                    "<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Cada op\u00e7\u00e3o tem uma CheckBox, que deve ser marcada caso a op\u00e7\u00e3o seja a correta!</span></p></body></html>", None))
        self.FCP_btn_anterior.setText(
            QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.FCP_btn_proximo.setText(QCoreApplication.translate(
            "MainWindow", u"Pr\u00f3xima", None))
        self.frame_dc_top_center_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:700; color:#000000;\">Docente</span></p></body></html>", None))
        self.btn_cancelar_dc_top_right.setText(
            QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.frame_dc_label_docente.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Docente</span></p></body></html>", None))
        self.frame_dc_lineEdit_docente.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Digite o seu nome", None))
        self.frame_dc_label_instituicao.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Institui\u00e7\u00e3o</span></p></body></html>", None))
        self.frame_dc_lineEdit_instituicao.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Ex.: Col\u00e9gio Estadual...", None))
        self.frame_dc_label_formacao.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Forma\u00e7\u00e3o</span></p></body></html>", None))
        self.frame_dc_lineEdit_formacao.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Ex.: Col\u00e9gio Estadual...", None))
        self.frame_dc_label_disciplina.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Disciplina</span></p></body></html>", None))
        self.frame_dc_lineEdit_disciplina.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Ex.: Matem\u00e1tica", None))
        self.frame_dc_label_logomarca.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Logomarca</span></p></body></html>", None))
        self.frame_dc_lineEdit_logomarca.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Escolha aqui a logomarca da sua institui\u00e7\u00e3o", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><img src=\":/icon/professor.png\"/></p></body></html>", None))
        self.toolButton_provas.setText(QCoreApplication.translate(
            "MainWindow", u"Provas", u"Navegar at\u00e9 provas"))
        self.toolButton_grupos.setText(
            QCoreApplication.translate("MainWindow", u"Grupos", None))
        self.toolButton_turmas.setText(
            QCoreApplication.translate("MainWindow", u"Turmas", None))
        self.toolButton_docente.setText(
            QCoreApplication.translate("MainWindow", u"Docente", None))
    # retranslateUi
