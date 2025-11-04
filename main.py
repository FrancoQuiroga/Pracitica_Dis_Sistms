#!/usr/bin/env python
"""
SISTEMA DE GESTION DE FLOTA AUTONOMA - DEMOSTRACION COMPLETA

Este script ensambla y demuestra todos los casos de uso y patrones
de diseño del sistema de gestion de flota, adaptado desde el
proyecto de gestion forestal.

Demuestra:
- Factory: Creacion de multiples tipos de vehiculos.
- Observer: Monitoreo de sensores (Trafico, Clima) y Bateria.
- Strategy: Algoritmos de ruteo intercambiables.
- Singleton: Instancia unica del VehicleServiceRegistry.
- Registry: Dispatch polimorfico para operaciones de mision.
- Arquitectura: Separacion clara de Entidades y Servicios por dominio.
"""

import time
import os
from datetime import date, timedelta

# ===== IMPORTS DEL SISTEMA (Servicios) =====
# (Analogia de imports de servicios de forestacion)

# Servicios de Infraestructura (Era: terrenos)
from python_autonomous_fleet.servicios.infraestructura.estacion_base_service import EstacionBaseService
from python_autonomous_fleet.servicios.infraestructura.flota_service import FlotaService
from python_autonomous_fleet.servicios.infraestructura.bitacora_service import BitacoraService

# Servicios de Operadores (Era: personal)
from python_autonomous_fleet.servicios.operadores.operador_service import OperadorService

# Servicios de Operaciones (Orquestador) (Era: negocio)
from python_autonomous_fleet.servicios.operaciones.flota_operations_service import FlotaOperationsService

# Servicios de Vehiculos (Singleton/Registry) (Era: cultivos)
from python_autonomous_fleet.servicios.vehiculos.vehicle_service_registry import VehicleServiceRegistry

# ===== IMPORTS DE ENTIDADES Y PATRONES =====
# (Necesarios para la demo)

# Entidades (Operadores)
from python_autonomous_fleet.entidades.operadores.operador import Operador
from python_autonomous_fleet.entidades.operadores.mision import TipoMision

# Patrones (Observer)
from python_autonomous_fleet.entidades.patrones.observer.servicio_externo import ServicioTrafico, ServicioClima
# Patrones (Strategy)
from python_autonomous_fleet.entidades.patrones.strategy.ruteo_strategy import RutaEcoStrategy, RutaMasSeguraStrategy

# Excepciones
from python_autonomous_fleet.excepciones.excepciones_operador import OperadorError


def main():
    """Punto de entrada principal de la demostracion."""
    
    # NOTA DE COMPATIBILIDAD (Igual que en el proyecto original)
    # Algunas consolas de Windows (no-modernas) no soportan emojis UTF-8.
    # Usaremos ASCII [OK], [!] para asegurar compatibilidad.
    
    print("=" * 70)
    print("  INICIANDO DEMOSTRACION: SISTEMA DE GESTION DE FLOTA AUTONOMA")
    print("=" * 70)
    
    try:
        # ===== SECCION 1: CREACION DE INFRAESTRUCTURA (Estaciones) =====
        # (Analg. SECCION 1: CREACION DE TERRENOS)
        print("\n" + "-" * 50)
        print("  1. INFRAESTRUCTURA: Creando Estaciones Base (Hubs)")
        print("-" * 50)
        
        estacion_service = EstacionBaseService()
        
        # US-101: Registrar estacion de carga
        hub_central = estacion_service.crear_estacion_base(
            id_estacion="HUB-CT-01",
            ubicacion="Zona Centro, Ciudad Capital",
            capacidad_kw=1000
        )
        print(f"[OK] Estacion Base creada: {hub_central.id}")
        
        
        # ===== SECCION 2: CREACION DE FLOTAS =====
        # (Analg. SECCION 2: CREACION DE PLANTACIONES)
        print("\n" + "-" * 50)
        print("  2. FLOTAS: Creando Flota Operativa")
        print("-" * 50)
        
        flota_service = FlotaService()
        
        # US-102: Crear flota de vehiculos asociada a estacion
        flota_centro = flota_service.crear_flota(
            id_flota="FLT-CT-A",
            nombre_flota="Flota 'Aguilas del Centro'",
            estacion_base=hub_central
        )
        print(f"[OK] Flota creada: {flota_centro.nombre}")
        
        
        # ===== SECCION 3: GESTION DE FLOTA (FACTORY PATTERN) =====
        # (Analg. SECCION 3: GESTION DE CULTIVOS (FACTORY))
        print("\n" + "-" * 50)
        print("  3. VEHICULOS (Factory): Agregando vehiculos a la flota")
        print("-" * 50)
        
        # US-201: Agregar Dron
        v_dron = flota_service.agregar_vehiculo_a_flota(
            flota_centro, hub_central, "DronEntrega", "DRN-001"
        )
        
        # US-202: Agregar Robot
        v_robot = flota_service.agregar_vehiculo_a_flota(
            flota_centro, hub_central, "RobotTerrestre", "RBT-002"
        )
        
        # US-203: Agregar Furgoneta
        v_furgoneta = flota_service.agregar_vehiculo_a_flota(
            flota_centro, hub_central, "FurgonetaAutonoma", "FGN-003"
        )
        
        # US-204: Agregar Bicicleta
        v_bici = flota_service.agregar_vehiculo_a_flota(
            flota_centro, hub_central, "BicicletaAutonoma", "BCL-004"
        )

        print("[INFO] 4 tipos de vehiculos creados usando VehicleFactory.")
        
        # US-103: Crear registro completo de flota (Reporte)
        flota_service.reporte_inventario(flota_centro)
        
        
        # ===== SECCION 4: GESTION DE OPERADORES (Tecnicos) =====
        # (Analg. SECCION 4: GESTION DE PERSONAL)
        print("\n" + "-" * 50)
        print("  4. OPERADORES: Registrando tecnicos y certificaciones")
        print("-" * 50)
        
        op_service = OperadorService()
        
        # US-401: Registrar operador
        op_ana = op_service.crear_operador(
            id_operador="TEC-101", 
            nombre_completo="Ana Garcia (Especialista Drones)"
        )
        
        # US-402: Asignar licencia de operacion (Certificacion)
        op_service.agregar_certificacion_a_operador(
            op_ana, 
            "Certificacion Drones Nivel 3", 
            date.today() + timedelta(days=365) # Vigente
        )
        
        # US-401 y US-402 (Ejemplo 2, para prueba de falla)
        op_juan = op_service.crear_operador(
            id_operador="TEC-102", 
            nombre_completo="Juan Perez (Especialista Furgonetas)"
        )
        op_service.agregar_certificacion_a_operador(
            op_juan, 
            "Certificacion Furgonetas Nivel 2", 
            date.today() - timedelta(days=30) # Vencida!
        )
        
        op_ana.mostrar_perfil()
        op_juan.mostrar_perfil()
        
        
        # ===== SECCION 5: SISTEMA DE MONITOREO (OBSERVER PATTERN) =====
        # (Analg. SECCION 5: SISTEMA DE RIEGO (OBSERVER))
        print("\n" + "-" * 50)
        print("  5. MONITOREO (Observer): Simulando eventos externos")
        print("-" * 50)

        # --- Parte 1: Vehiculo como Observer (US-301, US-302) ---
        print("[INFO] Parte A: Vehiculo (Observer) escucha a Sensores (Observable)")
        
        servicio_trafico = ServicioTrafico()
        servicio_clima = ServicioClima()
        
        # Suscribimos al Dron (v_dron) a los servicios de trafico y clima
        servicio_trafico.suscribir(v_dron)
        servicio_clima.suscribir(v_dron)

        # Simulamos eventos externos
        servicio_trafico.simular_congestion("Zona Centro")
        time.sleep(0.1)
        servicio_clima.simular_alerta_viento(65)
        
        # --- Parte 2: Vehiculo como Observable (US-303) ---
        print("\n[INFO] Parte B: Estacion (Observer) escucha a Vehiculo (Observable)")
        # (La suscripcion se hizo automaticamente en FlotaService)
        
        print(f"[INFO] Simulando consumo de bateria de {v_dron.id}...")
        v_dron.consumir_bateria(88.0) # Esto debe disparar el evento "BATERIA_BAJA"
        
        
        # ===== SECCION 6: ALGORITMOS DE RUTEO (STRATEGY PATTERN) =====
        # (Analg. SECCION 6: ALGORITMOS DE ABSORCION (STRATEGY))
        print("\n" + "-" * 50)
        print("  6. NAVEGACION (Strategy): Cambiando algoritmo de ruteo")
        print("-" * 50)
        
        print(f"[INFO] {v_furgoneta.id} iniciara mision (Strategy: Default/Rapida)")
        v_furgoneta.ejecutar_mision("Hub Central", "Almacen Norte")
        
        # US-304: Cambiar estrategia
        print(f"\n[INFO] Cambiando {v_furgoneta.id} a RutaEcoStrategy...")
        v_furgoneta.set_ruteo_strategy(RutaEcoStrategy())
        
        print(f"[INFO] {v_furgoneta.id} iniciara mision (Strategy: Eco)")
        v_furgoneta.ejecutar_mision("Hub Central", "Cliente B (Eco)")

        
        # ===== SECCION 7: OPERACIONES DE FLOTA (REGISTRY/SINGLETON) =====
        # (Analg. SECCION 7: OPERACIONES DE NEGOCIO (REGISTRY/SINGLETON))
        print("\n" + "-" * 50)
        print("  7. OPERACIONES (Registry/Singleton): Orquestando Casos de Uso")
        print("-" * 50)

        # 1. Obtenemos el Orquestador
        # (El Orquestador obtiene la instancia UNICA (Singleton) del Registry)
        ops_service = FlotaOperationsService()
        
        # 2. Demo Asignacion Mantenimiento (US-403) - Caso Exitoso
        print("\n[INFO] Prueba 1: Asignacion de Mantenimiento (EXITO)")
        ops_service.asignar_mision_mantenimiento(
            id_mision="M-001",
            vehiculo=v_dron,
            operador=op_ana,
            cert_requerida="Certificacion Drones Nivel 3"
        )
        
        # 3. Demo Asignacion Mantenimiento (US-403) - Caso Falla (No Calificado)
        print("\n[INFO] Prueba 2: Asignacion de Mantenimiento (FALLA - No Calificado)")
        ops_service.asignar_mision_mantenimiento(
            id_mision="M-002",
            vehiculo=v_furgoneta, # Furgoneta
            operador=op_ana,     # Operadora de Drones
            cert_requerida="Certificacion Furgonetas Nivel 2"
        )
        
        # 4. Demo Asignacion Mantenimiento (US-403) - Caso Falla (Vencido)
        print("\n[INFO] Prueba 3: Asignacion de Mantenimiento (FALLA - Cert Vencida)")
        ops_service.asignar_mision_mantenimiento(
            id_mision="M-003",
            vehiculo=v_furgoneta,
            operador=op_juan, # Certificacion Vencida
            cert_requerida="Certificacion Furgonetas Nivel 2"
        )
        
        # 5. Demo Delivery Polimorfico (US-501, US-T05)
        print("\n[INFO] Prueba 4: Delivery Polimorfico (Registry) y Persistencia")
        # El Orquestador usara el Registry para ejecutar esto, y luego
        # usara el BitacoraService para persistirlo.
        ops_service.ejecutar_mision_delivery_polimorfica(
            id_mision="D-001",
            vehiculo=v_dron, # (El Registry usara el 'dron_handler')
            origen="Hub Central",
            destino="Cliente A (Av. Siempreviva 123)"
        )
        
        
        # ===== SECCION 8: PERSISTENCIA (Bitacora) =====
        # (Analg. SECCION 8: PERSISTENCIA)
        print("\n" + "-" * 50)
        print("  8. PERSISTENCIA: Leyendo bitacora de misiones")
        print("-" * 50)
        
        # La persistencia (escritura) se realizo en el paso anterior (US-503).
        # Ahora solo leemos (US-504).
        
        bitacora_service = BitacoraService()
        
        print(f"[INFO] Recuperando historial de misiones para {v_dron.id}...")
        historial_dron = bitacora_service.leer_bitacora(v_dron.id)
        
        if not historial_dron:
            print(f"[!] No se encontro historial para {v_dron.id}")
        else:
            for registro in historial_dron:
                print(registro) # Imprime el __str__ de BitacoraMision
        
        print("[OK] Bitacora leida desde disco.")
        
        
        # ===== RESUMEN FINAL =====
        print("\n" + "=" * 70)
        print("              EJEMPLO COMPLETADO EXITOSAMENTE")
        print("=" * 70)
        print("  [OK] SINGLETON   - VehicleServiceRegistry (instancia unica)")
        print("  [OK] FACTORY     - Creacion de 4 tipos de vehiculos")
        print("  [OK] OBSERVER    - Sistema de sensores (Clima/Trafico) y Bateria")
        print("  [OK] STRATEGY    - Algoritmos de ruteo (Rapido, Eco)")
        print("  [OK] REGISTRY    - Dispatch polimorfico para misiones (sin if/isinstance)")
        print("  [OK] ARQUITECTURA- Separacion Entidades/Servicios/Excepciones por Dominio")
        print("=" * 70)

    except OperadorError as e:
        # Ejemplo de excepcion de negocio personalizada
        print("\n" + "!" * 70)
        print(f" [!] ERROR DE NEGOCIO CONTROLADO: {e.mensaje}")
        print("!" * 70)
    except Exception as e:
        # Excepcion generica
        print("\n" + "!" * 70)
        print(f" [!] ERROR INESPERADO: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        print("!" * 70)

if __name__ == "__main__":
    main()