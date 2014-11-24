# coding=utf-8

from blockext import *
import speech_recognition as sr

class Voice:
    def __init__(self):
        self.text = ""

    @command("listen %m.languages language", defaults=["English"], is_blocking=True)
    def recognize(self, languages):
        lang = {
            "English": "en-US",
            "Russian": "ru-RU",
        }[languages]
        r = sr.Recognizer(lang)
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            self.text = r.recognize(audio)
        except LookupError:
            self.text = "Could not understand audio"

    @reporter("text")
    def get_text(self):
        return self.text

descriptor = Descriptor(
    name = "Voice recognition",
    port = 5002,
    blocks = get_decorated_blocks_from_class(Voice),
    menus = dict(
        languages = ["English", "Russian"],
    ),
)

extension = Extension(Voice, descriptor)

if __name__ == "__main__":
    extension.run_forever(debug=True)
