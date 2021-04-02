from Model import PdfReader as Rd
from Model import SummaryModel as Sm

class Controlador():
    def __init__(self):
        self.Reader = Rd.Reader()
        self.Summary = Sm.SummaryModel()
    
    def DoSummary(self, file):
        pdf = self.Reader.getPdf(file)
        numpages = self.Reader.getNumpage()
        return self.Summary.getSummary(pdf, numpages)

    def DoSummaryEn(self, file):
        return self.Summary.TradEn(file)