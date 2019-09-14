import sys # test test
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# QTextEdit, QColorDialog, QCalendarWidget, QFontDialog, QProgressBar, QComboBox, QLabel, QStyleFactory, QCheckBox, QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.uic.properties import QtGui
# QtGui QutCore Qt Open GL  Qt XML Qt SQL Qt Networking

class window(QMainWindow):
    # everytime makes a window object, init runs
    # core application template
    def __init__(self):
        super(window, self).__init__() # inherite from parent, which is a QMainWindow object
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('pyqt5 Tut')
        # set.setWindowIcon(QIcon('pic.pn g'))

        extractAction = QAction('&Get to the choppah', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)

        openEditor = QAction('&Editor', self)
        openEditor.setShortcut('Ctrl+E')
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QAction('&Open File', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QAction('&Save File', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        self.statusBar()

        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('&file')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)

        self.home()

    # specific to that certain page you are on
    def home(self):
        btn = QPushButton('quit', self)
        # exit the current application
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0,100)

        extractAction = QAction(QIcon('pic.JPG'), 'flee the scene', self) # hover
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        fontChoice = QAction('Font', self) # hover
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar = self.addToolBar('Font')
        self.toolBar.addAction(fontChoice)

        checkBox = QCheckBox('Enlarge window', self)
        checkBox.move(300, 25)
        # checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        print(self.style().objectName())
        self.styleChoice = QLabel('Windows Vista', self)

        comboBox = QComboBox(self) # dropdown button
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsvista')

        comboBox.move(50,250)
        self.styleChoice.move(25, 150)
        comboBox.activated[str].connect(self.style_choice)

        cal = QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(300, 300)

        color = QColor(0,0,0)
        fontColor = QAction('font bg color', self)
        fontColor.triggered.connect(self.color_picker)
        self.toolBar.addAction(fontColor)

        self.show()

    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget{background-color: %s}' % color.name())

    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def file_open(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')
        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    def file_save(self):
        name, _ = QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def download(self):
        self.completed = 0;
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

    def close_application(self):
        choice = QMessageBox.question(self, 'Message',
                                    "Get into the chopper?",
                                    QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print('quit application. Extracting now!!')
            sys.exit()
        else:
            pass


def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()
# Three major compoennts
# 1. application
# app = QApplication(sys.argv) # can pass arguments from command line
#
# window = QWidget()
# # starting x, starting y, dimensions wide, tall
# # (0,0) top left
# window.setGeometry(50, 50, 500, 300)
# window.setWindowTitle('PyQt Tuts!')
# always have .show for application -- that's how graphic works
# build it first in the background and then show it
# window.show()
# sys.exit(app.exec_())
