import re

with open('/home/toninhorf/Documentos/Objdump-Project/arquivos_executaveis.txt', 'r') as file:
	entradas = file.read()

nomes = re.findall(r'([^\s:]+):', entradas)

with open('/home/toninhorf/Documentos/Objdump-Project/arquivosx2.txt', 'w') as file1:
	file1.write("".join(nomes))

