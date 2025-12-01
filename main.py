

from crear_reserva import (
    validar_fecha, 
    validar_horario, 
    validar_personas, 
    solicitar_datos_reserva)

from codigo_reserva import (
    verificar_disponibilidad, 
    asignar_codigo_a_reserva, 
    generar_codigo_unico)

from gestion_reservas import (
    buscar_reserva_por_codigo,
    listar_todas_reservas,
    cancelar_reserva,
    buscar_por_nombre,
    buscar_por_fecha,
    buscar_por_servicio,
    menu_busqueda_avanzada,
)

from reportes import (
    reporte_reservas_por_fecha,
    reporte_total_reservas,
    reporte_primera_y_ultima,
    exportar_a_archivo,
    menu_reportes
)

reservas = []

def crear_reserva_completa():
    print("\n" + "="*70)
    #espaciado para centrar el título, lo que es que arroja 70 caracteres de ancho
    print(" "*25 + "NUEVA RESERVA")
    #este hace una línea debajo del título
    print("="*70)
    
    # Solicitar datos de reserva
    print("\n📝 Por favor, ingrese los datos de la reserva:")
    nueva_reserva = solicitar_datos_reserva()
    
    # PASO 2: Verificar disponibilidad (usa función de Parte 2)
    print("\n🔍 Verificando disponibilidad...")
    disponible = verificar_disponibilidad(
        nueva_reserva['fecha'],
        nueva_reserva['horario'],
        nueva_reserva['servicio'],
        reservas
    )
    
    if not disponible:
        print("\n❌ Lo sentimos, no hay disponibilidad para:")
        print(f"   Servicio: {nueva_reserva['servicio']}")
        print(f"   Fecha:    {nueva_reserva['fecha']}")
        print(f"   Horario:  {nueva_reserva['horario']}")
        print("\n💡 Sugerencia: Intente con otro horario o fecha.")
        input("\nPresione Enter para continuar...")
        return
    
    # PASO 3: Asignar código único (usa función de Parte 2)
    print("\n🔢 Generando código de reserva...")
    nueva_reserva = asignar_codigo_a_reserva(nueva_reserva, reservas)
    
    # PASO 4: Agregar a la lista global
    reservas.append(nueva_reserva)
    
    # PASO 5: Confirmación
    print("\n" + "="*70)
    print(" "*25 + "✅ ¡RESERVA CREADA!")
    print("="*70)
    print(f"\n  Código:      {nueva_reserva['codigo']}")
    print(f"  Cliente:     {nueva_reserva['nombre']}")
    print(f"  Servicio:    {nueva_reserva['servicio']}")
    print(f"  Fecha:       {nueva_reserva['fecha']}")
    print(f"  Horario:     {nueva_reserva['horario']}")
    print(f"  Personas:    {nueva_reserva['personas']}")
    print(f"  Estado:      {nueva_reserva['estado'].upper()}")
    print("\n" + "="*70)
    
    input("\nPresione Enter para continuar...")
    
def mostrar_todas_reservas():
    listar_todas_reservas(reservas)
    input("\nPresione Enter para continuar...")
    
def buscar_reservas():
    menu_busqueda_avanzada(reservas)
    
def cancelar_reserva_menu():
    print("\n" + "="*70)
    print(" "*25 + "CANCELAR RESERVA")
    print("="*70)
    
    # Verificar que haya reservas
    if len(reservas) == 0:
        print("\n⚠️  No hay reservas en el sistema.\n")
        input("\nPresione Enter para continuar...")
        return
    
    # Solicitar código
    codigo = input("\nIngrese el código de la reserva a cancelar: ").strip()
    
    # Validar que no esté vacío
    if not codigo:
        print("\n❌ Código no puede estar vacío.\n")
        input("Presione Enter para continuar...")
        return
    
    # Usar función de Parte 3 y verificar resultado
    exito = cancelar_reserva(codigo, reservas)
    
    # Mostrar mensaje según resultado
    if exito:
        print("\n" + "="*70)
        print("✅ La reserva fue cancelada exitosamente.")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("⚠️  No se pudo cancelar la reserva.")
        print("   Posibles razones:")
        print("   • El código no existe en el sistema")
        print("   • La reserva ya estaba cancelada previamente")
        print("="*70)
    
    input("\nPresione Enter para continuar...")
    
