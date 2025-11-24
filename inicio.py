"""hola people"""
"""hola"""

# FUNION 1: VALIDAR FECHA

def validar_fecha(fecha):
    
    if len(fecha) != 10:
        return False
    
    partes = fecha.split('/')
    if len(partes) != 3:
        return False
    
    dia, mes, año = partes
    
    if not (dia.isdigit() and mes.isdigit() and año.isdigit()):
        return False
    
    dia = int(dia)
    mes = int(mes)
    año = int(año)
    
    if dia < 1 or dia > 31:
        return False
    if mes < 1 or mes > 12:
        return False    
    if año < 2025 or año > 2030:
        return False
    
    return True

# FUNION 2: VALIDAR HORARIO

def validar_horario(hora):
    
    if len(hora) != 5:
        return False
    
    partes = hora.split(':')
    if len(partes) != 2:
        return False
    
    horas, minutos = partes
    
    if not (horas.isdigit() and minutos.isdigit()):
        return False
    
    horas = int(horas)
    minutos = int(minutos)
    
    if horas < 0 or horas > 23:
        return False
    if minutos < 0 or minutos > 59:
        return False
    
    return True

def validar_personas(personas):
    
    if not isinstance(personas, int):
        return False
    
    if personas <= 0:
        return False
    return True

# FUNION 3: SOLICITAR DATOS DE RESERVA

def solicitar_datos_reserva():
    
    print('\n' + '='*50)
    print('            INGRESAR DATOS DE RESERVA')
    print('='*50)
    
    #solicitar nombre
    
    while True:
        nombre = input('\nIngrese su nombre completo: ').strip()
        if nombre == '':
            print('❌: El nombre no puede estar vacío. Intente nuevamente.')
        else:
            break
        
    #solicitar servicio
    print('\nTipos de servicio')
    print('Sala de reuniones')
    print('2. Mesa de restaurante')
    print('3. Evento especial')
    print('4. Sala de conferencias')
    
    while True:
        opcion = input('\nSeleccione el tipo de servicio (1-4): ').strip()
        servicios = {
            '1': 'Sala de reuniones',
            '2': 'Mesa de restaurante',
            '3': 'Evento especial',
            '4': 'Sala de conferencias'
        }
        if opcion in servicios:
            servicios = servicios[opcion]
            break
        else:
            print('❌: Opción inválida. Intente nuevamente.')
    
    #solicitar fecha
    
    while True:
        fecha = input('\nIngrese la fecha de la reserva (DD/MM/AAAA): ').strip()
        if validar_fecha(fecha):
            break
        else:
            print('❌ Error: Formato de fecha no válido. Intente nuevamente.')
            print('  Ejemplo: 25/12/2025')
    
    #solicitar horario
    
    while True:
        horario = input('\nIngrese la hora de la reserva (HH:MM): ').strip()
        if validar_horario(horario):
            break
        else:
            print('❌ Error: Formato de hora no válido. Intente nuevamente.')
            print('  Ejemplo: 19:00')
    
    #solicitar numero de personas
    
    while True:
        personas_str = input('\nIngrese el número de personas para la reserva: ').strip()
        if personas_str.isdigit() and int(personas_str) > 0:
            personas = int(personas_str)
            break
        else:
            print('❌ Error: Ingrese un número válido de personas (mayor que 0). Intente nuevamente.')
            
    # Crear y retornar diccionario
    reservas = {
        'codigo': '',  # Vacío, lo llenará Programador 2
        'nombre': nombre,
        'servicio': servicios,
        'fecha': fecha,
        'horario': horario,
        'personas': personas,
        'estado': 'activa'
    }
    return reservas
