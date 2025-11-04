"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet
Fecha de generacion: 2025-11-04 19:19:55
Total de archivos integrados: 37
Total de directorios procesados: 15
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#
# DIRECTORIO: entidades
#   2. __init__.py
#
# DIRECTORIO: entidades\infraestructura
#   3. __init__.py
#   4. bitacora_mision.py
#   5. estacion_base.py
#   6. flota.py
#
# DIRECTORIO: entidades\operadores
#   7. certificacion.py
#   8. mision.py
#   9. operador.py
#
# DIRECTORIO: entidades\patrones
#   10. __init__.py
#
# DIRECTORIO: entidades\patrones\factory
#   11. vehicle_factory.py
#
# DIRECTORIO: entidades\patrones\observer
#   12. __init__.py
#   13. observer_interface.py
#   14. servicio_externo.py
#
# DIRECTORIO: entidades\patrones\strategy
#   15. __init__.py
#   16. ruteo_strategy.py
#
# DIRECTORIO: entidades\vehiculos
#   17. __init__.py
#   18. bicicleta_autonoma.py
#   19. dron_entrega.py
#   20. furgoneta_autonoma.py
#   21. robot_terrestre.py
#   22. vehiculo.py
#
# DIRECTORIO: excepciones
#   23. __init__.py
#   24. excepciones_infra.py
#   25. excepciones_operador.py
#   26. excepciones_vehiculo.py
#
# DIRECTORIO: servicios
#   27. __init__.py
#
# DIRECTORIO: servicios\infraestructura
#   28. __init__.py
#   29. bitacora_service.py
#   30. estacion_base_service.py
#   31. flota_service.py
#
# DIRECTORIO: servicios\operaciones
#   32. __init__.py
#   33. flota_operations_service.py
#
# DIRECTORIO: servicios\operadores
#   34. __init__.py
#   35. operador_service.py
#
# DIRECTORIO: servicios\vehiculos
#   36. __init__.py
#   37. vehicle_service_registry.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/37: __init__.py
# Directorio: .
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 2/37: __init__.py
# Directorio: entidades
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\__init__.py
# ==============================================================================





################################################################################
# DIRECTORIO: entidades\infraestructura
################################################################################

# ==============================================================================
# ARCHIVO 3/37: __init__.py
# Directorio: entidades\infraestructura
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 4/37: bitacora_mision.py
# Directorio: entidades\infraestructura
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura\bitacora_mision.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 5/37: estacion_base.py
# Directorio: entidades\infraestructura
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura\estacion_base.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 6/37: flota.py
# Directorio: entidades\infraestructura
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\infraestructura\flota.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades\operadores
################################################################################

# ==============================================================================
# ARCHIVO 7/37: certificacion.py
# Directorio: entidades\operadores
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\operadores\certificacion.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 8/37: mision.py
# Directorio: entidades\operadores
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\operadores\mision.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 9/37: operador.py
# Directorio: entidades\operadores
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\operadores\operador.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Operador (Tecnico).

Analogia de 'Trabajador'.
Contiene los datos del tecnico y su lista de certificaciones.
"""

from typing import List
from .certificacion import Certificacion

class Operador:
    """
    Representa a un tecnico de mantenimiento o supervisor de flota (US-401).
    Contiene una coleccion de sus certificaciones (US-402).
    """

    def __init__(self, id_operador: str, nombre_completo: str):
        self._id_operador: str = id_operador
        self._nombre_completo: str = nombre_completo
        
        # Lista de certificaciones que posee el operador
        self._certificaciones: List[Certificacion] = []
        
        print(f"[Operador] Creado Operador: {self.nombre} (ID: {self.id})")

    @property
    def id(self) -> str:
        return self._id_operador

    @property
    def nombre(self) -> str:
        return self._nombre_completo

    def agregar_certificacion(self, certificacion: Certificacion):
        """Agrega una nueva certificacion a la lista del operador."""
        if isinstance(certificacion, Certificacion):
            self._certificaciones.append(certificacion)
            print(f"[Operador {self.id}] Certificacion '{certificacion.nombre}' agregada.")
        else:
            raise TypeError("Solo se pueden agregar objetos de tipo Certificacion")

    def esta_certificado_para(self, nombre_cert_requerida: str) -> bool:
        """
        Verifica si el operador posee una certificacion especifica
        Y si esta vigente.
        (Criterio de aceptacion de US-403)
        """
        for cert in self._certificaciones:
            if cert.nombre == nombre_cert_requerida:
                if cert.esta_vigente():
                    return True # La tiene y esta vigente
                else:
                    print(f"[Operador {self.id}] Alerta: Posee '{nombre_cert_requerida}' pero esta VENCIDA.")
                    return False # La tiene, pero vencida
        
        return False # No posee la certificacion

    def mostrar_perfil(self):
        """Muestra un resumen del operador y sus certificaciones."""
        print(f"\n--- Perfil de Operador: {self.nombre} ({self.id}) ---")
        if not self._certificaciones:
            print("  (Sin certificaciones registradas)")
        else:
            for cert in self._certificaciones:
                print(f"  - {cert}")
        print("-" * (30 + len(self.nombre) + len(self.id)))


################################################################################
# DIRECTORIO: entidades\patrones
################################################################################

# ==============================================================================
# ARCHIVO 10/37: __init__.py
# Directorio: entidades\patrones
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades\patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 11/37: vehicle_factory.py
# Directorio: entidades\patrones\factory
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\patrones\factory\vehicle_factory.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo que implementa el Factory Method para la creacion de Vehiculos.
(US-T01 y Epic 2: US-201 a US-204)
"""

