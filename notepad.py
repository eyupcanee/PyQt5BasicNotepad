import os
import sys

from PyQt5 import QtWidgets

class Notepad(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.text_area = QtWidgets.QTextEdit()
        self.clear = QtWidgets.QPushButton("Clear")
        self.open = QtWidgets.QPushButton("Open")
        self.save = QtWidgets.QPushButton("Save")

        h_box = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.clear)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.clear.clicked.connect(self.text_clear)
        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)

        self.show()

    def text_clear(self):
        self.text_area.clear()

    def open_file(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self,"Open File",os.getenv("Desktop"))

        try:
            with open(file_name[0],"r",encoding='utf-8') as file:
                self.text_area.setText(file.read())
        except:
            pass

    def save_file(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(self,"Save File",os.getenv("Desktop"))

        try:
            with open(file_name[0],"a",encoding='utf-8') as file:
                file.write(self.text_area.toPlainText())
        except:
            pass

class Menu(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        self.notepad = Notepad()
        self.setCentralWidget(self.notepad)

        self.build_menu()

    def build_menu(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")

        open_file = QtWidgets.QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file = QtWidgets.QAction("Save File",self)
        save_file.setShortcut("Ctrl+S")

        clear_text = QtWidgets.QAction("Clear Text",self)
        clear_text.setShortcut("Ctrl+D")

        exit = QtWidgets.QAction("Exit",self)
        exit.setShortcut("Ctrl+Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clear_text)
        file.addAction(exit)

        file.triggered.connect(self.response)

        self.setWindowTitle("Notepad")

        self.show()

    def response(self,action):

        if(action.text() == "Open File"):
            self.notepad.open_file()
        elif(action.text() == "Save File"):
            self.notepad.save_file()
        elif(action.text() == "Clear Text"):
            self.notepad.text_clear()
        elif(action.text() == "Exit"):
            QtWidgets.qApp.exit()

app = QtWidgets.QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())