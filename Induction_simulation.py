from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random
import math
import sys



ScreenSize = (1920, 1080)


 
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt paint - pythonspot.com'
        self.left = 0
        self.top = 100
        self.width = ScreenSize[0]
        self.height = ScreenSize[1]
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
 
        self.paintwidget = PaintWidget(self)
        self.paintwidget.move(0,0)
        self.paintwidget.resize(self.width,self.height)
 
        self.show()

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qpainter = QPainter(self)
        
        for xpix in range(ScreenSize[0]):
            for ypix in range(ScreenSize[1]):
                qpainter.setPen(Getcolor(xpix, ypix))
                qpainter.drawPoint(xpix, ypix)
                
                
                
def alpha(arg):
    return math.sin(arg)


                
def Getcolor(xpix, ypix):
    intensivity = 1 / (xpix / ScreenSize[0] + 1)
    
    R = (1 + alpha(intensivity * math.pi - math.pi / 3)) * 0.6
    G = (
        (1 + alpha(intensivity * math.pi * 1.5))         * 0.7 +
        (1 + alpha(intensivity * math.pi - math.pi / 3)) * 0.3
    )
    B = (1 + alpha(intensivity * math.pi / 2 + math.pi / 2)) * 1
        
    maximum = max([R, G, B])
    R /= maximum
    G /= maximum
    B /= maximum
    R *= 255
    G *= 255
    B *= 255
    
    return QColor(R, G, B)
 
 
 
try:
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())
except Exception as exc:
    input(exc)