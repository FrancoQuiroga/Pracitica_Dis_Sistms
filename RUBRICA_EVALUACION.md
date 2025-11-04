# Rubrica de Evaluacion Tecnica - Sistema de Gestion de Flota Autonoma

**Proyecto**: PythonAutonomousFleet
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Tipo de Evaluacion**: Tecnica Academica / Profesional

---

## Instrucciones de Uso

Esta rubrica esta disenada para evaluar proyectos de software que implementen patrones de diseno en Python. Se utiliza para:

1.  **Evaluacion academica**: Proyectos de estudiantes en cursos de Ingenieria de Software
2.  **Evaluacion tecnica**: Entrevistas tecnicas para desarrolladores
3.  **Code review**: Revision de calidad de codigo en proyectos profesionales
4.  **Autoevaluacion**: Chequeo de cumplimiento de buenas practicas

### Escala de Puntuacion

-   **Excelente (4 puntos)**: Cumple completamente con criterio, implementacion superior
-   **Bueno (3 puntos)**: Cumple con criterio, implementacion correcta con minimos detalles
-   **Suficiente (2 puntos)**: Cumple parcialmente, implementacion funcional con deficiencias
-   **Insuficiente (1 punto)**: No cumple o cumplimiento minimo, implementacion deficiente
-   **No Implementado (0 puntos)**: Criterio no implementado

### Puntaje Total

-   **Puntaje Maximo**: 260 puntos
-   **Puntaje de Aprobacion**: 182 puntos (70%)
-   **Puntaje de Excelencia**: 234 puntos (90%)

---

## Seccion 1: Patrones de Diseno (80 puntos)

### 1.1 Patron SINGLETON (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Implementacion correcta del patron** | 5 | Clase implementa Singleton con instancia unica | `__new__` con control de instancia unica |
| **Thread-safety** | 5 | Implementacion thread-safe con Lock | Uso de `threading.Lock` con double-checked locking |
| **Acceso consistente** | 3 | Metodo `get_instance()` disponible | Metodo de clase que retorna instancia |
| **Inicializacion perezosa** | 3 | Lazy initialization correcta | Instancia se crea solo cuando se solicita |
| **Uso apropiado en el sistema** | 4 | Singleton usado donde corresponde (Registry) | `VehicleServiceRegistry` es Singleton |

**Puntaje Seccion 1.1**: \_\_\_\_\_ / 20

---

### 1.2 Patron FACTORY METHOD (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Implementacion correcta del patron** | 5 | Factory encapsula creacion de objetos | Metodo estatico `crear_vehiculo(tipo)` |
| **Desacoplamiento** | 5 | Cliente no conoce clases concretas | Retorna tipo base `Vehiculo`, no tipos concretos |
| **Extensibilidad** | 4 | Facil agregar nuevos tipos | Metodo estatico o diccionario, no if/elif cascades |
| **Validacion de entrada** | 3 | Valida parametros y lanza excepciones | Lanza `ValueError` si tipo desconocido |
| **Uso apropiado en el sistema** | 3 | Factory usado en servicios (`FlotaService`) | `agregar_vehiculo_a_flota()` usa factory |

**Puntaje Seccion 1.2**: \_\_\_\_\_ / 20

---

### 1.3 Patron OBSERVER (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Implementacion correcta del patron** | 5 | `Observable` y `Observer` implementados | Clases/Interfaces `Observable` y `Observer` |
| **Tipo-seguridad (Typing)** | 5 | Uso de type hints (ej. `evento: dict`) | Firmas de metodos con type hints |
| **Notificaciones automaticas** | 4 | Observadores notificados al cambiar estado | `notificar(evento)` llamado en `Vehiculo` (bateria) y `ServicioExterno` |
| **Desacoplamiento** | 3 | Observable no conoce detalles de Observer | Lista generica de observadores |
| **Uso apropiado en el sistema** | 3 | `ServicioExterno` y `Vehiculo` (Observable), `Vehiculo` y `EstacionBase` (Observer) |

**Puntaje Seccion 1.3**: \_\_\_\_\_ / 20

---

