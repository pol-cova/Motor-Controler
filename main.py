import sys
import time
import serial
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider
)
from PyQt5.QtCore import Qt

class MotorControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        # Serial port
        try:
            self.serial = serial.Serial('/dev/cu.usbserial-1410', 9600, timeout=1)
        except serial.SerialException as e:
            print(f"Error al abrir el puerto serial: {e}")
            sys.exit()

    def init_ui(self):
        self.setWindowTitle("Control de Motor")
        layout = QVBoxLayout()

        # Status
        self.status_label = QLabel("Estado: Detenido", self)
        layout.addWidget(self.status_label)

        # Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 255)
        self.slider.setValue(0)
        layout.addWidget(self.slider)

        # Avanzar
        self.forward_button = QPushButton("Avanzar", self)
        self.forward_button.clicked.connect(self.move_forward)
        layout.addWidget(self.forward_button)

        # Retroceder
        self.backward_button = QPushButton("Retroceder", self)
        self.backward_button.clicked.connect(self.move_backward)
        layout.addWidget(self.backward_button)

        # Detener
        self.stop_button = QPushButton("Detener", self)
        self.stop_button.clicked.connect(self.stop_motor)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def move_forward(self):
        speed = self.slider.value()
        command = f'F{speed}\n'
        self.serial.write(command.encode())
        print(f"Enviando: {command.strip()}")  # Agrega esta línea
        self.status_label.setText('Estado: Avanzando')
        time.sleep(0.1)

    def move_backward(self):
        speed = self.slider.value()
        command = f'B{speed}\n'
        self.serial.write(command.encode())
        print(f"Enviando: {command.strip()}")  # Agrega esta línea
        self.status_label.setText('Estado: Retrocediendo')
        time.sleep(0.1)

    def stop_motor(self):
        self.serial.write(b'S\n')
        print("Enviando: S")  # Agrega esta línea
        self.status_label.setText('Estado: Detenido')
        time.sleep(0.1)

    def closeEvent(self, event):
        self.serial.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    motor_control_app = MotorControlApp()
    motor_control_app.show()
    sys.exit(app.exec_())
