import speech_recognition as sr
import argparse

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            print("[INFO] Loading audio file...")
            audio_data = recognizer.record(source)
            print("[INFO] Transcribing audio...")
            text = recognizer.recognize_google(audio_data)
            return text
    except FileNotFoundError:
        return "[ERROR] File not found. Please check the path."
    except sr.UnknownValueError:
        return "[ERROR] Could not understand the audio."
    except sr.RequestError:
        return "[ERROR] Could not request results from Google Speech Recognition service."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Speech-to-Text Transcription Tool")
    parser.add_argument("--file", type=str, required=True, help="Path to the audio file (.wav, .aiff, .flac)")
    args = parser.parse_args()

    result = transcribe_audio(args.file)
    print("\nTranscribed Text:\n", result)
