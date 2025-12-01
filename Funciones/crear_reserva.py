

# PARTE 1: VALIDACIONES Y ENTRADA DE DATOS
from datetime import datetime, timedelta

# ============================================================================
# CONFIGURACIÓN: LÍMITES DEL SISTEMA
# ============================================================================
PERSONAS_MINIMO = 1
PERSONAS_MAXIMO = 100  # Límite máximo de personas por reserva

#  Límite de días adelantados para reservar
DIAS_ADELANTADOS_MAXIMO = 15  # Máximo 15 días en el futuro

#  Horarios permitidos
HORA_INICIO = "08:00"  # Horario de apertura
HORA_CIERRE = "23:00"  # Horario de cierre (última reserva)

# ============================================================================
# FUNCIÓN 1: VALIDAR FECHA
# ============================================================================
def validar_fecha(fecha):

    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        hoy = datetime.now().date()
        fecha_limite = hoy + timedelta(days=DIAS_ADELANTADOS_MAXIMO)

        # Verificar que la fecha no esté en el pasado
        if fecha_dt.date() < hoy:
            return False, "La fecha no puede estar en el pasado."

        #  Verificar que no supere el límite de días adelantados
        if fecha_dt.date() > fecha_limite:
            return False, f"Solo se pueden hacer reservas hasta {DIAS_ADELANTADOS_MAXIMO} días adelantados."

        return True, "Fecha válida"

    except ValueError:
        return False, "Formato de fecha inválido."

# ============================================================================
# FUNCIÓN 2: VALIDAR HORARIO
# ============================================================================
def validar_horario(hora):

    try:
        hora_dt = datetime.strptime(hora, "%H:%M").time()
        hora_inicio_dt = datetime.strptime(HORA_INICIO, "%H:%M").time()
        hora_cierre_dt = datetime.strptime(HORA_CIERRE, "%H:%M").time()
        
        #  Verificar que esté dentro del horario de operación
        if hora_dt < hora_inicio_dt or hora_dt > hora_cierre_dt:
            return False, f"El horario debe estar entre {HORA_INICIO} y {HORA_CIERRE}."
        
        return True, "Horario válido"
        
    except ValueError:
        return False, "Formato de horario inválido."


# FUNCIÓN 3: VALIDAR FECHA Y HORARIO JUNTOS
# ============================================================================
def validar_fecha_y_horario(fecha, horario):

    try:
        # Convertir strings a objetos datetime
        reserva_dt = datetime.strptime(f"{fecha} {horario}", "%d/%m/%Y %H:%M")
        
        # Fecha y hora actual
        ahora_dt = datetime.now()
        
        # Validar que la reserva no esté en el pasado
        if reserva_dt <= ahora_dt:
            return False, "La fecha y hora no pueden estar en el pasado."
        
        return True, "Fecha y horario válidos"
    
    except ValueError:
        return False, "Error al validar fecha y horario."


# FUNCIÓN 4: VALIDAR NÚMERO DE PERSONAS
# ============================================================================
def validar_personas(personas):
    """
    Valida que el número de personas sea válido:
    - Debe ser un entero
    - Debe estar entre PERSONAS_MINIMO y PERSONAS_MAXIMO
    """
    if not isinstance(personas, int):
        return False
    
    if personas < PERSONAS_MINIMO or personas > PERSONAS_MAXIMO:
        return False
    
    return True


