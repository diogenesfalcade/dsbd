# import csv

# arq = open('exemplo.csv', 'r')
# csv_reader = csv.reader(arq,delimiter=';')
# for linha in csv_reader:
#     print(linha[1])
#     next(csv_reader)
# arq.close() 

# frase1 = "laranja laranja"
# frase2 = frase1.replace("laranja", "banana", 1)
# frase3 = frase1[0:3] + " " + frase1 + " " + frase2
# print(frase3)

# arq = open("documento.txt", "a")
# arq.write("Olá mundo\n")
# arq.write("Cruel\n")
# arq.close()

# arq = open("documento.txt", "w")
# arq.write("Esse é um documento de texto")
# arq.close()

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 8, 2, 4, 5, 
#            4, 9, 9, 12, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
#            40, 44, 4, 4, 4)
# count = 0
# for number in numbers:
#     if (number%2 == 0):
#         count += 1 
# print(count)