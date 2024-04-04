from googletrans import Translator

msg = input("Enter your message: ")
lng = input("Enter language you want to translate in: ")

translator = Translator()
translated_text = translator.translate(msg, dest=lng)

print(translated_text.text)