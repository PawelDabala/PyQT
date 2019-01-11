import sys

from PyQt5.QtCore import QItemSelectionModel
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, \
    QLineEdit, QTableWidget, QMessageBox

from untitled import *
from PyQt5.Qt import Qt


class Mian_Form(QDialog):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800,200)
        qbox = QHBoxLayout()
        self.but = QPushButton()
        
        self.table = QTableWidget()
        self.table.setMinimumSize(600,200)
        self.table.setRowCount(3)
        self.table.setColumnCount(4)
        self.table.itemChanged.connect(self.multipli_row_valu)
        
        self.line_edi = QLineEdit()
        self.line_edi.textChanged.connect(lambda: self.mulitiply_value("jedne"))
        self.but.clicked.connect(self.set_focus)
        #but.clicked.connect(self.get_value)
        qbox.addWidget(self.line_edi)
        qbox.addWidget(self.but)
        qbox.addWidget(self.table)
        self.setLayout(qbox)

    def set_focus(self):
        QMessageBox.critical(self, 'Uwaga!!!',
                             "Podana nazwa już istnieje.\nKliknij 'Nie' jeżeli chcesz podać nową nazwę. 'Tak' jeżeli chcesz nadpisać istniejącą nazwę",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        self.table.setCurrentCell(1, 1)
        self.table.editItem(self.table.item(1, 1))
        
    def mulitiply_value(self, par):
        print(par)
        text_li = self.line_edi.text()
        try:
            text_li = text_li.replace(",", ".")
            num = float(text_li)
        except ValueError:
            return
            
        for i in range(self.table.columnCount()):
            if self.table.item(0, i) is not None:
                try:
                    cell_text = self.table.item(0, i).text()
                    cell_text.replace(",", ".")
                    valu = float(cell_text)
                except ValueError:
                    print(f"Wartość w kolumnie {i+1} nie jest liczbą")
                    break
                item = QTableWidgetItem()
                item.setText(str(valu * num))
                self.table.setItem(1, i, item)
    
    def multipli_row_valu(self, item):
        print(item.row(), item.column())
        if item.row() == 0:
            try:
                val_row1 = float(item.text().replace(",", "."))
            except ValueError:
                print("wartosc w komurce nie jest liczbą")
                return
            try:
                val_line = float(self.line_edi.text().replace(",", "."))
            except ValueError:
                print("wartosc w polu nie jest liczbą")
                return

            new_item = QTableWidgetItem()
            new_item.setText(str(val_row1 * val_line))
            self.table.setItem(1, item.column(), new_item)
    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mian_Form()
    w.show()
    sys.exit(app.exec_())
