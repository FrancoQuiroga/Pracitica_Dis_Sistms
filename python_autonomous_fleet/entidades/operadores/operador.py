#!/usr/bin/env python3
"""
Modulo de la Entidad Operador (Tecnico).

Analogia de 'Trabajador'.
Contiene los datos del tecnico y su lista de certificaciones.
"""

from typing import List
from .certificacion import Certificacion

class Operador:
    """
    Representa a un tecnico de mantenimiento o supervisor de flota (US-401).
    Contiene una coleccion de sus certificaciones (US-402).
    """

    def __init__(self, id_operador: str, nombre_completo: str):
        self._id_operador: str = id_operador
        self._nombre_completo: str = nombre_completo
        
        # Lista de certificaciones que posee el operador
        self._certificaciones: List[Certificacion] = []
        
        print(f"[Operador] Creado Operador: {self.nombre} (ID: {self.id})")

    @property
    def id(self) -> str:
        return self._id_operador

    @property
    def nombre(self) -> str:
        return self._nombre_completo

    def agregar_certificacion(self, certificacion: Certificacion):
        """Agrega una nueva certificacion a la lista del operador."""
        if isinstance(certificacion, Certificacion):
            self._certificaciones.append(certificacion)
            print(f"[Operador {self.id}] Certificacion '{certificacion.nombre}' agregada.")
        else:
            raise TypeError("Solo se pueden agregar objetos de tipo Certificacion")

    def esta_certificado_para(self, nombre_cert_requerida: str) -> bool:
        """
        Verifica si el operador posee una certificacion especifica
        Y si esta vigente.
        (Criterio de aceptacion de US-403)
        """
        for cert in self._certificaciones:
            if cert.nombre == nombre_cert_requerida:
                if cert.esta_vigente():
                    return True # La tiene y esta vigente
                else:
                    print(f"[Operador {self.id}] Alerta: Posee '{nombre_cert_requerida}' pero esta VENCIDA.")
                    return False # La tiene, pero vencida
        
        return False # No posee la certificacion

    def mostrar_perfil(self):
        """Muestra un resumen del operador y sus certificaciones."""
        print(f"\n--- Perfil de Operador: {self.nombre} ({self.id}) ---")
        if not self._certificaciones:
            print("  (Sin certificaciones registradas)")
        else:
            for cert in self._certificaciones:
                print(f"  - {cert}")
        print("-" * (30 + len(self.nombre) + len(self.id)))