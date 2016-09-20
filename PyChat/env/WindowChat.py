import PyQt5.QtWidgets as qtWidget

class WindowChat(qtWidget.QWidget):

    #Window manager
    _windowManager = ""

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        qbtn = qtWidget.QPushButton('Quit', self)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()    


        
    def quit(self):
        sys.exit()