

#FUNCIÓN AUXILIAR: MOSTRAR UNA RESERVA EN FORMATO BONITA
def mostrar_reserva(reserva):

        print('-' * 80)
        print(f'Codigo:    {reserva['codigo']}')
        print(f'Nombre:    {reserva['nombre']}')
        print(f'Servicio:  {reserva['servicio']}')
        print(f'Fecha:     {reserva['fecha']}')
        print(f'Horario:   {reserva['horario']}')
        print(f'Personas:  {reserva['personas']}')
        print(f'Estado:    {reserva['estado'].upper()}')
        print('-' * 80)
        print('-----------------------------')

# FUNCIÓN 1: LISTAR TODAS LAS RESERVAS EN FORMATO TABLA
def listar_todas_reservas(reservas):

        print('\n' + '=' * 100)
        print('' * 35 + 'DETALLES DE LA RESERVA')
        print('=' * 100)
        
        # MANEJO DE ERRORES SIMPLIFICADO
        if len(reservas) == 0:
            print('\n ⚠️ No hay reservas para mostrar.\n')
            print('=' * 100 + '\n')
            return
        
        # Encabezados de tabla
        print(f'{'codigo':<20} {'nombre':<20} {'servicio':<20} {'fecha':<12} {'horario':<8} {'personas':<6} {'estado':<10}')
        print('-' * 100)
        
        # Mostrar cada reserva
        for reserva in reservas:
            # Usar Simbolos segun estado
            estado_visual = reserva['estado']
            if reserva['estado'] == 'activa':
                estado_visual = '✅ Activa'
            elif reserva['estado'] == 'cancelada':
                estado_visual = '❌ Cancelada'
            elif reserva['estado'] == 'pendiente':
                estado_visual = '⏳ Pendiente'
            
            print(f'{reserva['codigo']:<20} '
                    f'{reserva['nombre']:<20} '
                    f'{reserva['servicio']:<20} '
                    f'{reserva['fecha']:<12} '
                    f'{reserva['horario']:<8} '
                    f'{reserva['personas']:<6} '
                    f'{estado_visual:<10}')
            
            print('-' * 100)
            print(f' Total reservas: {len(reservas)}')
            print('=' * 100 + '\n')


 #FUNCION 2: BUSQUEDA DE RESERVA POR CODIGO

def buscar_reserva_por_codigo(codigo, reservas):
        # MANEJO DE ERROR: Código vacío
    if not codigo or codigo.strip() == "":
        print('\n ❌ El código de reserva no puede estar vacío.\n')
        return None
    
    # MANEJO DE ERROR: Lista vacía
    if len(reservas) == 0:
        print('\n ⚠️ No hay reservas para buscar.\n')
        return None
    
    # Buscar la reserva
    for reserva in reservas:
        if reserva['codigo'].upper() == codigo.upper(): # Ignorar mayúsculas/minúsculas
            return reserva
    
    # MANEJO DE ERROR: Código no encontrado
    print(f'\n ❌ No se encontró ninguna reserva con el código: {codigo}\n')
    return None


# FUNCIÓN 3: CANCELAR RESERVA

def cancelar_reserva(codigo, reservas):
    
    print('\n' + '=' * 80)
    print(' ' * 30 + 'CANCELAR RESERVA')
    print('=' * 80)
    
    #MANEJO DE ERROR: Código vacío
    if not codigo or codigo.strip() == "":
        print('\n ❌ El código de reserva no puede estar vacío.\n')
        print('=' * 80 + '\n')
        return False
    
    # MANEJO DE ERROR: Lista vacía
    if len(reservas) == 0:
        print('\n ⚠️ No hay reservas para cancelar.\n')
        print('=' * 80 + '\n')
        return False
    
    # Buscar la reserva
    for reserva in reservas:
        if reserva['codigo'].upper() == codigo.upper():
            
            #MANEJO DE ERROR: Reserva ya cancelada
            if reserva['estado'] == 'cancelada':
                print(f'\n ⚠️ La reserva con código {codigo} ya está cancelada.\n')
                mostrar_reserva(reserva)
                print('=' * 80 + '\n')
                return False
            
            # Mostrar datos antes de cancelar
            print('\n🧾 Datos de la reserva a cancelar:')
            mostrar_reserva(reserva)
            
            # Confirmar cancelación
            confirmacion = input('\n ¿Estás seguro de que deseas cancelar esta reserva? (S/N): ').strip().upper()
            
            if confirmacion == 'S' or confirmacion == 'SI' or confirmacion == 'Y' or confirmacion == 'YES' or confirmacion == 'SÍ':
                # Cancelar la reserva
                reserva['estado'] = 'cancelada'
                print('\n ✅ La reserva ha sido cancelada exitosamente.\n')
                print('=' * 80 + '\n')
                return True
            elif confirmacion == 'N' or confirmacion == 'NO' or confirmacion == 'NOT':
                print('\n ❌ La cancelación ha sido abortada por el usuario.\n')
                print('=' * 80 + '\n')
                return False
            else:
                print("\n ❌ Respuesta no valida. Se cancela la operación")
                
    # MANEJO DE ERROR: Código no encontrado
    print(f'\n ❌ No se encontró ninguna reserva con el código: {codigo}\n')
    print('=' * 80 + '\n')
    return False


# FUNCION 4: BUSQUEDA DE NOMBRE

