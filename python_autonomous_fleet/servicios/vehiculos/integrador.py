"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\vehiculos
Fecha: 2025-11-04 19:19:55
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\vehiculos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: vehicle_service_registry.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\vehiculos\vehicle_service_registry.py
# ================================================================================

#!/usr/bin/env python3
"""
Modulo que implementa el VehicleServiceRegistry (Patrones Singleton y Registry).

Analogia de 'CultivoServiceRegistry'.
Centraliza el mapeo de tipos de vehiculos a sus servicios/manejadores
especificos para operaciones polimorficas.
"""

from typing import Dict, Any, Callable
import threading

# Importamos las excepciones
from python_autonomous_fleet.excepciones.excepciones_vehiculo import (
    TipoVehiculoDesconocidoError,
    ServicioVehiculoNoDefinidoError
)

class VehicleServiceRegistry:
    """
    Implementa los patrones Singleton y Registry (Registro).
    
    (Singleton - US-T04): Asegura una unica instancia de este registro.
    (Registry - US-T05): Mapea tipos de vehiculo a sus servicios.
    """

    # --- Implementacion del Patron Singleton ---
    
    _instance = None
    _lock = threading.Lock() # Thread-safe singleton

    def __new__(cls, *args, **kwargs):
        """
        Sobrescribe __new__ para controlar la instanciacion
        y asegurar que sea unica (Singleton).
        """
        if cls._instance is None:
            with cls._lock:
                # Doble chequeo para seguridad en concurrencia
                if cls._instance is None:
                    cls._instance = super(VehicleServiceRegistry, cls).__new__(cls)
                    # Inicializar el registro solo la primera vez
                    cls._instance._inicializar_registro()
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Metodo de acceso publico a la instancia unica."""
        # La logica de creacion esta en __new__
        if cls._instance is None:
            return cls()
        return cls._instance

    # --- Implementacion del Patron Registry ---

    def _inicializar_registro(self):
        """
Localiza y carga todos los servicios (Handlers) para cada tipo de
vehiculo. Mantiene el dispatch polimorfico.
"""
        self._registry_handlers: Dict[str, Any] = {}
        print("[Registry] VehicleServiceRegistry (Singleton) inicializado.")
        # En una aplicacion real, esto podria cargar dinamicamente
        # los servicios, pero aqui los definimos explicitamente.
        
        # Simulacion de registro de servicios
        # (Estos servicios se crearian en servicios/vehiculos/handlers/)
        
        def dron_handler(vehiculo, mision):
            print(f"[RegistryHandler] Ejecutando mision de Dron {vehiculo.id}: {mision.descripcion}")
            vehiculo.despegar() # Metodo especifico de Dron
            
        def furgoneta_handler(vehiculo, mision):
            print(f"[RegistryHandler] Ejecutando mision de Furgoneta {vehiculo.id}: {mision.descripcion}")
            # ... logica especifica de furgoneta

        self.registrar_servicio("DronEntrega", dron_handler)
        self.registrar_servicio("FurgonetaAutonoma", furgoneta_handler)
        # Nota: RobotTerrestre y BicicletaAutonoma no tienen handler aun

    def registrar_servicio(self, tipo_vehiculo: str, servicio_handler: Callable):
        """
        (US-T05)
        Registra un servicio (handler) para un tipo de vehiculo especifico.
        """
        print(f"[Registry] Registrando handler para tipo: {tipo_vehiculo}")
        self._registry_handlers[tipo_vehiculo] = servicio_handler

    def get_servicio(self, tipo_vehiculo: str) -> Callable:
        """
        (US-T05)
        Obtiene el servicio (handler) especifico para un tipo de vehiculo.
        
        Permite el dispatch polimorfico.
        """
        if tipo_vehiculo not in self._registry_handlers:
            # Maneja el caso de un tipo valido pero sin servicio (ej. Robot)
            raise ServicioVehiculoNoDefinidoError(tipo_vehiculo)
            
        return self._registry_handlers[tipo_vehiculo]

    def ejecutar_mision_polimorfica(self, vehiculo, mision):
        """
        Ejemplo de caso de uso del Registry.
        Ejecuta una mision usando el handler correcto sin 'if/isinstance'.
        """
        tipo_vehiculo = vehiculo._tipo
        print(f"\n[Registry] Buscando handler para tipo: {tipo_vehiculo}...")
        
        try:
            # Obtiene el handler especifico del registro
            handler = self.get_servicio(tipo_vehiculo)
            
            # Ejecuta el handler
            handler(vehiculo, mision)
            
        except ServicioVehiculoNoDefinidoError as e:
            # Si no hay handler especifico, usa una logica generica
            print(f"[Registry] {e.mensaje}")
            print(f"[Registry] Usando handler generico para {tipo_vehiculo}.")
            # Logica generica (la que estaba en vehiculo.py)
            vehiculo.ejecutar_mision(mision.origen, mision.destino)
        except Exception as e:
            print(f"[Registry] Error inesperado al ejecutar mision polimorfica: {e}")

