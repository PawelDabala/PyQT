import sys

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem, QTableWidgetItem, QDialog
from PyQt5.QtCore import Qt
from table import Ui_Dialog

from PyQt5.QtCore import Qt


class Main_Form(QDialog):
    def __init__(self):
        print("start Main Form")
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.tab = ManageTab(self.ui.tableWidget,2,3)
        self.tab.setColumnHidden(1, True)



class ManageTab:
    def __init__(self, tab, row=0, col=0):
        self.tab = tab
        self.tab.setRowCount(row)
        self.tab.setColumnCount(col)

    def add_remove_but(self, row, col):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main_Form()
    w.show()
    sys.exit(app.exec_())