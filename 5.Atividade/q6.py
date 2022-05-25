print('Exercicio 02/05 Erimilson Silva')
print('Q4 - Ler 6 números Naturais e informe se são válidos para mega-sena. Caso seja inválido informe os.')

megaSena = []
invalido = []

print('\nInforme 6 Números Para Mega Sena \n')

for i in range(1,6):
    num = int (input('Informe um Número Inteiro: '))

    if num > 0 and num <= 60:
        megaSena = megaSena + [num]

    else:
        invalido = invalido + [num]
    

print('\nNúmeros Válidos para Mega Sena',megaSena)
print('Os Números',invalido,'são Invalidos')


