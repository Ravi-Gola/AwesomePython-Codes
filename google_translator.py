from googletrans import Translator
# create an object
translator = Translator()

# translate a string
translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='hindi')
print(translation.text)

# translate a list of sentences
# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='hindi')
# for translation in translations:
#   print(translation.origin, ' -> ', translation.text)
#
# # detect a language
# lang=translator.detect('이 문장은 한글로 쓰여졌습니다.')
# print(lang)