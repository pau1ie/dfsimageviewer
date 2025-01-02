import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QPushButton
from dfs import Ui_MainWindow
from dfile import fileContents
from model import Model

class MainWindowUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = Model()

    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)

    def refreshAll(self):
        self.Filename.setText(self.model.getFileName())
        self.Title.setText(self.model.getTitle())
        self.Writes.setText(str(self.model.getWrites()))
        self.Size.setText(str(self.model.getSize())+'k')
        self.BootOption.setText(str(self.model.getBootOption()))
        self.refreshCatalogue()
        
    def refreshCatalogue(self):
        self.catalogue.setRowCount(0)
        for i in range(len(self.model.ifileName)):
            if (self.model.ilength[i]>0):
                rowPos = self.catalogue.rowCount()
                self.catalogue.insertRow(rowPos)
                self.catalogue.setItem(rowPos,0,QTableWidgetItem(self.model.idir[i]))
                self.catalogue.setItem(rowPos,1,QTableWidgetItem(self.model.ifileName[i]))
                self.catalogue.setItem(rowPos,2,QTableWidgetItem(hex(self.model.iloadAddress[i])))
                self.catalogue.setItem(rowPos,3,QTableWidgetItem(hex(self.model.iexecAddress[i])))
                self.catalogue.setItem(rowPos,4,QTableWidgetItem(hex(self.model.ilength[i])))
                self.catalogue.setItem(rowPos,5,QTableWidgetItem(hex(self.model.ilocked[i])))
                btn=QPushButton(text="Display", clicked=self.displayFile)
                self.catalogue.setCellWidget(rowPos,7,btn)

    @QtCore.pyqtSlot()
    def browseSlot( self ):
        ''' Called when the user presses the Browse button
        '''
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Single Sided Disc (*.ssd)",
                        options=options)
        if fileName:
            self.model.setFileName( fileName )
            self.refreshAll()

    @QtCore.pyqtSlot()
    def displayFile( self ):
        button = self.sender()
        index = self.catalogue.indexAt(button.pos())
        if index.isValid():
            print(index.row())
            self.filec=fileContents()
            self.filec.refreshAll(self.model.getFileEntry(index.row()))
            self.filec.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindowUI()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__': main()
