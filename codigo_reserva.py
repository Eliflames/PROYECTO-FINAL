# PARTE 2: CÓDIGOS Y DISPONIBILIDAD
from datetime import datetime, date
from typing import List, Dict

# ============================================================================
# FUNCIÓN 1: GENERAR CÓDIGO ÚNICO
# ============================================================================
def generar_codigo_unico(reservas: List[Dict]) -> str:
    """
    Genera un código único con formato RES-AAAAMMDD-###
    """
    hoy_str = date.today().strftime('%Y%m%d')
    prefijo = f"RES-{hoy_str}-"

    # Tomar solo los códigos que pertenecen al día actual
    usados_hoy = {
        r['codigo']
        for r in reservas
        if r.get('codigo', '').startswith(prefijo)
    }

    # Buscar el primer número libre
    for i in range(1, 1000):
        codigo = f"{prefijo}{i:03d}"
        if codigo not in usados_hoy:
            return codigo

    raise RuntimeError("No quedan códigos disponibles para hoy (límite 999).")

# ============================================================================
# FUNCIÓN 2: VERIFICAR DISPONIBILIDAD
# ============================================================================
def verificar_disponibilidad(fecha: str, horario: str, servicio: str, reservas: List[Dict]) -> bool:
    """
    Verifica disponibilidad para fecha/horario/servicio.
    Reglas:
    - Fecha válida y no en pasado
    - Máximo 3 reservas activas por combinación
    """
    try:
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y').date()
    except ValueError:
        return False

    if fecha_dt < date.today():
        return False

    # Solo contar reservas ACTIVAS
    coincidencias = sum(
        1 for r in reservas
        if r.get('fecha') == fecha
        and r.get('horario') == horario
        and r.get('servicio') == servicio
        and r.get('estado') == 'activa'  # ✅ Solo contar activas
    )

    return coincidencias < 3

# ============================================================================
# FUNCIÓN 3: ASIGNAR CÓDIGO A RESERVA
# ============================================================================
def asignar_codigo_a_reserva(reserva: Dict, reservas: List[Dict]) -> Dict:
    """
    Asigna un código único a una reserva.
    ⚠️ NO agrega la reserva a la lista (eso lo hace main.py)
    """
    # Generar y asignar código
    reserva['codigo'] = generar_codigo_unico(reservas)
    
    # ✅ CORREGIDO: NO agregar aquí
    # reservas.append(reserva)  # ❌ ESTO CAUSABA EL DUPLICADO
    
    return reserva