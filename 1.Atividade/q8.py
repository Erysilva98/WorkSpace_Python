print ('\nAtividade 14/03 - Erimilson Silva')
print('\nQ8 - Ler uma figura geométrica (retângulo, triângulo ou círculo) e informe a área.')

print("\nInforme 3 Valores geométricos Inteiro e veja a Área ")

print('\nEscolha uma das Opção Abaixo.')
print('1 - Retângulo')
print('2 - Triângulo')
print('3 - Círculo')
opc = int (input('\nDigite: '))

if opc == 1:
    base = int(input('Informe o valor da Base: '))
    altura = int(input('Informe o vaor da Altura: '))
    resp = base * altura
    print('A Área do Retãngulo é:',resp)

if opc == 2:
    base = int(input('Informe o valor da Base: '))
    altura = int(input('Informe o vaor da Altura: '))
    resp = (base * altura) /2
    print('A Área do Triângulo é:',resp)

if opc == 3:
    raio = int(input('Informe o valor do Raio: '))
    resp = 3.14 * (raio * raio)
    print(f'A Área do Cérculo é :{resp:.2f}')