# Importamos las clases concretas de vehiculos
from python_autonomous_fleet.entidades.vehiculos.vehiculo import Vehiculo
from python_autonomous_fleet.entidades.vehiculos.dron_entrega import DronEntrega
from python_autonomous_fleet.entidades.vehiculos.robot_terrestre import RobotTerrestre
from python_autonomous_fleet.entidades.vehiculos.furgoneta_autonoma import FurgonetaAutonoma
from python_autonomous_fleet.entidades.vehiculos.bicicleta_autonoma import BicicletaAutonoma

# Importamos las estrategias de ruteo para asignar una por defecto
from python_autonomous_fleet.entidades.patrones.strategy.ruteo_strategy import RutaMasRapidaStrategy

class VehicleFactory:
    """
    Implementa el patron Factory Method para crear vehiculos.
    
    Desacopla la logica de instanciacion del codigo cliente (main.py).
    Cumple con la rubrica de evaluacion al centralizar la creacion.
    """

    @staticmethod
    def crear_vehiculo(tipo_vehiculo: str, id_vehiculo: str) -> Vehiculo:
        """
        Metodo Factory principal.
        Crea y devuelve una instancia de un Vehiculo concreto.
        
        Args:
            tipo_vehiculo (str): El tipo de vehiculo (ej. "Dron", "Robot").
            id_vehiculo (str): El ID unico para el nuevo vehiculo.

        Returns:
            Vehiculo: Una instancia de una subclase de Vehiculo.
            
        Raises:
            ValueError: Si el tipo_vehiculo no es reconocido.
        """
        
        # Asignamos una estrategia por defecto al crear el vehiculo
        strategy_default = RutaMasRapidaStrategy()

        if tipo_vehiculo == "DronEntrega":
            # US-201
            return DronEntrega(id_vehiculo, strategy_default)
            
        elif tipo_vehiculo == "RobotTerrestre":
            # US-202
            return RobotTerrestre(id_vehiculo, strategy_default)
            
        elif tipo_vehiculo == "FurgonetaAutonoma":
            # US-203
            return FurgonetaAutonoma(id_vehiculo, strategy_default)
            
        elif tipo_vehiculo == "BicicletaAutonoma":
            # US-204
            return BicicletaAutonoma(id_vehiculo, strategy_default)
            
        else:
            # Manejo de error si el tipo no existe
            raise ValueError(f"Tipo de vehiculo desconocido: '{tipo_vehiculo}'")

    @staticmethod
    def obtener_tipos_disponibles() -> list:
        """Devuelve los tipos de vehiculos que la factory puede crear."""
        return ["DronEntrega", "RobotTerrestre", "FurgonetaAutonoma", "BicicletaAutonoma"]


################################################################################
# DIRECTORIO: entidades\patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 12/37: __init__.py
# Directorio: entidades\patrones\observer
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 13/37: observer_interface.py
# Directorio: entidades\patrones\observer
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\patrones\observer\observer_interface.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo que define las interfaces Observer y Observable del patron.
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    La interfaz Observer declara el metodo de actualizacion, usado por
    los Observables (Subjects) para notificar a los observadores.
    """
    
    @abstractmethod
    def actualizar(self, evento: dict):
        """Recibe la notificacion del observable."""
        pass

class Observable(ABC):
    """
    La interfaz Observable (Subject) declara los metodos para gestionar
    suscriptores (observers).
    """
    
    @abstractmethod
    def suscribir(self, observer: Observer):
        """Agrega un observador."""
        pass

    @abstractmethod
    def desuscribir(self, observer: Observer):
        """Elimina un observador."""
        pass

    @abstractmethod
    def notificar(self, evento: dict):
        """Notifica a todos los observadores sobre un evento."""
        pass

# ==============================================================================
# ARCHIVO 14/37: servicio_externo.py
# Directorio: entidades\patrones\observer
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\patrones\observer\servicio_externo.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo que implementa los Observables (Subjects) del sistema.
Estos son los servicios de Tráfico y Clima que emiten eventos.
(US-301, US-302)
"""

