from random import randint

print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ3 - Gerar 3 númeos inteiros e distintos. Maior que 0 e menor que 30.')

for i in range(1,3):
    num1 = randint(1,29)
    num2 = randint(1,29)
    num3 = randint(1,29)

    while num1 == num2 or num1 == num3 or num2 == num3:
        num1 = randint(1,29)
        num2 = randint(1,29)
        num3 = randint(1,29)

print('\nO 1° Número Gerado: ',num1)
print('\nO 2° Número Gerado: ',num2)
print('\nO 3° Número Gerado: ',num3)
