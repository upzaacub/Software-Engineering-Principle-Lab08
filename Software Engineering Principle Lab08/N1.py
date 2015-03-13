
import sys
from PySide import QtCore, QtGui

class Simple_drawing_window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QtGui.QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QtGui.QPainter()
        p.begin(self)

        p.setPen(QtGui.QColor(0, 0, 0))
        p.setBrush(QtGui.QColor(0, 127, 0))
        p.drawPolygon([
            QtCore.QPoint(70, 100), QtCore.QPoint(100, 110),
            QtCore.QPoint(130, 100), QtCore.QPoint(100, 150),
       ])

        p.setPen(QtGui.QColor(255, 127, 0))
        p.setBrush(QtGui.QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
            QtCore.QPoint(50, 200), QtCore.QPoint(150, 200), QtCore.QPoint(100, 400),
        ])

        p.drawImage(QtCore.QRect(200, 100, 320, 320), self.rabbit)


class Simple_drawing_window3(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QtGui.QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QtGui.QPainter()
        p.begin(self)

        p.drawPolygon([
            QtCore.QPoint(50, 200), QtCore.QPoint(150, 200), QtCore.QPoint(100, 400),
        ])

        p.drawImage(QtCore.QRect(200, 100, 320, 320), self.rabbit)

    

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Simple_drawing_window()
    window.show()
    sys.exit(app.exec_())