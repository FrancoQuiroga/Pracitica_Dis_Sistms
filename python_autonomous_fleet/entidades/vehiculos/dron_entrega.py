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