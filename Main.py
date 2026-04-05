print("--- Bienvenido a la Tienda Escolar ---")


nombres_productos = []
precios_productos = []
cantidades_productos = []


while True:
    print("\n--- Menú Principal ---")
    print("1. Agregar un producto al carrito")
    print("2. Calcular el total de la compra ")
    print("3. Mostrar la información ")
    print("4. Salir")

    opcion = input("Elige una opción (1, 2, 3 o 4): ")

    
    if opcion == "1":
        print("\n--- Agregando Producto ---")
        nombre = input("Ingresa el nombre del producto: ").strip().title()
        precio = float(input("Ingresa el precio unitario: "))
        cantidad = int(input("¿Cuántas unidades deseas llevar?: "))
        
        if precio <= 0 or cantidad <= 0:
            print(">> Error: El precio y la cantidad deben ser mayores a cero.")
        else:
            nombres_productos.append(nombre)
            precios_productos.append(precio)
            cantidades_productos.append(cantidad)
            
            # Feedback dinámico usando f-strings
            print("-" * 30)
            print(f"¡Éxito! Se agregaron {cantidad} unidad(es) de '{nombre}' al carrito.")
            print(f"Precio unitario registrado: ${precio}")
       
    
    elif opcion == "2":
        print("\n--- Calculando Total ---")
        total_compra = 0  
        
        
        for i in range(len(nombres_productos)):
            subtotal = precios_productos[i] * cantidades_productos[i]
            total_compra = total_compra + subtotal
            
        print("El total actual de tu compra es: $" + str(total_compra))
        
    elif opcion == "3":
        print("\n" + "="*30)
        print("      RECIBO DE COMPRA")
        print("="*30)
        
        if len(nombres_productos) == 0:
            print("  No hay productos registrados.")
        else:
            total_acumulado = 0 
            
            for i in range(len(nombres_productos)):
                nombre = nombres_productos[i]
                precio = precios_productos[i]
                cantidad = cantidades_productos[i]
                subtotal = precio * cantidad
                total_acumulado = total_acumulado + subtotal
                
                print(f"- {cantidad}x {nombre} ..... ${precio} (Subtotal: ${subtotal})")
            
            print("-" * 30)
            print(f"TOTAL A PAGAR: ${total_acumulado}")
        print("="*30)
        
    elif opcion == "4":
        print("¡Gracias por usar la tienda escolar! Apagando sistema...")
        break  
        
    else:
        print(">> Error: Opción no válida. Por favor intenta de nuevo.")