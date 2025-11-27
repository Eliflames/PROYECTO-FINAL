"""Funciones del main """

def crear_reserva_completa():
    print("\n" + "="*70)
    print(" "*25 + "NUEVA RESERVA")
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