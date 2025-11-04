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