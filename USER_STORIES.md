# Historias de Usuario - Sistema de Gestión de Flota Autónoma

**Proyecto**: AutonomousFleetMgmt
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Metodologia**: User Story Mapping

---

## Índice

1. [Epic 1: Gestión de Estaciones y Flotas](#epic-1-gestión-de-estaciones-y-flotas)
2. [Epic 2: Gestión de Tipos de Vehículos](#epic-2-gestión-de-tipos-de-vehículos)
3. [Epic 3: Sistema de Navegación y Monitoreo](#epic-3-sistema-de-navegación-y-monitoreo)
4. [Epic 4: Gestión de Operadores y Mantenimiento](#epic-4-gestión-de-operadores-y-mantenimiento)
5. [Epic 5: Operaciones y Bitácora](#epic-5-operaciones-y-bitácora)
6. [Historias Técnicas (Patrones de Diseño)](#historias-técnicas-patrones-de-diseño)

---

## Epic 1: Gestión de Estaciones y Flotas

*(Analogía del Epic 1 de Forestación: "Gestión de Terrenos y Plantaciones")*

### US-101: Registrar Estación Base (Hub)

**Como** administrador de flota,
**Quiero** registrar una nueva "Estación Base" (Hub) con su ubicación (coordenadas) y su capacidad energética total (ej. 500 kW),
**Para** tener un control centralizado de mis puntos de carga y despacho.

#### Criterios de Aceptación

- [ ] El sistema debe permitir crear una Estación Base con:
  - `id_estacion` (único)
  - `ubicacion` (ej. lat/lon o dirección)
  - `capacidad_energetica_kw` (numérico)
- [ ] No se puede registrar una estación con un `id_estacion` duplicado.
- *(Analogía: `Tierra` [US-001])*

### US-102: Crear Flota Operativa

**Como** administrador de flota,
**Quiero** crear una "Flota" (ej. 'Flota Zona Centro') y asociarla a una Estación Base existente,
**Para** agrupar y organizar los vehículos por zona operativa.

#### Criterios de Aceptación

- [ ] El sistema debe permitir crear una Flota con:
  - `id_flota` (único)
  - `nombre_flota` (ej. "Flota Centro")
- [ ] Se debe poder asociar una Flota a una `id_estacion` válida.
- *(Analogía: `Plantacion` [US-002])*

### US-103: Inventariar vehículos en una Estación

**Como** administrador de flota,
**Quiero** poder consultar una Estación Base y ver un listado de todos los vehículos (con su ID y tipo) asignados a ella,
**Para** conocer el inventario y estado de mi flota en ese Hub.

#### Criterios de Aceptación

- [ ] La Estación Base debe mantener una lista (`inventario_vehiculos`) de los objetos `Vehiculo` asignados.
- [ ] Debe existir un método `estacion.listar_vehiculos()` que devuelva dicha lista.
- *(Analogía: `Plantacion.cultivos` [US-003])*

---

## Epic 2: Gestión de Tipos de Vehículos

*(Analogía del Epic 2 de Forestación: "Gestión de Cultivos")*

### US-201: Agregar Dron de Entrega Rápida

**Como** administrador de flota,
**Quiero** dar de alta un "Dron de Entrega Rápida" en el sistema,
**Para** que esté disponible en la flota para misiones de corto alcance y baja carga.

#### Criterios de Aceptación

- [ ] El sistema debe usar el `VehicleFactory` para crear una instancia de `DronEntrega`.
- [ ] El Dron debe tener atributos específicos: `autonomia_km: 20`, `carga_max_kg: 5`, `velocidad_max_kmh: 80`.
- *(Analogía: `Pino` [US-004])*

### US-202: Agregar Robot Terrestre

**Como** administrador de flota,
**Quiero** dar de alta un "Robot Terrestre" para corta distancia,
**Para** que esté disponible para entregas en aceras y zonas peatonales.

#### Criterios de Aceptación

- [ ] El sistema debe usar el `VehicleFactory` para crear una instancia de `RobotTerrestre`.
- [ ] El Robot debe tener atributos específicos: `autonomia_km: 15`, `carga_max_kg: 25`, `velocidad_max_kmh: 10`.
- *(Analogía: `Olivo` [US-005])*

### US-203: Agregar Furgoneta Autónoma

**Como** administrador de flota,
**Quiero** dar de alta una "Furgoneta Autónoma" para carga pesada,
**Para** que esté disponible para misiones de gran volumen y larga distancia.

#### Criterios de Aceptación

- [ ] El sistema debe usar el `VehicleFactory` para crear una instancia de `FurgonetaAutonoma`.
- [ ] La Furgoneta debe tener atributos específicos: `autonomia_km: 300`, `carga_max_kg: 500`, `volumen_carga_m3: 10`.
- *(Analogía: `Lechuga` [US-006])*

### US-204: Agregar Bicicleta Autónoma

**Como** administrador de flota,
**Quiero** dar de alta una "Bicicleta Autónoma" para zonas peatonales,
**Para** realizar entregas rápidas y ecológicas en zonas de acceso restringido.

#### Criterios de Aceptación

- [ ] El sistema debe usar el `VehicleFactory` para crear una instancia de `BicicletaAutonoma`.
- [ ] La Bicicleta debe tener atributos específicos: `autonomia_km: 40`, `carga_max_kg: 10`, `tipo: "E-bike"`.
- *(Analogía: `Tomate` [US-007])*

---

## Epic 3: Sistema de Navegación y Monitoreo

*(Analogía del Epic 3 de Forestación: "Sistema de Riego Automatizado")*

### US-301: Monitorear tráfico en tiempo real (Observer)

**Como** vehículo autónomo (Observer),
**Quiero** suscribirme a un 'Servicio de Tráfico' (Observable/Subject),
**Para** recibir notificaciones instantáneas (eventos) cuando haya alta congestión en mi zona de ruta.

#### Criterios de Aceptación

- [ ] Debe existir una clase `ServicioTrafico` (Observable) que implemente `suscribir(observer)` y `notificar()`.
- [ ] La clase `Vehiculo` (Observer) debe implementar `actualizar(evento)`.
- [ ] Al recibir un evento de "ALTA_CONGESTION", el vehículo debe registrarlo.
- *(Analogía: `SensorHumedad` [US-008])*

### US-302: Monitorear condiciones climáticas (Observer)

**Como** vehículo autónomo (Observer),
**Quiero** suscribirme a un 'Servicio de Clima' (Observable/Subject),
**Para** recibir alertas de "VIENTO_FUERTE" o "LLUVIA_INTENSA" que afecten mi navegación.

#### Criterios de Aceptación

- [ ] Debe existir una clase `ServicioClima` (Observable).
- [ ] Los Drones y Bicicletas deben suscribirse a este servicio.
- [ ] Al recibir un evento de "VIENTO_FUERTE", el Dron debe evaluar un cambio de ruta o regreso a base.
- *(Analogía: `SensorTemperatura` [US-010])*

### US-303: Monitorear batería del vehículo (Observer)

**Como** vehículo autónomo (Observable),
**Quiero** notificar a mi Estación Base (Observer) cuando mi nivel de batería caiga por debajo del 15%,
**Para** que la Estación Base pueda gestionar la cola de recarga.

#### Criterios de Aceptación

- [ ] La clase `Vehiculo` debe actuar como `Observable` en este caso.
- [ ] La `EstacionBase` debe actuar como `Observer` y suscribirse a sus vehículos.
- [ ] Al recibir el evento "BATERIA_BAJA", la Estación debe registrar el vehículo en `cola_de_carga`.
- *(Nueva Historia, inspirada en US-008)*

### US-304: Asignar algoritmo de ruteo (Strategy)

**Como** vehículo autónomo,
**Quiero** poder cambiar dinámicamente mi `AlgoritmoDeRuteo` (Strategy),
**Para** poder usar `RutaMasRapidaStrategy` (ignora batería) o `RutaEcoStrategy` (ahorra batería) según la misión.

#### Criterios de Aceptación

- [ ] Debe existir una interfaz `RuteoStrategy` con un método `calcular_ruta(origen, destino)`.
- [ ] Deben existir implementaciones concretas: `RutaMasRapidaStrategy`, `RutaEcoStrategy`, `RutaMasSeguraStrategy`.
- [ ] El `Vehiculo` debe tener un método `set_ruteo_strategy(strategy)`.
- *(Analogía: `AbsorcionStrategy` [US-011])*

### US-305: Ejecutar recarga automática

**Como** vehículo autónomo,
**Quiero** ejecutar autónomamente la acción "ir a recargar" cuando mi batería esté baja,
**Para** dirigirme a mi Estación Base asignada y conectarme al cargador.

#### Criterios de Aceptación

- [ ] Esta acción debe ser desencadenada por el evento "BATERIA_BAJA" (US-303).
- [ ] La acción debe usar el `RuteoStrategy` actual para calcular la ruta de vuelta a la Estación Base.
- *(Analogía: `Tierra.regar()` [US-009])*

---

## Epic 4: Gestión de Operadores y Mantenimiento

*(Analogía del Epic 4 de Forestación: "Gestión de Personal")*

### US-401: Registrar Operador (Técnico)

**Como** administrador de flota,
**Quiero** registrar un 'Operador' (Técnico de Mantenimiento) con sus datos personales y un listado de certificaciones,
**Para** gestionar el personal habilitado para el mantenimiento de los vehículos.

#### Criterios de Aceptación

- [ ] El Operador debe tener `id_operador`, `nombre` y `lista_certificaciones`.
- [ ] Las certificaciones deben ser validadas (ej. "Certificación Drones Nivel 3").
- *(Analogía: `Trabajador` [US-013])*

### US-402: Asignar Certificación de Operación

**Como** administrador de flota,
**Quiero** asignar una 'Certificación de Operación' (con fecha de vencimiento) a un Operador,
**Para** asegurar que solo personal cualificado y con licencia vigente pueda realizar mantenimientos.

#### Criterios de Aceptación

- [ ] La `Certificacion` debe tener `nombre_certificacion` y `fecha_vencimiento`.
- [ ] Un Operador con certificaciones vencidas no puede ser asignado a tareas de mantenimiento.
- *(Analogía: `AptoMedico` [US-014])*

### US-403: Asignar Misión de Mantenimiento

**Como** administrador de flota,
**Quiero** asignar una 'Misión de Mantenimiento' (ej. "Revisar Batería Dron-047") a un Operador cualificado,
**Para** asegurar la trazabilidad de las reparaciones y el estado óptimo de la flota.

#### Criterios de Aceptación

- [ ] El sistema no debe permitir asignar una Misión de Dron a un Operador que solo tiene certificación de Furgonetas.
- [ ] La Misión debe registrarse en el historial del Vehículo.
- *(Analogía: `Tarea` [US-015])*

---

## Epic 5: Operaciones y Bitácora

*(Analogía del Epic 5 y 6 de Forestación: "Operaciones de Negocio" y "Persistencia")*

### US-501: Asignar y completar Misión de Delivery

**Como** sistema,
**Quiero** asignar una "Misión de Delivery" (origen, destino, paquete) a un vehículo disponible y con carga suficiente,
**Para** completar una solicitud de entrega del cliente.

#### Criterios de Aceptación

- [ ] El sistema debe verificar que el vehículo tenga `estado: DISPONIBLE` y `bateria_percent > 30%`.
- [ ] Al finalizar, el estado del vehículo debe volver a `DISPONIBLE` o `NECESITA_CARGA`.
- *(Analogía: `Cosechar` [US-017])*

### US-502: Enviar comando de 'Actualización OTA' (Over-the-Air)

**Como** administrador de flota,
**Quiero** enviar un comando de "Actualización de Software OTA" a todos los vehículos de un tipo específico (ej. "actualizar firmware Furgonetas"),
**Para** mantener el software de la flota actualizado de forma masiva.

#### Criterios de Aceptación

- [ ] Debe existir un servicio que pueda iterar sobre todos los vehículos de un tipo (`FurgonetaAutonoma`) y ejecutar el método `actualizar_software()`.
- *(Analogía: `Fumigar` [US-018])*

### US-503: Persistir Bitácora de Misión

**Como** sistema,
**Quiero** persistir (guardar en disco/DB) una 'Bitácora de Misión' al finalizar un delivery o mantenimiento,
**Para** propósitos de auditoría, análisis de rendimiento y cumplimiento legal.

#### Criterios de Aceptación

- [ ] El registro debe contener `id_mision`, `id_vehiculo`, `tipo_vehiculo`, `ruta_realizada`, `hora_inicio`, `hora_fin`, `id_operador_asignado` (si aplica), `incidencias`.
- [ ] Debe usarse un servicio (ej. `BitacoraService`) para manejar la persistencia.
- *(Analogía: `RegistroForestalService.persistir()` [US-021])*

### US-504: Recuperar Bitácora de un vehículo

**Como** auditor de flota,
**Quiero** poder solicitar el historial de misiones de un vehículo específico (por `id_vehiculo`),
**Para** analizar su rendimiento o investigar un incidente.

#### Criterios de Aceptación

- [ ] El `BitacoraService` debe tener un método `leer_bitacora(id_vehiculo)` que devuelva una lista de todos sus registros de misión.
- *(Analogía: `RegistroForestalService.leer_registro()` [US-022])*

---

## Historias Técnicas (Patrones de Diseño)

### US-T01: Implementar VehicleFactory (Factory Method)

**Como** desarrollador,
**Quiero** implementar un `VehicleFactory` (Patrón Factory Method),
**Para** poder crear diferentes tipos de vehículos (`Dron`, `Robot`, `Furgoneta`) sin que el código cliente (`main.py`) conozca las clases concretas.

#### Criterios de Aceptación

- [ ] Debe existir una clase `VehicleFactory` con métodos estáticos (ej. `crear_vehiculo(tipo, **kwargs)`).
- [ ] El Factory debe manejar la creación de al menos 4 tipos de vehículos (US-201 a US-204).
- [ ] El código cliente no debe instanciar `DronEntrega()` directamente, debe usar `VehicleFactory`.
- *(Analogía: `CultivoFactory`)*

### US-T02: Implementar Sistema de Sensores (Observer)

**Como** desarrollador,
**Quiero** implementar el Patrón Observer,
**Para** que los servicios de Clima y Tráfico (Observables) puedan notificar a múltiples Vehículos (Observers) sobre eventos sin estar acoplados.

#### Criterios de Aceptación

- [ ] Deben existir interfaces `Observable` (con `suscribir`, `desuscribir`, `notificar`) y `Observer` (con `actualizar`).
- [ ] `ServicioTrafico` y `ServicioClima` deben implementar `Observable`.
- [ ] `Vehiculo` (o una subclase) debe implementar `Observer`.
- *(Analogía: `Sensor` y `Tierra`)*

### US-T03: Implementar Algoritmos de Ruteo (Strategy)

**Como** desarrollador,
**Quiero** implementar el Patrón Strategy para la navegación,
**Para** permitir que un vehículo cambie su algoritmo de cálculo de ruta en tiempo de ejecución (ej. de Rápido a Eco).

#### Criterios de Aceptación

- [ ] Debe existir una interfaz `RuteoStrategy` (ej. ABC de Python) con `calcular_ruta(a, b)`.
- [ ] Deben existir al menos dos implementaciones concretas (ej. `RutaMasRapidaStrategy`, `RutaEcoStrategy`).
- [ ] La clase `Vehiculo` debe tener un atributo para almacenar la estrategia actual y un método para cambiarla.
- *(Analogía: `AbsorcionStrategy`)*

### US-T04: Implementar VehicleServiceRegistry (Singleton y Registry)

**Como** desarrollador,
**Quiero** que el `VehicleServiceRegistry` se implemente como un **Singleton**,
**Para** asegurar que solo exista una instancia de este registro en toda la aplicación.

#### Criterios de Aceptación

- [ ] Múltiples llamadas a `VehicleServiceRegistry.get_instance()` deben devolver el mismo objeto en memoria.
- *(Analogía: `CultivoServiceRegistry` como Singleton)*

### US-T05: Implementar Dispatch Polimórfico (Registry)

**Como** desarrollador,
**Quiero** que `VehicleServiceRegistry` (Patrón Registry) mapee tipos de vehículos (strings) a sus servicios específicos,
**Para** poder invocar operaciones polimórficas (ej. `servicio.realizar_mantenimiento(vehiculo)`) sin usar cadenas de `if/elif/isinstance`.

#### Criterios de Aceptación

- [ ] El Registry debe tener un método `registrar_servicio(tipo_vehiculo, servicio)`.
- [ ] El Registry debe tener un método `get_servicio(tipo_vehiculo)` que devuelva el servicio correcto.
- [ ] Esto debe eliminar la necesidad de condicionales en el `main.py` al operar sobre vehículos.
- *(Analogía: `CultivoServiceRegistry` como Registry)*