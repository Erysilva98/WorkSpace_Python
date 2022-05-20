print ('\nAtividade 14/03 - Erimilson Silva')
print('\nQ1 - Programa ler 2 números Inteiros.')
                                                                         
num1 = int (input('\nDigite o 1° Número Inteiro: '))
num2 = int (input('\nDigite o 2° Número Inteiro: '))

if num2 % 2 == 0:
    resp = num1 + num2
    print('A Soma dos Números é:',resp)
else:
    resp = num1 * num2
    print('A Multiplicação dos Números é:',resp)