import pyttsx3
import PyPDF2
book = open('INPUT PDF NAME.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(INPUT PAGE NUMBER,ALSO FOR EX YOU WANT PAGE 7 PUT 6)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()