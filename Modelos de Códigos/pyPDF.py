from PyPDF2 import *

leitor = open('02-POO-EXERCICIOS.pdf', 'rb')
arquivo = PdfReader(leitor)
paginas = len(arquivo.pages)
print(f'O documento atual contém {paginas} páginas')