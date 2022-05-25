print('Exercicio 02/05 Erimilson Silva')
print('Q5 - Desenvolvido um sistema que ler um número Inteiro e informa se é múltiplo de 2 e 3 ao mesmo tempo.')

num = int (input('\nDigite Um numero Inteiro: '))

if num % 2 == 0 and num % 3 == 0:
    print(' O Numero ',num,'é Múltiplo de 2 e de 3 ')
else:
    print(' O Numero ',num,'não é Múltiplo de 2 e de 3 ')