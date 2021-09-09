#! usr/bin/env python
import bs4 as bs  
import urllib.request  
import re
import nltk
import bs4
import urllib.request
import requests
from bs4 import BeautifulSoup
import urllib.request
from inscriptis import get_text
from googletrans import Translator
#Para la version de googletrans es -> pip install googletrans==3.1.0a0
from pdfminer.high_level import extract_text
from nltk import word_tokenize,sent_tokenize
import heapq  
nltk.download('punkt')
nltk.download('stopwords')
#Librería para la 
from textblob import TextBlob
#Librería para leer txt utf-8
import codecs
################################
nltk.download('stopwords')     #
nltk.download('punkt')         #
################################

class SummaryModel():
    def __init__(self):
        super(SummaryModel, self).__init__()
        self.paso2 = ""
        self.paso3 = ""
        self.paso4 = ""
        self.paso5 = ""
        self.paso6 = ""
        self.paso7 = ""
        self.paso8 = ""
        self.paso9 = ""
        self.paso10 = ""
        self.interSummary = ""

    def tokenize(self, text):
        tokenz = text.split()
        self.paso2 = tokenz
        return tokenz

    def StopWords(self):
        try:
            words = set(nltk.corpus.stopwords.words('english'))
        except:
            print("stopwords error")
        return words

    def getInterSummary(self):
        summaries = ""
        su1 = self.interSummary.find('Resumen')
        su2 = self.interSummary.find('RESUMEN')
        as1 = self.interSummary.find('Abstract')
        as2 = self.interSummary.find('ABSTRACT')
        an1 = self.interSummary.find('Analytical')
        an2 = self.interSummary.find('ANALYTICAL')
        
        start = su2 if(su2 > su1) else su1
        end1 = as2 if(as2 >= as1) else as1
        end2 = an2 if(an2 >= an1) else an1
        end = end1 if(end1 >= end2) else end2
        summaries = self.interSummary[start:end]
        return summaries 

    def getSummary(self, file, numpages):
        pdfRead = extract_text(file) # ----> Aquí insertas tu PDF (Recuerda que el nombre de tu pdf debe ser igual)
        articulo_texto = pdfRead
        num_words = 80
        articulo_texto = articulo_texto.replace("[ edit ]", "")
        # Elimina palabras vacías, espacios extras
        articulo_texto = re.sub(r'\[[0-9]*\]', ' ', articulo_texto)  
        articulo_texto = re.sub(r'\s+', ' ', articulo_texto)  

        formatear_articulo = re.sub('[^a-zA-Z]', ' ', articulo_texto )  
        formatear_articulo = re.sub(r'\s+', ' ', formatear_articulo)  
        
        lista_palabras = nltk.sent_tokenize(articulo_texto)  
        stopwords = nltk.corpus.stopwords.words('english')
        self.interSummary = formatear_articulo
        self.paso2 = self.tokenize(formatear_articulo)
        self.paso4 = lista_palabras
        frecuencia_palabras = {}  
        for word in nltk.word_tokenize(formatear_articulo):  
            if word not in stopwords:
                if word not in frecuencia_palabras.keys():
                    frecuencia_palabras[word] = 1
                else:
                    frecuencia_palabras[word] += 1
        max_frecuencia = max(frecuencia_palabras.values())
        self.paso6 = max_frecuencia
        for word in frecuencia_palabras.keys():  
            frecuencia_palabras[word] = (frecuencia_palabras[word]/max_frecuencia)
        self.paso3 = frecuencia_palabras
        if(numpages <= 40):
            num_words = 90
        else:
            num_words = 150

        #Calcula frases repetidas
        max_oracion = dict()  
        for sent in lista_palabras:  
            for word in nltk.word_tokenize(sent.lower()):
                if word in frecuencia_palabras.keys():
                    if len(sent.split(' ')) < num_words: # -----------> Este numero variará de acuerdo a la cantidad de páginas que tengas
                        if sent not in max_oracion.keys():
                            max_oracion[sent] = frecuencia_palabras[word]
                        else:
                            max_oracion[sent] += frecuencia_palabras[word]
        self.paso5 = max_oracion

        self.paso7 = average = int(max_frecuencia/len(max_oracion))
        #Resumen
        resumen_oracion = heapq.nlargest(6, max_oracion, key=max_oracion.get)
        summary = ""
        for sentence in lista_palabras:
            if (sentence in max_oracion) and (max_oracion[sentence] > (1.2 * average)):
                summary += " " + sentence
                self.paso8 += "\n" + sentence

        delete_text = resumen_oracion[0]
        text_lon = delete_text [0:7]
        if(text_lon == "Londoño"):
            resumen_oracion[0] = delete_text[7:]
        resumen = ' '.join(resumen_oracion)  
        self.paso9 = resumen_oracion
        #Traducción
        translator = Translator()
        translate = translator.translate(resumen, src="es", dest="es")
        self.paso10 = translate.text
        return translate.text


    def TradEn(self, text):
        translator = Translator()
        translate = translator.translate(text, dest="en")
        return translate.text
