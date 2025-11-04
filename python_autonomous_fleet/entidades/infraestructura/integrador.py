"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura
Fecha: 2025-11-04 19:19:55
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: bitacora_mision.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura\bitacora_mision.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: estacion_base.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura\estacion_base.py
# ================================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad EstacionBase (Hub).

Analogia de 'Tierra'.
Implementa la interfaz Observer (US-303) para suscribirse a los
eventos de bateria de los vehiculos que alberga.
"""

from typing import List, Set

# Importamos la interfaz Observer
from python_autonomous_fleet.entidades.patrones.observer.observer_interface import Observer

class EstacionBase(Observer):
    """
    Representa un Hub de carga y despacho (US-101).
    Actua como Observer para monitorear la bateria de sus vehiculos (US-303).
    """

    def __init__(self, id_estacion: str, ubicacion: str, capacidad_energetica_kw: int):
        self._id_estacion: str = id_estacion
        self._ubicacion: str = ubicacion
        self._capacidad_energetica_kw: int = capacidad_energetica_kw
        
        # Lista de IDs de vehiculos que necesitan recarga
        self._cola_de_carga: Set[str] = set()
        
        print(f"[Estacion] Creada Estacion Base: {self.id} en {self.ubicacion}")

    @property
    def id(self) -> str:
        return self._id_estacion

    @property
    def ubicacion(self) -> str:
        return self._ubicacion

    # --- Metodo del Patrón Observer (EstacionBase como Observer) ---

    def actualizar(self, evento: dict):
        """
        Implementacion de Observer (US-303).
        La Estacion es notificada por un Vehiculo (Observable).
        """
        if evento.get("tipo") == "BATERIA_BAJA":
            id_vehiculo = evento.get("id_vehiculo")
            nivel = evento.get("nivel")
            
            print(f"[Observer Estacion {self.id}] ¡Alerta recibida!")
            print(f"    -> Vehiculo: {id_vehiculo} reporta bateria baja ({nivel:.1f}%)")
            
            # Agregamos el vehiculo a la cola de recarga si no estaba ya
            if id_vehiculo not in self._cola_de_carga:
                self._cola_de_carga.add(id_vehiculo)
                print(f"    -> {id_vehiculo} anadido a la cola de recarga.")
                self.gestionar_cola_de_carga()

    def gestionar_cola_de_carga(self):
        """Logica de negocio simulada para manejar la recarga."""
        print(f"[Estacion {self.id}] Gestionando cola de carga. Vehiculos en espera: {len(self._cola_de_carga)}")
        # ... Logica para asignar cargadores ...

    def describir(self) -> str:
        return (f"EstacionBase(ID: {self.id}, "
                f"Ubicacion: {self.ubicacion}, "
                f"Capacidad: {self._capacidad_energetica_kw}kW)")

# ================================================================================
# ARCHIVO 4/4: flota.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura\flota.py
# ================================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Flota.

Analogia de 'Plantacion'.
Contiene la coleccion de vehiculos asignados.
"""

from typing import List
from python_autonomous_fleet.entidades.vehiculos.vehiculo import Vehiculo

class Flota:
    """
    Representa una coleccion de vehiculos agrupados (US-102).
    Mantiene el inventario de vehiculos (US-103).
    """

    def __init__(self, id_flota: str, nombre_flota: str, id_estacion_base: str):
        self._id_flota: str = id_flota
        self._nombre_flota: str = nombre_flota
        self._id_estacion_base: str = id_estacion_base # FK a EstacionBase
        
        # US-103: Inventario de vehiculos en esta flota
        self._inventario_vehiculos: List[Vehiculo] = []
        
        print(f"[Flota] Creada Flota '{self.nombre}' (ID: {self.id}) "
              f"asignada a Estacion {self._id_estacion_base}")

    @property
    def id(self) -> str:
        return self._id_flota

    @property
    def nombre(self) -> str:
        return self._nombre_flota

    @property
    def vehiculos(self) -> List[Vehiculo]:
        return self._inventario_vehiculos

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        """Agrega un vehiculo al inventario de esta flota."""
        if vehiculo not in self._inventario_vehiculos:
            self._inventario_vehiculos.append(vehiculo)
            print(f"[Flota {self.id}] Vehiculo {vehiculo.id} ({vehiculo._tipo}) agregado.")

    def obtener_vehiculo_por_id(self, id_vehiculo: str) -> Vehiculo | None:
        """Busca un vehiculo en el inventario por su ID."""
        for v in self._inventario_vehiculos:
            if v.id == id_vehiculo:
                return v
        return None

    def listar_inventario(self):
        """Muestra el inventario actual de la flota (US-103)."""
        print(f"\n--- Inventario de Flota: {self.nombre} ({self.id}) ---")
        if not self._inventario_vehiculos:
            print("  (Flota vacia)")
            return
            
        for v in self._inventario_vehiculos:
            print(f"  - ID: {v.id:<10} | Tipo: {v._tipo:<18} | Estado: {v.estado.name}")
        print("-" * (30 + len(self.nombre) + len(self.id)))

