from random import randint

print ('\nExercícios 08/06 - Erimilson Silva')
print('Q15. Sistema de conta de energia.')

consumo = randint(300,1000)

bandeira = randint(1,4)

if bandeira == 1:
    
    custoTotal = consumo * 10

    print('\nBandeira tarifária - Verde ')
    print('Consumo do Mẽs =',consumo,'Quilowatts-hora')
    print(f'Valor a pagar = R$:{custoTotal:,.2f}')

elif bandeira == 2:
    
    taxa = consumo / 100
    custo = consumo * 10
    custoTotal = custo + ( taxa * 1 )

    print('\nBandeira tarifária - Amarela ')
    print('Consumo do Mẽs =',consumo,'Quilowatts-hora')
    print(f'Taxa no valor de R$:{taxa:,.2f}')
    print(f'Valor a pagar = R$:{custoTotal:,.2f}')

elif bandeira == 3:
    
    taxa = consumo / 100
    custo = consumo * 10
    custoTotal = custo + ( taxa * 3 )

    print('\nBandeira tarifária - Vermelha Patamar 1 ')
    print('Consumo do Mẽs =',consumo,'Quilowatts-hora')
    print(f'Taxa no valor de R$:{taxa:,.2f}')
    print(f'Valor a pagar = R$:{custoTotal:,.2f}')

else:
    
    taxa = consumo / 100
    custo = consumo * 10
    custoTotal = custo + ( taxa * 5 )

    print('\nBandeira tarifária - Vermelha Patamar 1 ')
    print('Consumo do Mẽs =',consumo,'Quilowatts-hora')
    print(f'Taxa no valor de R$:{taxa:,.2f}')
    print(f'Valor a pagar = R$:{custoTotal:,.2f}')