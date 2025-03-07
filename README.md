# Hands-on2-SLR 📊 Regresión Lineal Simple: Caso Benetton 🛍️

Este trabajo implementa una **regresión lineal simple** (SLR) desde cero en Python, utilizando un enfoque orientado a objetos. El objetivo es predecir las ventas de la empresa Benetton en función de su inversión en publicidad. 🎯

---

## 📋 Descripción del Proyecto

El proyecto consta de una clase `SimpleLinearRegression` que:
1. Ajusta un modelo de regresión lineal a los datos proporcionados.
2. Predice las ventas en función de nuevos valores de publicidad.

Los datos utilizados son del caso Benetton, donde se muestran las ventas y la inversión en publicidad durante varios años. 📈

---

## 🛠️ Requisitos

- **Python 3.x**: El código está escrito en Python y no requiere bibliotecas externas. 🐍
- **Ninguna instalación adicional**: Todo está implementado desde cero, sin usar bibliotecas.

---

## 🚀 Observar resultados

   - El programa imprimirá la ecuación de regresión lineal.
   - También mostrará predicciones de ventas para nuevos valores de publicidad.

---

## 🧮 Explicación del Código

### Estructura del Proyecto

- **`SimpleLinearRegression`**: Clase que implementa la regresión lineal simple.
  - **`fit(X, y)`**: Ajusta el modelo a los datos de entrenamiento.
  - **`predict(X)`**: Predice los valores de `y` (ventas) para nuevos valores de `X` (publicidad).

- **Datos Hardcodeados**: Los datos de ventas y publicidad de Benetton están directamente en el código.

- **Predicciones**: Se eligen cinco valores de publicidad no vistos para predecir las ventas.

---

### Ejemplo de Salida

Al ejecutar el script, verás algo como esto:

```
Ecuación de Regresión: Ventas = 168.00 + 23.00 * Publicidad
Publicidad: 20 millones de euros, Predicción de Ventas: 628.00 millones de euros
Publicidad: 35 millones de euros, Predicción de Ventas: 973.00 millones de euros
Publicidad: 45 millones de euros, Predicción de Ventas: 1203.00 millones de euros
Publicidad: 50 millones de euros, Predicción de Ventas: 1318.00 millones de euros
Publicidad: 60 millones de euros, Predicción de Ventas: 1548.00 millones de euros
```

---

## 📊 Interpretación de los Resultados

- **Ecuación de Regresión**: `Ventas = 168.00 + 23.00 * Publicidad`
  - **168.00**: Es el valor esperado de ventas cuando no se invierte en publicidad (intersección).
  - **23.00**: Por cada millón de euros invertido en publicidad, las ventas aumentan en 23 millones de euros (pendiente).

- **Predicciones**: El modelo predice las ventas para nuevos valores de publicidad, lo que puede ser útil para la planificación estratégica de la empresa. 🎯

---

## 🧠 Aprendizaje

Este proyecto es ideal para:
- Entender cómo funciona la regresión lineal simple.
- Aprender a implementar algoritmos de machine learning desde cero.
- Practicar programación orientada a objetos en Python.

---

¡Gracias por visitar este repositorio! Espero que te sea útil. 😊

---

### Captura de Pantalla 

![image](https://github.com/user-attachments/assets/28f6475d-2d67-4441-b843-a57db90478e4)


---