### 1.4 Patron STRATEGY (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Implementacion correcta del patron** | 5 | Interfaz Strategy con implementaciones | `RuteoStrategy` (abstracta) |
| **Algoritmos intercambiables** | 5 | Multiples estrategias implementadas | `RutaMasRapidaStrategy`, `RutaEcoStrategy`, `RutaMasSeguraStrategy` |
| **Inyeccion de dependencias** | 4 | Estrategia inyectada via constructor | `Vehiculo` recibe `ruteo_strategy_inicial` en `__init__` |
| **Delegacion correcta** | 3 | Contexto delega calculo a estrategia | `Vehiculo.ejecutar_mision()` llama a `_strategy_ruteo.calcular_ruta()` |
| **Uso apropiado en el sistema** | 3 | Estrategias usadas segun contexto | `set_ruteo_strategy()` permite cambio dinamico |

**Puntaje Seccion 1.4**: \_\_\_\_\_ / 20

---

**PUNTAJE TOTAL SECCION 1**: \_\_\_\_\_ / 80

---

## Seccion 2: Arquitectura y Diseno (60 puntos)

### 2.1 Separacion de Responsabilidades (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Entidades vs Servicios** | 5 | Entidades solo datos, servicios solo logica | Clases en `entidades/` vs `servicios/` |
| **Service Layer Pattern** | 5 | Capa de servicios bien definida | Servicios contienen toda la logica de negocio |
| **Principio SRP** | 4 | Cada clase una unica responsabilidad | Una clase = un concepto de dominio |
| **Cohesion alta** | 3 | Elementos relacionados agrupados | Modulos tematicos (vehiculos, infraestructura, operadores) |
| **Acoplamiento bajo** | 3 | Dependencias minimizadas | Uso de interfaces, inyeccion de dependencias |

**Puntaje Seccion 2.1**: \_\_\_\_\_ / 20

---

### 2.2 Jerarquia de Clases (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Herencia apropiada** | 5 | Jerarquia logica de clases | `Vehiculo` (base) -> `DronEntrega` (concreta) |
| **Eliminacion de duplicacion** | 4 | Codigo compartido en clases base | `Vehiculo` contiene logica comun (bateria, estado) |
| **Polimorfismo** | 3 | Subtipos intercambiables | Todos los vehiculos son `Vehiculo` |
| **Interfaces bien definidas** | 3 | Contratos claros entre clases | Metodos abstractos (`describir()`), interfaces (`Observer`) |

**Puntaje Seccion 2.2**: \_\_\_\_\_ / 15

---

### 2.3 Manejo de Excepciones (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Jerarquia de excepciones** | 5 | Excepciones personalizadas heredan de base | `OperadorError`, `VehiculoError` (bases) |
| **Excepciones especificas** | 4 | Excepciones de dominio implementadas | `CertificacionVencidaError`, `OperadorNoCalificadoError`, `TipoVehiculoDesconocidoError` |
| **Mensajes descriptivos** | 3 | Mensajes claros para usuario y tecnico | Mensajes de error especificos |
| **Uso apropiado** | 3 | Excepciones usadas en puntos correctos | `OperadorService` lanza `OperadorNoCalificadoError` |

**Puntaje Seccion 2.3**: \_\_\_\_\_ / 15

---

### 2.4 Organizacion del Codigo (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Estructura de paquetes** | 3 | Organizacion logica de modulos | Paquetes: entidades, servicios, patrones, excepciones |
| **Modulos tematicos** | 3 | Agrupacion por dominio | vehiculos/, infraestructura/, operadores/ |
| **Archivos `__init__.py`** | 2 | Inicializacion de paquetes | Todos los paquetes con `__init__.py` |
| **Importaciones limpias** | 2 | Sin imports circulares | Importaciones absolutas desde la raiz del paquete |

**Puntaje Seccion 2.4**: \_\_\_\_\_ / 10

---

**PUNTAJE TOTAL SECCION 2**: \_\_\_\_\_ / 60

---

## Seccion 3: Calidad de Codigo (60 puntos)

### 3.1 PEP 8 Compliance (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Nombres de variables** | 4 | `snake_case`, descriptivos, sin abreviaciones | `id_vehiculo` no `idV`, `capacidad_kw` no `cap` |
| **Nombres de clases** | 3 | `PascalCase` consistente | `VehicleFactory`, `FlotaService` |
| **Nombres de constantes** | 3 | `UPPER_SNAKE_CASE` | Constantes definidas apropiadamente (ej. en `bitacora_service.py`) |
| **Organizacion de imports** | 4 | PEP 8: Standard -> Third-party -> Local | Secciones comentadas (si aplica) |
| **Longitud de linea** | 2 | Maximo 100-120 caracteres | No lineas excesivamente largas |
| **Espaciado y formato** | 4 | Espaciado consistente segun PEP 8 | 2 lineas entre clases, 1 entre metodos |

