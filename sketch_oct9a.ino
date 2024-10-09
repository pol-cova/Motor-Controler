#include <Arduino.h>

int in3 = 7; // Pin para IN3 (OUT B)
int in4 = 8; // Pin para IN4 (OUT A)
int enB = 9; // Pin de Enable para el motor

void setup() {
  Serial.begin(9600);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enB, OUTPUT);
}

void loop() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        
        Serial.print("Comando recibido: ");
        Serial.println(command);
        if (command.length() > 0) {
            char cmd = command.charAt(0);
            Serial.println(cmd);
            switch (cmd) {
                case 'F': // Avanza
                    digitalWrite(in3, HIGH);
                    digitalWrite(in4, LOW);
                    int speedForward = command.substring(1).toInt();
                    analogWrite(enB, speedForward);
                    Serial.println("Avanzando");
                    break;

                case 'B': // Retrocede
                    digitalWrite(in3, LOW);
                    digitalWrite(in4, HIGH);
                    int speedBackward = command.substring(1).toInt();
                    analogWrite(enB, speedBackward);
                    Serial.println("Retrocediendo");
                    break;

                case 'S': // Detener
                    digitalWrite(in3, LOW); // Apagar el pin IN3
                    digitalWrite(in4, LOW); // Apagar el pin IN4
                    analogWrite(enB, 0);
                    Serial.println("Motor detenido");
                    break;
            }
            // Imprimir estado de los pines
            Serial.print("Estado de IN3: ");
            Serial.println(digitalRead(in3));
            Serial.print("Estado de IN4: ");
            Serial.println(digitalRead(in4));
            Serial.print("Velocidad del motor: ");
            Serial.println(analogRead(enB));
        }
    }
}
