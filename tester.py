#!/usr/bin/env python3
"""
Script helper para evaluacion automatizada.
Uso: python evaluador_automatico.py --proyecto /path/to/proyecto --config config.json
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
import os

# --- Constantes de Colores (Opcional, para mejor UI) ---
# (Se pueden deshabilitar si la terminal no los soporta)
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

class EvaluadorAutomatico:
    def __init__(self, proyecto_path: str, config_path: str):
        self.proyecto_path = Path(proyecto_path).resolve() # Resuelve la ruta absoluta
        self.config = self._cargar_config(config_path)
        self.resultados = []
        self._resumen_generado = False
        self._resumen_cache = {}

    def _cargar_config(self, config_path: str) -> Dict:
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"{ROJO}[!] Error Fatal: No se encontro el archivo de configuracion: {config_path}{RESET}")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"{ROJO}[!] Error Fatal: El archivo JSON de configuracion esta mal formado: {config_path}{RESET}")
            sys.exit(1)

    def ejecutar_comando(self, comando: str) -> Dict[str, Any]:
        """Ejecuta comando y retorna resultado."""
        
        # Ajuste para compatibilidad Windows/Linux
        # Reemplaza 'grep' con 'findstr' en Windows si es necesario (aunque 'grep' funciona en Git Bash)
        # Reemplaza 'find' con 'dir'
        
        # Por simplicidad, asumimos un entorno tipo Unix (Git Bash en Windows)
        # o que los comandos son compatibles (ej. 'python -m ...')
        
        try:
            resultado = subprocess.run(
                comando,
                shell=True,
                cwd=self.proyecto_path, # Ejecuta en el directorio del proyecto
                capture_output=True,
                text=True,

                # --- INICIO DE CORRECCION 1 (Encoding y AttributeError) ---
                # Usamos el encoding de la consola de Windows ('oem') o un fallback seguro
                encoding=sys.stdout.encoding or "latin-1",
                errors="ignore",
                # --- FIN DE CORRECCION 1 ---
                timeout=30
            )
            return {
                'exitcode': resultado.returncode,
                # --- INICIO DE CORRECCION 2 (AttributeError) ---
                # Aseguramos que stdout/stderr no sean None antes de .strip()
                'stdout': (resultado.stdout or "").strip(),
                'stderr': (resultado.stderr or "").strip(),
                # --- FIN DE CORRECCION 2 ---
                'exito': resultado.returncode == 0
            }
        except subprocess.TimeoutExpired:
            return {
                'exitcode': -1,
                'stdout': '',
                'stderr': 'Timeout (30s)',
                'exito': False
            }
        except Exception as e:
            return {
                'exitcode': -99,
                'stdout': '',
                'stderr': f'Error de Subprocess: {e}',
                'exito': False
            }
        

    def evaluar_criterio(self, criterio: Dict, categoria: str) -> Dict:
        """Evalua un criterio individual."""
        
        print(f"  {AMARILLO}Evaluando [{criterio['id']}]...{RESET} {criterio['descripcion']}")
        
        # Validacion basica del criterio
        if 'comando' not in criterio or 'threshold' not in criterio:
            print(f"    {ROJO}Criterio mal formado (falta 'comando' o 'threshold'){RESET}")
            return {'id': criterio['id'], 'pasado': False, 'puntaje_obtenido': 0}

        resultado_cmd = self.ejecutar_comando(criterio['comando'])
        # Contar coincidencias (lineas no vacias)
        coincidencias = len([linea for linea in resultado_cmd['stdout'].splitlines() if linea.strip()])

        # Evaluar segun threshold
        inverted = criterio.get('inverted', False)
        pasado = False
        
        if inverted:
            # Invertido: buscamos que las coincidencias sean MENORES o IGUALES
            pasado = coincidencias <= criterio['threshold']
        else:
            # Normal: buscamos que las coincidencias sean MAYORES o IGUALES
            pasado = coincidencias >= criterio['threshold']

        if pasado:
            print(f"    {VERDE}[✓] PASO{RESET} (Coincidencias: {coincidencias}, Esperadas: {criterio['threshold']})")
        else:
            print(f"    {ROJO}[✗] FALLO{RESET} (Coincidencias: {coincidencias}, Esperadas: {criterio['threshold']})")
            if resultado_cmd['stderr']:
                print(f"      {ROJO}Error: {resultado_cmd['stderr']}{RESET}")

        return {
            'id': criterio['id'],
            'descripcion': criterio['descripcion'],
            'categoria': categoria, # <--- FIN CORRECCION 3 (Usar 'categoria' del argumento)
            'pasado': pasado,
            'coincidencias': coincidencias,
            'threshold': criterio['threshold'],
            'puntaje_max': criterio.get('puntaje', 0),
            'puntaje_obtenido': criterio.get('puntaje', 0) if pasado else 0,
            'peso': criterio.get('peso', 1.0),
            'output': resultado_cmd['stdout'][:500]  # Primeros 500 chars
        }

    def evaluar_todos(self) -> Dict:
        """Evalua todos los criterios y cachea el resultado."""
        if self._resumen_generado:
            return self._resumen_cache
            
        print(f"\n{AZUL}--- INICIANDO EVALUACION ---{RESET}")
        print(f"Proyecto en: {self.proyecto_path}\n")

        for categoria_info in self.config['evaluacion']:
            # --- INICIO CORRECCION 4 (KeyError) ---
            categoria_nombre = categoria_info['categoria'] # Obtenemos el nombre
            print(f"\n{AZUL}Categoria: {categoria_nombre}{RESET}")
            
            for criterio in categoria_info['criterios']:
                # Pasamos el nombre de la categoria a la funcion
                resultado = self.evaluar_criterio(criterio, categoria_nombre)
                self.resultados.append(resultado)
            # --- FIN CORRECCION 4 ---

        # Calcular totales
        puntaje_total = sum(r['puntaje_obtenido'] for r in self.resultados)
        puntaje_maximo = sum(r['puntaje_max'] for r in self.resultados)
        
        if puntaje_maximo == 0:
            porcentaje = 0
        else:
            porcentaje = (puntaje_total / puntaje_maximo) * 100

        # Determinar calificacion
        calificacion = 'Insuficiente' # Default
        for rango in self.config['calificacion']['rangos']:
            if porcentaje >= rango['min_porcentaje']:
                calificacion = rango['nombre']
                break # Los rangos deben estar ordenados de mayor a menor

        aprobado = porcentaje >= self.config['calificacion']['min_aprobacion']

        resumen = {
            'puntaje_total': puntaje_total,
            'puntaje_maximo': puntaje_maximo,
            'porcentaje': round(porcentaje, 2),
            'calificacion': calificacion,
            'aprobado': aprobado,
            'criterios_pasados': sum(1 for r in self.resultados if r['pasado']),
            'criterios_fallados': sum(1 for r in self.resultados if not r['pasado']),
            'resultados': self.resultados
        }
        
        self._resumen_generado = True
        self._resumen_cache = resumen
        return resumen

    def generar_reporte_json(self, output_path: str):
        """Genera reporte en formato JSON."""
        resumen = self.evaluar_todos()
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(resumen, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"{ROJO}Error al escribir JSON: {e}{RESET}")

    def generar_reporte_markdown(self, output_path: str):
        """Genera reporte en formato Markdown."""
        resumen = self.evaluar_todos()

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# Reporte de Evaluacion Automatizada\n\n")
                f.write(f"**Proyecto**: {self.proyecto_path.name}\n")
                f.write(f"**Fecha**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                f.write(f"## Resumen\n\n")
                estado_str = f"{VERDE}APROBADO{RESET}" if resumen['aprobado'] else f"{ROJO}NO APROBADO{RESET}"
                f.write(f"- **Puntaje Total**: {resumen['puntaje_total']}/{resumen['puntaje_maximo']}\n")
                f.write(f"- **Porcentaje**: {resumen['porcentaje']}%\n")
                f.write(f"- **Calificacion**: {resumen['calificacion']}\n")
                f.write(f"- **Estado**: {estado_str}\n\n")

                f.write(f"## Detalles\n\n")
                f.write(f"| Criterio | Categoria | Pasado | Puntaje | Coincidencias |\n")
                f.write(f"|----------|-----------|--------|---------|---------------|\n")
                
                for r in self.resultados:
                    estado = f'{VERDE}✓{RESET}' if r['pasado'] else f'{ROJO}✗{RESET}'
                    f.write(f"| {r['id']} | {r['categoria']} | {estado} | {r['puntaje_obtenido']}/{r['puntaje_max']} | {r['coincidencias']}/{r['threshold']} |\n")

        except IOError as e:
            print(f"{ROJO}Error al escribir Markdown: {e}{RESET}")
            
    def imprimir_resumen_consola(self):
        """Imprime un resumen formateado en la consola."""
        resumen = self.evaluar_todos()
        
        print(f"\n{AZUL}=== RESUMEN DE EVALUACION ==={RESET}")
        print(f"Puntaje:      {resumen['puntaje_total']}/{resumen['puntaje_maximo']} ({resumen['porcentaje']}%)")
        print(f"Calificacion: {resumen['calificacion']}")
        
        estado_str = f"{VERDE}APROBADO{RESET}" if resumen['aprobado'] else f"{ROJO}NO APROBADO{RESET}"
        print(f"Estado:       {estado_str}")
        
        print(f"\nCriterios Pasados:  {VERDE}{resumen['criterios_pasados']}{RESET}")
        print(f"Criterios Fallados: {ROJO}{resumen['criterios_fallados']}{RESET}")
        print(f"{AZUL}============================={RESET}")


if __name__ == '__main__':
    import argparse

    # --- Setup de Argparse ---
    parser = argparse.ArgumentParser(description='Evaluador automatico de proyectos de diseno de sistemas.')
    parser.add_argument('--proyecto', 
                        default='.', 
                        help='Path al directorio raiz del proyecto (default: directorio actual).')
    
    parser.add_argument('--config', 
                        required=True, 
                        help='Path al archivo de configuracion JSON.')
    
    parser.add_argument('--output-json', 
                        help='Path opcional para generar reporte JSON.')
    
    parser.add_argument('--output-md', 
                        help='Path opcional para generar reporte Markdown.')
    
    parser.add_argument('--no-color', 
                        action='store_true', 
                        help='Deshabilita la salida con colores.')

    args = parser.parse_args()

    # --- Deshabilitar Colores ---
    if args.no_color or not sys.stdout.isatty():
        VERDE = ROJO = AMARILLO = AZUL = RESET = ''

    # --- Validar Directorio de Proyecto ---
    if not os.path.isdir(args.proyecto):
        print(f"{ROJO}[!] Error Fatal: El directorio del proyecto no existe: {args.proyecto}{RESET}")
        sys.exit(1)

    # --- Ejecutar Evaluador ---
    evaluador = EvaluadorAutomatico(args.proyecto, args.config)
    
    evaluador.imprimir_resumen_consola()

    # --- Generar Reportes (si se solicitaron) ---
    if args.output_json:
        evaluador.generar_reporte_json(args.output_json)
        print(f"\n{VERDE}[OK] Reporte JSON generado: {args.output_json}{RESET}")

    if args.output_md:
        evaluador.generar_reporte_markdown(args.output_md)
        print(f"{VERDE}[OK] Reporte Markdown generado: {args.output_md}{RESET}")

    # --- Salir con Codigo de Error ---
    resumen_final = evaluador._resumen_cache
    sys.exit(0 if resumen_final['aprobado'] else 1)
