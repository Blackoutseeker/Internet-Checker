from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt
from socket import gethostbyname, create_connection

style_window = """
QMainWindow {
    background-color: black;
    border: 2px solid #0066ff;
}
"""

style_label = """
QLabel {
    color: #fff;
    font-size: 12pt;
}
"""

style_button = """
QPushButton {
    background-color: transparent;
    border: 2px solid #0066ff;
    color: #fff;
    font-size: 8pt;
    font-weight: bold;
}
QPushButton:hover {
    border-color: #fff;
}
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('', self)
        self.label.setStyleSheet(style_label)
        self.label.setText('Internet has been shut down!')
        self.label.setGeometry(0, 0, 275, 140)
        self.label.move(35, 0)
        self.button = QPushButton('X', self)
        self.button.setGeometry(0, 0, 20, 20)
        self.button.setStyleSheet(style_button)
        self.button.move(260, 0)
        self.button.clicked.connect(lambda: QApplication.quit())
        self.setWindowTitle('Internet Checker')
        self.setGeometry(0, 0, 280, 140)
        self.setStyleSheet(style_window)
        self.move(QApplication.desktop().frameGeometry().width() - 280, QApplication.desktop().height() - 140)
        self.setFixedSize(280, 140)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)


App = QApplication(argv)
window = Window()
mem1 = 0
while True:
    try:
        host = gethostbyname("www.google.com")
        s = create_connection((host, 80), 2)
        s.close()
        mem2 = 1
        if mem2 == mem1:
            pass
        else:
            mem1 = mem2
    except Exception as e:
        mem2 = 0
        if mem2 == mem1:
            pass
        else:
            mem1 = mem2
            window.show()
            exit(App.exec_())
