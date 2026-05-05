import sys

from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QGridLayout, QLabel, QListView, QPushButton
from Modelo_lista_Treas import Modelo_lista



class EjemploGridLayout (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo con Grid layout Excel")

        listaElementos = ["Hoja 1", "Hoja 2", "Hoja 3", "Hoja 4", "Hoja 5", "Hoja 6"]
        self.modeloListaVisibles  = Modelo_lista(listaElementos) # para que sea visible la lista
        self.modeloListaOcultas = Modelo_lista()

        labelHojasVisibles = QLabel("Hojas visibles")
        labelHojasOcultas = QLabel("Hojas ocultas")
        self.listWidget_HojasVisibles = QListView()
        self.listWidget_HojasVisibles.setModel(self.modeloListaVisibles)
        self.listWidget_HojasVisibles.setSelectionMode(QListView.SelectionMode.SingleSelection)  # Para seleccionar el modo de seleccion
        botonMostrar = QPushButton("Mostrar")
        self.listWidget_HojasOcultas = QListView()
        self.listWidget_HojasOcultas.setModel(self.modeloListaOcultas)
        self.listWidget_HojasOcultas.setSelectionMode(QListView.SelectionMode.SingleSelection)  # Para seleccionar el modo de seleccion

        botonMostrar = QPushButton("<< Mostrar")
        botonOcultar = QPushButton("Ocultar >>")
        botonOcultar.clicked.connect(self.on_btn_ocultar_clicked)
        botonCerrar = QPushButton("Cerrar")
        Espacio = QWidget()
        Espacio.setFixedSize(10,5)



        # ASIGAMOS LA CAJA
        malla = QGridLayout()
        malla.addWidget(labelHojasVisibles,0,0)
        malla.addWidget(labelHojasOcultas,0,2)
        malla.addWidget(self.listWidget_HojasVisibles,1,0, 5, 1) # dos ultimos son filas ocupadas y columnas ocupadas
        malla.addWidget(botonOcultar,1,1)
        malla.addWidget(botonMostrar,3,1)
        malla.addWidget(self.listWidget_HojasOcultas,1,2,5,1)
        malla.addWidget(Espacio,6,2)
        malla.addWidget(botonCerrar,7,2)



        # Para las medidad de los cuadros derechos sean iguales uso qvbox
        #caixaV = QVBoxLayout()

        # CAJA  PRINCIPAL
        Contenedor = QWidget()
        Contenedor.setLayout(malla)
        self.setCentralWidget(Contenedor)
        # Para mostrarlo en pantalla . Averiguar docu porque es similar a setvisible
        self.show()


    def on_btn_ocultar_clicked(self):
        indices = self.listWidget_HojasVisibles.selectedIndexes()
        if indices:
            self.modeloListaOcultas.elementos.append(self.modeloListaVisibles.elementos.pop(indices[0].row()))
        self.modeloListaVisibles.layoutChanged.emit()
        self.modeloListaOcultas.layoutChanged.emit()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiesta = EjemploGridLayout()
    aplicacion.exec()


