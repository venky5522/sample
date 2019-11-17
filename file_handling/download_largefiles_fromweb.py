import requests

pdf_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"

a = requests.get(pdf_url,stream = True)

with open('my_pdf.pdf',"wb") as pdf:
    for chunk in a.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(a.content)