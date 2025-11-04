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