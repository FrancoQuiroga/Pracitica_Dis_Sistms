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