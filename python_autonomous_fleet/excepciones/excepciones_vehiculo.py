#!/usr/bin/env python3
"""
Modulo de Excepciones personalizadas para el dominio de Vehiculos y el Registry.
"""

class VehiculoError(Exception):
    """Clase base para excepciones de este dominio."""
    pass

class TipoVehiculoDesconocidoError(VehiculoError):
    """
    Lanzada por el Registry cuando se solicita un servicio
    para un tipo de vehiculo que no ha sido registrado.
    """
    def __init__(self, tipo_vehiculo: str):
        self.mensaje = f"Tipo de vehiculo '{tipo_vehiculo}' no reconocido o no registrado en el ServiceRegistry."
        super().__init__(self.mensaje)

class ServicioVehiculoNoDefinidoError(VehiculoError):
    """
    Lanzada por el Registry si el tipo de vehiculo es valido
    pero no se le ha asignado un servicio.
    """
    def __init__(self, tipo_vehiculo: str):
        self.mensaje = f"No se ha definido un servicio (Handler) para el tipo '{tipo_vehiculo}'."
        super().__init__(self.mensaje)