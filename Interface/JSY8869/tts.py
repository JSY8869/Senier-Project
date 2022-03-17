from playsound import playsound


def speak(weather):
    if weather == 0:
        playsound("sound/rain_voice.mp3")
    elif weather == 1:
        playsound("sound/RainOrSnow_voice.mp3")
    elif weather == 2:
        playsound("sound/snow_voice.mp3")
    elif weather == 3:
        playsound("sound/shower_voice.mp3")
    else:
        playsound("sound/sunny_voice.mp3")

def start_voice():
    playsound("sound/start_voice.mp3")