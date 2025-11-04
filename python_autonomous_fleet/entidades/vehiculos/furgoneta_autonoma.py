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