import time
from typing import List
from .observer_interface import Observable, Observer

class ServicioExterno(Observable):
    """
    Clase base para los servicios externos que actuan como Observables.
    Gestiona la lista de suscriptores.
    """
    
    def __init__(self, nombre_servicio: str):
        self._observers: List[Observer] = []
        self._nombre_servicio = nombre_servicio

    def suscribir(self, observer: Observer):
        """Suscribe un observer (ej. un Vehiculo) a este servicio."""
        if observer not in self._observers:
            print(f"[{self._nombre_servicio}] Vehiculo {getattr(observer, '_id_vehiculo', '')} suscrito.")
            self._observers.append(observer)

    def desuscribir(self, observer: Observer):
        """Desuscribe un observer."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notificar(self, evento: dict):
        """Notifica a todos los vehiculos suscritos."""
        print(f"[{self._nombre_servicio}] EMITIENDO EVENTO: {evento.get('detalle')}")
        for observer in self._observers:
            observer.actualizar(evento)

    def simular_cambio(self, detalle: str, tipo_evento: str):
        """Metodo para simular un evento externo."""
        evento = {
            "tipo": tipo_evento,
            "detalle": detalle,
            "timestamp": time.time()
        }
        self.notificar(evento)

# --- Implementaciones Concretas ---

class ServicioTrafico(ServicioExterno):
    """
    Observable concreto para el Trafico (US-301).
    """
    def __init__(self):
        super().__init__("Servicio de Trafico")

    def simular_congestion(self, zona: str):
        """Simula un evento de alta congestion."""
        self.simular_cambio(f"Alta congestion en {zona}", "ALERTA_TRAFICO")

class ServicioClima(ServicioExterno):
    """
    Observable concreto para el Clima (US-302).
    """
    def __init__(self):
        super().__init__("Servicio de Clima")

    def simular_alerta_viento(self, velocidad_viento_kmh: int):
        """Simula una alerta de viento fuerte."""
        self.simular_cambio(f"Alerta de viento: {velocidad_viento_kmh} km/h", "ALERTA_CLIMA")


################################################################################
# DIRECTORIO: entidades\patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 15/37: __init__.py
# Directorio: entidades\patrones\strategy
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 16/37: ruteo_strategy.py
# Directorio: entidades\patrones\strategy
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\patrones\strategy\ruteo_strategy.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo que define la interfaz Strategy y sus implementaciones concretas
para los algoritmos de ruteo.
(US-304)
"""

from abc import ABC, abstractmethod
from typing import List

class RuteoStrategy(ABC):
    """
    La interfaz Strategy declara la operacion comun para todos los
    algoritmos de ruteo soportados.
    """
    
    @abstractmethod
    def calcular_ruta(self, origen: str, destino: str) -> List[str]:
        """Calcula una ruta y devuelve los pasos como una lista de strings."""
        pass

# --- Implementaciones Concretas ---

class RutaMasRapidaStrategy(RuteoStrategy):
    """
    (Strategy Concreta)
    Calcula la ruta mas rapida, ignorando el consumo de bateria.
    """
    def calcular_ruta(self, origen: str, destino: str) -> List[str]:
        print("[RuteoStrategy] Calculando ruta (Modo: Mas Rapido)")
        # Logica simulada
        return [origen, "Autopista Central", "Via Rapida", destino]

class RutaEcoStrategy(RuteoStrategy):
    """
    (Strategy Concreta)
    Calcula la ruta mas eficiente en consumo de bateria,
    evitando autopistas.
    """
    def calcular_ruta(self, origen: str, destino: str) -> List[str]:
        print("[RuteoStrategy] Calculando ruta (Modo: Eco - Ahorro Bateria)")
        # Logica simulada
        return [origen, "Avenida Principal", "Calle Secundaria", destino]

class RutaMasSeguraStrategy(RuteoStrategy):
    """
    (Strategy Concreta)
    Calcula la ruta mas segura, evitando zonas de alta congestion
    o alertas climaticas (usado por Drones).
    """
    def calcular_ruta(self, origen: str, destino: str) -> List[str]:
        print("[RuteoStrategy] Calculando ruta (Modo: Mas Seguro - Evitando Zonas)")
        # Logica simulada
        return [origen, "Desvio Zona Segura", "Calle Residencial", destino]


################################################################################
# DIRECTORIO: entidades\vehiculos
################################################################################

