import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QApplication, QHeaderView, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class Coffe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.load_database()

    def load_database(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("coffee.sqlite")
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable("coffee")
        model.select()
        for section, value in enumerate(
            [
                "ID",
                "название сорта",
                "степень обжарки",
                "молотый/в зернах",
                "описание вкуса",
                "цена",
                "объем упаковки",
            ]
        ):
            model.setHeaderData(section, Qt.Horizontal, value)
        self.tableView.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Coffe()
    window.show()
    sys.exit(app.exec())
