while True:
    idade = input("\nGostaria de conferir o preço?\nPara sair digite 'q', senão, insira a idade: ")
    if idade == 'q':
        break

    try:
        idade = int(idade)
    except:
        print('\nDIGITE UM NÚMERO')
        continue

    valorBase = 10.0
    if idade > 5 and idade <=12:
        preço = valorBase / 2
    elif idade <= 5: 
        preço = 0
    elif idade >=13 and idade <=17:
        preço = valorBase * 0.8
    elif idade >= 70:
        preço = 0
    else:
        preço = valorBase
    print('Preço: R$' + str(preço))


        




