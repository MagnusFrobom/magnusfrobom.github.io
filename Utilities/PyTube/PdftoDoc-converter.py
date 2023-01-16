import pypdf2

file_path = 'C:/Users/HP/Documents/Magnus-Fröbom-Cover-letter-CV-Telus-international-2023-01-10.pdf'

with open(file_path, mode='rb') as f:
    
    reader = pypdf2.pdfFilereader(f)
    
    page = reader.getPage(0)
    
    print(page.extractText())
