

# PARTE 3: GESTIÓN DE RESERVAS

# FUNCIÓN AUXILIAR: MOSTRAR UNA RESERVA
def mostrar_reserva(reserva):  #parámetro singular
    """Muestra una reserva individual con formato bonito"""
    print('-' * 80)
    print(f"  Código:    {reserva['codigo']}")
    print(f"  Nombre:    {reserva['nombre']}")
    print(f"  Servicio:  {reserva['servicio']}")
    print(f"  Fecha:     {reserva['fecha']}")
    print(f"  Horario:   {reserva['horario']}")
    print(f"  Personas:  {reserva['personas']}")
    print(f"  Estado:    {reserva['estado'].upper()}")
    print('-' * 80)


# FUNCIÓN 1: LISTAR TODAS LAS RESERVAS

def listar_todas_reservas(reservas):
    """Muestra todas las reservas en formato tabla"""
    print('\n' + '=' * 100)
    print(' ' * 35 + 'LISTADO DE RESERVAS')
    print('=' * 100)
    
    # Manejo de lista vacía
    if len(reservas) == 0:
        print('\n  ⚠️  No hay reservas registradas.\n')
        print('=' * 100 + '\n')
        return
    
    # Encabezados
    print(f"\n{'Código':<20} {'Cliente':<20} {'Servicio':<20} {'Fecha':<12} {'Hora':<8} {'Pers.':<6} {'Estado':<15}")
    print('-' * 100)
    
    # Mostrar cada reserva
    for reserva in reservas:
        # Símbolos según estado
        if reserva['estado'] == 'activa':
            estado_visual = '✅ Activa'
        elif reserva['estado'] == 'cancelada':
            estado_visual = '❌ Cancelada'
        else:
            estado_visual = '⏳ ' + reserva['estado'].capitalize()

        print(f"{reserva['codigo']:<20} "
            f"{reserva['nombre']:<20} "
            f"{reserva['servicio']:<20} "
            f"{reserva['fecha']:<12} "
            f"{reserva['horario']:<8} "
            f"{reserva['personas']:<6} "
            f"{estado_visual:<15}")
    
    # print('-' * 100)  #ESTA LÍNEA CAUSABA IMPRESIÓN DOBLE
    
    print('-' * 100)
    print(f'  Total de reservas: {len(reservas)}')
    print('=' * 100 + '\n')

# ============================================================================
# FUNCIÓN 2: BUSCAR POR CÓDIGO
# ============================================================================
def buscar_reserva_por_codigo(codigo, reservas):
    """Busca una reserva por su código"""
    if not codigo or codigo.strip() == "":
        print('\n❌ El código no puede estar vacío.\n')
        return None
    
    if len(reservas) == 0:
        print('\n⚠️  No hay reservas registradas.\n')
        return None
    
    for reserva in reservas:
        if reserva['codigo'].upper() == codigo.upper():
            return reserva
    
    print(f'\n❌ No se encontró reserva con código: {codigo}\n')
    return None

# ============================================================================
# FUNCIÓN 3: CANCELAR RESERVA
# ============================================================================
def cancelar_reserva(codigo, reservas):
    """Cancela una reserva por su código"""
    print('\n' + '=' * 80)
    print(' ' * 30 + 'CANCELAR RESERVA')
    print('=' * 80)
    
    if not codigo or codigo.strip() == "":
        print('\n❌ El código no puede estar vacío.\n')
        print('=' * 80 + '\n')
        return False
    
    if len(reservas) == 0:
        print('\n⚠️  No hay reservas para cancelar.\n')
        print('=' * 80 + '\n')
        return False
    
    for reserva in reservas:
        if reserva['codigo'].upper() == codigo.upper():
            
            # Ya cancelada
            if reserva['estado'] == 'cancelada':
                print(f"\n⚠️  La reserva {codigo} ya está cancelada.\n")
                mostrar_reserva(reserva)
                print('=' * 80 + '\n')
                return False

            # Mostrar datos
            print('\n📋 Datos de la reserva a cancelar:')
            mostrar_reserva(reserva)

            # Confirmar
            confirmacion = input('\n¿Confirma cancelar esta reserva? (S/N): ').strip().upper()

            if confirmacion in ('S', 'SI', 'SÍ', 'Y', 'YES'):
                reserva['estado'] = 'cancelada'
                print('\n✅ Reserva cancelada exitosamente.\n')
                print('=' * 80 + '\n')
                return True
            else:
                print('\n❌ Cancelación abortada.\n')
                print('=' * 80 + '\n')
                return False
    
    print(f'\n❌ No se encontró reserva con código: {codigo}\n')
    print('=' * 80 + '\n')
    return False