# ==============================================================================
# ARCHIVO 17/37: __init__.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 18/37: bicicleta_autonoma.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\bicicleta_autonoma.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Concreta: BicicletaAutonoma
"""

from .vehiculo import Vehiculo
from python_autonomous_fleet.entidades.patrones.strategy.ruteo_strategy import RuteoStrategy

class BicicletaAutonoma(Vehiculo):
    """
    Implementacion concreta de un Vehiculo tipo Bicicleta.
    (US-204)
    """
    
    def __init__(self, id_vehiculo: str, ruteo_strategy_inicial: RuteoStrategy):
        super().__init__(id_vehiculo, "BicicletaAutonoma", ruteo_strategy_inicial)
        
        # Atributos especificos de US-204
        self.carga_max_kg: int = 10
        self.tipo_bici: str = "E-bike"
        self.autonomia_km: int = 40

    def describir(self) -> str:
        """Implementacion del metodo abstracto."""
        return (f"[{self.id}] BicicletaAutonoma | "
                f"Carga: {self.carga_max_kg}kg | "
                f"Tipo: {self.tipo_bici}")

# ==============================================================================
# ARCHIVO 19/37: dron_entrega.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\dron_entrega.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Concreta: DronEntrega
"""

from .vehiculo import Vehiculo
from python_autonomous_fleet.entidades.patrones.strategy.ruteo_strategy import RuteoStrategy

class DronEntrega(Vehiculo):
    """
    Implementacion concreta de un Vehiculo tipo Dron.
    (US-201)
    """
    
    def __init__(self, id_vehiculo: str, ruteo_strategy_inicial: RuteoStrategy):
        super().__init__(id_vehiculo, "DronEntrega", ruteo_strategy_inicial)
        
        # Atributos especificos de US-201
        self.carga_max_kg: int = 5
        self.velocidad_max_kmh: int = 80
        self.autonomia_km: int = 20

    def describir(self) -> str:
        """Implementacion del metodo abstracto."""
        return (f"[{self.id}] DronEntrega | "
                f"Carga: {self.carga_max_kg}kg | "
                f"Velocidad: {self.velocidad_max_kmh}km/h")

    def despegar(self):
        print(f"[Dron {self.id}] Despegando...")

# ==============================================================================
# ARCHIVO 20/37: furgoneta_autonoma.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\furgoneta_autonoma.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Concreta: FurgonetaAutonoma
"""

from .vehiculo import Vehiculo
from python_autonomous_fleet.entidades.patrones.strategy.ruteo_strategy import RuteoStrategy

class FurgonetaAutonoma(Vehiculo):
    """
    Implementacion concreta de un Vehiculo tipo Furgoneta.
    (US-203)
    """
    
    def __init__(self, id_vehiculo: str, ruteo_strategy_inicial: RuteoStrategy):
        super().__init__(id_vehiculo, "FurgonetaAutonoma", ruteo_strategy_inicial)
        
        # Atributos especificos de US-203
        self.carga_max_kg: int = 500
        self.volumen_carga_m3: int = 10
        self.autonomia_km: int = 300

    def describir(self) -> str:
        """Implementacion del metodo abstracto."""
        return (f"[{self.id}] FurgonetaAutonoma | "
                f"Carga: {self.carga_max_kg}kg | "
                f"Volumen: {self.volumen_carga_m3}m3")

# ==============================================================================
# ARCHIVO 21/37: robot_terrestre.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\robot_terrestre.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Concreta: RobotTerrestre
"""

from .vehiculo import Vehiculo
from python_autonomous_fleet.entidades.patrones.strategy.ruteo_strategy import RuteoStrategy

class RobotTerrestre(Vehiculo):
    """
    Implementacion concreta de un Vehiculo tipo Robot.
    (US-202)
    """
    
    def __init__(self, id_vehiculo: str, ruteo_strategy_inicial: RuteoStrategy):
        super().__init__(id_vehiculo, "RobotTerrestre", ruteo_strategy_inicial)
        
        # Atributos especificos de US-202
        self.carga_max_kg: int = 25
        self.velocidad_max_kmh: int = 10
        self.autonomia_km: int = 15

    def describir(self) -> str:
        """Implementacion del metodo abstracto."""
        return (f"[{self.id}] RobotTerrestre | "
                f"Carga: {self.carga_max_kg}kg | "
                f"Velocidad: {self.velocidad_max_kmh}km/h")

# ==============================================================================
# ARCHIVO 22/37: vehiculo.py
# Directorio: entidades\vehiculos
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\vehiculo.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Vehiculo (Clase Base Abstracta).

