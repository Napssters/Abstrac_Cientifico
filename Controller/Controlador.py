from Model import PdfReader as Rd
from Model import SummaryModel as Sm

class Controlador():
    def __init__(self):
        self.interSummary = ""
        self.Summary = Sm.SummaryModel()

    def getInterSummary(self):
        return self.interSummary

    def DoSummary(self, file):
        Reader = Rd.Reader()
        pdf = Reader.getPdf(file)
        numpages = Reader.getNumpage()
        summary = self.Summary.getSummary(file, numpages)
        self.interSummary = self.Summary.getInterSummary()
        return summary

    def DoSummaryEn(self, file):
        return self.Summary.TradEn(file)

    def getStopWord(self):
        return self.Summary.StopWords()

    def getSteps(self):
        pasos = [
            self.Summary.paso2,
            self.Summary.paso3,
            self.Summary.paso4,
            self.Summary.paso5,
            self.Summary.paso6,
            self.Summary.paso7,
            self.Summary.paso8,
            self.Summary.paso9,
            self.Summary.paso10
        ]
        return pasos
