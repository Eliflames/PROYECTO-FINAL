

from datetime import datetime, date
from typing import List, Dict


# -------------------------------------------------------------------
# FUNCIONES OPTIMIZADAS
# -------------------------------------------------------------------

def generar_codigo_unico(reservas: List[Dict]) -> str:
    """
    Genera un código único con formato RES-AAAAMMDD-### basado en la fecha actual.
    Optimizado: solo compara con códigos del día actual para mayor eficiencia.
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


def verificar_disponibilidad(fecha: str, horario: str, servicio: str, reservas: List[Dict]) -> bool:
    """
    Verifica disponibilidad para fecha/horario/servicio.
    Reglas:
    - Fecha válida y no en pasado.
    - Máximo 3 reservas por combinación.
    """
    try:
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y').date()
    except ValueError:
        return False

    if fecha_dt < date.today():
        return False

    coincidencias = sum(
        1 for r in reservas
        if r.get('fecha') == fecha
        and r.get('horario') == horario
        and r.get('servicio') == servicio
    )

    return coincidencias < 3


def asignar_codigo_a_reserva(reserva: Dict, reservas: List[Dict]) -> Dict:
    """
    Asigna un código único a una reserva nueva, validando disponibilidad
    cuando se ingresa fecha+horario+servicio.
    """
    requiere_validación = all(k in reserva for k in ('fecha', 'horario', 'servicio'))

    if requiere_validación:
        disponible = verificar_disponibilidad(
            reserva['fecha'], reserva['horario'], reserva['servicio'], reservas
        )
        if not disponible:
            raise ValueError("No hay disponibilidad para la reserva indicada.")

    reserva['codigo'] = generar_codigo_unico(reservas)
    reservas.append(reserva)
    return reserva



