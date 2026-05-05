from PyQt6.QtCore import  Qt, QAbstractListModel, QAbstractItemModel

class Modelo_lista(QAbstractListModel):
    def __init__(self, elementos=None): # en principio none por si no se le pasara la lista
        super().__init__()
        self.elementos = elementos or []

    def data(self,indice, rol): # indice es para indicar cual metodo de la lista escojo
        if rol ==Qt.ItemDataRole.DisplayRole:
            return self.elementos[indice.row()]
    def rowCount(self,indice):# row count contar filas
        return len(self.elementos)

