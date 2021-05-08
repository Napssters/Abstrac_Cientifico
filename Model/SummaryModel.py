#! usr/bin/env python
from google_trans_new import google_translator
import re
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import PyPDF2

################################
nltk.download('stopwords')     #
nltk.download('punkt')         #
################################

class SummaryModel():
    def __init__(self):
        super(SummaryModel, self).__init__()
        self.trl = google_translator()

    def tokenize(self, text):
        tokenz = text.split()
        return tokenz
    
    def StopWords(self):
        words = set(stopwords.words("english"))
        return words

    def getSummary(self, pdf, numpages):
        SW = self.StopWords()
        text = ""
        if(numpages > 8):
            for i in range(1, (numpages - 3)):
                page = pdf.getPage(i)
                text += "\n" + self.trl.translate(page.extractText(), lang_tgt='en')
        else:
            for i in range(1, (numpages)):
                page = pdf.getPage(i)
                text += "\n" + self.trl.translate(page.extractText(), lang_tgt='en')

        words = self.tokenize(text)
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in SW:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1

        sentences = sent_tokenize(text)
        sentenceValue = dict()
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                        if sentence in sentenceValue:
                            sentenceValue[sentence] += freq
                        else:
                            sentenceValue[sentence] = freq

        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]

        average = int(sumValues/ len(sentenceValue))
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence
        return self.getReSummary(summary) 


    def getReSummary(self, page_content):
        article_text = page_content
        article_text = article_text.replace("[ edit ]", "")
        article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
        sentence_list = nltk.sent_tokenize(article_text)
        
        stopwords = nltk.corpus.stopwords.words('english')
        word_frequencies = {}
        for word in nltk.word_tokenize(formatted_article_text):
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1

        maximum_frequncy = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

        sentence_scores = {}
        for sent in sentence_list:
            for word in nltk.word_tokenize(sent.lower()):
                if word in word_frequencies.keys():
                    if len(sent.split(' ')) < 50:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word]
                        else:
                            sentence_scores[sent] += word_frequencies[word]


        summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)

        summary = ' '.join(summary_sentences)
        summary = self.trl.translate(summary, lang_tgt='es')
        return summary

    def TradEn(self, text):
        texts = self.trl.translate(text, lang_tgt='en')
        return texts