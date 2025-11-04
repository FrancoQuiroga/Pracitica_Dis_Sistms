"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos
Fecha: 2025-11-04 19:19:55
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: bicicleta_autonoma.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\bicicleta_autonoma.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/6: dron_entrega.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\dron_entrega.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/6: furgoneta_autonoma.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\furgoneta_autonoma.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/6: robot_terrestre.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\robot_terrestre.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/6: vehiculo.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\vehiculos\vehiculo.py
# ================================================================================

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

