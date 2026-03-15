"""
Nama    : Syazwani
NIM     : F1F02310140
Kelas   : D

TUGAS 2 - Konversi Suhu
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class KonversiSuhuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.resize(450, 400)
        
        self.judul_label = QLabel("KONVERSI SUHU")
        self.judul_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.judul_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
            padding: 15px;
            background-color: #3498db;
            border-radius: 8px;
            margin-bottom: 15px;
        """)
        
        self.input_label = QLabel("Masukkan Suhu (Celsius):")
        self.input_label.setStyleSheet("font-size: 14px; margin-top: 10px;")

        self.input_suhu = QLineEdit()
        self.input_suhu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_suhu.setStyleSheet("""
            padding: 12px;
            font-size: 14px;
            border: 2px solid #3498db;
            border-radius: 5px;
            margin-bottom: 20px;
            min-width: 400px;
        """)
        self.input_suhu.setMinimumWidth(400)

        regex = QRegularExpression("^-?\\d*\\.?\\d*$")
        validator = QRegularExpressionValidator(regex)
        self.input_suhu.setValidator(validator)

        input_layout = QHBoxLayout()
        input_layout.addStretch()
        input_layout.addWidget(self.input_suhu)
        input_layout.addStretch()
     
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)
        
        self.tombol_fahrenheit = QPushButton("Fahrenheit")
        self.tombol_fahrenheit.setStyleSheet("""
            QPushButton {
                padding: 12px 15px;
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
        self.tombol_fahrenheit.clicked.connect(self.konversi_ke_fahrenheit)
        
        self.tombol_kelvin = QPushButton("Kelvin")
        self.tombol_kelvin.setStyleSheet("""
            QPushButton {
                padding: 12px 15px;
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
        self.tombol_kelvin.clicked.connect(self.konversi_ke_kelvin)
        
        self.tombol_reamur = QPushButton("Reamur")
        self.tombol_reamur.setStyleSheet("""
            QPushButton {
                padding: 12px 15px;
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
        self.tombol_reamur.clicked.connect(self.konversi_ke_reamur)
        
        button_layout.addStretch()
        button_layout.addWidget(self.tombol_fahrenheit)
        button_layout.addWidget(self.tombol_kelvin)
        button_layout.addWidget(self.tombol_reamur)
        button_layout.addStretch()
        
        self.hasil_label_title = QLabel("Hasil Konversi:")
        self.hasil_label_title.setStyleSheet("""
            font-size: 14px;
            margin-top: 25px;
        """)
        
        self.hasil_label = QLabel("")
        self.hasil_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hasil_label.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #2c3e50;
            padding: 20px;
            background-color: #f9f9f9;
            border: 2px solid #3498db;
            border-radius: 8px;
            margin-top: 10px;
            min-height: 15px;
        """)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        main_layout.setContentsMargins(40, 20, 40, 20)
        
        main_layout.addWidget(self.judul_label)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.input_label)
        main_layout.addLayout(input_layout)
        main_layout.addSpacing(15)
        main_layout.addLayout(button_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.hasil_label_title)
        main_layout.addWidget(self.hasil_label)
        main_layout.addStretch()
        
        self.setLayout(main_layout)
        
        self.input_suhu.setFocus()
    
    def get_suhu(self):
        """Mengambil nilai suhu dari input dengan validasi"""
        try:
            teks = self.input_suhu.text().strip()
            
            if teks == "":
                QMessageBox.warning(self, "Input Kosong", "Masukkan suhu dalam Celsius!")
                return None
            
            if teks == "-" or teks == "." or teks == "-.":
                QMessageBox.warning(self, "Input Tidak Valid", "Masukkan angka yang valid!")
                return None
            
            teks = teks.replace(',', '.')
            
            suhu = float(teks)
            return suhu
            
        except ValueError:
            QMessageBox.warning(self, "Input Tidak Valid", "Masukkan angka yang valid!")
            return None
    
    def konversi_ke_fahrenheit(self):
        """Konversi Celsius ke Fahrenheit"""
        suhu = self.get_suhu()
        if suhu is not None:
            fahrenheit = (suhu * 9/5) + 32
            if suhu.is_integer():
                self.hasil_label.setText(f"{suhu:.0f} Celsius = {fahrenheit:.2f} Fahrenheit")
            else:
                self.hasil_label.setText(f"{suhu:.2f} Celsius = {fahrenheit:.2f} Fahrenheit")
    
    def konversi_ke_kelvin(self):
        """Konversi Celsius ke Kelvin"""
        suhu = self.get_suhu()
        if suhu is not None:
            kelvin = suhu + 273.15
            if suhu.is_integer():
                self.hasil_label.setText(f"{suhu:.0f} Celsius = {kelvin:.2f} Kelvin")
            else:
                self.hasil_label.setText(f"{suhu:.2f} Celsius = {kelvin:.2f} Kelvin")
    
    def konversi_ke_reamur(self):
        """Konversi Celsius ke Reamur"""
        suhu = self.get_suhu()
        if suhu is not None:
            reamur = suhu * 4/5
            if suhu.is_integer():
                self.hasil_label.setText(f"{suhu:.0f} Celsius = {reamur:.2f} Reamur")
            else:
                self.hasil_label.setText(f"{suhu:.2f} Celsius = {reamur:.2f} Reamur")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhuApp()
    window.show()
    sys.exit(app.exec())