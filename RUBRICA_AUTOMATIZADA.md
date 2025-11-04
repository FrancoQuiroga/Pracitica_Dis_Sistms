# Rubrica de Evaluacion Automatizada - Compatible con n8n

**Proyecto**: PythonAutonomousFleet
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Proposito**: Automatizacion de correccion de proyectos en n8n

---

## Introduccion

Este documento define criterios de evaluacion automatizables mediante n8n para proyectos de software que implementen patrones de diseno. Cada criterio incluye:

1.  **ID unico**: Para referencia en workflows de n8n
2.  **Tipo de verificacion**: Estatica (codigo) o Dinamica (ejecucion)
3.  **Metodo de deteccion**: Como automatizar la verificacion
4.  **Comando/Regex**: Script o patron para ejecutar
5.  **Puntaje**: Puntos asignados al criterio
6.  **Threshold**: Umbral de aprobacion

---

## Formato JSON para n8n

Cada criterio se puede representar en JSON para workflows de n8n:

```json
{
  "criterio_id": "SING-001",
  "categoria": "Singleton",
  "descripcion": "Verificar implementacion de Singleton",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -r '_instance = None' --include='*registry*.py'",
  "puntaje_max": 5,
  "threshold": 1,
  "peso": "critico"
}