def acceder_reportes():
    menu_reportes(reservas)

def menu_principal():
    # si el usuario el de a enter la condicion se cumple y entra al bucle
    while True:
        print("\n" + "="*70)
        print(" "*20 + "SISTEMA DE GESTIÓN DE RESERVAS")
        print("="*70)
        print("\n📋 MENÚ PRINCIPAL:\n")
        print("  1. 📝 Crear nueva reserva")
        print("  2. 📊 Listar todas las reservas")
        print("  3. 🔍 Buscar reserva")
        print("  4. ❌ Cancelar reserva")
        print("  5. 📈 Reportes y estadísticas")
        print("  6. 💾 Exportar datos")
        print("  7. 🚪 Salir del sistema")
        print("\n" + "="*70)
        
        # Mostrar info rápida
        activas = sum(1 for r in reservas if r.get('estado') == 'activa')
        # este print muestra el estado actual de las reservas
        print(f"\n📊 Estado actual: {len(reservas)} reserva(s) total | {activas} activa(s)")
        # pide al usuario que seleccione una opción
        
        opcion = input("\n👉 Seleccione una opción (1-7): ").strip()
        
        if opcion == '1':
            crear_reserva_completa()
        
        elif opcion == '2':
            mostrar_todas_reservas()  
        
        elif opcion == '3':
            buscar_reservas()  
        
        elif opcion == '4':
            cancelar_reserva_menu()  
        
        elif opcion == '5':
            acceder_reportes()
        
        elif opcion == '6':
            # Exportar directamente
            print("\n" + "="*70)
            print(" "*25 + "EXPORTAR DATOS")
            print("="*70)
            
            if len(reservas) == 0:
                # no reservara si no hay nada que exportar
                print("\n⚠️  No hay reservas para exportar.\n")
                input("Presione Enter para continuar...")
                continue
            
            from datetime import datetime
            #aqui se genera el nombre del archivo con la fecha y hora actual
            fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"reservas_{fecha_actual}.txt"
            
            print(f"\n💾 Exportando a: {nombre_archivo}")
            exito = exportar_a_archivo(reservas, nombre_archivo)
            
            if exito:
                print(f"\n✅ Datos exportados exitosamente!")
            
            input("\nPresione Enter para continuar...")
        
        elif opcion == '7':
            # aqui se maneja la salida del programa
            print("\n" + "="*70)
            print(" "*15 + "¡Gracias por usar el sistema!")
            print(" "*20 + "Hasta pronto 👋")
            print("="*70 + "\n")
            break
        #aqui se maneja el caso de una opción inválida
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-7.")
            input("\nPresione Enter para continuar...")

def mostrar_bienvenida():
    # Mensaje de bienvenida, que va antes del menú principal
    print("\n" + "="*70)
    print(" "*15 + "BIENVENIDO AL SISTEMA DE RESERVAS")
    print("="*70)
    print("\n  Este sistema le permite:")
    print("    ✓ Crear y gestionar reservas")
    print("    ✓ Consultar disponibilidad")
    print("    ✓ Generar reportes y estadísticas")
    print("    ✓ Exportar información")
    print("\n" + "="*70)
    input("\n  Presione Enter para continuar...")

if __name__ == "__main__":
    # Manejo de excepciones a nivel global
    try:
        # Mostrar bienvenida y menú principal
        mostrar_bienvenida()
        menu_principal()
        
    except KeyboardInterrupt:
        # Manejo de Ctrl+C para salir limpiamente
        print("\n\n⚠️  Programa interrumpido por el usuario.")
        print("👋 ¡Hasta pronto!\n")
    
    except Exception as e:
        # Manejo de cualquier otra excepción inesperada
        print(f"\n❌ Error inesperado: {e}")
        print("Por favor, contacte al administrador del sistema.\n")
        import traceback

        traceback.print_exc()


