from pypdf import PdfReader

reader= PdfReader("C:/Users/kisho/Downloads/1782286021_Unit 5- LM 1 Expert Systems - Stages in the development of an Expert System.pdf")

text=""
for page in reader.pages:
    text+=page.extract_text()+'\n'

print(len(text))
print(text[:1000])