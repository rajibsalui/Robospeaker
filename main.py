import win32com.client as wincom
if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1. Created by Rajib")
    speak = wincom.Dispatch("SAPI.SpVoice")
    while True:
        x = input("Enter what you want me to speak : ")
        if x == "q":
            speak.Speak("bye bye friend")
            break
        speak.Speak(x)

