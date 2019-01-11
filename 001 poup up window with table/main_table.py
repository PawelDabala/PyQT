import sys

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem, QTableWidgetItem

from table import Ui_Form



class Mian_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.table = self.ui.tableWidget
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['jeden', 'dwa', 'trzy'])
        
        self.ui.pushButton.clicked.connect(self.add)
        
    def add(self):
        values = ['Jeden', 'Dwa', 'Trzy']
        for value in values:
            rowcount = self.table.rowCount()
            self.table.insertRow(rowcount)
            item = QTableWidgetItem(value)
            self.table.setItem(rowcount,0, item)
            
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mian_Form()
    w.show()
    sys.exit(app.exec_())