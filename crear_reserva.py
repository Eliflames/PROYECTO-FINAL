
# PARTE 1: VALIDACIONES Y ENTRADA DE DATOS
from datetime import datetime

# ============================================================================
# CONFIGURACIÓN: LÍMITES DEL SISTEMA
# ============================================================================
PERSONAS_MINIMO = 1
PERSONAS_MAXIMO = 100  # ✅ Límite máximo de personas por reserva

# ============================================================================
# FUNCIÓN 1: VALIDAR FECHA
# ============================================================================
def validar_fecha(fecha):
    """
    Valida que la fecha:
    - Tenga formato DD/MM/AAAA
    - No esté en el pasado
    """
    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        hoy = datetime.now().date()

        # Verificar que la fecha no esté en el pasado
        if fecha_dt.date() < hoy:
            return False

        return True

    except ValueError:
        return False

# ============================================================================
# FUNCIÓN 2: VALIDAR HORARIO
# ============================================================================
def validar_horario(hora):
    """
    Valida que el horario tenga formato HH:MM válido
    """
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

# ============================================================================
# FUNCIÓN 3: VALIDAR FECHA Y HORARIO JUNTOS
# ============================================================================
def validar_fecha_y_horario(fecha, horario):
    """
    Valida que la combinación fecha+horario no esté en el pasado
    """
    try:
        # Convertir strings a objetos datetime
        reserva_dt = datetime.strptime(f"{fecha} {horario}", "%d/%m/%Y %H:%M")
        
        # Fecha y hora actual
        ahora_dt = datetime.now()
        
        # Validar que la reserva no esté en el pasado
        if reserva_dt <= ahora_dt:
            return False
        return True
    
    except ValueError:
        return False

# ============================================================================
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

# ============================================================================
# FUNCIÓN 5: SOLICITAR DATOS DE RESERVA
# ============================================================================
def solicitar_datos_reserva():
    """
    Solicita todos los datos para crear una reserva
    Valida cada campo antes de aceptarlo
    """
    print('\n' + '='*70)
    print('            INGRESAR DATOS DE RESERVA')
    print('='*70)
    
    # ========================================
    # SOLICITAR NOMBRE
    # ========================================
    while True:
        nombre = input('\n👤 Ingrese su nombre completo: ').strip()
        if nombre == '':
            print('❌ El nombre no puede estar vacío. Intente nuevamente.')
        else:
            break
    
    # ========================================
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
            servicio = servicios[opcion]  # ✅ CORREGIDO: era 'servicios = servicios[opcion]'
            break
        else:
            print('❌ Opción inválida. Seleccione 1-4.')
    
    # ========================================
    # SOLICITAR FECHA
    # ========================================
    while True:
        fecha = input('\n📅 Ingrese la fecha de la reserva (DD/MM/AAAA): ').strip()
        if validar_fecha(fecha):
            break
        else:
            print('❌ Error: Fecha inválida o en el pasado.')
            print('   Ejemplo: 25/12/2025')
    
    # ========================================
    # SOLICITAR HORARIO
    # ========================================
    while True:
        horario = input('\n🕐 Ingrese la hora de la reserva (HH:MM): ').strip()

        if not validar_horario(horario):
            print('❌ Formato inválido. Ejemplo: 19:00')
            continue

        if not validar_fecha_y_horario(fecha, horario):
            print('❌ La fecha y hora no pueden estar en el pasado.')
            print('   Por favor, ingrese una fecha/hora futura.')
            continue

        break
    
    # ========================================
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
    
    # ========================================
    # CREAR DICCIONARIO DE RESERVA
    # ========================================
    reserva = {
        'codigo': '',  # Vacío, lo llenará Programador 2
        'nombre': nombre,
        'servicio': servicio,  # ✅ CORREGIDO
        'fecha': fecha,
        'horario': horario,
        'personas': personas,
        'estado': 'activa'
    }
    
    return reserva