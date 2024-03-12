import speech_recognition as sr

def audio_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error processing the request.")
        return ""



    