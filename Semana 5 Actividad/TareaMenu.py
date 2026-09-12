"""
Aplicación interactiva sobre tuplas, diccionarios, excepciones y strings.
"""



def sumar_tupla(tupla_numeros):
	"""Retorna la suma de todos los elementos de una tupla."""
	return sum(tupla_numeros)


def gestionar_tuplas():
	print("\n" + "-" * 55)
	print("SECCIÓN 1: TUPLAS")
	print("-" * 55)

	numeros = (7.5, 9.0, 8.0, 6.5, 10.0)
	print(f"Tupla original: {numeros}")
	print(f"Tercer elemento: {numeros[2]}")

	num1 = float(input("Ingresa el primer número nuevo: "))
	num2 = float(input("Ingresa el segundo número nuevo: "))
	nueva_tupla = numeros + (num1, num2)

	print(f"Nueva tupla: {nueva_tupla}")
	lista_ordenada = sorted(nueva_tupla, reverse=True)
	print(f"Lista ordenada (mayor a menor): {lista_ordenada}")
	print(f"Suma total: {sumar_tupla(nueva_tupla)}")



def buscar_telefono(contactos, nombre):
	"""Retorna el teléfono del contacto o None si no existe."""
	return contactos.get(nombre)


def gestionar_diccionarios(contactos):
	print("\n" + "-" * 55)
	print("SECCIÓN 2: DICCIONARIOS")
	print("-" * 55)

	nombre_nuevo = input("Nombre del nuevo contacto: ")
	telefono_nuevo = input("Teléfono del nuevo contacto: ")
	contactos[nombre_nuevo] = telefono_nuevo
	print(f"Contacto '{nombre_nuevo}' agregado correctamente.")

	print("\nNombres registrados:")
	for nombre in contactos:
		print(f"- {nombre}")

	nombre_buscar = input("\n¿Qué contacto deseas buscar? ")
	telefono = buscar_telefono(contactos, nombre_buscar)
	if telefono is not None:
		print(f"El teléfono de {nombre_buscar} es: {telefono}")
	else:
		print(f"El contacto '{nombre_buscar}' no está registrado en la agenda.")



def gestionar_excepciones():
	print("\n" + "-" * 55)
	print("SECCIÓN 3: EXCEPCIONES")
	print("-" * 55)

	try:
		num1 = int(input("Primer número entero: "))
		num2 = int(input("Segundo número entero: "))
		print(f"La suma de {num1} y {num2} es: {num1 + num2}")
		print(f"La división de {num1} entre {num2} es: {num1 / num2}")
	except ValueError:
		print("Error: Debes ingresar únicamente números enteros.")
	except ZeroDivisionError:
		print("Error: No es posible dividir entre cero.")



def contar_palabras(texto):
	"""Retorna la cantidad de palabras de un texto."""
	return len(texto.split())


def gestionar_strings():
	print("\n" + "-" * 55)
	print("SECCIÓN 4: STRINGS")
	print("-" * 55)

	mensaje = input("Escribe un mensaje para analizar: ")
	print(f"Longitud del mensaje: {len(mensaje)}")
	print(f"En mayúsculas: {mensaje.upper()}")
	print(f"Texto reemplazado: {mensaje.replace('Python', 'programación')}")
	print(f"Palabras totales: {contar_palabras(mensaje)}")



def mostrar_menu():
	print("\n" + "=" * 55)
	print("      APLICACIÓN INTEGRADORA: PYTHON EN ACCIÓN")
	print("=" * 55)
	print("1. Tuplas")
	print("2. Diccionarios")
	print("3. Excepciones")
	print("4. Strings")
	print("5. Finalizar")
	print("=" * 55)


def main():
	contactos = {"Ana": "555-0101", "Luis": "555-0102", "Mía": "555-0103"}

	while True:
		mostrar_menu()
		opcion = input("Selecciona una opción (1-5): ").strip()

		if opcion == "1":
			gestionar_tuplas()
		elif opcion == "2":
			gestionar_diccionarios(contactos)
		elif opcion == "3":
			gestionar_excepciones()
		elif opcion == "4":
			gestionar_strings()
		elif opcion == "5":
			print("\nPrograma finalizado. ¡Hasta luego!")
			break
		else:
			print("\nOpción no válida. Por favor, elige un número del 1 al 5.")
			continue

		input("\nPresiona ENTER para volver al menú principal...")


if __name__ == "__main__":
	main()
