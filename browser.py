import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):

    def nav_h(self):
        defurl = "https://google.com"
        self.browser.setUrl(QUrl(defurl))

    def nav_url(self):
        n_url = self.ubar.text()
        self.browser.setUrl(QUrl('https://'+n_url))

    def update_u_n(self, qurl):
        self.ubar.setText(qurl.toString())


    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        url = "https://github.com"
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        nav = QToolBar()
        self.addToolBar(nav)
        b_button = QAction('back',self)
        b_button.triggered.connect(self.browser.back)
        nav.addAction(b_button)
        f_button = QAction('forward',self)
        f_button.triggered.connect(self.browser.forward)
        nav.addAction(f_button)
        r_button = QAction('reload', self)
        r_button.triggered.connect(self.browser.reload)
        nav.addAction(r_button)
        h_button = QAction('home', self)
        h_button.triggered.connect(self.nav_h)
        nav.addAction(h_button)
        self.ubar = QLineEdit()
        self.ubar.returnPressed.connect(self.nav_url)
        nav.addWidget(self.ubar)
        self.browser.urlChanged.connect(self.update_u_n)



App = QApplication(sys.argv)
QApplication.setApplicationName('Python Browser')
Window = MainWindow()
App.exec_()

