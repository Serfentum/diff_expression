import sys
import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMainWindow, QInputDialog, QLineEdit
from PyQt5 import QtGui
from geo import geo_load
from kolmogorov_smirnov import different_expression


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.geo, self.genes, self.p_value = self.initUI()

    def initUI(self):
        # Button creation
        # accept = QPushButton('Ok', self)

        # Text upon hover on button
        # accept.setToolTip('This is a <b>QPushButton</b> widget')

        # Specify size
        # accept.resize(accept.sizeHint())
        # Button place
        # accept.move(50, 50)
        # Create event for button - close upon click
        # accept.clicked.connect(self.close)

        # accept.clicked.connect(self.getText())



        # Text box
        # edit = qtw.QLineEdit(self)
        # edit.move(50, 10)
        # edit.resize(accept.sizeHint())



        # Size of window, title
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('MyFirstWindow')

        self.show()
        title = 'Differential Expression'

        geo, okPressed = QInputDialog.getText(self, title, 'Geo id', QLineEdit.Normal, '')
        genes, okPressed = QInputDialog.getText(self, title, 'Path to file with genes', QLineEdit.Normal, '')
        p_value, okPressed = QInputDialog.getDouble(self, title, 'p-value threshold', 0.05, 0, 1, 5)

        if not all((geo, genes, p_value)):
            raise ValueError('You didn\'t specify some arguments')
        self.close()
        return geo, genes, p_value





def main():
    app = QApplication(sys.argv)
    ex = MyWindow()

    expression = geo_load(ex.geo)
    different_expression(expression, ex.genes, ex.p_value)



if __name__ == '__main__':
    main()