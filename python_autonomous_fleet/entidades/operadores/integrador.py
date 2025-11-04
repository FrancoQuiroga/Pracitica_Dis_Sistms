"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\operadores
Fecha: 2025-11-04 19:19:55
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: certificacion.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\operadores\certificacion.py
# ================================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Certificacion.

Analogia de 'AptoMedico'.
Representa una licencia o certificacion con fecha de vencimiento.
"""

from datetime import date

class Certificacion:
    """
    Representa una certificacion o licencia que un Operador debe poseer
    para realizar mantenimientos (US-402).
    """

    def __init__(self, nombre_certificacion: str, fecha_vencimiento: date):
        self._nombre_certificacion: str = nombre_certificacion
        self._fecha_vencimiento: date = fecha_vencimiento
        
        if not isinstance(fecha_vencimiento, date):
            raise TypeError("fecha_vencimiento debe ser un objeto datetime.date")

    @property
    def nombre(self) -> str:
        return self._nombre_certificacion

    @property
    def vencimiento(self) -> date:
        return self._fecha_vencimiento

    def esta_vigente(self) -> bool:
        """
        Verifica si la certificacion no ha expirado.
        (Criterio de aceptacion de US-402)
        """
        return date.today() <= self._fecha_vencimiento

    def __str__(self) -> str:
        estado = "VIGENTE" if self.esta_vigente() else "VENCIDA"
        return (f"Certificacion(Nombre: {self.nombre}, "
                f"Vence: {self.vencimiento}, Estado: {estado})")

# ================================================================================
# ARCHIVO 2/3: mision.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\operadores\mision.py
# ================================================================================

#!/usr/bin/env python3
"""
Modulo de la Entidad Mision.

Analogia de 'Tarea'.
Representa una asignacion de trabajo (Mantenimiento o Delivery)
para un Operador y un Vehiculo.
"""

from enum import Enum, auto
from datetime import datetime

class TipoMision(Enum):
    """Define los tipos de misiones que se pueden asignar."""
    MANTENIMIENTO_PREVENTIVO = auto()
    REPARACION_AVERIA = auto()
    SUPERVISION_CARGA = auto() # (US-501)
    
class EstadoMision(Enum):
    """Define los estados de una mision."""
    ASIGNADA = auto()
    EN_PROGRESO = auto()
    COMPLETADA = auto()
    CANCELADA = auto()

class Mision:
    """
    Representa una asignacion de trabajo (US-403).
    Vincula un Operador, un Vehiculo y una descripcion del trabajo.
    """

    def __init__(self,
                 id_mision: str,
                 tipo_mision: TipoMision,
                 id_vehiculo_asignado: str,
                 id_operador_asignado: str,
                 descripcion: str):
                     
        self.id_mision: str = id_mision
        self.tipo_mision: TipoMision = tipo_mision
        self.id_vehiculo_asignado: str = id_vehiculo_asignado
        self.id_operador_asignado: str = id_operador_asignado
        self.descripcion: str = descripcion
        self.estado: EstadoMision = EstadoMision.ASIGNADA
        self.fecha_creacion: datetime = datetime.now()
        
        print(f"[Mision {self.id_mision}] Creada: {self.tipo_mision.name} "
              f"para Vehiculo {self.id_vehiculo_asignado} "
              f"asignada a Operador {self.id_operador_asignado}")

    def iniciar_mision(self):
        self.estado = EstadoMision.EN_PROGRESO
        print(f"[Mision {self.id_mision}] EN PROGRESO.")

    def completar_mision(self):
        self.estado = EstadoMision.COMPLETADA
        print(f"[Mision {self.id_mision}] COMPLETADA.")

    def __str__(self) -> str:
        return (f"Mision(ID: {self.id_mision}, "
                f"Tipo: {self.tipo_mision.name}, "
                f"Vehiculo: {self.id_vehiculo_asignado}, "
                f"Operador: {self.id_operador_asignado}, "
                f"Estado: {self.estado.name})")

# ================================================================================
# ARCHIVO 3/3: operador.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\entidades\operadores\operador.py
# ================================================================================

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

