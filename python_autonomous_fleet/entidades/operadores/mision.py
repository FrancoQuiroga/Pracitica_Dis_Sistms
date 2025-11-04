#!/usr/bin/env python3
"""
Modulo de la Entidad Mision.

Analogia de 'Tarea'.
Representa una asignacion de trabajo (Mantenimiento o Delivery)
para un Operador y un Vehiculo.
"""

from enum import Enum, auto
from datetime import datetime

class TipoMision(Enum):
    """Define los tipos de misiones que se pueden asignar."""
    MANTENIMIENTO_PREVENTIVO = auto()
    REPARACION_AVERIA = auto()
    SUPERVISION_CARGA = auto() # (US-501)
    
class EstadoMision(Enum):
    """Define los estados de una mision."""
    ASIGNADA = auto()
    EN_PROGRESO = auto()
    COMPLETADA = auto()
    CANCELADA = auto()

class Mision:
    """
    Representa una asignacion de trabajo (US-403).
    Vincula un Operador, un Vehiculo y una descripcion del trabajo.
    """

    def __init__(self,
                 id_mision: str,
                 tipo_mision: TipoMision,
                 id_vehiculo_asignado: str,
                 id_operador_asignado: str,
                 descripcion: str):
                     
        self.id_mision: str = id_mision
        self.tipo_mision: TipoMision = tipo_mision
        self.id_vehiculo_asignado: str = id_vehiculo_asignado
        self.id_operador_asignado: str = id_operador_asignado
        self.descripcion: str = descripcion
        self.estado: EstadoMision = EstadoMision.ASIGNADA
        self.fecha_creacion: datetime = datetime.now()
        
        print(f"[Mision {self.id_mision}] Creada: {self.tipo_mision.name} "
              f"para Vehiculo {self.id_vehiculo_asignado} "
              f"asignada a Operador {self.id_operador_asignado}")

    def iniciar_mision(self):
        self.estado = EstadoMision.EN_PROGRESO
        print(f"[Mision {self.id_mision}] EN PROGRESO.")

    def completar_mision(self):
        self.estado = EstadoMision.COMPLETADA
        print(f"[Mision {self.id_mision}] COMPLETADA.")

    def __str__(self) -> str:
        return (f"Mision(ID: {self.id_mision}, "
                f"Tipo: {self.tipo_mision.name}, "
                f"Vehiculo: {self.id_vehiculo_asignado}, "
                f"Operador: {self.id_operador_asignado}, "
                f"Estado: {self.estado.name})")