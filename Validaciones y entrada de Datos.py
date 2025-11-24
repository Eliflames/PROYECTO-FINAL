reservas = []
validacion_fechas = [] # Si la funcion es valida no necesitas almacenarla aqui y los datos los debes almacenarlas en el diccionario no en listas
import datetime
"""este es un modulo(import)el cual se engarga de facilitar las validaciones,entradas y datos-
    con relacion a fechas y el tiempo"""
def validacion_dato_de_la_fecha(fecha):          # Te falto validar el Horario y es una funcion aparte
    """Valida que `fecha` tenga formato YYYY-MM-DD(año,mes y dia) y sea una fecha verdadera.

    Usa datetime.datetime.strptime para validar el calendario (incluye meses, días
    correctos y los  años si son  bisiestos).
    """
    try:
        
        datetime.datetime.strptime(fecha, "%Y-%m-%d") # Esto esta mal, la validacion es alreves Ejemplo DD/MM/AAAA 
        """Valida si la fecha es correcta en el calendario para ser ingresada""" 
        return True
    
    except ValueError:
        """aqui se evalua la excepcion de si la fecha es erronea"""
        return False
        """este determinara si la fecha que se ingreso en erronea o imposible de ingresar"""
def agregar_reserva(nombre, fecha):
    if validacion_dato_de_la_fecha(fecha):
        reservas.append({'nombre': nombre, 'fecha': fecha})
        """Agrega la reserva a la lista si la fecha es válida"""
        return "Reserva agregada exitosamente." # Te falto imprimir el str
    else:
        return "Fecha inválida. Use el formato AAAA-MM-DD."
    """esta funcion se encarga de mandar al usuario a que ingrese una fecha correcta"""
def mostrar_reservas():
    return reservas
"""esta funcion se encarga de mostrar las reservas que se han ingresado hasta el momento"""
def validacion_datos_de_ID_de_entrada(valor):# Bro eso no fue lo que te aparecio lo de validar por ID, es validar por numero de personas. Y es otra funcion la que te falto
                                             # Ojo y que la validacion sea > 0
    """esta lo que hace es que valida si el dato ingresado es un numero entero-
     para que sea un ID valido.
     """
    
    try:
        numero = int(valor)
        return True, numero
        """Valida si el valor es un número entero y lo asigna a la variable numero  """
    except ValueError:
        """se evalua si no es un numero entero, retornara falso pd: el none es que el numero es nulo """
        return False, None
def solicitar_datos_para_la_reserva(mensaje): # Aqui hay dos problemitas, 1ro es No solicita: servicio, horario, personas 2do No retorna diccionario completo, 3ro No tiene estructura correcta
                                             # tambien esta funcion valida un ID, no los datos de la reserva
    """esta funcion se encarga de solicitar los datos para la reserva, en este caso el ID"""
    while True:
        """ Solicita al usuario que ingrese un número entero hasta que lo haga correctamente"""
        entrada = input(mensaje)
        es_valida, numero = validacion_datos_de_ID_de_entrada(entrada)
        if es_valida:
            """si el dato es valido, verificar que sea positivo (>= 1)"""
            if numero >= 1:
                return numero
            else:
                print("Entrada inválida. Por favor, ingrese un número entero positivo (>= 1).")
        else:
            """de lo contrario le dira que la entrada es invalida"""
            print("Entrada inválida. Por favor, ingrese un número entero.")
            # Te falto Crear y retornar diccionario COMPLETO
            # Con eso guardas los datos 


"""Ejemplos de pruebo del uso del programa"""
print(agregar_reserva("Juan Perez", "2023-10-15"))

print(agregar_reserva("Maria Gomez", "2023-15-10"))  # Fecha Invalida

print(mostrar_reservas())

num_asistentes = solicitar_datos_para_la_reserva("Ingrese el número de asistentes: ")
print(f"Número de asistentes: {num_asistentes}")


    





