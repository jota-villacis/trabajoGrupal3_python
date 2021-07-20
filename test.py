'''
DESARROLLO

Hoy simularemos que nuestra tienda virtual tiene muchos usuarios comprando desesperadamente. De igual forma, simularemos un alto movimiento de proveedores 
que renuevan nuestro stock de productos a ofrecer.

Primero, desarrollaremos una forma de almacenar nuestro stock de dos productos. El primer producto tendrá 120 unidades y el segundo 150.
Luego, simularemos cada 3 segundos una compra de “n” unidades de cualquiera de los dos productos. n representa un número aleatorio entre 1 y 10.
Cada compra, como es natural, afecta el stock inicial de productos. Es decir, si una compra simulada es de 3 unidades del producto 1, este se debe descontar del stock.
Cada 10 compras, el programa debe imprimir en pantalla el número de unidades disponibles por producto. ¿Lo lograron?
Por último, cuando un producto tenga un stock de menos de 100 unidades, los proveedores enviarán automáticamente 50 unidades más. Esto se debe reflejar en el stock de cada producto.
Lamentablemente, los proveedores solo tienen stock suficiente para enviar 150 unidades en total de productos 1 y 2
'''
# Librerias
import random
import time
# 1.Desarrollar una forma de almacenar nuestro stock de dos productos. El primer producto tendrá 120 unidades y el segundo 150
stock_p1 = 120
stock_p2 = 150
proveedores = 10000
solicitud = 50
# 2.Simular cada 3 segundos una compra de “n” unidades de cualquiera de los dos productos. n representa un número aleatorio entre 1 y 10
unidades_p1 = random.randrange(1,11)
unidades_p2 = random.randrange(1,11)

# 3.Cada compra simulada se debe descontar del stock
stock_p1 = stock_p1 - unidades_p1
stock_p2 = stock_p2 - unidades_p2

# 4.Cada 10 compras, el programa debe imprimir en pantalla el número de unidades disponibles por producto
contador_compras = 0
if contador_compras == 10:
    print(f'Unidades disponibles de p1: {stock_p1}')
    print(f'Unidades disponibles de p2: {stock_p2}')


# 5.Cuando un producto tenga un stock de menos de 100 unidades, los proveedores enviarán automáticamente 50 unidades más. Esto se debe reflejar en el stock de cada producto.
if stock_p1 <= 100:
    print(f'Quedan menos de 100 unidades, exactamente {stock_p1}')
    solicitud_producto = proveedores - solicitud
    print('Se solicitaron 50 productos mas')
    stock_p1 = stock_p1 + solicitud
    print(stock_p1)
    print(proveedores)
elif stock_p2 <= 100:
    print(f'Quedan menos de 100 unidades, exactamente {stock_p2}')
    solicitud_producto = proveedores - solicitud
    print('Se solicitaron 50 productos mas')
    stock_p2 = stock_p2 + solicitud
    print(stock_p2)
    print(proveedores)

time.sleep(.3)