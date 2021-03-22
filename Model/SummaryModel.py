#! usr/bin/env python
from google_trans_new import google_translator
import re
import heapq
import nltk
import PyPDF2

class SummaryModel():
    def __init__(self):
        self.trl = google_translator()

    def getSummary(self, pdf, numpages):
        page_content = ""
        if(numpages > 8):
            for i in range(1, (numpages - 3)):
                page = pdf.getPage(i)
                page_content += "\n" + self.trl.translate(page.extractText(), lang_tgt='en')
        else:
            for i in range(1, (numpages)):
                page = pdf.getPage(i)
                page_content += "\n" + self.trl.translate(page.extractText(), lang_tgt='en')

        article_text = page_content
        article_text = article_text.replace("[ edit ]", "")
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
        sentence_list = nltk.sent_tokenize(article_text)
        #EN ESTA PARTE ENCUENTRA LA FRECUENCIA DE CADA PALABRA
        stopwords = nltk.corpus.stopwords.words('english')
        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_article_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

        #cALCULA LA FRECENCIA DE LAS PALABRAS SEGUN PONDERACIONES (PANDAS)
        maximum_frequncy = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

        #CALCULA LAS FRASES QUE MÁS SE REPITEN
        sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 28:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]

        #REALIZA EL RESUMEN CON LAS MEJORES FRASES

        summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)

        summary = ' '.join(summary_sentences)
        summary = self.trl.translate(summary, lang_tgt='es')
        return summary