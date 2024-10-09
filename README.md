# Controlador de Motor con PyQt y Arduino

¡Bienvenido al proyecto de Controlador de Motor! Este proyecto utiliza PyQt para crear una interfaz gráfica que permite controlar un motor mediante un Arduino.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción del Proyecto

Este proyecto permite controlar un motor a través de una interfaz gráfica desarrollada en Python con PyQt. Los comandos de control se envían a un Arduino que maneja el motor.

## Requisitos

Asegúrate de tener instalados los siguientes programas y bibliotecas:

- Python 3.x
- PyQt5
- pySerial
- Arduino IDE

### Instalación de Dependencias

Para instalar las dependencias de Python, ejecuta el siguiente comando:

```
bash
pip install pyqt5 pyserial
```

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/pol-cova/Motor-Controler.git
   ```

2. **Sube el código al Arduino:**

   Abre el archivo `.ino` en el Arduino IDE y sube el código al Arduino.

3. **Ejecuta la aplicación de PyQt:**

   Navega al directorio del proyecto y ejecuta el siguiente comando:

   ```bash
   python main.py
   ```

## Uso

1. Conecta el motor y el Arduino según el esquema de conexión proporcionado.
2. Ejecuta la aplicación de PyQt.
3. Utiliza el deslizador para ajustar la velocidad del motor.
4. Presiona el botón "Avanzar" para mover el motor hacia adelante.
5. Presiona el botón "Retroceder" para mover el motor hacia atrás.
6. Presiona el botón "Detener" para detener el motor.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar en este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
