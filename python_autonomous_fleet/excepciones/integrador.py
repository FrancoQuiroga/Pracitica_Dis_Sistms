"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones
Fecha: 2025-11-04 19:19:55
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: excepciones_infra.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones\excepciones_infra.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: excepciones_operador.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones\excepciones_operador.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: excepciones_vehiculo.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones\excepciones_vehiculo.py
# ================================================================================

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

