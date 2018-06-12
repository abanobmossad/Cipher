from PyQt5.QtWidgets import QMainWindow, QTableView, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import *


class TableModel(QStandardItemModel):
    def __init__(self):
        super().__init__()

    def setMatrix(self, matrix):

        self.setColumnCount(len(matrix[0]))
        for (i, colHeader) in enumerate(matrix[0]):
            self.setHeaderData(i, Qt.Horizontal, colHeader)

        for (i, row) in enumerate(matrix[1:]):
            self.insertRow(i)
            for (j, cell) in enumerate(row):
                self.setData(self.index(i, j), cell)


def see_table(matrix):
    print('Running test..')


    model.setMatrix(matrix)

    mainlisting = QTableView()
    mainlisting.setSortingEnabled(True)
    mainlisting.setModel(model)
    mainlisting.resizeColumnToContents(True)
    mainlisting.setEditTriggers(QAbstractItemView.NoEditTriggers)
    mainwindow.setCentralWidget(mainlisting)
    for i in range(len(matrix[0])):
        mainlisting.resizeColumnToContents(i)
    mainwindow.show()


# vim: set ts=4 sw=4 ai si expandtab:
