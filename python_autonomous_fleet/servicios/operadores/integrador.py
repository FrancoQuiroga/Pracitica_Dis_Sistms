"""
Archivo integrador generado automaticamente
Directorio: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operadores
Fecha: 2025-11-04 19:19:55
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operadores\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: operador_service.py
# Ruta: C:\Users\Admin\Documents\Facultad\SegundoProyectoDiseñoSistemas\python_autonomous_fleet\servicios\operadores\operador_service.py
# ================================================================================

#!/usr/bin/env python3
"""
Modulo de Servicio para Operador.

Analogia de 'TrabajadorService'.
Contiene la logica de negocio para gestionar Operadores,
Certificaciones y Misiones.
"""

from datetime import date

# Import de Entidades
from python_autonomous_fleet.entidades.operadores.operador import Operador
from python_autonomous_fleet.entidades.operadores.certificacion import Certificacion
from python_autonomous_fleet.entidades.operadores.mision import Mision, TipoMision

# Import de Excepciones
from python_autonomous_fleet.excepciones.excepciones_operador import OperadorNoCalificadoError

class OperadorService:
    """
    Servicio encargado de la logica de negocio de Operadores.
    (Cumple Epic 4: US-401, US-402, US-403)
    """

    def crear_operador(self, id_operador: str, nombre_completo: str) -> Operador:
        """
        Caso de Uso: Registrar un nuevo Operador (US-401).
        """
        print(f"[OperadorService] Registrando nuevo operador: {nombre_completo}")
        operador = Operador(id_operador=id_operador, nombre_completo=nombre_completo)
        
        # ... logica de persistencia (ej. self.db.save(operador))
        return operador

    def agregar_certificacion_a_operador(self, 
                                          operador: Operador, 
                                          nombre_cert: str, 
                                          fecha_venc: date) -> Certificacion:
        """
        Caso de Uso: Asignar una certificacion a un operador (US-402).
        """
        print(f"[OperadorService] Agregando certificacion '{nombre_cert}' a {operador.nombre}")
        
        if not isinstance(operador, Operador):
            raise TypeError("El objeto 'operador' no es de tipo Operador.")
            
        certificacion = Certificacion(
            nombre_certificacion=nombre_cert,
            fecha_vencimiento=fecha_venc
        )
        
        operador.agregar_certificacion(certificacion)
        
        # ... logica de persistencia (ej. self.db.update(operador))
        return certificacion

    def crear_y_asignar_mision(self,
                               id_mision: str,
                               tipo_mision: TipoMision,
                               id_vehiculo: str,
                               operador: Operador,
                               descripcion: str,
                               cert_requerida: str) -> Mision:
        """
        Caso de Uso: Asignar una mision de mantenimiento a un operador (US-403).
        
        Verifica que el operador este calificado (US-403 Criterio Aceptacion).
        """
        print(f"[OperadorService] Intentando asignar mision {id_mision} a {operador.nombre}...")
        
        # Validacion de Negocio (Criterio de Aceptacion US-403)
        # El OperadorService verifica la calificacion antes de crear la Mision.
        if not operador.esta_certificado_para(cert_requerida):
            raise OperadorNoCalificadoError(
                f"FALLO ASIGNACION: Operador {operador.nombre} no esta calificado "
                f"o su certificacion '{cert_requerida}' esta vencida."
            )

        print(f"[OperadorService] Operador {operador.nombre} esta calificado. Creando mision.")
        
        mision = Mision(
            id_mision=id_mision,
            tipo_mision=tipo_mision,
            id_vehiculo_asignado=id_vehiculo,
            id_operador_asignado=operador.id,
            descripcion=descripcion
        )
        
        # ... logica de persistencia (ej. self.db.save(mision))
        return mision

    def iniciar_mision_operador(self, mision: Mision):
        """Caso de Uso: El operador inicia la mision asignada."""
        mision.iniciar_mision()
        
    def completar_mision_operador(self, mision: Mision):
        """Caso de Uso: El operador completa la mision."""
        mision.completar_mision()

