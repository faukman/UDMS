import sys
from PyQt5 import QtWidgets
from structures import MainWindow

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.username = QtWidgets.QLineEdit(self)
        self.password = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.username.text() == 'a' and
            self.password.text() == 'a'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self,'Error','Bad user or password')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
