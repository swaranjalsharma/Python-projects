import PyPDF2

pdfiles = ["samplepdf1.pdf", "samplepdf2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfiles = open(filename, 'rb')
    pdfReader    = PyPDF2.PdfReader(pdfiles)
    merger.append(pdfReader)
pdfiles.close()
merger.write('merged.pdf')





