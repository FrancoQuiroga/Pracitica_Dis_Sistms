#!/usr/bin/env python3
"""
Modulo de Servicio para Flota.

Contiene la logica de negocio para gestionar las Flotas y
la asignacion de vehiculos.
"""

from python_autonomous_fleet.entidades.infraestructura.flota import Flota
from python_autonomous_fleet.entidades.infraestructura.estacion_base import EstacionBase
from python_autonomous_fleet.entidades.vehiculos.vehiculo import Vehiculo
from python_autonomous_fleet.entidades.patrones.factory.vehicle_factory import VehicleFactory

class FlotaService:
    """
    Servicio encargado de la logica de negocio de las Flotas.
    (Cumple US-102, US-103 y Epic 2)
    """

    def crear_flota(self, id_flota: str, nombre_flota: str, estacion_base: EstacionBase) -> Flota:
        """
        Caso de Uso: Crear una flota y asociarla a una estacion (US-102).
        """
        print(f"[FlotaService] Creando flota '{nombre_flota}'...")
        if not isinstance(estacion_base, EstacionBase):
            raise TypeError("La flota debe estar asociada a una EstacionBase valida.")
            
        flota = Flota(
            id_flota=id_flota,
            nombre_flota=nombre_flota,
            id_estacion_base=estacion_base.id
        )
        
        print(f"[FlotaService] Flota '{flota.nombre}' creada.")
        return flota

    def agregar_vehiculo_a_flota(self, 
                                 flota: Flota, 
                                 estacion_base: EstacionBase,
                                 tipo_vehiculo: str, 
                                 id_vehiculo: str) -> Vehiculo:
        """
        Caso de Uso: Dar de alta un nuevo vehiculo usando el Factory
        y asignarlo a una flota y estacion (US-201 a US-204).
        
        Ademas, suscribe la Estacion Base al vehiculo (US-303).
        """
        print(f"[FlotaService] Agregando vehiculo tipo '{tipo_vehiculo}' a flota '{flota.nombre}'...")
        
        # 1. Usar el Factory para crear el vehiculo (US-T01)
        try:
            vehiculo = VehicleFactory.crear_vehiculo(tipo_vehiculo, id_vehiculo)
        except ValueError as e:
            print(f"[FlotaService] Error al crear vehiculo: {e}")
            return None

        # 2. Agregar el vehiculo al inventario de la flota (US-103)
        flota.agregar_vehiculo(vehiculo)
        
        # 3. Suscribir la Estacion Base al vehiculo (Patron Observer) (US-303)
        # La estacion ahora escuchara eventos de bateria baja de este vehiculo.
        vehiculo.suscribir(estacion_base)
        print(f"[FlotaService] Estacion {estacion_base.id} suscrita a {vehiculo.id}.")

        return vehiculo

    def obtener_vehiculo(self, flota: Flota, id_vehiculo: str) -> Vehiculo | None:
        """Caso de Uso: Buscar un vehiculo especifico en una flota."""
        return flota.obtener_vehiculo_por_id(id_vehiculo)
        
    def reporte_inventario(self, flota: Flota):
        """Caso de Uso: Mostrar el inventario de la flota (US-103)."""
        flota.listar_inventario()