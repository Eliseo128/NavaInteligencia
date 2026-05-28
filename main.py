def mostrar_tabla():
    print("=========================================")
    print("   TABLA DE MULTIPLICAR INTERACTIVA")
    print("=========================================")
    
    while True:
        try:
            # Preguntar al usuario qué tabla desea ver
            opcion = input("\n¿Qué tabla de multiplicar deseas ver? (1 al 10) o escribe 'salir' para terminar: ")
            
            # Opción para salir del programa
            if opcion.lower() == 'salir':
                print("¡Gracias por usar el programa! Hasta luego.")
                break
            
            # Convertir la entrada a entero
            numero = int(opcion)
            
            # Validar que el número esté en el rango de 1 al 10
            if 1 <= numero <= 10:
                print(f"\n--- Tabla del {numero} ---")
                for i in range(1, 11):
                    resultado = numero * i
                    print(f"{numero} x {i} = {resultado}")
                print("-------------------------")
            else:
                print("Por favor, introduce un número que esté entre el 1 y el 10.")
                
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero o escribe 'salir'.")

if __name__ == "__main__":
    mostrar_tabla()
