#! usr/bin/env python
import PyPDF2


class Reader():
    def __init__(self):
        self.numpages = 0

    def getPdf(self, file):
        pdf = open(file, "rb")
        reader = PyPDF2.PdfFileReader(pdf)
        self.numpages = reader.getNumPages()
        return reader
    
    def getNumpage(self):
        return self.numpages