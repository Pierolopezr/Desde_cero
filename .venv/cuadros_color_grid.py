import sys

from PyQt6.QtGui import QColor, QPalette
# el qtgui es orientado para la decoracion
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QMainWindow, QGridLayout


class CajaColor(QMainWindow):
    def __init__(self, color):
        super().__init__()

        # para dar color de fondo
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        #
        self.setPalette(paleta)

class EjemploGridLayout (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo con BoxLayout")
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquaMarine"))
        self.setPalette(paleta)

        cajaAzul = CajaColor("blue")
        cajaVerde = CajaColor("green")
        cajaRosa = CajaColor("pink")
        cajaAmarillo = CajaColor("yellow")
        cajaMorado = CajaColor("purple")
        cajaGris = CajaColor("grey")

        # ASIGAMOS LA CAJA
        malla = QGridLayout()

        malla.addWidget(cajaAzul,0,0,1,1)
        malla.addWidget(cajaVerde,1,0,1,1)
        malla.addWidget(cajaRosa,2,0,1,1)
        malla.addWidget(cajaAmarillo,0,1,3,1)
      #  malla.addWidget(cajaMorado,0,2,2,1)
      #  malla.addWidget(cajaGris,2,2,1,1)

        # Para las medidad de los cuadros derechos sean iguales uso qvbox
        caixaV = QVBoxLayout()
        caixaV.addWidget(cajaMorado)
        caixaV.addWidget(cajaGris)
        malla.addLayout(caixaV, 0, 2, 3, 1)

        # CAJA  PRINCIPAL
        Contenedor = QWidget()
        Contenedor.setLayout(malla)
        self.setCentralWidget(Contenedor)
        # Para mostrarlo en pantalla . Averiguar docu porque es similar a setvisible
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiesta = EjemploGridLayout()
    aplicacion.exec()