def buscar_por_nombre(nombre, reservas):
    
    print('\n' + '=' * 80)
    print(' ' * 25 + 'BUSCAR RESERVA POR NOMBRE')
    print('=' * 80)
    
    # MANEJO DE ERROR: Nombre vacío
    if not nombre or nombre.strip() == "":
        print('\n ❌ El nombre no puede estar vacío.\n')
        print('=' * 80 + '\n')
        return []
    
    # MANEJO DE ERROR: Lista vacía
    if len(reservas) == 0:
        print('\n ⚠️ No hay reservas para buscar.\n')
        print('=' * 80 + '\n')
        return []
    
    # Buscar reservas que contengan el nombre (búsqueda parcial)
    resultados = []
    for reserva in reservas:
        if nombre.lower() in reserva['nombre'].lower(): # Ignorar mayúsculas/minúsculas
            resultados.append(reserva)
    
    # Mostrar resultados
    if len(resultados) == 0:
        print(f'\n ❌ No se encontraron reservas para el nombre: {nombre}\n')       
        print('=' * 80 + '\n')
        return []
    
    #Mostrar resultados
    
    if len(resultados) > 0:
        print(f'\n ✅ Se encontraron {len(resultados)} reservas para el nombre: {nombre}\n')
    else:
        print(f'\n ⚠️ No se encontraron reservas para el cliente: {nombre}\n')
        print('=' * 80 + '\n')
        return []
    
    for i, reserva in enumerate(resultados, 1):
        print(f'\n--- Reserva {i} ---')
        mostrar_reserva(reserva)
    
    print('=' * 80 + '\n')
    return resultados

# FUNCION 5: BUSQUEDA POR FECHA

def buscar_por_fecha(fecha, reservas):

    print('\n' + '=' * 80)
    print(' ' * 30 + 'BUSCAR RESERVA POR FECHA')
    print('=' * 80)
    
    # MANEJO DE ERROR: Fecha vacía
    if not fecha or fecha.strip() == "":
        print('\n ❌ La fecha no puede estar vacía.\n')
        print('=' * 80 + '\n')
        return []
    
    # MANEJO DE ERROR: Lista vacía
    if len(reservas) == 0:
        print('\n ⚠️ No hay reservas para buscar.\n')
        print('=' * 80 + '\n')
        return []
    
    # Buscar reservas por fecha exacta
    resultados = []
    for reserva in reservas:
        if reserva['fecha'] == fecha:
            resultados.append(reserva)
    
    # Mostrar resultados
    if len(resultados) == 0:
        print(f'\n ❌ No se encontraron reservas para la fecha: {fecha}\n')       
        print('=' * 80 + '\n')
        return []
    
    print(f'\n ✅ Se encontraron {len(resultados)} reservas para la fecha: {fecha}\n')
    
    for i, reserva in enumerate(resultados, 1):
        print(f'\n--- Reserva {i} ---')
        mostrar_reserva(reserva)
    
    print('=' * 80 + '\n')
    return resultados


# FUNCIÓN 6: BUSQUEDA POR SERVICIO

def buscar_por_servicio(servicio, reservas):
    
    print('\n' + '=' * 80)
    print(' ' * 28 + 'BUSCAR RESERVA POR SERVICIO')
    print('=' * 80)
    
    # MANEJO DE ERROR: Servicio vacío
    if not servicio or servicio.strip() == "":
        print('\n ❌ El servicio no puede estar vacío.\n')
        print('=' * 80 + '\n')
        return []
    
    # MANEJO DE ERROR: Lista vacía
    if len(reservas) == 0:
        print('\n ⚠️ No hay reservas para buscar.\n')
        print('=' * 80 + '\n')
        return []
    # Buscar reservas que contengan el servicio (búsqueda parcial)
    resultados = []
    for reserva in reservas:
        if servicio.lower() in reserva['servicio'].lower(): # Ignorar mayúsculas/minúsculas
            resultados.append(reserva)
    
    # Mostrar resultados
    if len(resultados) == 0:
        print(f'\n ❌ No se encontraron reservas para el servicio: {servicio}\n')       
        print('=' * 80 + '\n')
        return []
    
    print(f'\n ✅ Se encontraron {len(resultados)} reservas para el servicio: {servicio}\n')
    
    for i, reserva in enumerate(resultados, 1):
        print(f'\n--- Reserva {i} ---')
        mostrar_reserva(reserva)
    
    print('=' * 80 + '\n')
    return resultados


# MENÚ DE BÚSQUEDA AVANZADA

def menu_busqueda_avanzada(reservas):
    while True:
        print('\n' + '=' * 80)
        print(' ' * 30 + 'MENÚ DE BÚSQUEDA AVANZADA')
        print('=' * 80)
        print('1. Buscar por Nombre')
        print('2. Buscar por Fecha')
        print('3. Buscar por Servicio')
        print('4. Volver al Menú Principal')
        
        opcion = input('\nSeleccione una opción (1-4): ').strip()
        
        if opcion == '1':
            nombre = input('\nIngrese el nombre del cliente a buscar: ').strip()
            buscar_por_nombre(nombre, reservas)
        elif opcion == '2':
            fecha = input('\nIngrese la fecha (DD/MM/AAAA) a buscar: ').strip()
            buscar_por_fecha(fecha, reservas)
        elif opcion == '3':
            servicio = input('\nIngrese el servicio a buscar: ').strip()
            buscar_por_servicio(servicio, reservas)
        elif opcion == '4':
            print('\n Volviendo al menú principal...\n')
            break
        else:
            print('\n ❌ Opción inválida. Por favor, seleccione una opción válida (1-4).\n')



#prueba de ejecución




