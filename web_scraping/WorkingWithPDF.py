
import PyPDF2
file=open('flask.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(file)
page_one=pdf_reader.getPage(7)
page_one_text=page_one.extractText()
print(page_one_text)
print(pdf_reader.numPages)
file.close()
