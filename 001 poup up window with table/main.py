import sys

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import Qt
from main_form import Ui_Form
from children_form import  Ui_Form as ChildrenForm
from PyQt5.QtCore import Qt


class Main_Form(QWidget):
    def __init__(self):
        print("start Main Form")
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.show_window)
        
        self.year = self.ui.label.text()
        self.client = self.ui.label_2.text()
        self.salehouse = self.ui.label_3.text()
        self.table = self.ui.tableWidget
        
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name', 'Wartość', 'Guzik'])
        values = ['jeden', 'dwa', 'trzy']
        self.ui.pushButton_add.clicked.connect(lambda: self.add_schurges(values))
        
    def show_window(self):
        self.children = Children_Form(self.year, self.client, self.salehouse, self)
        self.children.show()
        
    def add_schurges(self, schurges):
        print("add schurge")
        for schurge in schurges:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            item = QTableWidgetItem(schurge)
            self.table.setItem(row_position, 0, item)
        
        
class Children_Form(QWidget):
    def __init__(self, year, client, salehoue, parent=None):
        super(Children_Form, self).__init__(parent)
        self.ui = ChildrenForm()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlag(Qt.Window)
        
        self.ui.label.setText(year)
        self.ui.label_2.setText(client)
        self.ui.label_3.setText(salehoue)
        
        self.list_view = self.ui.listView
        
        surcharges = ["drugi reklamodawca", "duo spot", "wyłączność w bloku"]
        self.model = QStandardItemModel(self.list_view)
        self.add_surcharges(surcharges)
        self.ui.pushButton.clicked.connect(lambda: self.add_surcharges([self.ui.lineEdit.text()]))
        self.ui.pushButton_remove.clicked.connect(self.remove_surcharge)
        self.ui.buttonBox.accepted.connect(self.send_surcharge)
        self.partner = parent
        #self.show()
        
    def add_surcharges(self, surcharges):
        for surcharge in surcharges:
            item = QStandardItem(surcharge)
            item.setCheckable(True)
            self.model.appendRow(item)
        
        self.list_view.setModel(self.model)
        
    def send_surcharge(self):
        print("send_surcharge")
        i = 0
        items = []
        while self.model.item(i):
            if self.model.item(i).checkState():
                items.append(self.model.item(i).text())
            i += 1
        print(type(self.partner))
        self.partner.add_schurges(items)
        
        self.close()
    
    def remove_surcharge(self):
        i = 0
        while self.model.item(i):
            if self.model.item(i).checkState():
                self.model.removeRow(i)
            i += 1
    
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main_Form()
    w.show()
    sys.exit(app.exec_())