Implementa la interfaz base para todos los vehiculos de la flota y
actua como:
1. Context (Strategy Pattern) para Ruteo.
2. Observer (Observer Pattern) para alertas de trafico/clima.
3. Observable (Observer Pattern) para reportar su bateria.
"""

from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List

# Import de patrones
from python_autonomous_fleet.entidades.patrones.strategy.ruteo_strategy import RuteoStrategy
from python_autonomous_fleet.entidades.patrones.observer.observer_interface import Observer, Observable


class EstadoVehiculo(Enum):
    """Enum para los estados posibles de un vehiculo."""
    DISPONIBLE = auto()
    EN_MISION = auto()
    CARGANDO = auto()
    MANTENIMIENTO = auto()
    AVERIADO = auto()



class Vehiculo(Observer, Observable): # <--- [OK] ESTA ES LA CORRECCION
    """
    Clase Base Abstracta para cualquier vehiculo autonomo de la flota.
    Implementa las interfaces Observer y Observable.
    """
    
    def __init__(self, id_vehiculo: str, tipo: str, ruteo_strategy_inicial: RuteoStrategy):
        self._id_vehiculo: str = id_vehiculo
        self._tipo: str = tipo
        self._bateria_percent: float = 100.0
        self._estado: EstadoVehiculo = EstadoVehiculo.DISPONIBLE
        
        # (Strategy) Referencia a la estrategia de ruteo
        self._strategy_ruteo: RuteoStrategy = ruteo_strategy_inicial
        
        # (Observable) Lista de observers (ej. EstacionBase) suscritos a este vehiculo
        self._observers_bateria: List[Observer] = []
        
        print(f"[Vehiculo] Creado {self._tipo} con ID: {self._id_vehiculo}")

    @property
    def id(self) -> str:
        return self._id_vehiculo
        
    @property
    def estado(self) -> EstadoVehiculo:
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: EstadoVehiculo):
        print(f"[Estado {self.id}] Cambiando de {self._estado.name} -> {nuevo_estado.name}")
        self._estado = nuevo_estado

    # --- Metodos del Patrón Observer (Vehiculo como Observer) ---
    # US-301 y US-302: Recibe alertas de Clima/Trafico
    
    def actualizar(self, evento: dict):
        """
        Implementacion de Observer. El vehiculo es notificado por un
        servicio externo (Trafico, Clima).
        """
        if evento.get("tipo") == "ALERTA_TRAFICO":
            print(f"[Observer {self.id}] ¡Alerta de trafico recibida! {evento.get('detalle')}")
            # Logica para re-evaluar ruta
            
        elif evento.get("tipo") == "ALERTA_CLIMA":
            print(f"[Observer {self.id}] ¡Alerta de clima recibida! {evento.get('detalle')}")
            # Si somos un Dron, podriamos cambiar a RuteoSeguroStrategy
            if self._tipo == "DronEntrega":
                print(f"[Observer {self.id}] Dron evaluando regreso a base por clima...")

    # --- Metodos del Patrón Observable (Vehiculo como Observable) ---
    # US-303: Notifica a la EstacionBase sobre bateria baja

    def suscribir(self, observer: Observer):
        """Suscribe un observer (ej. EstacionBase) a este vehiculo."""
        if observer not in self._observers_bateria:
            self._observers_bateria.append(observer)

    def desuscribir(self, observer: Observer):
        """Desuscribe un observer."""
        if observer in self._observers_bateria:
            self._observers_bateria.remove(observer)

    def notificar(self, evento: dict):
        """Notifica a todos los observers suscritos (EstacionBase)."""
        for observer in self._observers_bateria:
            observer.actualizar(evento)
            
    def consumir_bateria(self, porcentaje: float):
        """Simula el consumo de bateria y notifica si es baja."""
        self._bateria_percent -= porcentaje
        if self._bateria_percent < 0:
            self._bateria_percent = 0
            
        print(f"[Bateria {self.id}] Nivel: {self._bateria_percent:.1f}%")

        if self._bateria_percent < 15.0 and self.estado != EstadoVehiculo.CARGANDO:
            evento = {
                "tipo": "BATERIA_BAJA",
                "id_vehiculo": self.id,
                "nivel": self._bateria_percent
            }
            # Notifica a la Estacion Base (US-303)
            self.notificar(evento)

    # --- Metodos del Patrón Strategy (Vehiculo como Context) ---
    # US-304: Permite cambiar la estrategia de ruteo

    def set_ruteo_strategy(self, strategy: RuteoStrategy):
        """Permite cambiar la estrategia de ruteo dinamicamente."""
        print(f"[Strategy {self.id}] Cambiando ruteo a: {strategy.__class__.__name__}")
        self._strategy_ruteo = strategy

    def ejecutar_mision(self, origen: str, destino: str):
        """Usa la estrategia de ruteo actual para ejecutar la mision."""
        if self.estado != EstadoVehiculo.DISPONIBLE:
            print(f"[Mision {self.id}] No se puede iniciar mision, estado: {self.estado.name}")
            return
            
        self.estado = EstadoVehiculo.EN_MISION
        print(f"[Mision {self.id}] Iniciando mision de {origen} a {destino}.")
        
        # Delega el calculo de la ruta a la estrategia (Strategy Pattern)
        ruta_calculada = self._strategy_ruteo.calcular_ruta(origen, destino)
        
        print(f"[Mision {self.id}] Ruta calculada: {' -> '.join(ruta_calculada)}")
        
        # Simula consumo
        self.consumir_bateria(25.0)
        print(f"[Mision {self.id}] Mision completada.")
        self.estado = EstadoVehiculo.DISPONIBLE

    # --- Metodo Abstracto ---
    
    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripcion de las capacidades especificas del vehiculo."""
        pass


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 23/37: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/37: excepciones_infra.py
# Directorio: excepciones
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones\excepciones_infra.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 25/37: excepciones_operador.py
# Directorio: excepciones
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones\excepciones_operador.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 26/37: excepciones_vehiculo.py
# Directorio: excepciones
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\excepciones\excepciones_vehiculo.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 27/37: __init__.py
# Directorio: servicios
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios\infraestructura
################################################################################

