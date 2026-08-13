import threading
import pyttsx3


class VoiceAssistant:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 165)

        voices = self.engine.getProperty("voices")

        if len(voices) > 0:
            self.engine.setProperty("voice", voices[0].id)

    def _speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()

    def speak(self, text):

        threading.Thread(
            target=self._speak,
            args=(text,),
            daemon=True
        ).start()