**Puntaje Seccion 3.1**: \_\_\_\_\_ / 20

---

### 3.2 Documentacion (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Docstrings en clases** | 4 | Todas las clases documentadas | Docstring en cada clase publica |
| **Docstrings en metodos** | 4 | Metodos publicos documentados | Google Style: Args, Returns, Raises |
| **Formato Google Style** | 3 | Estilo consistente (NO JavaDoc) | `Args:` / `Returns:` / `Raises:` |
| **Comentarios en codigo complejo** | 2 | Explicacion de logica no obvia | Comentarios donde necesario |
| **README y documentacion externa** | 2 | Documentacion de proyecto completa | `README.md`, `USER_STORIES.md` |

**Puntaje Seccion 3.2**: \_\_\_\_\_ / 15

---

### 3.3 Type Hints (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Type hints en firmas** | 4 | Parametros y retornos tipados | `def metodo(param: str) -> int:` |
| **Uso de `typing`** | 3 | Uso de `List`, `Dict`, `Callable`, `Set` | `_observers: List[Observer]` |
| **Uso de `| None`** | 3 | Unions para retornos opcionales | `-> Vehiculo | None:` |

**Puntaje Seccion 3.3**: \_\_\_\_\_ / 10

---

### 3.4 Principios de Codigo Limpio (15 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **NO magic numbers** | 5 | Constantes centralizadas | CERO valores hardcodeados |
| **NO lambdas** | 4 | Funciones/metodos nombrados | Metodos dedicados en Registry |
| **Funciones pequenas** | 3 | Metodos con responsabilidad unica | Funciones < 30 lineas idealmente |
| **Nombres descriptivos** | 3 | Variables y metodos autoexplicativos | `ejecutar_mision_polimorfica()` |

**Puntaje Seccion 3.4**: \_\_\_\_\_ / 15

---

**PUNTAJE TOTAL SECCION 3**: \_\_\_\_\_ / 60

---

## Seccion 4: Funcionalidad del Sistema (40 puntos)

### 4.1 Gestion de Vehiculos (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Multiples tipos de vehiculos** | 4 | Al menos 4 tipos implementados | Dron, Robot, Furgoneta, Bicicleta |
| **Creacion funcional** | 4 | Sistema agrega vehiculos via Factory | `agregar_vehiculo_a_flota()` funcional |
| **Ejecucion de mision funcional** | 4 | Misiones se ejecutan y consumen bateria | `ejecutar_mision()` funcional |

**Puntaje Seccion 4.1**: \_\_\_\_\_ / 12

---

### 4.2 Sistema de Monitoreo Automatizado (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Sensores/Servicios operativos** | 4 | Simulacion de Trafico y Clima | `ServicioExterno` notifica |
| **Control automatico (Eventos)** | 4 | Reaccion a eventos (bateria, clima) | `EstacionBase` y `Vehiculo` implementan `actualizar()` |
| **Suscripcion/Desuscripcion** | 4 | Suscripcion dinamica | `suscribir()` llamado en `FlotaService` |

**Puntaje Seccion 4.2**: \_\_\_\_\_ / 12

---

### 4.3 Gestion de Operadores (8 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Operadores y misiones** | 4 | Sistema asigna y ejecuta misiones | `crear_y_asignar_mision()` funcional |
| **Certificacion (Apto)** | 4 | Validacion de certificacion vigente | `esta_certificado_para()` y excepcion |

**Puntaje Seccion 4.3**: \_\_\_\_\_ / 8

---

### 4.4 Persistencia (8 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Guardado funcional** | 4 | Bitacoras persisten en disco | `persistir_bitacora()` crea archivo .pkl |
| **Lectura funcional** | 4 | Bitacoras recuperadas correctamente | `leer_bitacora()` deserializa |

**Puntaje Seccion 4.4**: \_\_\_\_\_ / 8

---

**PUNTAJE TOTAL SECCION 4**: \_\_\_\_\_ / 40

---

