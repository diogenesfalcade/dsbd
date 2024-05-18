import sys

#le arquivo e armazena a string original
arq = open(sys.argv[1])
textoStr = arq.read()
texto = textoStr.splitlines()

#lê apenas a primeira linha da lista e divide por vírgula
primeiraLinha = texto[1]
colunas = primeiraLinha.split(',')
nomesColunas = ""

#itera por cada item da coluna, divide por ponto e cria o texto para o header
for item in colunas:
   header = item.split(':')
   strToReplace = header[0] + ':'
   textoStr = textoStr.replace(strToReplace,'')
   nomesColunas += header[0] + ','
nomesColunas = nomesColunas[0:(len(nomesColunas) - 1)] + '\n'

#escreve arquivo e fecha handlers
with open('dados_saida.csv', 'w') as arqSaida:
   arqSaida.write(nomesColunas)
   arqSaida.write(textoStr)
   arqSaida.close()

arq.close()