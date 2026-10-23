import sys
import os
from PyQt5 import QtWidgets, uic


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Obtener la ruta absoluta del archivo ventana.ui
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_ui = os.path.join(dir_actual, "ventana.ui")

        # Cargar la interfaz
        try:
            uic.loadUi(ruta_ui, self)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ruta_ui}'")
            sys.exit(1)

        # Configurar el campo de contraseña para que oculte los caracteres (puntos/asteriscos)
        self.campoContrasena.setEchoMode(QtWidgets.QLineEdit.Password)

        # Conectar el clic del botón con el método de validación
        self.botonLogin.clicked.connect(self.validar_login)

        # Permitir iniciar sesión presionando Enter en la contraseña
        self.campoContrasena.returnPressed.connect(self.validar_login)

    def validar_login(self):
        # Obtener los textos de los campos y quitar espacios sobrantes
        usuario = self.campoUsuario.text().strip()
        contrasena = self.campoContrasena.text()

        # Datos de prueba para simular el inicio de sesión
        USUARIO_CORRECTO = "admin"
        CONTRASENA_CORRECTA = "1234"

        # Validación
        if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
            QtWidgets.QMessageBox.information(
                self,
                "Acceso concedido",
                f"¡Bienvenido, {usuario}!\nHas iniciado sesión correctamente."
            )
            # Aquí podrías abrir tu siguiente ventana
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Error de autenticación",
                "Usuario o contraseña incorrectos."
            )
            # Limpiar el campo de contraseña y enfocarlo de nuevo
            self.campoContrasena.clear()
            self.campoContrasena.setFocus()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ventana = LoginWindow()
    ventana.show()
    
    sys.exit(app.exec_())