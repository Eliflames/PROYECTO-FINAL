# reportes.py

# DATOS DE PRUEBA - BORRAR en integración final
reservas = [
	{
		'codigo': 'RES-20250119-001',
		'nombre': 'Juan Pérez',
		'servicio': 'Mesa de restaurante',
		'fecha': '25/12/2025',
		'horario': '19:30',
		'personas': 4,
		'estado': 'activa'
	},
	{
		'codigo': 'RES-20250119-002',
		'nombre': 'María García',
		'servicio': 'Sala de reuniones',
		'fecha': '26/12/2025',
		'horario': '10:00',
		'personas': 8,
		'estado': 'activa'
	},
	{
		'codigo': 'RES-20250119-003',
		'nombre': 'Carlos López',
		'servicio': 'Evento especial',
		'fecha': '25/12/2025',
		'horario': '20:00',
		'personas': 50,
		'estado': 'cancelada'
	},
	{
		'codigo': 'RES-20250120-001',
		'nombre': 'Ana Martínez',
		'servicio': 'Sala de conferencias',
		'fecha': '27/12/2025',
		'horario': '15:00',
		'personas': 12,
		'estado': 'activa'
	}
]

#Las funciones de reporte reciben la lista de reservas como parámetro.
def reporte_reservas_por_fecha(fecha, reservas):
	"""Imprime todas las reservas para una fecha dada (formato DD/MM/AAAA)."""
	resultados = [r for r in reservas if r.get('fecha') == fecha]
	print("\n=== Reporte: Reservas para fecha: {} ===".format(fecha))
	if not resultados:
		print("No hay reservas para esa fecha.")
		return

	# Cabecera
	encabezado = "{:<20} {:<20} {:<20} {:<6} {:<8} {:<10}".format(
		'Código', 'Nombre', 'Servicio', 'Horario', 'Personas', 'Estado')
	print(encabezado)
	print('-' * len(encabezado))
	for r in resultados:
		print("{:<20} {:<20} {:<20} {:<6} {:<8} {:<10}".format(
			r.get('codigo', ''),
			r.get('nombre', ''),
			r.get('servicio', ''),
			r.get('horario', ''),
			str(r.get('personas', '')),
			r.get('estado', '')
		))


def reporte_total_reservas(reservas):
	"""Imprime el total de reservas y un desglose por estado."""
	total = len(reservas)
	activas = sum(1 for r in reservas if r.get('estado') == 'activa')
	canceladas = sum(1 for r in reservas if r.get('estado') == 'cancelada')
	print("\n=== Reporte: Total de reservas ===")
	print(f"Total: {total}")
	print(f"Activas: {activas}")
	print(f"Canceladas: {canceladas}")


def reporte_primera_y_ultima(reservas):
	"""Imprime la primera y la última reserva ingresada (según orden en la lista)."""
	print("\n=== Reporte: Primera y última reserva ===")
	if not reservas:
		print("La lista de reservas está vacía.")
		return

	primera = reservas[0]
	ultima = reservas[-1]

	def resumen(r):
		return "{codigo} | {nombre} | {fecha} {horario} | {servicio} | {personas} pers. | {estado}".format(**r)

	print("Primera:")
	print(resumen(primera))
	print("\nÚltima:")
	print(resumen(ultima))


def exportar_a_archivo(reservas, nombre_archivo):
	"""Exporta el historial de reservas a un archivo de texto.

	Cada reserva se guarda en una línea en formato legible.
	Retorna True si se escribe correctamente, False en caso de error.
	"""
	try:
		with open(nombre_archivo, 'w', encoding='utf-8') as f:
			for r in reservas:
				linea = (
					f"{r.get('codigo','')};{r.get('nombre','')};{r.get('servicio','')};"
					f"{r.get('fecha','')};{r.get('horario','')};{r.get('personas','')};{r.get('estado','')}\n"
				)
				f.write(linea)
		print(f"Exportación completada a '{nombre_archivo}'")
		return True
	except Exception as e:
		print(f"Error al exportar a archivo: {e}")
		return False


def menu_reportes(reservas):
	"""Submenú para ejecutar reportes interactivos."""
	while True:
		print("\n--- Menú de Reportes ---")
		print("1. Reporte por fecha")
		print("2. Reporte total de reservas")
		print("3. Primera y última reserva")
		print("4. Exportar a archivo")
		print("5. Volver")
		opcion = input("Seleccione opción (1-5): ").strip()

		if opcion == '1':
			fecha = input("Fecha (DD/MM/AAAA): ").strip()
			reporte_reservas_por_fecha(fecha, reservas)
		elif opcion == '2':
			reporte_total_reservas(reservas)
		elif opcion == '3':
			reporte_primera_y_ultima(reservas)
		elif opcion == '4':
			nombre = input("Nombre de archivo (ej. reservas.txt): ").strip()
			if not nombre:
				print("Nombre inválido")
				continue
			exportar_a_archivo(reservas, nombre)
		elif opcion == '5':
			break
		else:
			print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
	# Pruebas rápidas
	reporte_reservas_por_fecha("25/12/2025", reservas)
	reporte_total_reservas(reservas)
	reporte_primera_y_ultima(reservas)
	exito = exportar_a_archivo(reservas, "reservas_test.txt")
	print(f"Exportación exitosa: {exito}")

