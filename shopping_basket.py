import sys
from PyQt4 import QtGui, QtCore

input = [['사이다', 2 , 5000],['콜라', 1, 5000],['새우깡', 2, 5000],['환타', 3, 4000]]


basket = []

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1280, 720)
        self.setWindowTitle("Festival_controller")
        self.setWindowIcon(QtGui.QIcon('inhun_favicon.png'))
        self.home()

    def home(self):
        y = 50

        for i in input:
            for j in i:
                basket.append(j)
            i = str(i)
            print (i)

            btn = QtGui.QPushButton(i, self)
            btn.resize (250, 50)
            btn.move(50,y)
            y = y + 100

        self.show()



app = QtGui.QApplication(sys.argv)
GUI = Window()

print(basket)
sys.exit(app.exec_())
