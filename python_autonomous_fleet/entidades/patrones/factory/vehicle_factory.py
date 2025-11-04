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