from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

import threading
def runserver():
    import os
    server_path = 'C:\\Users\\Chris\\Desktop\\web\\myproject'
    CWD=os.getcwd()
    os.chdir(server_path)
    os.system('python manage.py runserver')
    os.chdir(CWD)
thread=threading.Thread(target=runserver)
thread.start()

class Browser():
    def __init__(self):
        super(Browser, self)
        self.window = QWidget()
        self.window.setWindowTitle(' ')  # no title
        self.layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)
        self.browser.setUrl(QUrl('http://127.0.0.1:8000/'))
        self.window.setLayout(self.layout)
        self.window.showFullScreen()

browser_ = QApplication([])
window = Browser()
browser_.exec_()
