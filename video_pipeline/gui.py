import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    DND_AVAILABLE = True
except ImportError:
    DND_AVAILABLE = False

from .process_video import extract_audio, transcribe_audio, summarize_text


def process_video_file(path: Path):
    audio_path = path.with_suffix('.wav')
    trans_text = transcribe_audio(extract_audio(path, audio_path))
    summary = summarize_text(trans_text)
    out_dir = path.with_name(path.stem + '_resumed')
    out_dir.mkdir(exist_ok=True)
    transcript_file = out_dir / 'transcripcion.txt'
    summary_file = out_dir / 'resumen.txt'
    transcript_file.write_text(trans_text, encoding='utf-8')
    summary_file.write_text(summary, encoding='utf-8')
    messagebox.showinfo('Proceso finalizado', f'Archivos guardados en {out_dir}')


def on_drop(event):
    path = event.data
    if path:
        process_video_file(Path(path.strip('{}')))


def select_file():
    filename = filedialog.askopenfilename(filetypes=[('MP4 files', '*.mp4')])
    if filename:
        process_video_file(Path(filename))


def main():
    if DND_AVAILABLE:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()
    root.title('Video Summarizer')
    instr = tk.Label(root, text='Arrastra un archivo .mp4 aqui\no usa el boton para seleccionarlo', width=40, height=10, bg='lightgray')
    instr.pack(padx=10, pady=10, fill='both', expand=True)
    button = tk.Button(root, text='Seleccionar archivo', command=select_file)
    button.pack(pady=(0,10))
    if DND_AVAILABLE:
        instr.drop_target_register(DND_FILES)
        instr.dnd_bind('<<Drop>>', on_drop)
    root.mainloop()


if __name__ == '__main__':
    main()
