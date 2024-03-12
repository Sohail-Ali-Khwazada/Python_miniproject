from gtts import gTTS
import os
import pygame



def text_to_audio(text):
    try:
        tts = gTTS(text=text, lang="en")
        tts.save("output.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
    except Exception as e:  # Catch general exceptions for saving/playback
        print(f"Error playing audio: {e}")
    finally:  # Always stop and quit mixer (optional)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        os.remove("output.mp3")