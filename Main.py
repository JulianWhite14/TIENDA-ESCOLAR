print("--- Bienvenido a la Tienda Escolar ---")


nombres_productos = []
precios_productos = []
cantidades_productos = []


while True:
    print("\n--- Menú Principal ---")
    print("1. Agregar un producto al carrito")
    print("2. Calcular el total de la compra ")
    print("3. Mostrar la información (Tarea de Laura)")
    print("4. Salir")

    opcion = input("Elige una opción (1, 2, 3 o 4): ")

    
    if opcion == "1":
        print("\n--- Agregando Producto ---")
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio unitario: "))
        cantidad = int(input("¿Cuántas unidades deseas llevar?: "))
        
        nombres_productos.append(nombre)
        precios_productos.append(precio)
        cantidades_productos.append(cantidad)
        
        print("¡Producto guardado exitosamente en el carrito!")
       
    
    elif opcion == "2":
        print(">> Aquí pondremos el código para calcular el total.")
        
    elif opcion == "3":
        print(">> Aquí pondremos el código de Laura.")
        
    elif opcion == "4":
        print("¡Gracias por usar la tienda escolar! Apagando sistema...")
        break  
        
    else:
        print(">> Error: Opción no válida. Por favor intenta de nuevo.")