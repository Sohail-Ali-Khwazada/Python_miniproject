# import speech_recognition as sr
import datetime as dt
import webbrowser
# import win32com.client
import google.generativeai as genai
from . import config
genai.configure(api_key=config.API_KEY)

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
convo = model.start_chat()

def get_promptans(prompt):
    result = convo.send_message(prompt)
    return result.text

# def say(text):
#     speaker.Speak(text)


def get_time():
    current_time = dt.datetime.now().strftime("%I:%M %p")
    # say(f"The time is {current_time}")
    print(f"The time is {current_time}")
    return current_time


def open_sites(query,websites):
    for website, url in websites.items():
        if f"open {website.lower()}" in query.lower():

            try:
                webbrowser.open(url)
                # say(f"Opening {website}")
                return f"Opening {website}"
            except:
                print("Error")
                # say(f"Sorry, I couldn't open {website}. Would you like me to try understanding your request again?")
                # confirmation = takeCommand().lower()
                # if "yes" in confirmation:
                    # query = takeCommand().lower()

# def start():
#     say("Hello I am your personal voice assistant")
#     websites = {
#         "Google": "https://www.google.com/",
#         "YouTube": "https://www.youtube.com/",
#         "Facebook": "https://www.facebook.com/",
#         "Instagram": "https://www.instagram.com/",
#         "Twitter": "https://twitter.com/?lang=en",
#         "Wikipedia": "https://www.wikipedia.org/",
#         "Amazon": "https://www.amazon.com/",
#         "Reddit": "https://www.reddit.com/",
#         "Yahoo": "https://www.yahoo.com/",
#         "Netflix": "https://www.netflix.com/",
#         "Apple": "https://www.apple.com/",
#         "WhatsApp": "https://www.whatsapp.com/",
#         "Microsoft": "https://www.microsoft.com/",
#         "Spotify": "https://www.spotify.com/",
#         "eBay": "https://www.ebay.com/",
#         "Twitch": "https://www.twitch.tv/",
#         "Zoom": "https://zoom.us/",
#         "Facebook Messenger": "https://www.messenger.com/",
#     }
#     while True:
#         print("Listening...")
#         query = takeCommand()

#         if not query or "exit" in query:
#             say("GoodBye")
#             break

#         elif "time" in query:
#             get_time()

#         elif "open" in query:
#             open_sites(query,websites)

#         else:
#             required_output = get_promptans(query)
#             say("Here is the answer, have a look")
#             print(f"A.I said: {required_output}")

# start()
def start(query):
    # say("Hello I am your personal voice assistant")
    websites = {
        "Google": "https://www.google.com/",
        "YouTube": "https://www.youtube.com/",
        "Facebook": "https://www.facebook.com/",
        "Instagram": "https://www.instagram.com/",
        "Twitter": "https://twitter.com/?lang=en",
        "Wikipedia": "https://www.wikipedia.org/",
        "Amazon": "https://www.amazon.com/",
        "Reddit": "https://www.reddit.com/",
        "Yahoo": "https://www.yahoo.com/",
        "Netflix": "https://www.netflix.com/",
        "Apple": "https://www.apple.com/",
        "WhatsApp": "https://www.whatsapp.com/",
        "Microsoft": "https://www.microsoft.com/",
        "Spotify": "https://www.spotify.com/",
        "eBay": "https://www.ebay.com/",
        "Twitch": "https://www.twitch.tv/",
        "Zoom": "https://zoom.us/",
        "Facebook Messenger": "https://www.messenger.com/",
    }

    if "who are you" in query.lower():  # Ensure case insensitivity
        print("Matched 'who are you' condition")
        return "I'm an AI language model. You can think of me as a virtual assistant programmed to help users with various tasks, answer questions, provide information, generate text based on prompts, and more. How can I assist you today?"
    


    
    if not query or "exit" in query:
        # say("GoodBye")
        print("GoodBye")

    elif "time" in query:
        return get_time()

    elif "open" in query:
        return open_sites(query,websites)

    else:
        required_output = get_promptans(query)
        # say("Here is the answer, have a look")
        print(f"A.I said: {required_output}")
        return required_output