#  NUEVA FUNCIÓN: CONFIGURAR LÍMITES DEL SISTEMA
# ============================================================================
def configurar_limites():

    global DIAS_ADELANTADOS_MAXIMO, HORA_INICIO, HORA_CIERRE, PERSONAS_MAXIMO
    
    print('\n' + '='*70)
    print('         CONFIGURACIÓN DE LÍMITES DEL SISTEMA')
    print('='*70)
    print('\n📋 Configuración actual:')
    print(f'  • Días adelantados máximo:  {DIAS_ADELANTADOS_MAXIMO} días')
    print(f'  • Horario de apertura:      {HORA_INICIO}')
    print(f'  • Horario de cierre:        {HORA_CIERRE}')
    print(f'  • Personas máximo:          {PERSONAS_MAXIMO}')
    print('='*70)
    
    # Configurar días adelantados
    while True:
        respuesta = input('\n¿Desea cambiar los días adelantados? (S/N): ').strip().upper()
        if respuesta in ('S', 'SI', 'SÍ'):
            while True:
                dias = input(f'Ingrese nuevos días adelantados (1-365) [actual: {DIAS_ADELANTADOS_MAXIMO}]: ').strip()
                if dias.isdigit() and 1 <= int(dias) <= 365:
                    DIAS_ADELANTADOS_MAXIMO = int(dias)
                    print(f'✅ Días adelantados configurados a: {DIAS_ADELANTADOS_MAXIMO}')
                    break
                else:
                    print('❌ Error: Ingrese un número entre 1 y 365.')
            break
        elif respuesta in ('N', 'NO'):
            break
        else:
            print('❌ Respuesta inválida. Ingrese S o N.')
    
    # Configurar horario de apertura
    while True:
        respuesta = input('\n¿Desea cambiar el horario de apertura? (S/N): ').strip().upper()
        if respuesta in ('S', 'SI', 'SÍ'):
            while True:
                hora = input(f'Ingrese nuevo horario de apertura (HH:MM) [actual: {HORA_INICIO}]: ').strip()
                try:
                    datetime.strptime(hora, "%H:%M")
                    HORA_INICIO = hora
                    print(f'✅ Horario de apertura configurado a: {HORA_INICIO}')
                    break
                except ValueError:
                    print('❌ Error: Formato inválido. Use HH:MM (ej: 08:00)')
            break
        elif respuesta in ('N', 'NO'):
            break
        else:
            print('❌ Respuesta inválida. Ingrese S o N.')
    
    # Configurar horario de cierre
    while True:
        respuesta = input('\n¿Desea cambiar el horario de cierre? (S/N): ').strip().upper()
        if respuesta in ('S', 'SI', 'SÍ'):
            while True:
                hora = input(f'Ingrese nuevo horario de cierre (HH:MM) [actual: {HORA_CIERRE}]: ').strip()
                try:
                    hora_dt = datetime.strptime(hora, "%H:%M").time()
                    hora_inicio_dt = datetime.strptime(HORA_INICIO, "%H:%M").time()
                    
                    if hora_dt <= hora_inicio_dt:
                        print(f'❌ Error: El horario de cierre debe ser después de {HORA_INICIO}')
                        continue
                    
                    HORA_CIERRE = hora
                    print(f'✅ Horario de cierre configurado a: {HORA_CIERRE}')
                    break
                except ValueError:
                    print('❌ Error: Formato inválido. Use HH:MM (ej: 23:00)')
            break
        elif respuesta in ('N', 'NO'):
            break
        else:
            print('❌ Respuesta inválida. Ingrese S o N.')
    
    # Configurar personas máximo
    while True:
        respuesta = input('\n¿Desea cambiar el límite de personas? (S/N): ').strip().upper()
        if respuesta in ('S', 'SI', 'SÍ'):
            while True:
                personas = input(f'Ingrese nuevo límite de personas (1-1000) [actual: {PERSONAS_MAXIMO}]: ').strip()
                if personas.isdigit() and 1 <= int(personas) <= 1000:
                    PERSONAS_MAXIMO = int(personas)
                    print(f'✅ Límite de personas configurado a: {PERSONAS_MAXIMO}')
                    break
                else:
                    print('❌ Error: Ingrese un número entre 1 y 1000.')
            break
        elif respuesta in ('N', 'NO'):
            break
        else:
            print('❌ Respuesta inválida. Ingrese S o N.')
    
    print('\n' + '='*70)
    print('✅ CONFIGURACIÓN ACTUALIZADA')
    print('='*70)
    print(f'  • Días adelantados máximo:  {DIAS_ADELANTADOS_MAXIMO} días')
    print(f'  • Horario de apertura:      {HORA_INICIO}')
    print(f'  • Horario de cierre:        {HORA_CIERRE}')
    print(f'  • Personas máximo:          {PERSONAS_MAXIMO}')
    print('='*70)
    input('\nPresione Enter para continuar...')


#  NUEVA FUNCIÓN: MOSTRAR LÍMITES ACTUALES
# ============================================================================
def mostrar_limites():

    print('\n' + '='*70)
    print('         LÍMITES ACTUALES DEL SISTEMA')
    print('='*70)
    print(f'\n  📅 Reservas: Hasta {DIAS_ADELANTADOS_MAXIMO} días adelantados')
    print(f'  🕐 Horario: {HORA_INICIO} - {HORA_CIERRE}')
    print(f'  👥 Personas: {PERSONAS_MINIMO} - {PERSONAS_MAXIMO}')
    print('='*70 + '\n')


