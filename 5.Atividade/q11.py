print('Exercicio 02/05 Erimilson Silva')
print('Q11 - Ler a altura e o sexo. Maior e Menor altura; A média de altura das mulheres; O número de homens;')

homem = 0
maiorAltura = 0
menorAltura = 10
media = 0
div = 0
repita = True

while repita:
    sexo = int(input('\nInforme seu Sexo: (1) Masculino ou  (2) Feminino: '))
    altura = float(input('Informe sua Altura ex(1.70): '))

    if sexo == 1:
        homem =+ 1

        if altura > maiorAltura:
            maiorAltura = altura

        if altura < menorAltura:
            menorAltura = altura
    
    if sexo == 2:

        if altura > maiorAltura:
            maiorAltura = altura

        if altura < menorAltura:
            menorAltura = altura

        div= + 1
        media= altura / div

    print('Deseja Informa uma Nova Informação: ')
    print('\n(1) SIM'
          '\n(2) NÂO :')
    opc = int(input('\nDigite: '))
    if opc == 1:
        repita = True
    else:
        repita = False


print(f'\nA Maior altura do grupo: {maiorAltura:,.2f}')
print(f'A Menor altura do grupo: {menorAltura:,.2f}')
print(f'A média de altura das mulheres: {media:,.2f}')
print('O número de homens:',homem)