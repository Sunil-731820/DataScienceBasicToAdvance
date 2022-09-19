import pyttsx3
book = open(r"DataScience.txt")
book_text = book.readline()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()