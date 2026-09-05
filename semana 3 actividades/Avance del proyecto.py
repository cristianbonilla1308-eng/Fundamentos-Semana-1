
# Avzanze del proyecto
# Tacos La Chilaca
# ======================
precio = 15.0        
existencia = 20      
total_dia = 0.0        

opc = 0

while opc != 3:
    print("=== TACOS LA CHILACA ===")
    print("1. Vender taco")
    print("2. Ver total del dia")
    print("3. Salir")
    opc = int(input("Elige una opcion: "))

    if opc == 1:
        cantidad = int(input("Cantidad de tacos: "))

        if cantidad <= existencia:
            existencia = existencia - cantidad
            total_dia = total_dia + (cantidad * precio)
            print("Venta registrada.")
        else:
            print("No hay suficiente existencia.")

    elif opc == 2:
        print("Total del dia:", total_dia)
        print("Existencia restante:", existencia)

    elif opc != 3:
        print("Opcion invalida, intenta de nuevo.")

print("Gracias por su visita.")
