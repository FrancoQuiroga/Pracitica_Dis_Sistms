#!/usr/bin/env python3
"""
Modulo de Servicio para BitacoraMision (Persistencia).

Analogia de 'RegistroForestalService'.
Maneja la logica de guardar y leer bitacoras en disco (Pickle).
"""

import pickle
import os
from typing import List

from python_autonomous_fleet.entidades.infraestructura.bitacora_mision import BitacoraMision

# Define el directorio donde se guardaran las bitacoras
DIRECTORIO_BITACORAS = "bitacoras_misiones"

class BitacoraService:
    """
    Servicio encargado de la logica de persistencia de las misiones.
    (Cumple US-503 y US-504)
    """

    def __init__(self):
        # Asegura que el directorio de persistencia exista
        if not os.path.exists(DIRECTORIO_BITACORAS):
            os.makedirs(DIRECTORIO_BITACORAS)
            print(f"[BitacoraService] Creado directorio de persistencia: {DIRECTORIO_BITACORAS}")

    def _get_ruta_archivo(self, id_vehiculo: str) -> str:
        """Metodo helper para obtener la ruta estandar del archivo de bitacora."""
        # Guarda un archivo por vehiculo
        return os.path.join(DIRECTORIO_BITACORAS, f"bitacora_vehiculo_{id_vehiculo}.pkl")

    def persistir_bitacora(self, bitacora: BitacoraMision):
        """
        Caso de Uso: Persistir una bitacora de mision (US-503).
        
        Utiliza Pickle para guardar, igual que el proyecto original.
        Agrega el registro a la lista existente de ese vehiculo.
        """
        ruta_archivo = self._get_ruta_archivo(bitacora.id_vehiculo)
        
        # Lee las bitacoras existentes (si las hay)
        bitacoras_existentes = self.leer_bitacora(bitacora.id_vehiculo)
        
        # Agrega la nueva bitacora
        bitacoras_existentes.append(bitacora)
        
        # Escribe la lista completa de nuevo
        try:
            with open(ruta_archivo, 'wb') as f:
                pickle.dump(bitacoras_existentes, f)
            print(f"[BitacoraService] Bitacora {bitacora.id_mision} persistida para vehiculo {bitacora.id_vehiculo}.")
        except IOError as e:
            print(f"[BitacoraService] ERROR: No se pudo persistir la bitacora en {ruta_archivo}. {e}")
        except pickle.PicklingError as e:
            print(f"[BitacoraService] ERROR: Falla al 'picklear' la bitacora. {e}")

    def leer_bitacora(self, id_vehiculo: str) -> List[BitacoraMision]:
        """
        Caso de Uso: Recuperar el historial de misiones de un vehiculo (US-504).
        
        Utiliza Pickle para leer, igual que el proyecto original.
        """
        ruta_archivo = self._get_ruta_archivo(id_vehiculo)
        
        if not os.path.exists(ruta_archivo):
            #print(f"[BitacoraService] No se encontro historial para {id_vehiculo}. Se asume vacio.")
            return [] # Devuelve lista vacia si no hay archivo

        try:
            with open(ruta_archivo, 'rb') as f:
                bitacoras = pickle.load(f)
                if not isinstance(bitacoras, list):
                     raise TypeError("El archivo de bitacora no contiene una lista.")
                return bitacoras
        except (IOError, pickle.UnpicklingError, TypeError, EOFError) as e:
            print(f"[BitacoraService] ERROR: No se pudo leer la bitacora {ruta_archivo}. Archivo corrupto o invalido. {e}")
            # Si hay corrupcion, mejor devolver vacio para no romper el sistema
            return []