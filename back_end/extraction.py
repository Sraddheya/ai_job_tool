# Use the PyPDF2 library to extract text from a PDF file

import PyPDF2

# Open the PDF file in read mode
pdf_file = open('uploads/cv.pdf', 'rb')

# Create a PDF reader object
pdfreader = PyPDF2.PdfReader(pdf_file)

# Get the total number of pages
x = pdfreader.numPages

# Iterate through all the pages
for i in range(x):
    # Get the page at index i
    pageobj = pdfreader.getPage(i)

    # Extract the text from the page
    print(pageobj.extractText())
