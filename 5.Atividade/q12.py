print('Exercicio 02/05 Erimilson Silva')
print('Q12 - Conversão de graus centígrados para Farenheit. Variação de 50 a 150 de 1 em 1.')

print('\nTabela de Centígrados em de graus Farenheit, que variam de 50 a 150 de 1 em 1. \n')

#C = (5/9) * (F - 32)

for i in range(50,150):

    grau = i
    
    celcius = grau / 9
    farenheit = grau - 32

    print(f'{celcius:,.2f}°C | {farenheit:,.2f}°F')
    print('\n')
