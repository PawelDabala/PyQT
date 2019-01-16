import sys

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog, QPushButton, QTableWidget
from PyQt5.QtCore import Qt
from master_form import Ui_Dialog
from PyQt5.QtCore import Qt
from base import Session, engine
from sqlalchemy import update
from client import  Client


class Main_Form(QDialog):
    def __init__(self):
        print("start Main Form")
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.tab = self.ui.tableView
        self.lin_edi = self.ui.lineEdit_add
        self.add_but = self.ui.pushButton_add
        
        session = Session()
        mt = MasterTableView(self.tab,
                             4,
                             ['id', 'name', '', ''],
                             session,
                             Client,
                             {'1': 'name'})
        self.add_but.clicked.connect(lambda: self.add_value(session, mt))
        
        #odcztyt z bazy
        clients = session.query(Client).all()
        for client in clients:
            values = {
                "0": f"{client.id}",
                "1": f"{client.name}"
            }
            mt.add_row(values, (0, 1), 2, 3, 1)
            
    def add_value(self, session, mt):
        client = Client(self.lin_edi.text())
        session.add(client)
        session.flush()
        session.commit()
        values = {
            "0": f"{client.id}",
            "1": f"{client.name}"
        }
        mt.add_row(values, (0, 1), 2, 3, 1)
        

class MasterTableView:

    def __init__(self, tab, col_nr, hd_name, session=None, tab_name=None, columns=None):
        """
        :param tab: tableView
        :param col_nr: columns where set strings
        :param hd_name: headers name
        :param session: session database
        :param tab_name: table name
        """
        self.tab = tab
        self.col_nr = col_nr
        self.hd_name = hd_name
        self.stim = QStandardItemModel()
        self.col_block = None
        self.session = session
        self.tab_name = tab_name
        self.columns = columns
        self.set_tab()
        
    def set_tab(self):
        self.stim.setColumnCount(self.col_nr)
        self.stim.setHorizontalHeaderLabels(self.hd_name)
        self.tab.setModel(self.stim)
        
    def add_row(self, values, col_block, bt_edit=None, bt_remove=None, chec_box=-1):
        self.col_block = col_block
        row_count = self.stim.rowCount()
        for key, value in values.items():
            item = QStandardItem(value)
            if int(key) == chec_box:
                item.setCheckable(True)
            if int(key) in self.col_block:
                item.setEditable(False)
            self.stim.setItem(row_count, int(key), item)
            
        if bt_edit:
            but1 = QPushButton('Edycja')
            but1.clicked.connect(lambda: self.edit_cells(but1))
            self.tab.setIndexWidget(self.stim.index(row_count, bt_edit), but1)
            
        if bt_remove:
            but2 = QPushButton('Usuń')
            but2.clicked.connect(lambda: self.remove_row(but2))
            self.tab.setIndexWidget(self.stim.index(row_count, bt_remove), but2)
            
    def remove_row(self, but):
        index = self.tab.indexAt(but.pos())
        """
        database access
        """
        if self.session:
            idnr = self.stim.item(index.row(), 0).text()
            self.session.query(self.tab_name).filter(self.tab_name.id == idnr).delete()
            self.session.commit()
        if index.isValid():
            self.stim.removeRow(index.row())
            
        
            
    def edit_cells(self, but):
        """
        :param but:
        """
        index = self.tab.indexAt(but.pos())
        if index.isValid():
            for i in self.col_block:
                item = self.stim.item(index.row(), i)
                item.setEditable(True)
            but.setText("Zapisz")
            but.clicked.connect(lambda: self.save_cell(but))
    
    def save_cell(self, but):
        but.setText("Edycja")
        but.clicked.connect(lambda: self.edit_cells(but))
        index = self.tab.indexAt(but.pos())
        
        idnr = self.stim.item(index.row(), 0).text()
        form_val = {}
        for key, val in self.columns.items():
            form_val[val] = self.stim.item(index.row(), int(key)).text()
        stm = update(self.tab_name).where(self.tab_name.id == idnr).values(**form_val)
        engine.execute(stm)
        if index.isValid():
            
            for i in self.col_block:
                item = self.stim.item(index.row(), i)
                item.setEditable(False)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main_Form()
    w.show()
    sys.exit(app.exec_())