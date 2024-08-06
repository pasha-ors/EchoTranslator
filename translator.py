import speech_utils
from googletrans import Translator


def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


if __name__ == "__main__":
    target_language = "ru"  # Replace with your target language code
    text = ""

    while True:
        text = speech_utils.recognize_speech()
        if text:
            print(f"You said: {text}")
            translated_text = translate_text(text, target_language)
            print(f"Translated: {translated_text}")
            speech_utils.speak_text(translated_text)