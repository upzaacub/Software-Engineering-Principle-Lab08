__author__ = 'Shiraga-P'

import sys

from PySide import QtCore
from PySide import QtGui
from PySide import QtUiTools


class Canvas(QtGui.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pressed = False
        self.points = list()

    def mousePressEvent(self, event):
        self.pressed = True
        self.update()

    def mouseReleaseEvent(self, event):
        self.pressed = False

    def paintEvent(self, event):
        p = QtGui.QPainter(self)
        p.setPen(QtGui.QColor(0, 0, 0))
        p.setBrush(QtGui.QColor(0, 0, 0))

        for point in self.points:
            p.drawRoundedRect(point.x(), point.y(), 20, 20, 20, 20)
            
        if self.pressed == False:
            return
        point = self.mapFromGlobal(QtGui.QCursor.pos())
        self.points.append(point)
        if self.pressed:
            self.update()
        p.end()

    def draw(self, p):
        while self.pressed:
            point = self.mapFromGlobal(QtGui.QCursor.pos())
            p.drawRoundedRect(point.x(), point.y(), 20, 20, 20, 20)



class Paint_window(QtGui.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QtUiTools.QUiLoader(self)
        form = loader.load('form.ui')
        
        self.canvas = Canvas()
        self.gridLayout = form.findChild(QtGui.QGridLayout, 'gridLayout')
        self.gridLayout.addWidget(self.canvas)

        self.pushButton = form.findChild(QtGui.QPushButton, 'pushButton')
        self.pushButton.clicked.connect(self.clearActionListener)

        layout = QtGui.QGridLayout()
        layout.addWidget(form)

        self.setLayout(layout)

        self.setFixedWidth(form.width() + 15)
        self.setFixedHeight(form.height() + 15)
        self.setWindowTitle('Painter')

    def clearActionListener(self):
        self.canvas.points = list()
        self.canvas.update()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Paint_window()
    window.show()
    sys.exit(app.exec_())