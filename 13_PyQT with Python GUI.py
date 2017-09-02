import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QPushButton, QApplication
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('PyQT tuts!')
        self.setWindowIcon(QIcon('icon_save.png'))

        extractAction = QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave The App")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        extractionAction = QAction(QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractionAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractionAction)



        self.show()

    def close_application(self):
        print("whooaaaaa so custom!!!")
        sys.exit()

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()