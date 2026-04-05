print("--- Bienvenido a la Tienda Escolar ---")

# Nuestras "cajas grandes" (Listas) para guardar el historial de la compra
nombres_productos = []
precios_productos = []
cantidades_productos = []

# Bucle principal (como el void loop, mantiene el programa encendido)
while True:
    print("\n--- Menú Principal ---")
    print("1. Agregar un producto al carrito")
    print("2. Calcular el total de la compra (Tarea de Carlos)")
    print("3. Mostrar la información (Tarea de Laura)")
    print("4. Salir")

    opcion = input("Elige una opción (1, 2, 3 o 4): ")

    # Evaluando la opción del usuario (Condicionales)
    if opcion == "1":
        print(">> Aquí pondremos el código para registrar el producto.")
    
    elif opcion == "2":
        print(">> Aquí pondremos el código para calcular el total.")
        
    elif opcion == "3":
        print(">> Aquí pondremos el código de Laura.")
        
    elif opcion == "4":
        print("¡Gracias por usar la tienda escolar! Apagando sistema...")
        break  # Esta instrucción 'rompe' el bucle y permite que el programa termine
        
    else:
        print(">> Error: Opción no válida. Por favor intenta de nuevo.")