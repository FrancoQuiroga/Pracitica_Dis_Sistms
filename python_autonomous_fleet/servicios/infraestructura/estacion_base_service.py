#!/usr/bin/env python3
"""
Modulo de Servicio para EstacionBase.

Contiene la logica de negocio para gestionar las Estaciones Base (Hubs).
"""
from python_autonomous_fleet.entidades.infraestructura.estacion_base import EstacionBase
from python_autonomous_fleet.entidades.infraestructura.estacion_base import EstacionBase

class EstacionBaseService:
    """
    Servicio encargado de la logica de negocio relacionada con EstacionBase.
    (Cumple US-101)
    """

    def crear_estacion_base(self, id_estacion: str, ubicacion: str, capacidad_kw: int) -> EstacionBase:
        """
        Caso de Uso: Registrar una nueva estacion de carga (US-101).
        
        Args:
            id_estacion (str): ID unico.
            ubicacion (str): Direccion o coordenadas.
            capacidad_kw (int): Capacidad energetica total.

        Returns:
            EstacionBase: La entidad creada.
        """
        print(f"[EstacionService] Registrando nueva Estacion Base en {ubicacion}...")
        
        # Validaciones de negocio (ej. ubicacion no duplicada, capacidad minima)
        if capacidad_kw < 100:
            raise ValueError("La capacidad energetica debe ser de al menos 100 kW.")
            
        estacion = EstacionBase(
            id_estacion=id_estacion,
            ubicacion=ubicacion,
            capacidad_energetica_kw=capacidad_kw
        )
        
        # Logica de persistencia (ej. self.db_adapter.save(estacion))
        print(f"[EstacionService] Estacion {estacion.id} registrada exitosamente.")
        return estacion