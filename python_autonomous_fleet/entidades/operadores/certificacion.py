#!/usr/bin/env python3
"""
Modulo de la Entidad Certificacion.

Analogia de 'AptoMedico'.
Representa una licencia o certificacion con fecha de vencimiento.
"""

from datetime import date

class Certificacion:
    """
    Representa una certificacion o licencia que un Operador debe poseer
    para realizar mantenimientos (US-402).
    """

    def __init__(self, nombre_certificacion: str, fecha_vencimiento: date):
        self._nombre_certificacion: str = nombre_certificacion
        self._fecha_vencimiento: date = fecha_vencimiento
        
        if not isinstance(fecha_vencimiento, date):
            raise TypeError("fecha_vencimiento debe ser un objeto datetime.date")

    @property
    def nombre(self) -> str:
        return self._nombre_certificacion

    @property
    def vencimiento(self) -> date:
        return self._fecha_vencimiento

    def esta_vigente(self) -> bool:
        """
        Verifica si la certificacion no ha expirado.
        (Criterio de aceptacion de US-402)
        """
        return date.today() <= self._fecha_vencimiento

    def __str__(self) -> str:
        estado = "VIGENTE" if self.esta_vigente() else "VENCIDA"
        return (f"Certificacion(Nombre: {self.nombre}, "
                f"Vence: {self.vencimiento}, Estado: {estado})")