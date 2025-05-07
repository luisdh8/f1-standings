# 🏁 F1 Standings Analyzer

Este proyecto analiza imágenes de resultados de carreras de Fórmula 1 para extraer los nombres de los pilotos y calcular sus puntos según sus posiciones en cada carrera. Utiliza Python, OpenCV y EasyOCR para el reconocimiento de texto y procesamiento de imágenes, y matplotlib para graficar los resultados de pilotos y equipos.

## 🚀 Requisitos

- Python 3.x
- OpenCV (`opencv-python`)
- EasyOCR (`easyocr`)
- NumPy (`numpy`)
- RapidFuzz (`rapidfuzz`)
- Matplotlib (`matplotlib`)
- mplcursors (`mplcursors`)

## 🛠️ Instrucciones de Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/usuario/F1-Standings-Analyzer.git
cd F1-Standings-Analyzer
```

2. **Crear y activar el entorno virtual**

```bash
python -m venv venv
```

En Windows:
```bash
.\venv\Scripts\activate
```

En macOS/Linux:
```bash
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install opencv-python easyocr numpy rapidfuzz matplotlib mplcursors
```

4. **Descargar los archivos de entrada**

Coloca las imágenes de resultados de carreras en la carpeta Assets/ con el nombre del país seguido de .png. Por ejemplo:

```bash
Assets/Australia.png
Assets/China.png
Assets/Japan.png
```

5. **Ejecutar el programa**
```bash
python main.py
```

## 🧑‍💻 Funcionalidad

- **Detección de Pilotos**: Identifica los nombres de los pilotos en las imágenes de resultados usando EasyOCR y filtra los nombres más probables utilizando RapidFuzz para corregir errores de reconocimiento.
- **Asignación de Puntos**: Calcula los puntos de cada piloto y equipo según su posición en las carreras.
- **Visualización de Resultados**: Genera gráficos interactivos para los standings de pilotos y constructores usando matplotlib.

## ⚙️ Descripción del Código

- **standings.py**: Procesa las imágenes para extraer los nombres de los pilotos y corrige errores de OCR usando RapidFuzz.
- **f1_data.py**: Calcula los puntos de los pilotos y equipos y genera gráficos para visualizar los standings.
- **main.py**: Ejecuta el flujo completo de procesamiento de imágenes y generación de gráficos.

## 💡 Mejoras Futuras

- Mejorar la precisión del OCR para nombres cortos y en condiciones de baja calidad.
- Implementar un sistema de clasificación de pilotos más robusto usando aprendizaje automático.
- Añadir soporte para más categorías de clasificación como vueltas rápidas y poles.

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
