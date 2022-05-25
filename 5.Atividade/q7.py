print('Exercicio 02/05 Erimilson Silva')
print('Q7 - Desenvolvido um programa que ler um número inteiro e exibe seu fatorial.')

num = int (input('\nInforme um Número Inteiro; '))

result = 1
count = 1

while count <= num:
    result *= count
    count +=1

print('\nO Fatorial de',num,'é =',result)