# ==============================================================================
# ARCHIVO 28/37: __init__.py
# Directorio: servicios\infraestructura
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\infraestructura\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 29/37: bitacora_service.py
# Directorio: servicios\infraestructura
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\infraestructura\bitacora_service.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de Servicio para BitacoraMision (Persistencia).

Analogia de 'RegistroForestalService'.
Maneja la logica de guardar y leer bitacoras en disco (Pickle).
"""

import pickle
import os
from typing import List

from python_autonomous_fleet.entidades.infraestructura.bitacora_mision import BitacoraMision

# Define el directorio donde se guardaran las bitacoras
DIRECTORIO_BITACORAS = "bitacoras_misiones"

class BitacoraService:
    """
    Servicio encargado de la logica de persistencia de las misiones.
    (Cumple US-503 y US-504)
    """

    def __init__(self):
        # Asegura que el directorio de persistencia exista
        if not os.path.exists(DIRECTORIO_BITACORAS):
            os.makedirs(DIRECTORIO_BITACORAS)
            print(f"[BitacoraService] Creado directorio de persistencia: {DIRECTORIO_BITACORAS}")

    def _get_ruta_archivo(self, id_vehiculo: str) -> str:
        """Metodo helper para obtener la ruta estandar del archivo de bitacora."""
        # Guarda un archivo por vehiculo
        return os.path.join(DIRECTORIO_BITACORAS, f"bitacora_vehiculo_{id_vehiculo}.pkl")

    def persistir_bitacora(self, bitacora: BitacoraMision):
        """
        Caso de Uso: Persistir una bitacora de mision (US-503).
        
        Utiliza Pickle para guardar, igual que el proyecto original.
        Agrega el registro a la lista existente de ese vehiculo.
        """
        ruta_archivo = self._get_ruta_archivo(bitacora.id_vehiculo)
        
        # Lee las bitacoras existentes (si las hay)
        bitacoras_existentes = self.leer_bitacora(bitacora.id_vehiculo)
        
        # Agrega la nueva bitacora
        bitacoras_existentes.append(bitacora)
        
        # Escribe la lista completa de nuevo
        try:
            with open(ruta_archivo, 'wb') as f:
                pickle.dump(bitacoras_existentes, f)
            print(f"[BitacoraService] Bitacora {bitacora.id_mision} persistida para vehiculo {bitacora.id_vehiculo}.")
        except IOError as e:
            print(f"[BitacoraService] ERROR: No se pudo persistir la bitacora en {ruta_archivo}. {e}")
        except pickle.PicklingError as e:
            print(f"[BitacoraService] ERROR: Falla al 'picklear' la bitacora. {e}")

    def leer_bitacora(self, id_vehiculo: str) -> List[BitacoraMision]:
        """
        Caso de Uso: Recuperar el historial de misiones de un vehiculo (US-504).
        
        Utiliza Pickle para leer, igual que el proyecto original.
        """
        ruta_archivo = self._get_ruta_archivo(id_vehiculo)
        
        if not os.path.exists(ruta_archivo):
            #print(f"[BitacoraService] No se encontro historial para {id_vehiculo}. Se asume vacio.")
            return [] # Devuelve lista vacia si no hay archivo

        try:
            with open(ruta_archivo, 'rb') as f:
                bitacoras = pickle.load(f)
                if not isinstance(bitacoras, list):
                     raise TypeError("El archivo de bitacora no contiene una lista.")
                return bitacoras
        except (IOError, pickle.UnpicklingError, TypeError, EOFError) as e:
            print(f"[BitacoraService] ERROR: No se pudo leer la bitacora {ruta_archivo}. Archivo corrupto o invalido. {e}")
            # Si hay corrupcion, mejor devolver vacio para no romper el sistema
            return []

# ==============================================================================
# ARCHIVO 30/37: estacion_base_service.py
# Directorio: servicios\infraestructura
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\infraestructura\estacion_base_service.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de Servicio para EstacionBase.

Contiene la logica de negocio para gestionar las Estaciones Base (Hubs).
"""
from python_autonomous_fleet.entidades.infraestructura.estacion_base import EstacionBase
from python_autonomous_fleet.entidades.infraestructura.estacion_base import EstacionBase

