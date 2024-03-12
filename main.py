from audio_to_text import audio_to_text
from text_to_audio import text_to_audio


inputText = audio_to_text()
print(f"You said {inputText}")
text_to_audio(inputText)