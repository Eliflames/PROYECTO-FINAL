"""reportes.py

Funciones de reportes para el sistema de reservas.

Las funciones reciben la lista de reservas como parámetro; este módulo no
contiene datos de prueba para evitar interferir con la lista global.
"""

from datetime import datetime


def _parse_date(fecha_str):
    """Intenta parsear una fecha en formatos DD-MM-YYYY o DD/MM/YYYY y devuelve date o None."""
    if not fecha_str:
        return None
    for fmt in ('%d-%m-%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(fecha_str, fmt).date()
        except Exception:
            continue
    return None


def reporte_reservas_por_fecha(fecha, reservas):
    """Imprime todas las reservas para una fecha dada (acepta DD-MM-YYYY o DD/MM/YYYY)."""
    fecha_dt = _parse_date(fecha)
    print(f"\n=== Reporte: Reservas para fecha: {fecha} ===")
    if fecha_dt is None:
        print("Formato de fecha inválido. Use DD-MM-YYYY o DD/MM/YYYY")
        return

    resultados = [r for r in reservas if _parse_date(r.get('fecha')) == fecha_dt]
    if not resultados:
        print("No hay reservas para esa fecha.")
        return

    encabezado = "{:<20} {:<20} {:<20} {:<8} {:<8} {:<10}".format(
        'Código', 'Nombre', 'Servicio', 'Horario', 'Personas', 'Estado')
    print(encabezado)
    print('-' * len(encabezado))
    for r in resultados:
        print("{:<20} {:<20} {:<20} {:<8} {:<8} {:<10}".format(
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
                    f"{r.get('fecha','')};{r.get('horario','')};{r.get('personas','')};{r.get('estado','')} \n"
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
            fecha = input("Fecha (DD-MM-YYYY o DD/MM/YYYY): ").strip()
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

