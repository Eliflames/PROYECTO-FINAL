

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
    # Intentar parsear la fecha con formatos comunes (DD-MM-YYYY y DD/MM/YYYY)
    fecha_dt = None
    for fmt in ('%d-%m-%Y', '%d/%m/%Y'):
        try:
            fecha_dt = datetime.strptime(fecha, fmt).date()
            break
        except ValueError:
            continue

    if fecha_dt is None:
        return False

    if fecha_dt < date.today():
        return False

    # Comparar normalizando las fechas de las reservas
    def _parse_reserva_fecha(f):
        if not f:
            return None
        for fmt in ('%d-%m-%Y', '%d/%m/%Y'):
            try:
                return datetime.strptime(f, fmt).date()
            except Exception:
                continue
        return None

    coincidencias = 0
    for r in reservas:
        r_fecha = _parse_reserva_fecha(r.get('fecha'))
        if r_fecha == fecha_dt and r.get('horario') == horario and r.get('servicio') == servicio:
            coincidencias += 1

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
    return reserva



