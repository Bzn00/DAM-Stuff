import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ventanaPrincipal import Ui_MainWindow
from PySide6.QtGui import QIcon

class Ventana(QMainWindow):

        

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.botonIntroducirTarea.clicked.connect(self.introducirTareas)
        self.setWindowTitle("Mi app")
        self.setWindowIcon(QIcon("C:\\Users\\PC GAMER\\Documents\\VSCode\\ventanasPyside6\\Icon\\SORAKAxAHRI.ico"))
        
    def introducirTareas(self):
        texto = self.ui.campoIntroducirTarea.text()
        self.ui.listaTareas.addItem(texto)
        self.ui.campoIntroducirTarea.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventanaPrincipal = Ventana()
    ventanaPrincipal.show()
    sys.exit(app.exec())
