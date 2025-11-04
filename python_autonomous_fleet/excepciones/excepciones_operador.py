#!/usr/bin/env python3
"""
Modulo de Excepciones personalizadas para el dominio de Operadores.
"""

class OperadorError(Exception):
    """Clase base para excepciones de este dominio."""
    pass

class CertificacionVencidaError(OperadorError):
    """
    Lanzada cuando se intenta asignar una tarea a un operador
    cuya certificacion requerida ha expirado. (US-402)
    """
    def __init__(self, mensaje="La certificacion del operador esta vencida."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class OperadorNoCalificadoError(OperadorError):
    """
    Lanzada cuando se intenta asignar una tarea a un operador
    que no posee la certificacion requerida. (US-403)
    """
    def __init__(self, mensaje="El operador no posee la calificacion requerida."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)