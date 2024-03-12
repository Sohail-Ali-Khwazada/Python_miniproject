from audio_to_text import audio_to_text
from text_to_audio import text_to_audio
from datetime import datetime


# inputText = audio_to_text()
# print(f"You said {inputText}")
# text_to_audio(inputText)


def get_time():
    current_time = datetime.now().strftime("%I:%M %p")
    text_to_audio(f"The current time is {current_time}")
    print(f"The current time is {current_time}")

text_to_audio("Hello, I'm your voice assistant. How can I help you today?")
while True:
    inputText = audio_to_text()
    if "exit" in inputText:
        text_to_audio("Goodbye!")
        break
    elif "time" in inputText:
        get_time()
    else:
        text_to_audio("Sorry, I can't help with that.")