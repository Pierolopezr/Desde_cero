import sys
from ctypes.macholib.dylib import dylib_info

# Qt contiene cosas internas de PyQt como constantes y modelos avanzados.
# QAbstractTableModel sirve para crear un "modelo de datos" personalizado para tablas.
from PyQt6.QtCore import Qt, QAbstractTableModel

# Aquí importamos todos los widgets visuales que vamos a usar en la interfaz.
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QLineEdit, QWidget, \
    QGridLayout, QHBoxLayout, QGroupBox, QListWidget, QTabWidget, QCheckBox, QRadioButton, QSlider, QTextEdit, \
    QComboBox, QTableWidget, QTableView


# Aquí creas tu "molde" para los datos, igual que en Java usas interfaces o clases abstractas.
class ModeloTabla(QAbstractTableModel):

    def __init__(self, tabla):
        # Inicializamos la clase padre para que todo funcione correctamente internamente.
        super().__init__()

        # Guardamos los datos que vamos a mostrar en la tabla.
        self.tabla = tabla

    def rowCount(self, index):
        # Devuelve el número de filas que tendrá la tabla.
        return len(self.tabla)

    def columnCount(self, index):
        # Devuelve el número de columnas.
        # Cogemos la primera fila para saber cuántas columnas existen.
        return len(self.tabla[0])

    def data(self, index, role):

        # Esta función se ejecuta constantemente cuando la tabla necesita pintar datos.
        # PyQt le pregunta: "¿Qué tengo que mostrar en esta celda?"

        # Verificamos que el índice exista realmente.
        if index.isValid():

            # DisplayRole significa que solo queremos mostrar texto visualmente.
            if role == Qt.ItemDataRole.DisplayRole:

                # Sacamos el dato usando fila y columna.
                dataGrid = self.tabla[index.row()][index.column()]

                # Devolvemos el dato para que aparezca en pantalla.
                return dataGrid


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Título de la ventana.
        self.setWindowTitle("Nuevo")

        # Tamaño mínimo de la ventana.
        self.setMinimumSize(434, 434)

        # Lista de listas que contiene todos los datos de la tabla.
        self.datos = [['Nombre', 'Dni', 'Género', 'Fallecido'],
                      ['Ana', '1234R', 'Femenino', 'True'],
                      ['Pedro', '5678P', 'Masculino', 'False'],
                      ['Luis', '91011L', 'Masculino', 'False']]

        # Layout tipo rejilla.
        # Permite colocar widgets usando filas y columnas.
        self.grid = QGridLayout()

        # Caja vertical.
        # Coloca widgets uno debajo de otro.
        self.vBox = QVBoxLayout()

        # Caja horizontal.
        # Coloca widgets uno al lado del otro.
        self.hBox = QHBoxLayout()

        # Metemos la caja vertical dentro del grid.
        self.grid.addLayout(self.vBox, 3, 0, -1, -1)

        # Etiquetas de texto.
        self.nombre = QLabel("Nombre")
        self.dni = QLabel("DNI")
        self.genero = QLabel("Género")
        self.fallecido = QLabel("Fallecido")

        # Cuadros de texto.
        self.nomEnt = QLineEdit()
        self.dniEnt = QLineEdit()

        # ComboBox = desplegable de opciones.
        self.generoEnt = QComboBox()

        # Lista de opciones para el ComboBox.
        self.cmbGenero = ['Indefinido', 'Masculino', 'Femenino', 'Otro']

        # Añadimos todas las opciones al desplegable.
        self.generoEnt.addItems(self.cmbGenero)

        # Checkbox = casilla de verdadero/falso.
        self.fallecidoEnt = QCheckBox()

        # Añadimos widgets al grid indicando:
        # fila, columna
        self.grid.addWidget(self.nombre, 0, 0)
        self.grid.addWidget(self.nomEnt, 0, 1)

        self.grid.addWidget(self.dni, 0, 2)
        self.grid.addWidget(self.dniEnt, 0, 3)

        self.grid.addWidget(self.genero, 1, 0)
        self.grid.addWidget(self.generoEnt, 1, 1)

        self.grid.addWidget(self.fallecido, 1, 2)
        self.grid.addWidget(self.fallecidoEnt, 1, 3)

        # Añadimos la caja horizontal al grid.
        self.grid.addLayout(self.hBox, 2, 0, 1, -1)

        # Botones.
        self.bot1 = QPushButton("Añadir")
        self.bot1.pressed.connect(self.on_botonAnadir_presionado)
        self.bot2 = QPushButton("Modificar")
        self.bot2.pressed.connect(self.on_botonEditar_presionado)
        self.bot3 = QPushButton("Aceptar")
        self.bot3.pressed.connect(self.on_botonAceptar_presionado)
        self.bot4 = QPushButton("Cancelar")
        self.bot4.pressed.connect(self.on_botonCancelar_presionado)

        # Desabilitar controles
        self.desabilitarControles()

        # Metemos los botones dentro de la caja horizontal.
        self.hBox.addWidget(self.bot1)
        self.hBox.addWidget(self.bot2)
        self.hBox.addWidget(self.bot3)
        self.hBox.addWidget(self.bot4)

        # QTableView muestra datos usando un modelo personalizado.
        self.tView = QTableView()

        # Creamos el modelo y le pasamos los datos.
        self.modelo = ModeloTabla(self.datos)

        # Asociamos el modelo a la tabla visual.
        self.tView.setModel(self.modelo)

        # Añadimos la tabla a la caja vertical.
        self.vBox.addWidget(self.tView)

        # Widget contenedor principal.
        # Los layouts necesitan estar dentro de un QWidget.
        self.container = QWidget()

        # Asignamos el layout principal al contenedor.
        self.container.setLayout(self.grid)

        # Convertimos el contenedor en el contenido central de la ventana.
        self.setCentralWidget(self.container)

        # Mostramos la ventana.
        self.show()



    def addData(self):

        # Recogemos el texto escrito en los inputs.
        nombre = self.nomEnt.text()
        dni = self.dniEnt.text()

    def on_botonAnadir_presionado(self):
        self.limpiarControles()
        self.habilitarControles()
        self.bot1.setEnabled(False)
        self.bot2.setEnabled(False)

    def on_botonCancelar_presionado(self):
        self.limpiarControles()
        self.desabilitarControles()
        self.bot1.setEnabled(True)
        self.bot2.setEnabled(True)

    def on_botonEditar_presionado(self):

        # Obtenemos los índices de la tabla seleccionados por el usuario.
        # Devuelve una lista de celdas seleccionadas.
        indices = self.tView.selectedIndexes()

        # Si hay algo seleccionado (evitamos errores si no se selecciona nada).
        if indices:

            # Activamos los controles para poder editar los datos.
            self.habilitarControles()

            # Deshabilitamos botones de añadir y modificar para evitar conflictos.
            self.bot1.setEnabled(False)
            self.bot2.setEnabled(False)

            # Guardamos la fila seleccionada (solo usamos la primera celda seleccionada).
            fila = indices[0].row()

            # Rellenamos el campo nombre con el valor de la columna 0.
            self.nomEnt.setText(self.modelo.tabla[fila][0])

            # Rellenamos el campo DNI con la columna 1.
            self.dniEnt.setText(self.modelo.tabla[fila][1])

            # Según el valor del género, seleccionamos el índice correcto del ComboBox.
            # Esto permite sincronizar el valor de la tabla con el desplegable.
            match self.modelo.tabla[fila][2]:

                case "Indefinido":
                    self.generoEnt.setCurrentIndex(0)

                case "Masculino":
                    self.generoEnt.setCurrentIndex(1)

                case "Femenino":
                    self.generoEnt.setCurrentIndex(2)

                case "Otro":
                    self.generoEnt.setCurrentIndex(3)

            # Comprobamos si el campo fallecido es True o False.
            # IMPORTANTE: aquí comparas con string "True" porque tus datos iniciales son texto.
            if self.modelo.tabla[fila][3] == "True":

                # Marcamos el checkbox si está como "True"
                self.fallecidoEnt.setChecked(True)

            else:

                # Desmarcamos el checkbox si no es "True"
                self.fallecidoEnt.setChecked(False)
    def on_botonAceptar_presionado (self):

        novoRexistro = (self.nomEnt.text(), self.dniEnt.text(), self.generoEnt.currentText(), self.fallecidoEnt.isChecked())
        self.modelo.tabla.append(novoRexistro)
        self.modelo.layoutChanged.emit()
        self.on_botonCancelar_presionado()

    def desabilitarControles (self):
        self.nomEnt.setEnabled(False)
        self.dniEnt.setEnabled(False)
        self.generoEnt.setEnabled(False)
        self.fallecidoEnt.setEnabled(False)
        self.bot3.setEnabled(False)
        self.bot4.setEnabled(False)

    def habilitarControles (self):
        self.nomEnt.setEnabled(True)
        self.dniEnt.setEnabled(True)
        self.generoEnt.setEnabled(True)
        self.fallecidoEnt.setEnabled(True)
        self.bot3.setEnabled(True)
        self.bot4.setEnabled(True)

    def limpiarControles (self):
        self.nomEnt.setText("")
        self.dniEnt.setText("")
        self.generoEnt.setCurrentIndex(-1)
        self.fallecidoEnt.setChecked(True)



# Punto de entrada principal del programa.
if __name__ == '__main__':

    # QApplication es obligatoria en cualquier aplicación PyQt.
    # Gestiona eventos, ventanas y funcionamiento interno.
    app = QApplication(sys.argv)

    # Creamos nuestra ventana.
    window = MainWindow()

    # Ejecutamos el bucle infinito de la aplicación.
    app.exec()

    # comentar el puto codigo