# FUNCIÓN 5: SOLICITAR DATOS DE RESERVA
# ============================================================================
def solicitar_datos_reserva():

    print('\n' + '='*70)
    print('            INGRESAR DATOS DE RESERVA')
    print('='*70)
    
    # Mostrar límites actuales
    print(f'\n📋 Límites actuales:')
    print(f'  • Reservas hasta: {DIAS_ADELANTADOS_MAXIMO} días adelantados')
    print(f'  • Horario: {HORA_INICIO} - {HORA_CIERRE}')
    print(f'  • Personas: {PERSONAS_MINIMO} - {PERSONAS_MAXIMO}')
    
    
    # SOLICITAR NOMBRE
    # ========================================
    while True:
        nombre = input('\n👤 Ingrese su nombre completo: ').strip() # Arreglado 
        if nombre == '' or nombre.isdigit():
            print('❌ El nombre no puede estar vacío ni ser un numero. Intente nuevamente.')
        else:
            break
    
    
    # SOLICITAR SERVICIO
    # ========================================
    print('\n📋 Tipos de servicio disponibles:')
    print('  1. Sala de reuniones')
    print('  2. Mesa de restaurante')
    print('  3. Evento especial')
    print('  4. Sala de conferencias')
    
    while True:
        opcion = input('\nSeleccione el tipo de servicio (1-4): ').strip()
        servicios = {
            '1': 'Sala de reuniones',
            '2': 'Mesa de restaurante',
            '3': 'Evento especial',
            '4': 'Sala de conferencias'
        }
        if opcion in servicios:
            servicio = servicios[opcion]
            break
        else:
            print('❌ Opción inválida. Seleccione 1-4.')
    
    
    # SOLICITAR FECHA
    # ========================================
    while True:
        # Calcular fecha máxima
        fecha_maxima = (datetime.now() + timedelta(days=DIAS_ADELANTADOS_MAXIMO)).strftime("%d/%m/%Y")
        
        fecha = input(f'\n📅 Fecha de reserva (DD/MM/AAAA) [hasta {fecha_maxima}]: ').strip()
        es_valida, mensaje = validar_fecha(fecha)
        
        if es_valida:
            break
        else:
            print(f'❌ Error: {mensaje}')
            print('   Ejemplo: 25/12/2025')
    
    
    # SOLICITAR HORARIO
    # ========================================
    while True:
        horario = input(f'\n🕐 Hora de reserva (HH:MM) [{HORA_INICIO} - {HORA_CIERRE}]: ').strip()

        # Validar formato y rango de horario
        es_valido, mensaje = validar_horario(horario)
        if not es_valido:
            print(f'❌ Error: {mensaje}')
            print(f'   Ejemplo: 14:30')
            continue

        # Validar que fecha+horario no esté en el pasado
        es_valida_combinacion, mensaje_combinacion = validar_fecha_y_horario(fecha, horario)
        if not es_valida_combinacion:
            print(f'❌ Error: {mensaje_combinacion}')
            print('   Por favor, ingrese una fecha/hora futura.')
            continue

        break
    
    
    # SOLICITAR NÚMERO DE PERSONAS
    # ========================================
    while True:
        personas_str = input(f'\n👥 Número de personas ({PERSONAS_MINIMO}-{PERSONAS_MAXIMO}): ').strip()
        
        if not personas_str.isdigit():
            print(f'❌ Error: Ingrese un número válido.')
            continue
        
        personas = int(personas_str)
        
        if personas < PERSONAS_MINIMO:
            print(f'❌ Error: Mínimo {PERSONAS_MINIMO} persona(s).')
        elif personas > PERSONAS_MAXIMO:
            print(f'❌ Error: Máximo {PERSONAS_MAXIMO} persona(s) por reserva.')
            print(f'   Para grupos mayores, contacte al administrador.')
        else:
            break
    
    # CREAR DICCIONARIO DE RESERVA
    # ========================================
    reserva = {
        'codigo': '',  # Vacío, lo llenará Programador 2
        'nombre': nombre,
        'servicio': servicio,
        'fecha': fecha,
        'horario': horario,
        'personas': personas,
        'estado': 'activa'
    }
    
    return reserva
    