class EstacionBaseService:
    """
    Servicio encargado de la logica de negocio relacionada con EstacionBase.
    (Cumple US-101)
    """

    def crear_estacion_base(self, id_estacion: str, ubicacion: str, capacidad_kw: int) -> EstacionBase:
        """
        Caso de Uso: Registrar una nueva estacion de carga (US-101).
        
        Args:
            id_estacion (str): ID unico.
            ubicacion (str): Direccion o coordenadas.
            capacidad_kw (int): Capacidad energetica total.

        Returns:
            EstacionBase: La entidad creada.
        """
        print(f"[EstacionService] Registrando nueva Estacion Base en {ubicacion}...")
        
        # Validaciones de negocio (ej. ubicacion no duplicada, capacidad minima)
        if capacidad_kw < 100:
            raise ValueError("La capacidad energetica debe ser de al menos 100 kW.")
            
        estacion = EstacionBase(
            id_estacion=id_estacion,
            ubicacion=ubicacion,
            capacidad_energetica_kw=capacidad_kw
        )
        
        # Logica de persistencia (ej. self.db_adapter.save(estacion))
        print(f"[EstacionService] Estacion {estacion.id} registrada exitosamente.")
        return estacion

# ==============================================================================
# ARCHIVO 31/37: flota_service.py
# Directorio: servicios\infraestructura
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\infraestructura\flota_service.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de Servicio para Flota.

Contiene la logica de negocio para gestionar las Flotas y
la asignacion de vehiculos.
"""

from python_autonomous_fleet.entidades.infraestructura.flota import Flota
from python_autonomous_fleet.entidades.infraestructura.estacion_base import EstacionBase
from python_autonomous_fleet.entidades.vehiculos.vehiculo import Vehiculo
from python_autonomous_fleet.entidades.patrones.factory.vehicle_factory import VehicleFactory

class FlotaService:
    """
    Servicio encargado de la logica de negocio de las Flotas.
    (Cumple US-102, US-103 y Epic 2)
    """

    def crear_flota(self, id_flota: str, nombre_flota: str, estacion_base: EstacionBase) -> Flota:
        """
        Caso de Uso: Crear una flota y asociarla a una estacion (US-102).
        """
        print(f"[FlotaService] Creando flota '{nombre_flota}'...")
        if not isinstance(estacion_base, EstacionBase):
            raise TypeError("La flota debe estar asociada a una EstacionBase valida.")
            
        flota = Flota(
            id_flota=id_flota,
            nombre_flota=nombre_flota,
            id_estacion_base=estacion_base.id
        )
        
        print(f"[FlotaService] Flota '{flota.nombre}' creada.")
        return flota

    def agregar_vehiculo_a_flota(self, 
                                 flota: Flota, 
                                 estacion_base: EstacionBase,
                                 tipo_vehiculo: str, 
                                 id_vehiculo: str) -> Vehiculo:
        """
        Caso de Uso: Dar de alta un nuevo vehiculo usando el Factory
        y asignarlo a una flota y estacion (US-201 a US-204).
        
        Ademas, suscribe la Estacion Base al vehiculo (US-303).
        """
        print(f"[FlotaService] Agregando vehiculo tipo '{tipo_vehiculo}' a flota '{flota.nombre}'...")
        
        # 1. Usar el Factory para crear el vehiculo (US-T01)
        try:
            vehiculo = VehicleFactory.crear_vehiculo(tipo_vehiculo, id_vehiculo)
        except ValueError as e:
            print(f"[FlotaService] Error al crear vehiculo: {e}")
            return None

        # 2. Agregar el vehiculo al inventario de la flota (US-103)
        flota.agregar_vehiculo(vehiculo)
        
        # 3. Suscribir la Estacion Base al vehiculo (Patron Observer) (US-303)
        # La estacion ahora escuchara eventos de bateria baja de este vehiculo.
        vehiculo.suscribir(estacion_base)
        print(f"[FlotaService] Estacion {estacion_base.id} suscrita a {vehiculo.id}.")

        return vehiculo

    def obtener_vehiculo(self, flota: Flota, id_vehiculo: str) -> Vehiculo | None:
        """Caso de Uso: Buscar un vehiculo especifico en una flota."""
        return flota.obtener_vehiculo_por_id(id_vehiculo)
        
    def reporte_inventario(self, flota: Flota):
        """Caso de Uso: Mostrar el inventario de la flota (US-103)."""
        flota.listar_inventario()


################################################################################
# DIRECTORIO: servicios\operaciones
################################################################################

# ==============================================================================
# ARCHIVO 32/37: __init__.py
# Directorio: servicios\operaciones
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operaciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 33/37: flota_operations_service.py
# Directorio: servicios\operaciones
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operaciones\flota_operations_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios\operadores
################################################################################

# ==============================================================================
# ARCHIVO 34/37: __init__.py
# Directorio: servicios\operadores
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operadores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 35/37: operador_service.py
# Directorio: servicios\operadores
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operadores\operador_service.py
# ==============================================================================

#!/usr/bin/env python3
"""
Modulo de Servicio para Operador.

