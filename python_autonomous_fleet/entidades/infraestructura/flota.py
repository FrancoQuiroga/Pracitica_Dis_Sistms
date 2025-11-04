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