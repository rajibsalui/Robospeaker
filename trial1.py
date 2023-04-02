import win32com.client as wincom

# you can insert gaps in the narration by adding sleep calls
import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = "Python text-to-speech test. using win32com.client"
speak.Speak(text)

# 3 second sleep
time.sleep(3)

text = "This text is read after 3 seconds"
speak.Speak(text)