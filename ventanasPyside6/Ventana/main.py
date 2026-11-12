import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ventanaLogin import Ui_MainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Login")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.ir_a_ventana_principal)

    def ir_a_ventana_principal(self):
        usuario = self.ui.leUsuario.text()
        contraseña = self.ui.leContrasena.text()

        if usuario == "" or contraseña == "":
            print("Por favor introduce tus datos")
            return


        if usuario == "admin" and contraseña == "1234":
            self.ventana_principal = VentanaPrincipal()
            self.ventana_principal.show()

            self.close()
        
        else:
            print("Usuario o contraseña incorrectos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_login = LoginWindow()
    ventana_login.show()
    sys.exit(app.exec())