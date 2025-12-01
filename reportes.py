from datetime import datetime

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


# FUNCIÓN OPCIONAL: EXPORTAR A ARCHIVO
# ============================================================================
def exportar_a_archivo(reservas, nombre_archivo=None):
    """
    Exporta todas las reservas a un archivo de texto
    
    Args:
        reservas: Lista de todas las reservas
        nombre_archivo: Nombre del archivo (opcional)
    
    Returns:
        True si se exportó exitosamente, False si hubo error
    """
    print("\n" + "="*60)
    print("        EXPORTAR HISTORIAL A ARCHIVO")
    print("="*60)
    
    # Verificar si hay reservas
    if len(reservas) == 0:
        print("\n⚠️  No hay reservas para exportar.\n")
        print("="*60 + "\n")
        return False
    
    # Generar nombre de archivo si no se proporcionó
    if nombre_archivo is None:
        fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"reservas_{fecha_actual}.txt"
    
    try:
        # Abrir archivo para escribir
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            # Escribir encabezado
            archivo.write("="*60 + "\n")
            archivo.write("         HISTORIAL DE RESERVAS\n")
            archivo.write("="*60 + "\n")
            
            # Fecha de exportación
            fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            archivo.write(f"Fecha de exportación: {fecha_hora}\n")
            archivo.write(f"Total de reservas: {len(reservas)}\n")
            archivo.write("="*60 + "\n\n")
            
            # Escribir cada reserva
            for i, reserva in enumerate(reservas, 1):
                archivo.write(f"[{i}] {reserva['codigo']}\n")
                archivo.write(f"    Cliente:  {reserva['nombre']}\n")
                archivo.write(f"    Servicio: {reserva['servicio']}\n")
                archivo.write(f"    Fecha:    {reserva['fecha']}\n")
                archivo.write(f"    Horario:  {reserva['horario']}\n")
                archivo.write(f"    Personas: {reserva['personas']}\n")
                archivo.write(f"    Estado:   {reserva['estado'].upper()}\n")
                archivo.write("\n" + "-"*60 + "\n\n")
            
            # Escribir estadísticas al final
            activas = sum(1 for r in reservas if r['estado'] == 'activa')
            canceladas = sum(1 for r in reservas if r['estado'] == 'cancelada')
            total_personas = sum(r['personas'] for r in reservas if r['estado'] == 'activa')
            
            archivo.write("="*60 + "\n")
            archivo.write("ESTADÍSTICAS:\n")
            archivo.write(f"  Reservas activas:    {activas}\n")
            archivo.write(f"  Reservas canceladas: {canceladas}\n")
            archivo.write(f"  Total de personas:   {total_personas}\n")
            archivo.write("="*60 + "\n")
            archivo.write("Fin del reporte\n")
            archivo.write("="*60 + "\n")
        
        # Confirmación
        print(f"\n✅ Historial exportado exitosamente!")
        print(f"   Archivo: {nombre_archivo}")
        print(f"   Total de reservas exportadas: {len(reservas)}")
        print("="*60 + "\n")
        return True
        
    except Exception as e:
        print(f"\n❌ Error al exportar archivo: {e}\n")
        print("="*60 + "\n")
        return False

# ============================================================================
# FUNCIÓN OPCIONAL: REPORTE DE SERVICIO MÁS RESERVADO
# ============================================================================
def reporte_servicio_mas_reservado(reservas):
    """
    Muestra estadísticas por tipo de servicio
    """
    print("\n" + "="*60)
    print("     REPORTE: SERVICIOS MÁS RESERVADOS")
    print("="*60)
    
    if len(reservas) == 0:
        print("\n⚠️  No hay reservas registradas.\n")
        print("="*60 + "\n")
        return
    
    # Contar reservas por servicio
    servicios_count = {}
    
    for reserva in reservas:
        if reserva['estado'] == 'activa':
            servicio = reserva['servicio']
            if servicio not in servicios_count:
                servicios_count[servicio] = 0
            servicios_count[servicio] += 1
    
    # Ordenar por cantidad (de mayor a menor)
    servicios_ordenados = sorted(servicios_count.items(), 
                                key=lambda x: x[1], 
                                reverse=True)
    
    # Mostrar ranking
    print("\n🏆 RANKING DE SERVICIOS:\n")
    for i, (servicio, cantidad) in enumerate(servicios_ordenados, 1):
        barra = "█" * cantidad
        print(f"  {i}. {servicio:<25} {barra} ({cantidad})")
    
    print("="*60 + "\n")

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
