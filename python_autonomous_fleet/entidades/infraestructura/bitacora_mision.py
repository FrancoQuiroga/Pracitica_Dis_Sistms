#!/usr/bin/env python3
"""
Modulo de la Entidad BitacoraMision (Registro).

Analogia de 'RegistroForestal'.
Almacena los datos de una mision completada para persistencia.
"""

from datetime import datetime
from typing import List

class BitacoraMision:
    """
    Entidad de datos que representa un registro de mision para
    auditoria y persistencia (US-503).
    """

    def __init__(self,
                 id_mision: str,
                 id_vehiculo: str,
                 tipo_vehiculo: str,
                 ruta_realizada: List[str],
                 id_operador: str | None = None,
                 incidencias: str = "Ninguna"):
                     
        self.id_mision: str = id_mision
        self.id_vehiculo: str = id_vehiculo
        self.tipo_vehiculo: str = tipo_vehiculo
        self.ruta_realizada: List[str] = ruta_realizada
        self.id_operador: str | None = id_operador
        self.incidencias: str = incidencias
        self.timestamp: datetime = datetime.now()

    def __str__(self) -> str:
        """Representacion en string para mostrar el registro."""
        ruta_str = ' -> '.join(self.ruta_realizada)
        operador_str = self.id_operador if self.id_operador else "N/A (Automatizado)"
        
        return (
            f"\n--- [BITACORA DE MISION: {self.id_mision}] ---\n"
            f"  Fecha/Hora:   {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"  Vehiculo:     {self.id_vehiculo} ({self.tipo_vehiculo})\n"
            f"  Operador:     {operador_str}\n"
            f"  Ruta:         {ruta_str}\n"
            f"  Incidencias:  {self.incidencias}\n"
            f"--------------------------------------"
        )