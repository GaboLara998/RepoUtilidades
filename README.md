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

### Pasos para ejecutar

1. Clonar el repositorio en la carpeta que prefiera y entrar en él

   ```bash
   git clone <URL-del-repositorio>
   cd RepoUtilidades
   ```

2. *(Opcional)* Crear y activar un entorno virtual

   ```bash
   python -m venv env
   source env/bin/activate  # en Windows use env\Scripts\activate
   ```

3. Instalar las dependencias

   ```bash
   bash setup.sh
   ```

4. Ejecutar el pipeline indicando la ruta del video

   ```bash
   python video_pipeline/process_video.py ruta/al/video.mp4
   ```

### Interfaz gráfica

El paquete incluye un script muy sencillo para usar el pipeline con una
ventana gráfica. Puede ejecutarlo con:

```bash
python -m video_pipeline.gui
```

Si tiene instalado `tkinterdnd2` podrá arrastrar el archivo `.mp4` sobre la
ventana. En caso contrario utilice el botón **Seleccionar archivo**.
El programa generará los archivos `transcripcion.txt` y `resumen.txt` dentro
de una carpeta llamada como el video con el sufijo `_resumed`.
