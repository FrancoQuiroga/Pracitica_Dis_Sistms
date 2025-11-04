#!/usr/bin/env python3
"""
Modulo de Excepciones personalizadas para el dominio de Infraestructura
(Estaciones y Flotas).
"""

class InfraestructuraError(Exception):
    """Clase base para excepciones de este dominio."""
    pass

class EstacionBaseError(InfraestructuraError):
    """Lanzada por EstacionBaseService."""
    pass

class FlotaError(InfraestructuraError):
    """Lanzada por FlotaService."""
    pass