import binascii
import os
import psutil
from PySide6.QtWidgets import QMainWindow
from fun1 import get_pid_by_name, dump_process_memory
from ui import Ui_MainWindow

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.button_pressed)
        for proc in psutil.process_iter(['name']):
            self.ui.comboBox.addItem(proc.info['name'])

    def on_combobox_show(self):
        self.ui.comboBox.showPopup()

    def button_pressed(self):
        if self.ui.pushButton.pressed and self.ui.comboBox.currentText() is not None:
            if self.ui.textEdit.toPlainText() == '0':
                dump_process_memory((get_pid_by_name(self.ui.comboBox.currentText())),
                                    (int(self.ui.textEdit.toPlainText(), 16)),
                                    (int(self.ui.textEdit_3.toPlainText(), 16)))
                self.ui.plainTextEdit.setPlainText("Done")
            else:
                num_bytes = int(self.ui.textEdit_2.toPlainText())
                with open('dump.bin', 'rb') as f:
                    data = f.read(num_bytes)
                data = binascii.hexlify(data).decode('utf-8') 
                data = ' '.join([data[i:i + 2] for i in range(0, len(data), 2)]) 
                self.ui.plainTextEdit.setPlainText(data)
        if self.ui.checkBox.isChecked() and self.ui.comboBox.currentText():
            self.ui.plainTextEdit.setPlainText(
                f"{self.ui.comboBox.currentText()}-{get_pid_by_name(self.ui.comboBox.currentText())} was killed")
            os.system(f"taskkill /F /PID {self.ui.comboBox.currentText()}")
