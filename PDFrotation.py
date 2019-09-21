import PyPDF2

filename = 'QS_Graduate_Employability_Rankings_2020.pdf'
doc = open(filename, 'rb')

pdfread = PyPDF2.PdfFileReader(doc)

rotatedpdf = PyPDF2.PdfFileWriter()

for page in range(pdfread.numPages):
    pageobj = pdfread.getPage(page)
    pageobj.rotateClockwise(90)
    rotatedpdf.addPage(pageobj)

newfile = open('rotated' + filename, 'wb')
rotatedpdf.write(newfile)
newfile.close()
doc.close()

