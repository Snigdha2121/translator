from googletrans import Translator

msg = input("Enter your message: ")
lng = input("Enter the language you want to translate into: ")

translator = Translator()
translated_text = translator.translate(msg, dest=lng)

print("The translated message: ",translated_text.text)
