class SimpleLinearRegression:
    def __init__(self):
        # Inicializa los coeficientes de la regresión lineal
        # B0: Intersección (intercepto)
        # B1: Pendiente (coeficiente de la variable independiente)
        self.B0 = 0
        self.B1 = 0

    def fit(self, X, y):
        """
        Ajusta el modelo de regresión lineal a los datos proporcionados.
        
        Parámetros:
        - X: Lista de valores de la variable independiente (Publicidad).
        - y: Lista de valores de la variable dependiente (Ventas).
        """
        n = len(X)  # Número de observaciones
        mean_X = sum(X) / n  # Media de X (Publicidad)
        mean_y = sum(y) / n  # Media de y (Ventas)

        # Calcula el numerador y el denominador para la pendiente B1
        # Numerador: Suma de (X[i] - mean_X) * (y[i] - mean_y)
        numerator = sum((X[i] - mean_X) * (y[i] - mean_y) for i in range(n))
        # Denominador: Suma de (X[i] - mean_X)^2
        denominator = sum((X[i] - mean_X) ** 2 for i in range(n))

        # Calcula los coeficientes B1 (pendiente) y B0 (intersección)
        self.B1 = numerator / denominator  # Pendiente
        self.B0 = mean_y - self.B1 * mean_X  # Intersección

    def predict(self, X):
        """
        Predice los valores de y (Ventas) para los nuevos valores de X (Publicidad).
        
        Parámetros:
        - X: Lista de nuevos valores de la variable independiente (Publicidad).
        
        Retorna:
        - Lista de predicciones de y (Ventas) redondeadas a 2 decimales.
        """
        return [round(self.B0 + self.B1 * x, 2) for x in X]  # Redondea a 2 decimales

# Datos del caso Benetton
years = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Años
sales = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518]  # Ventas en millones de euros
advertising = [23, 26, 30, 34, 43, 48, 52, 57, 58]  # Publicidad en millones de euros

# Crear y entrenar el modelo
model = SimpleLinearRegression()  # Instancia del modelo
model.fit(advertising, sales)  # Ajuste del modelo a los datos

# Imprimir la ecuación de regresión
print(f"Ecuación de Regresión: Ventas = {model.B0:.2f} + {model.B1:.2f} * Publicidad")

# Predecir ventas para nuevos valores de publicidad
new_advertising = [20, 35, 45, 50, 60]  # Nuevos valores de publicidad en millones de euros
predictions = model.predict(new_advertising)  # Predicciones de ventas

# Imprimir las predicciones
for adv, pred in zip(new_advertising, predictions):
    print(f"Publicidad: {adv} millones de euros, Predicción de Ventas: {pred} millones de euros")