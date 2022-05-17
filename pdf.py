import pdfplumber

with pdfplumber.open("sta.pdf",password="1219900723810") as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())
