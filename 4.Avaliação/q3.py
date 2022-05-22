from random import randint

print('\nAvaliação - Erimilson Silva')
print('\nQ3 - Sistema de controle de Cinema')

valorTotal = 0

n = randint(0,50)

print('\n',n,'Pessoas foram ao Cinema de Belo Jardim, ',end='')

for i in range(n):

    ingresso = randint(0,200)

    if ingresso % 2 == 0:
        valorTotal = valorTotal + 30.00
    
    else:
        valorTotal = valorTotal + 15.00

print('gerando RS:',valorTotal,'de Reais para o cinema no Final do Dia')
