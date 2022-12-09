from textblob import TextBlob
word=input("enter a word")
blob_obj = TextBlob(word)
corrected_word = str(blob_obj.correct())
print(corrected_word)