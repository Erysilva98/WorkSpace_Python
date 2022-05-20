print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ2 - Ler a Base e o Expoente de uma potência e exiba o resultado.')

base = int(input('\nInforme um Número Inteiro para a Base: '))
expo = int(input('\nInforme um Número Inteiro para o Expoente: '))

elevado = 1
cont = 1

while cont <= expo:
    elevado *= base
    cont+=1

print('A Base',base,'Elevado ao Expoente',expo,'=',elevado)