## Seccion 5: Buenas Practicas Avanzadas (20 puntos)

### 5.1 Threading y Concurrencia (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Threads (Simulacion)** | 3 | Simulacion de eventos (no aplica threading) | (N/A en esta version, puntaje otorgado si Observer funciona) |
| **Thread-safety (Singleton)** | 4 | Operaciones thread-safe donde necesario | Lock en Singleton |
| **Manejo de recursos** | 3 | Cierre apropiado (N/A) | (N/A) |

**Puntaje Seccion 5.1**: \_\_\_\_\_ / 10

*(Nota: Seccion adaptada ya que los Sensores no usan Threads en esta version)*

---

### 5.2 Validacion y Robustez (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
| :--- | :--- | :--- | :--- |
| **Validacion de entrada** | 4 | Parametros validados en setters/servicios | `capacidad_kw > 100`, `isinstance` |
| **Defensive copying** | 3 | Listas inmutables donde apropiado | (Menos aplicable, pero `vehiculos.copy()` si se implementa) |
| **Manejo de errores** | 3 | Try/except apropiados | `OperadorService` maneja `OperadorNoCalificadoError` |

**Puntaje Seccion 5.2**: \_\_\_\_\_ / 10

---

**PUNTAJE TOTAL SECCION 5**: \_\_\_\_\_ / 20

---

## Resumen de Evaluacion

### Desglose por Seccion

| Seccion | Puntaje Obtenido | Puntaje Maximo | Porcentaje |
| :--- | :--- | :--- | :--- |
| 1\. Patrones de Diseno | \_\_\_\_\_ | 80 | \_\_\_\_\_% |
| 2\. Arquitectura y Diseno | \_\_\_\_\_ | 60 | \_\_\_\_\_% |
| 3\. Calidad de Codigo | \_\_\_\_\_ | 60 | \_\_\_\_\_% |
| 4\. Funcionalidad del Sistema | \_\_\_\_\_ | 40 | \_\_\_\_\_% |
| 5\. Buenas Practicas Avanzadas | \_\_\_\_\_ | 20 | \_\_\_\_\_% |
| **TOTAL** | **\_\_\_\_\_** | **260** | **\_\_\_\_\_%** |

### Calificacion Final

| Rango de Puntaje | Calificacion | Descripcion |
| :--- | :--- | :--- |
| 234 - 260 (90%+) | **Excelente** | Implementacion profesional de alta calidad |
| 208 - 233 (80-89%) | **Muy Bueno** | Implementacion solida con practicas avanzadas |
| 182 - 207 (70-79%) | **Bueno** | Implementacion correcta que cumple requisitos |
| 156 - 181 (60-69%) | **Suficiente** | Implementacion funcional con deficiencias |
| 0 - 155 (<60%) | **Insuficiente** | Requiere mejoras significativas |

**CALIFICACION FINAL**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## Anexo: Mapeo de Historias de Usuario a Criterios

### Epic 1: Estaciones y Flotas
-   **US-101**: Seccion 4.1
-   **US-102**: Seccion 4.1
-   **US-103**: Seccion 4.1

### Epic 2: Gestion de Vehiculos
-   **US-201 a US-204**: Seccion 4.1, Seccion 1.2 (Factory)

### Epic 3: Navegacion y Monitoreo
-   **US-301, 302, 303**: Seccion 4.2 (Monitoreo), Seccion 1.3 (Observer)
-   **US-304**: Seccion 1.4 (Strategy)
-   **US-305**: Seccion 4.1 (Ejecucion de mision)

### Epic 4: Gestion de Operadores
-   **US-401 a US-403**: Seccion 4.3 (Gestion de Operadores), Seccion 2.3 (Excepciones)

### Epic 5: Operaciones y Bitacora
-   **US-501**: Seccion 4.1, Seccion 1.1/1.5 (Singleton/Registry)
-   **US-502**: (Opcional, N/A en demo principal)
-   **US-503, 504**: Seccion 4.4 (Persistencia)

### Historias Tecnicas
-   **US-T01**: Seccion 1.2 (Factory)
-   **US-T02**: Seccion 1.3 (Observer)
-   **US-T03**: Seccion 1.4 (Strategy)
-   **US-T04**: Seccion 1.1 (Singleton)
-   **US-T05**: Seccion 1.1 (Registry, implementado como parte del Singleton)