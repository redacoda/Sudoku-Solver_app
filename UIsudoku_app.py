from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
from code_source_app import * 


ui,_ = loadUiType('UiPyQt.ui')

class MainApp(QMainWindow , ui):
    def __init__(self, parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        # Titre de la fenetre
        self.setWindowTitle("Sudoku Solver")
        
        # Réajustements du tableau
        self.tableWidget.setGeometry(100, 100, 495, 450)
        self.tableWidget.move(40, 30)
        
        for i in range(9):
            self.tableWidget.setColumnWidth(i, 55)
            self.tableWidget.setRowHeight(i, 50)
        
        # Bouton remplissage de tableau lié à sa fonction
        self.pushButton_2.clicked.connect(self.state)

        # Bouton "Go" lié à sa fonction
        self.pushButton.clicked.connect(self.state1)
        
        self.setFixedSize(self.size())
        
    def state(self):
        global L1, L2, L3, L4, L5, L6, L7, L8, L9
        self.label.setText("State : Waiting for the table to be validated")
        self.tableWidget.clearContents()

    def state1(self):    
        
        L1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        L2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        L3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        L4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        L5 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        L6 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        L7 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        L8 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        L9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]  
        
       # Récupération des valeurs dans les cases
        for col in range(9):
            for row in range(9):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    try:
                        value = item.text()
                        ligne = eval(f"L{row+1}")
                        ligne[col] = int(value)
                    except : 
                        pass
                          
        self.label.setText("State : Done !") 
        
        # Bloc de code pour centrer le texte dans toutes les cases
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)
                    
        action(L1, L2, L3, L4, L5, L6, L7, L8, L9)
        
        for row in range(9):
            for col in range(9):
                txt = str(eval(f"L{row + 1}")[col])
                item = QTableWidgetItem(txt)
                self.tableWidget.setItem(row, col, item)
             
               
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
    
    
if __name__ == '__main__':

    main()