# ============================================================================
# FUNCIÓN 4: BUSCAR POR NOMBRE
# ============================================================================
def buscar_por_nombre(nombre, reservas):
    """Busca reservas por nombre (búsqueda parcial)"""
    print('\n' + '=' * 80)
    print(' ' * 25 + 'BÚSQUEDA POR NOMBRE')
    print('=' * 80)
    
    if not nombre or nombre.strip() == "":
        print('\n❌ El nombre no puede estar vacío.\n')
        print('=' * 80 + '\n')
        return []
    
    if len(reservas) == 0:
        print('\n⚠️  No hay reservas registradas.\n')
        print('=' * 80 + '\n')
        return []
    
    resultados = [
        r for r in reservas
        if nombre.lower() in r['nombre'].lower()
    ]
    
    if len(resultados) == 0:
        print(f"\n❌ No se encontraron reservas para: {nombre}\n")
        print('=' * 80 + '\n')
        return []

    print(f"\n✅ Se encontraron {len(resultados)} reserva(s):\n")
    
    for i, reserva in enumerate(resultados, 1):
        print(f"\n--- Resultado {i} ---")
        mostrar_reserva(reserva)
    
    print('=' * 80 + '\n')
    return resultados

# ============================================================================
# FUNCIÓN 5: BUSCAR POR FECHA
# ============================================================================
def buscar_por_fecha(fecha, reservas):
    """Busca reservas por fecha exacta"""
    print('\n' + '=' * 80)
    print(' ' * 30 + 'BÚSQUEDA POR FECHA')
    print('=' * 80)
    
    if not fecha or fecha.strip() == "":
        print('\n❌ La fecha no puede estar vacía.\n')
        print('=' * 80 + '\n')
        return []
    
    if len(reservas) == 0:
        print('\n⚠️  No hay reservas registradas.\n')
        print('=' * 80 + '\n')
        return []
    
    resultados = [r for r in reservas if r['fecha'] == fecha]
    
    if len(resultados) == 0:
        print(f'\n❌ No se encontraron reservas para: {fecha}\n')
        print('=' * 80 + '\n')
        return []
    
    print(f'\n✅ Se encontraron {len(resultados)} reserva(s):\n')
    
    for i, reserva in enumerate(resultados, 1):
        print(f"\n--- Resultado {i} ---")
        mostrar_reserva(reserva)
    
    print('=' * 80 + '\n')
    return resultados

# ============================================================================
# FUNCIÓN 6: BUSCAR POR SERVICIO
# ============================================================================
def buscar_por_servicio(servicio, reservas):
    """Busca reservas por tipo de servicio"""
    print('\n' + '=' * 80)
    print(' ' * 28 + 'BÚSQUEDA POR SERVICIO')
    print('=' * 80)
    
    if not servicio or servicio.strip() == "":
        print('\n❌ El servicio no puede estar vacío.\n')
        print('=' * 80 + '\n')
        return []
    
    if len(reservas) == 0:
        print('\n⚠️  No hay reservas registradas.\n')
        print('=' * 80 + '\n')
        return []
    
    resultados = [
        r for r in reservas
        if servicio.lower() in r['servicio'].lower()
    ]
    
    if len(resultados) == 0:
        print(f'\n❌ No se encontraron reservas de: {servicio}\n')
        print('=' * 80 + '\n')
        return []
    
    print(f'\n✅ Se encontraron {len(resultados)} reserva(s):\n')
    
    for i, reserva in enumerate(resultados, 1):
        print(f"\n--- Resultado {i} ---")
        mostrar_reserva(reserva)
    
    print('=' * 80 + '\n')
    return resultados

# ============================================================================
# MENÚ DE BÚSQUEDA AVANZADA
# ============================================================================
def menu_busqueda_avanzada(reservas):
    """Menú interactivo para búsquedas"""
    while True:
        print('\n' + '=' * 80)
        print(' ' * 28 + 'BÚSQUEDA AVANZADA')
        print('=' * 80)
        print('  1. Buscar por código')
        print('  2. Buscar por nombre')
        print('  3. Buscar por fecha')
        print('  4. Buscar por servicio')
        print('  5. Volver al menú principal')
        print('=' * 80)
        
        opcion = input('\nSeleccione una opción (1-5): ').strip()
        
        if opcion == '1':
            codigo = input('\nCódigo de reserva: ').strip()
            reserva = buscar_reserva_por_codigo(codigo, reservas)
            if reserva:
                print('\n✅ Reserva encontrada:')
                mostrar_reserva(reserva)
                input('\nPresione Enter para continuar...')
        
        elif opcion == '2':
            nombre = input('\nNombre del cliente: ').strip()
            buscar_por_nombre(nombre, reservas)
            input('\nPresione Enter para continuar...')
        
        elif opcion == '3':
            fecha = input('\nFecha (DD/MM/AAAA): ').strip()
            buscar_por_fecha(fecha, reservas)
            input('\nPresione Enter para continuar...')
        
        elif opcion == '4':
            servicio = input('\nTipo de servicio: ').strip()
            buscar_por_servicio(servicio, reservas)
            input('\nPresione Enter para continuar...')
        
        elif opcion == '5':
            print('\n👋 Volviendo al menú principal...\n')
            break
        
        else:
            print('\n❌ Opción inválida. Seleccione 1-5.\n')

            input('Presione Enter para continuar...')

