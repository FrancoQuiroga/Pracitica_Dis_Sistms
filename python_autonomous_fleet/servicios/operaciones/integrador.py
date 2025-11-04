"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operaciones
Fecha: 2025-11-04 19:19:55
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operaciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: flota_operations_service.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operaciones\flota_operations_service.py
# ================================================================================

#!/usr/bin/env python3
"""
Modulo de Servicio de Operaciones de Flota (Orquestador).

Analogia de 'FincasService'.
Este servicio orquesta operaciones complejas que involucran
multiples dominios (Operadores, Vehiculos, Bitacora).
"""

# Import de Entidades
from python_autonomous_fleet.entidades.vehiculos.vehiculo import Vehiculo
from python_autonomous_fleet.entidades.operadores.operador import Operador
from python_autonomous_fleet.entidades.operadores.mision import Mision, TipoMision
from python_autonomous_fleet.entidades.infraestructura.bitacora_mision import BitacoraMision

# Import de Servicios (los que orquesta)
from python_autonomous_fleet.servicios.operadores.operador_service import OperadorService
from python_autonomous_fleet.servicios.infraestructura.bitacora_service import BitacoraService

# Import de Patrones (Singleton/Registry)
from python_autonomous_fleet.servicios.vehiculos.vehicle_service_registry import VehicleServiceRegistry

# Import de Excepciones
from python_autonomous_fleet.excepciones.excepciones_operador import OperadorError

class FlotaOperationsService:
    """
    Servicio Orquestador.
    Maneja casos de uso de alto nivel.
    """

    def __init__(self):
        # Obtenemos la instancia unica del Registry (Singleton)
        # Esto es analogo a como 'FincasService' importaba el 'CultivoServiceRegistry'
        self._registry = VehicleServiceRegistry.get_instance()
        
        # Instanciamos los servicios que este orquestador va a utilizar
        self._operador_service = OperadorService()
        self._bitacora_service = BitacoraService()
        
        print("[OperationsService] Servicio de Operaciones (Orquestador) inicializado.")

    def asignar_mision_mantenimiento(self,
                                      id_mision: str,
                                      vehiculo: Vehiculo,
                                      operador: Operador,
                                      cert_requerida: str) -> Mision | None:
        """
        Caso de Uso Orquestado (US-403):
        Asigna una mision de mantenimiento, validando la certificacion
        del operador.
        
        Orquesta: OperadorService + Entidad Mision
        """
        print(f"\n[OperationsService] Orquestando asignacion de mantenimiento para {vehiculo.id}...")
        
        try:
            descripcion = f"Mantenimiento preventivo para {vehiculo._tipo} (ID: {vehiculo.id})"
            
            # 1. Delega la logica de validacion y creacion al OperadorService
            mision = self._operador_service.crear_y_asignar_mision(
                id_mision=id_mision,
                tipo_mision=TipoMision.MANTENIMIENTO_PREVENTIVO,
                id_vehiculo=vehiculo.id,
                operador=operador,
                descripcion=descripcion,
                cert_requerida=cert_requerida
            )
            
            print(f"[OperationsService] ORQUESTACION EXITOSA: Mision {mision.id} asignada.")
            return mision
            
        except OperadorError as e:
            print(f"[OperationsService] ORQUESTACION FALLIDA: {e.mensaje}")
            return None
        except Exception as e:
            print(f"[OperationsService] ORQUESTACION FALLIDA (Error inesperado): {e}")
            return None

    def ejecutar_mision_delivery_polimorfica(self,
                                              id_mision: str,
                                              vehiculo: Vehiculo,
                                              origen: str,
                                              destino: str) -> bool:
        """
        Caso de Uso Orquestado (US-501, US-T05, US-503):
        Ejecuta una mision de delivery usando el Registry y persiste
        la bitacora al finalizar.
        
        Orquesta: Registry (Polimorfismo) + BitacoraService (Persistencia)
        """
        print(f"\n[OperationsService] Orquestando Mision de Delivery (Polimorfica)...")
        
        # 1. Crear la entidad Mision
        # (En un sistema real, el operador seria N/A o un supervisor)
        mision_delivery = Mision(
            id_mision=id_mision,
            tipo_mision=TipoMision.SUPERVISION_CARGA, # O TipoMision.DELIVERY
            id_vehiculo_asignado=vehiculo.id,
            id_operador_asignado="SISTEMA_AUTO",
            descripcion=f"Delivery de {origen} a {destino}"
        )
        
        # 2. Ejecutar usando el Registry (Dispatch Polimorfico - US-T05)
        # Esto es analogo a 'fincas_service.cosechar_y_empaquetar'
        try:
            # El Registry decide que 'handler' o logica usar segun el tipo de vehiculo
            self._registry.ejecutar_mision_polimorfica(vehiculo, mision_delivery)
        except Exception as e:
            print(f"[OperationsService] ORQUESTACION FALLIDA (Ejecucion): {e}")
            return False

        # 3. Persistir la Bitacora (US-503)
        # Esto es analogo a 'fincas_service' usando 'RegistroForestalService'
        print(f"[OperationsService] Mision {id_mision} completada. Persistiendo bitacora...")
        
        # (Simulamos la ruta que se calculo internamente)
        ruta_simulada = [origen, "Punto Intermedio", destino]
        
        bitacora_entry = BitacoraMision(
            id_mision=id_mision,
            id_vehiculo=vehiculo.id,
            tipo_vehiculo=vehiculo._tipo,
            ruta_realizada=ruta_simulada,
            id_operador="SISTEMA_AUTO"
        )
        
        self._bitacora_service.persistir_bitacora(bitacora_entry)
        
        print(f"[OperationsService] ORQUESTACION EXITOSA: Delivery completado y bitacora guardada.")
        return True

