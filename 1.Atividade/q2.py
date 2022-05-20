print ('\nAtividade 14/03 - Erimilson Silva')
print('\nQ2 - Calcular o peso ideal de Uma Pessoa.')

altura = float (input('\nDigite sua Altura, ex(1.70): '))
print('Sexo:\n 1 - Masculino \n 2 - Feminino')
opc = int (input('Opção: '))

peso = 0

if opc == 1:
    peso = (62.1 * altura) - 44.7
    print(f'\nSeu Peso ideal é: {peso:,.2f}')
elif opc == 2:
    peso = (72.2 * altura) - 58
    print(f'\nSeu Peso ideal é: {peso:,.2f}')
else:
    print('Opção Inválida! ')