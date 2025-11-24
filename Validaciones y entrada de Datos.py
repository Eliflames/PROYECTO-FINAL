reservas = {}
validacion_fechas = [] 
import datetime

"""este es un modulo(import)el cual se engarga de facilitar las validaciones,entradas y datos-
    con relacion a fechas y el tiempo"""

def validacion_dato_de_la_fecha(fecha):    
    """Valida que `fecha` tenga formato DD-MM-YYYY(dia,mes y año) y sea una fecha verdadera.

    Usa datetime.datetime.strptime para validar el calendario (incluye meses, días
    correctos y los  años si son  bisiestos).
    """
    try:
        
        datetime.datetime.strptime(fecha, "%d-%m-%Y") 
        """Valida si la fecha es correcta en el calendario para ser ingresada""" 
        return True
    
    except ValueError:
        """aqui se evalua la excepcion de si la fecha es erronea"""
        return False
        """este determinara si la fecha que se ingreso en erronea o imposible de ingresar"""

def horario_laboral():
    """Valida que la hora ingresada esté dentro del horario laboral."""
    hora_inicio = 12  # 12 PM PD: el formato de horas es de 24 horas 
    hora_fin = 23     # 11 PM
    """aqui se le pide al usuario que ingrese la hora a la que desea hacer la reserva"""
    while True:
        hora_input = input("Ingrese la hora de la reserva (HH:MM): ")

        try:
            hora, minuto = map(int, hora_input.split(':'))
            
            if 0 <= minuto < 60:  # se usa este rango de minutos como los validos
                if hora_inicio <= hora < hora_fin:
                    return f"{hora:02d}:{minuto:02d}"
                    """la funcion de arriba permita que se muestre la hora y minuto en formato de dos- 
                    digitos como tambien muestra las horas en pantalla pd:el que me lo borre es (MARICON)"""
                else:
                    print(f"La hora debe estar entre {hora_inicio}:00 y {hora_fin}:00.")
            else:
                print("Minutos inválidos. Use 00 a 59.")

        except ValueError:
            print("Formato inválido. Use HH:MM.")

"""y si las horas y minutos ingresadas no estan dentro del rango de tiempo establecido se le indicara- 
-al usuario que ingrese una hora valida"""

def validar_numero_de_clientes(personas):
    """Valida que el número de personas sea un entero positivo."""
    try:
        #el numero de clientes se convierte a entero
        num_clientes = int(personas)
        #si el numero de clientes es mayor o igual a 1, retornara verdadero
        if num_clientes >= 1:
            return True, num_clientes
        else:
            return False, None
        #aqui se evalua si el numero de clientes es menor a 1 estara en falso
    except ValueError:
        #aqui se evalua la excepcion de si el valor no es un numero entero
        return False, None
    
def solicitar_datos_para_la_reserva(): # recaba todos los datos y devuelve un diccionario
    """Solicita todos los datos necesarios para una reserva al usuario.

    Returns:
        dict: Diccionario con estructura:
              {
                  'nombre': str,
                  'fecha': str (DD-MM-YYYY),
                  'horario': str (HH:MM),
                  'personas': int,
                  'codigo': ''
              }
    """
    datos_de_la_reserva = {}

    # Solicitar nombre
    datos_de_la_reserva['nombre'] = input("Ingrese su nombre: ").strip()

    # Solicitar y validar fecha
    while True:
        fecha = input("Ingrese la fecha (DD-MM-YYYY): ").strip()
        if validacion_dato_de_la_fecha(fecha):
            datos_de_la_reserva['fecha'] = fecha
            break
        else:
            print("Formato de fecha inválido. Use DD-MM-YYYY")

    # Solicitar y validar horario
    datos_de_la_reserva['horario'] = horario_laboral()

    # Solicitar y validar número de personas
    while True:
        personas = input("Ingrese el número de personas: ").strip()
        valido, numero = validar_numero_de_clientes(personas)
        if valido:
            datos_de_la_reserva['personas'] = numero
            break
        else:
            print("El número de personas debe ser mayor a 0")

    # Código vacío según especificación
    datos_de_la_reserva['codigo'] = ''
    return datos_de_la_reserva
    
    
            #aqui es donde se le indica al usuario que ingrese un numero entero valido


"""Ejemplos de pruebo del uso del programa"""

if __name__ == "__main__":
    print(validacion_dato_de_la_fecha("31-10-2025"))  # Fecha Valida

    print(validacion_dato_de_la_fecha("10-15-2023"))  # Fecha Invalida
    print(horario_laboral())  # Valida si la hora esta dentro del horario laboral

    datos_reserva = solicitar_datos_para_la_reserva()
    print(f"Datos de la reserva: {datos_reserva}")

# Si quieres construir un diccionario de reserva, crea una función o una variable
# con los valores actuales (nombre, fecha, horario, personas, servicio). No se
# deben usar variables no definidas al nivel superior del módulo.


    





