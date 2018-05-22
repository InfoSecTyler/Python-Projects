'''
Tool that takes a supplied dictonary and atempts to decrypt a supplied
.PDF document
'''

# Imports
import PyPDF2

# Identify the PDF to use the tool against.
inputPdf = PyPDF2.PdfFileReader(open('test.pdf', 'rb'))

# Create the string where we house the dictonary of paswords

# Function to try and decrypt the PDF.
def bForce():
    while inputPdf.isEncrypted == True:
        for x in attack_dict:
            pdfReader.decrypt(x)
            if pdfReader.decrypt(x) == 1:
                print(x "was the password!")
