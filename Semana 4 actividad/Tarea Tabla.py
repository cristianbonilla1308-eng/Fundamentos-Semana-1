def generar_tabla(n=10):
    tabla = []
    for i in range(1, n + 1):
        fila = []
        for j in range(1, n + 1):
            fila.append(i * j)
        tabla.append(fila)
    return tabla


def imprimir_tabla(tabla):
    for i, fila in enumerate(tabla, start=1):
        print(f"{i:>3}: " + " ".join(f"{v:>4}" for v in fila))


def main():
    tabla = generar_tabla()
    imprimir_tabla(tabla)

    while True:
        renglon = int(input("\nRenglón del 1-10): "))
        if renglon == 0:
            break
        columna = int(input("Columna del 1-10): "))
        print(f"{renglon} x {columna} = {tabla[renglon-1][columna-1]}")


if __name__ == "__main__":
    main()
