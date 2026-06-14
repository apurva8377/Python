##################################################################################################################
#
#  Program Name : 105_DuckTyping.py
#  Discription  : Duck Typing
#  Author       : Apurva Vilas Shinde
#  Date         : 19/05/2026
#
##################################################################################################################

# Duck typing : It is a concept where the type of an object is determined by its behaviouor , not by its class

class InkjetPrinter:
    def printdocument(self,document):
        print("Inkjet printer printing : ",document)

class LaserPrinter:
    def printdocument(self, document):
        print("Laser printer printing : ",document)

class PDFWriter:
    def printdocument(self, document):
        print(f"Svaing {document} as PDF")

def StartPrinting(Device):
    Device.printdocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()