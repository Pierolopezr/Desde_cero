import sys
# sys.argv permite que la aplicación PyQt reciba argumentos del sistema operativo, como hacen las aplicaciones gráficas reales.
# Aunque no pases argumentos, PyQt espera esa lista para inicializarse correctamente.
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton, QLineEdit, QPlainTextEdit
# Instalar en python interpreter en ajustes "pyqt6"

class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicacion saludo")

        # Dimensiones de la ventana al ejecutar
        self.setGeometry(300, 300, 300, 300)
        # Dimensiones pantalla completa
        #pantalla = QApplication.primaryScreen() # obtiene la pantalla principal del sistema
        #tamanoPantalla = pantalla.availableGeometry() # Devuelve un rectángulo (QRect) con el área disponible de la pantalla
        #self.setGeometry(tamanoPantalla) # Le pasas directamente ese rectángulo a la ventana

        # Crea una caja vertical vacía, donde QBOXLAYOUT coloca los widgets uno debajo de otro (verticalmente)
        cajaVertical = QVBoxLayout()

        # Texto
        self.NAsaludo = QLabel("Hola mundo") # convertimos en propiedades self. para poder trabajar en la clase de clickeado
        cajaVertical.addWidget(self.NAsaludo)

        # Cuadro de texto
        self.CuadroTexto = QLineEdit()
        self.CuadroTexto.setPlaceholderText("Introduce tu nombre") # Colocar texto como marca de agua dentro del cuadro
        cajaVertical.addWidget(self.CuadroTexto) # no importa el orden donde lo pongas puede ser después del enter o antes.
        # Tecla 'Enter' dentro de Cuadro de texto
        self.CuadroTexto.returnPressed.connect(self.presionado_cuadroTexto_enter) # el returnPressed es una señal propia de QLineEdit
                                                                            # Se dispara cuando el usuario pulsa la tecla Enter mientras el foco está en ese cuadro de texto.

        # Botón
        botonSaludar = QPushButton("Saludar")
        botonSaludar.clicked.connect(self.botonsaludar_clickeado) # si se presiona el botón , se ejecuta el metodo
        cajaVertical.addWidget(botonSaludar)

        # Diseño principal
        contenedor = QWidget()
        contenedor.setLayout(cajaVertical)
        self.setCentralWidget(contenedor)

        #Para que la ventana sea visible
        self.setVisible(True)

    # Si presionamos el botón pasa esto:
    def saludoPersonalizado(self):
        nome = self.CuadroTexto.text()
        if nome != "":
            self.NAsaludo.setText("Hola " + nome + ". Encantado de saludarte")

    def presionado_cuadroTexto_enter(self):
        self.saludoPersonalizado()

    def botonsaludar_clickeado(self):
        self.saludoPersonalizado()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiesta = FiestaPrincipal()
    aplicacion.exec()