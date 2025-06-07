# RepoUtilidades

Este repositorio contiene varias utilidades y ejemplos.

## Video Pipeline

El paquete `video_pipeline` incluye un script para procesar un archivo de video y obtener una transcripción resumida.

El flujo de trabajo que realiza `process_video.py` es el siguiente:
1. Extrae la pista de audio de un archivo `.mp4` con `moviepy`.
2. Transcribe el audio utilizando la biblioteca [`whisper`](https://github.com/openai/whisper) especificando el idioma.
3. Resume la transcripción con un modelo de `transformers`, por ejemplo `google/mt5-small`.

### Uso

```bash
python video_pipeline/process_video.py ruta/al/video.mp4
```

Opciones:
- `--audio PATH` : ubicación para almacenar el archivo de audio intermedio (por defecto `extracted_audio.wav`).
- `--model NAME` : tamaño del modelo Whisper a usar (por defecto `base`).
- `--lang COD` : código de idioma ISO 639-1 del audio (por defecto `es`).
- `--summary-model NAME` : modelo de transformers para resumir (por defecto `google/mt5-small`).
- `--output PATH` : archivo para guardar la transcripción y el resumen (opcional).

### Ejemplos

Ejecutar el pipeline con las opciones por defecto:

```bash
python video_pipeline/process_video.py ruta/al/video.mp4
```

Usar un modelo de Whisper distinto y guardar el audio temporal en `mi_audio.wav`:

```bash
python video_pipeline/process_video.py ruta/al/video.mp4 --model small --audio mi_audio.wav
```
Guardar la salida en un archivo `resultado.txt`:

```bash
python video_pipeline/process_video.py ruta/al/video.mp4 --output resultado.txt
```

### Dependencias

Puede instalar las dependencias ejecutando el script `setup.sh` incluido en el
repositorio:

```bash
bash setup.sh
```

Este script utiliza `pip` para instalar `moviepy`, `openai-whisper`,
`transformers` y `torch`. Si lo prefiere, puede instalarlos manualmente con:

```bash
pip install moviepy openai-whisper transformers torch
```

El script descargará los modelos necesarios la primera vez que se ejecute.
