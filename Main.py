print("Bienvenido a la Tienda Escolar")

# Registrando la información del producto
nombre_producto = input("Por favor, ingresa el nombre del producto: ")
precio_producto = float(input("Por favor, ingresa el precio del producto: "))

# Nueva mejora: Pedir la cantidad
cantidad_producto = int(input("¿Cuántas unidades deseas llevar?: "))

# Calculando el total de la compra (La tarea de Carlos)
total_compra = precio_producto * cantidad_producto