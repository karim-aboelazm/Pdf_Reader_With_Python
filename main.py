# ---------------------------------------------|
# Auther => Engineer Karim Mohammed Aboelazm   |
# Date => 2-2-2022                             |
# Library used => PyPDF2 , pyttsx3             |
# using => pip install PyPDF2                  |
#       => pip install pyttsx3                 |
# ---------------------------------------------|
import PyPDF2 as pdf
import pyttsx3 as pytts

def text_to_voice(text):
    engine = pytts.init('sapi5')
    voice = engine.getProperty('voices')
    engine.setProperty('voices',voice[1])
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()

def read_pdf_files(url,pn):
    file = open(url, 'rb')
    pdf_reader = pdf.PdfFileReader(file)
    form_page = pdf_reader.getPage(pn-1)
    txt = form_page.extractText()
    text_to_voice(txt)

read_pdf_files('E:\\Python\\Projects\\PdfReader\\new.pdf',6)


