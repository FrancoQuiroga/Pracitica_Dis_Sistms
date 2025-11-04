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