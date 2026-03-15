"""
Nama    : Syazwani
NIM     : F1F02310140
Kelas   : D

TUGAS 3 - Login Form
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QLineEdit, QVBoxLayout, QHBoxLayout, QCheckBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("Login")
        self.resize(400, 450)
        
        self.judul_label = QLabel("LOGIN")
        self.judul_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.judul_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
            background-color: #6a1b9a;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        """)
        
        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet("font-size: 12px; margin-top: 10px;")
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Masukkan username")
        self.username_input.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            margin-bottom: 15px;
        """)
        self.username_input.textChanged.connect(self.reset_input_style)
        
        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("font-size: 12px;")
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Masukkan password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            margin-bottom: 5px;
        """)
        self.password_input.textChanged.connect(self.reset_input_style)
        
        self.tampilkan_password_checkbox = QCheckBox("Tampilkan Password")
        self.tampilkan_password_checkbox.setStyleSheet("font-size: 12px; margin-bottom: 15px;")
        self.tampilkan_password_checkbox.stateChanged.connect(self.toggle_password_visibility)
        
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                font-size: 14px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.login_button.clicked.connect(self.login)
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                font-size: 14px;
                background-color: #95a5a6;
                color: white;
                border: none;
                border-radius: 5px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        self.reset_button.clicked.connect(self.reset_form)
        
        button_layout.addStretch()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.reset_button)
        button_layout.addStretch()
        
        self.hasil_label = QLabel("")
        self.hasil_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hasil_label.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            padding: 15px;
            background-color: #f9f9f9;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            margin-top: 20px;
            min-height: 40px;
        """)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        main_layout.setContentsMargins(40, 20, 40, 20)
        
        main_layout.addWidget(self.judul_label)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.username_label)
        main_layout.addWidget(self.username_input)
        main_layout.addWidget(self.password_label)
        main_layout.addWidget(self.password_input)
        main_layout.addWidget(self.tampilkan_password_checkbox)
        main_layout.addSpacing(10)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.hasil_label)
        main_layout.addStretch()
        
        self.setLayout(main_layout)
        
        self.username_input.setFocus()
    
    def toggle_password_visibility(self, state):
        """Menampilkan atau menyembunyikan password"""
        if state == Qt.CheckState.Checked.value:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    
    def reset_input_style(self):
        """Mengembalikan style input ke warna default"""
        self.username_input.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            margin-bottom: 15px;
        """)
        self.password_input.setStyleSheet("""
            padding: 10px;
            font-size: 14px;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
            margin-bottom: 5px;
        """)
    
    def login(self):
        """Memvalidasi login"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        self.reset_input_style()
        
        if username == "admin" and password == "12345":
            self.hasil_label.setText("Login berhasil! Selamat datang, admin.")
            self.hasil_label.setStyleSheet("""
                font-size: 14px;
                font-weight: bold;
                color: #27ae60;
                padding: 15px;
                background-color: #e8f5e9;
                border: 2px solid #27ae60;
                border-radius: 5px;
                margin-top: 20px;
                min-height: 40px;
            """)
            
            self.username_input.setStyleSheet("""
                padding: 10px;
                font-size: 14px;
                border: 2px solid #27ae60;
                border-radius: 5px;
                margin-bottom: 15px;
            """)
            self.password_input.setStyleSheet("""
                padding: 10px;
                font-size: 14px;
                border: 2px solid #27ae60;
                border-radius: 5px;
                margin-bottom: 5px;
            """)
        else:
            self.hasil_label.setText("Login gagal! Username atau password salah.")
            self.hasil_label.setStyleSheet("""
                font-size: 14px;
                font-weight: bold;
                color: #c0392b;
                padding: 15px;
                background-color: #fdedec;
                border: 2px solid #c0392b;
                border-radius: 5px;
                margin-top: 20px;
                min-height: 40px;
            """)
            
            self.username_input.setStyleSheet("""
                padding: 10px;
                font-size: 14px;
                border: 2px solid #c0392b;
                border-radius: 5px;
                margin-bottom: 15px;
            """)
            self.password_input.setStyleSheet("""
                padding: 10px;
                font-size: 14px;
                border: 2px solid #c0392b;
                border-radius: 5px;
                margin-bottom: 5px;
            """)
    
    def reset_form(self):
        """Mengosongkan form input dan label hasil"""
        self.username_input.clear()
        self.password_input.clear()
        self.hasil_label.setText("")
        self.reset_input_style()
        self.hasil_label.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            padding: 15px;
            background-color: #f9f9f9;
            border: 1px solid #bdc3c7;
            border-radius: 5px;
            margin-top: 20px;
            min-height: 40px;
        """)
        self.username_input.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())