
from random import randint

print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ5 - Calcula o Lucro de um Estacionamento de um Shopping')

moto = 0
carro = 0
onibus = 0
lucroMoto = 0
lucroCarro = 0
lucroOnibus = 0
lucroTotal = 0

# Gerando os Veiculos
for i in range(1,400):
    
    tipo = randint(1,3)

    if tipo == 1:
        moto = moto + 1
    elif tipo == 2:
        carro = carro + 1
    else:
        onibus = onibus + 1

#Calculando Lucro

lucroMoto = moto * 4
lucroCarro = carro * 8
lucroOnibus = onibus * 20

lucroTotal = lucroMoto + lucroCarro + lucroOnibus

print('\nForam Cobradas Taxas de',moto,'Motos, um total de R$:',lucroMoto,',00')
print('Foram Cobradas Taxas de',carro,'Motos, um total de R$:',lucroCarro,',00')
print('Foram Cobradas Taxas de',onibus,'Motos, um total de R$:',lucroOnibus,',00')

print('\nO Shopping obetve um lucro diário de R$:',lucroTotal,',00')