import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QPushButton, QApplication, QCheckBox, QProgressBar, QLabel, QComboBox, QStyleFactory
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

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

        checkBox = QCheckBox('Shrink Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn = QPushButton("Download", self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        self.styleChoice = QLabel("Windows Vista", self)

        comboBox = QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)
        self.show()

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50,50,1000, 60)
        else:
            self.setGeometry(50,50,500,300)

    def close_application(self):
        print("whooaaaaa so custom!!!")
        sys.exit()

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()