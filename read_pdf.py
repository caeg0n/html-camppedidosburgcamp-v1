import pypdf

reader = pypdf.PdfReader('cardapio.pdf')
for page in reader.pages:
    print(page.extract_text())
