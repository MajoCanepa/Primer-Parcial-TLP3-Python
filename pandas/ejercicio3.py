import pandas as pd
import matplotlib.pyplot as plt

productos = [
    {"nombre": "Camiseta", "precio": 20, "cantidad_disponible":100},
    {"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
    {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
    {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
    {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
    {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
    {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
    {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
    {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
    {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible":25},
    {"nombre": "Calcetines", "precio": 10, "cantidad_disponible":150},
    {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
    {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
    {"nombre": "Pendientes", "precio": 15, "cantidad_disponible":180},
    {"nombre": "Cinturón", "precio": 20, "cantidad_disponible":100},
    {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
    {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
    {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
    {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
    {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]

df = pd.DataFrame(productos)
# Cálculo del valor total del inventario por producto.
df['inventario_total_producto'] = df['precio'] * df['cantidad_disponible']
# Valor total del inventario.
df['inventario_total'] = df["inventario_total_producto"].cumsum()
# simular algunas ventas y actualizar la cantidad de productos vendidos.
df['cantidad_disponible'] = df['cantidad_disponible'] - 10
# Mostar cantidad restante de cada producto después de las ventas.
print(df[['nombre', 'cantidad_disponible']])
# DataFrame: Con las columnas: nombres(productos) y cantidad(productos)
productos = {
    'Nombres': df['nombre'],
    'Cantidad de Productos': df['cantidad_disponible']
}

# Gráfico de barras
df = pd.DataFrame(productos)
df.plot(kind='bar', x='Nombres', y='Cantidad de Productos', color='blue')
plt.xlabel('Nombre de los Productos')
plt.ylabel('Cantidad Disponible')
plt.title('Cantidad de Productos Disponibles')
plt.show()