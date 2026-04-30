import sys

from PyQt6.QtGui import QColor, QPalette
# el qtgui es orientado para la decoracion
from PyQt6.QtWidgets import QWidget, QApplication,QVBoxLayout, QHBoxLayout, QMainWindow

class CajaColor(QMainWindow):
    def __init__(self, color):
        super().__init__()

        # para dar color de fondo
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        #
        self.setPalette(paleta)

class EjemploBoxLayout (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo con BoxLayout")
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquaMarine"))
        self.setPalette(paleta)

        # ASIGAMOS LA CAJA
        cajaHorizontal = QHBoxLayout()

        cajaV1 = QVBoxLayout()
        cajaV1.addWidget(CajaColor("red"))
        cajaV1.addWidget(CajaColor("yellow"))
        cajaV1.addWidget(CajaColor("white"))

        cajaHorizontal.addLayout(cajaV1)
        cajaHorizontal.addWidget(CajaColor("green"))

        cajaV2 = QVBoxLayout()
        cajaV2.addWidget(CajaColor("red"))
        cajaV2.addWidget(CajaColor("white"))
        cajaHorizontal.addLayout(cajaV2)

        # CAJA  PRINCIPAL
        Contenedor = QWidget()
        Contenedor.setLayout(cajaHorizontal)
        cajaVertical = QVBoxLayout()
        self.setCentralWidget(Contenedor)
        # Para mostrarlo en pantalla . Averiguar docu porque es similar a setvisible
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiesta = EjemploBoxLayout()
    aplicacion.exec()


