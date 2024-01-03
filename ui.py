# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 675)
        font = QFont()
        font.setFamilies([u"Andy"])
        font.setPointSize(16)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:0, \n"
"        stop:0 rgba(28, 28, 28, 255), \n"
"        stop:1 rgba(105, 105, 105, 255)\n"
"    );\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 380, 81, 31))
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 426, 761, 231))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color:white;\n"
"font-family:Andy;\n"
"font-size:16pt;\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(15, 28, 131, 31))
        font1 = QFont()
        font1.setFamilies([u"Andy"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(14, 70, 771, 28))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    font-size: 13pt;\n"
"    font-family: 'Andy';\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"    background-color: rgba(0, 0, 0, 100);  \n"
"    selection-color: black; \n"
"    selection-background-color: white;\n"
"}\n"
"\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(15, 157, 231, 31))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(15, 197, 231, 41))
        self.textEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(281, 208, 21, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(4, 15, 791, 101))
        self.frame.setStyleSheet(u"background-color: rgba(1, 1, 1, 35);  /* \u0422\u0435\u043c\u043d\u043e-\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"border: 1px solid rgba(255, 255, 255, 100);  /* \u0411\u0435\u043b\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0441 \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u0431\u043e\u043b\u044c\u0448\u0435\u0439 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c\u044e */\n"
"border-radius: 7px;  /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(5, 149, 591, 101))
        self.frame_2.setStyleSheet(u"background-color: rgba(1, 1, 1, 35);  /* \u0422\u0435\u043c\u043d\u043e-\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"border: 1px solid rgba(255, 255, 255, 100);  /* \u0411\u0435\u043b\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0441 \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u0431\u043e\u043b\u044c\u0448\u0435\u0439 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c\u044e */\n"
"border-radius: 7px;  /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 366, 791, 301))
        self.frame_3.setStyleSheet(u"background-color: rgba(1, 1, 1, 35);  /* \u0422\u0435\u043c\u043d\u043e-\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"border: 1px solid rgba(255, 255, 255, 100);  /* \u0411\u0435\u043b\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0441 \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u0431\u043e\u043b\u044c\u0448\u0435\u0439 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c\u044e */\n"
"border-radius: 7px;  /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(334, 197, 231, 41))
        self.textEdit_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(607, 149, 191, 101))
        self.frame_4.setStyleSheet(u"background-color: rgba(1, 1, 1, 35);  /* \u0422\u0435\u043c\u043d\u043e-\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"border: 1px solid rgba(255, 255, 255, 100);  /* \u0411\u0435\u043b\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0441 \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u0431\u043e\u043b\u044c\u0448\u0435\u0439 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c\u044e */\n"
"border-radius: 7px;  /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(15, 17, 161, 30))
        self.pushButton.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 60); \n"
"    padding-top: 7px; \n"
"    padding-left: 7px;\n"
"    border: 1px solid rgba(255, 255, 255, 90); \n"
"}\n"
"QPushButton\n"
"{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-family:Andy;\n"
" font-size:16pt;\n"
"}")
        self.checkBox = QCheckBox(self.frame_4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(14, 57, 161, 31))
        self.checkBox.setStyleSheet(u"QCheckBox::indicator {\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 3px;\n"
"    width: 12px;\n"
"    height: 12px; \n"
"	margin-left: 5px;\n"
"}\n"
"QCheckBox\n"
"{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-family:Andy;\n"
"font-size:16pt\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgba(255, 255, 255, 255);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"}")
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(5, 257, 251, 101))
        self.frame_5.setStyleSheet(u"background-color: rgba(1, 1, 1, 35);  /* \u0422\u0435\u043c\u043d\u043e-\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"border: 1px solid rgba(255, 255, 255, 100);  /* \u0411\u0435\u043b\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0441 \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u0431\u043e\u043b\u044c\u0448\u0435\u0439 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c\u044e */\n"
"border-radius: 7px;  /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(8, 10, 231, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.textEdit_2 = QTextEdit(self.frame_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(9, 55, 231, 31))
        self.textEdit_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(269, 257, 531, 101))
        self.frame_6.setStyleSheet(u"background-color: rgba(1, 1, 1, 35);  /* \u0422\u0435\u043c\u043d\u043e-\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"border: 1px solid rgba(255, 255, 255, 100);  /* \u0411\u0435\u043b\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0441 \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u0431\u043e\u043b\u044c\u0448\u0435\u0439 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c\u044e */\n"
"border-radius: 7px;  /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_5.raise_()
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.plainTextEdit.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.textEdit.raise_()
        self.label_4.raise_()
        self.textEdit_3.raise_()
        self.frame_6.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EasyDumper", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Outputs:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Select process:</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"System", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"fsdf", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"fsdf", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"fsdf", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"fsdf", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"sd", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"fsd", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"f", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"sdf", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Input memory dump region:</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Andy'; font-size:16pt; color:#ffffff;\">0000000000000000</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">to</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Andy'; font-size:16pt; color:#ffffff;\">00007fffffffffff</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"QPushButton\n"
"{\n"
"color:white\n"
"}", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Kill process", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Read bytes</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12.75pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Andy'; font-size:16pt; color:#ffffff;\">0000000000000000</span></p></body></html>", None))
    # retranslateUi

