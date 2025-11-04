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