Analogia de 'TrabajadorService'.
Contiene la logica de negocio para gestionar Operadores,
Certificaciones y Misiones.
"""

from datetime import date

# Import de Entidades
from python_autonomous_fleet.entidades.operadores.operador import Operador
from python_autonomous_fleet.entidades.operadores.certificacion import Certificacion
from python_autonomous_fleet.entidades.operadores.mision import Mision, TipoMision

# Import de Excepciones
from python_autonomous_fleet.excepciones.excepciones_operador import OperadorNoCalificadoError

class OperadorService:
    """
    Servicio encargado de la logica de negocio de Operadores.
    (Cumple Epic 4: US-401, US-402, US-403)
    """

    def crear_operador(self, id_operador: str, nombre_completo: str) -> Operador:
        """
        Caso de Uso: Registrar un nuevo Operador (US-401).
        """
        print(f"[OperadorService] Registrando nuevo operador: {nombre_completo}")
        operador = Operador(id_operador=id_operador, nombre_completo=nombre_completo)
        
        # ... logica de persistencia (ej. self.db.save(operador))
        return operador

    def agregar_certificacion_a_operador(self, 
                                          operador: Operador, 
                                          nombre_cert: str, 
                                          fecha_venc: date) -> Certificacion:
        """
        Caso de Uso: Asignar una certificacion a un operador (US-402).
        """
        print(f"[OperadorService] Agregando certificacion '{nombre_cert}' a {operador.nombre}")
        
        if not isinstance(operador, Operador):
            raise TypeError("El objeto 'operador' no es de tipo Operador.")
            
        certificacion = Certificacion(
            nombre_certificacion=nombre_cert,
            fecha_vencimiento=fecha_venc
        )
        
        operador.agregar_certificacion(certificacion)
        
        # ... logica de persistencia (ej. self.db.update(operador))
        return certificacion

    def crear_y_asignar_mision(self,
                               id_mision: str,
                               tipo_mision: TipoMision,
                               id_vehiculo: str,
                               operador: Operador,
                               descripcion: str,
                               cert_requerida: str) -> Mision:
        """
        Caso de Uso: Asignar una mision de mantenimiento a un operador (US-403).
        
        Verifica que el operador este calificado (US-403 Criterio Aceptacion).
        """
        print(f"[OperadorService] Intentando asignar mision {id_mision} a {operador.nombre}...")
        
        # Validacion de Negocio (Criterio de Aceptacion US-403)
        # El OperadorService verifica la calificacion antes de crear la Mision.
        if not operador.esta_certificado_para(cert_requerida):
            raise OperadorNoCalificadoError(
                f"FALLO ASIGNACION: Operador {operador.nombre} no esta calificado "
                f"o su certificacion '{cert_requerida}' esta vencida."
            )

        print(f"[OperadorService] Operador {operador.nombre} esta calificado. Creando mision.")
        
        mision = Mision(
            id_mision=id_mision,
            tipo_mision=tipo_mision,
            id_vehiculo_asignado=id_vehiculo,
            id_operador_asignado=operador.id,
            descripcion=descripcion
        )
        
        # ... logica de persistencia (ej. self.db.save(mision))
        return mision

    def iniciar_mision_operador(self, mision: Mision):
        """Caso de Uso: El operador inicia la mision asignada."""
        mision.iniciar_mision()
        
    def completar_mision_operador(self, mision: Mision):
        """Caso de Uso: El operador completa la mision."""
        mision.completar_mision()


################################################################################
# DIRECTORIO: servicios\vehiculos
################################################################################

# ==============================================================================
# ARCHIVO 36/37: __init__.py
# Directorio: servicios\vehiculos
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\vehiculos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/37: vehicle_service_registry.py
# Directorio: servicios\vehiculos
# Ruta completa: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\vehiculos\vehicle_service_registry.py
# ==============================================================================

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


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 37
# Generado: 2025-11-04 19:19:55
################################################################################
