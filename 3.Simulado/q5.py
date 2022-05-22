from random import randint

print('\nSimulado - Erimilon Silva ')
print('\nQ5 - Gerar Trios Númericos entre 0 a 200')

print('\nGere trios numéricos inteiros entre 0 e 200.'
'\nCaso os números sejam iguais informe o número gerados.'
'\nCaso os um dos números seja diferente dos demais gere um novo trio.'
'\nInforme quantos trio foram necessários gerar')

num1 = randint(0,200)
num2 = randint(0,200)
num3 = randint(0,200)

cont = 0

while num1 != num2 and num1 != num3 and num2 != num3:
    num1 = randint(0,200)
    num2 = randint(0,200)
    num3 = randint(0,200)

    cont += 1

print('\nOs números Iguais Formados foi: ',num1)
print('\nForam Necessários',cont,'Repetições')