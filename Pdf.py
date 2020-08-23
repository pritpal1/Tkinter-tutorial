import PyPDF2
pdf_obj=open("8259.pdf","rb")
pdf_reader=PyPDF2.PdfFileReader(pdf_obj)
pageObj=pdf_reader.getPage(0)
print(pageObj.extractText())