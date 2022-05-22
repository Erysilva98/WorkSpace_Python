print('\nSimulado - Erimilon Silva ')
print('\nQ6 - Ler N. Pessoas e Informa as Três Mais Novas')

idade1 = idade2 = idade3 = 1000
nome1 = nome2 = nome3 = ''

loop = True

while loop:
    nome = input('\nInforme o nome da Pessoa: ')
    print('Informe a Idade de',nome,': ', end ='')
    idade = int(input())

    if idade1 > idade:
        idade3 = idade3
        nome3 = nome2

        idade2 = idade1
        nome2 = nome1

        idade1 = idade
        nome1 = nome

    elif idade2 > idade:
        idade3 = idade2
        nome3 = nome2

        idade2 = idade
        nome2 = nome

    elif idade3 > idade:
        idade3 = idade
        nome3 = nome
    
    else:
        print('\nIdade Descartada')

    opc = int (input('\nDigite 1 para Informar uma nova pessoa e 2 para Sair: '))

    if opc == 2:
        loop = False

print('\n',nome1,'1° Pessoa mais nova com',idade1,'Anos')
print('\n',nome2,'2° Pessoa mais nova com',idade2,'Anos')
print('\n',nome3,'3° Pessoa mais nova com',idade3,'Anos')