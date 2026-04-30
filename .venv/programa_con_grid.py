import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QLabel, QWidget, QPushButton, \
    QLineEdit, QPlainTextEdit, QListWidget, QSizePolicy


class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo grid layout")

        malla = QGridLayout()


        boton1 = QPushButton("Botón 1")
        boton2 = QPushButton("Botón 2")
        boton3 = QPushButton("Botón 3")
        boton3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding) # se pone lo mismo para x , y
        boton4 = QPushButton("Botón 4")
        boton5 = QPushButton("Botón 5")
        boton6 = QPushButton("Botón 6")

        lsLista = QListWidget()
        malla.addWidget(boton1,0,0,1,1)
        malla.addWidget(boton2,0,1,1,2) # los dos siguientes es alto y ancho *
        malla.addWidget(boton3,1,0,2,1)
        malla.addWidget(boton4,1,1,1,2)
        malla.addWidget(boton5,2,1,1,1)
        malla.addWidget(boton6,2,2,1,1)

        # Declaramos a malla como contenedor principal
        centralWidget = QWidget()
        centralWidget.setLayout(malla)
        self.setCentralWidget(centralWidget)

        # Para que la ventana sea visible
        self.setVisible(True)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiesta = FiestaPrincipal()
    aplicacion.exec()


# TAREA HACER LO DE ESSEMNTIA DE CUADRO DE COLORES
# TAREA HACER CUADRO EJERCICIO DE INTERFACE LIST BOTONES