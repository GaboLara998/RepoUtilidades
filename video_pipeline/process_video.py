import argparse
from pathlib import Path

from moviepy.editor import VideoFileClip
import whisper
from transformers import pipeline


def extract_audio(video_path: Path, audio_path: Path) -> Path:
    """Extract audio from an mp4 file and save it as wav."""
    with VideoFileClip(str(video_path)) as clip:
        clip.audio.write_audiofile(str(audio_path))
    return audio_path


def transcribe_audio(audio_path: Path, model_name: str = "base", language: str = "es") -> str:
    """Transcribe audio using Whisper specifying the language."""
    model = whisper.load_model(model_name)
    result = model.transcribe(str(audio_path), language=language)
    return result.get("text", "")


def summarize_text(text: str, model_name: str = "google/mt5-small") -> str:
    """Summarize text using a transformers pipeline."""
    summarizer = pipeline("summarization", model=model_name)
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]["summary_text"]


def main():
    parser = argparse.ArgumentParser(description="Process video to summarized transcription")
    parser.add_argument("video", type=Path, help="Path to input .mp4 file")
    parser.add_argument("--audio", type=Path, default=Path("extracted_audio.wav"), help="Path to temporary audio file")
    parser.add_argument("--model", type=str, default="base", help="Whisper model size to use")
    parser.add_argument("--lang", type=str, default="es", help="Idioma del audio (codigo ISO 639-1)")
    parser.add_argument("--summary-model", type=str, default="google/mt5-small", help="Transformers model for summarization")
    parser.add_argument("--output", type=Path, help="Archivo de salida para guardar la transcripcion y el resumen")
    args = parser.parse_args()

    audio_path = extract_audio(args.video, args.audio)
    text = transcribe_audio(audio_path, args.model, args.lang)
    summary = summarize_text(text, args.summary_model)
    if args.output:
        with args.output.open("w", encoding="utf-8") as f:
            f.write(text + "\n\n" + summary)

    print("\nTranscription:\n", text)
    print("\nSummary:\n", summary)


if __name__ == "__main__":
    main()
