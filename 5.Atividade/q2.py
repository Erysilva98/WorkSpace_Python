from random import randint

print('Exercicio 02/05 Erimilson Silva')
print('Q2 - Desenvolvido um sistema para calcula o tempo que Chico leva para chegar na Escola.')

print('\nCalculando o tempo de percuso do Chico para chegar á escola ')

# Uma légua e meia em Km
distancia = 7.25  #Km
tempoTotal = 50

# Atrasos
diasQuentes = randint(0,3)
pomar = randint(0,3)
rosinha = randint(0,3)

if diasQuentes == 1:
    tempoTotal = tempoTotal + 40
    trajeto = tempoTotal / distancia 
    print('\nUm Percuso de 7.25 Km')
    print('\n Estava um dia Quente! ')
    print(f'Chico fez um percuso de: {trajeto:,.2f} Metros por minuto')
    print('O Tempo gasto por Chico para chegar à escola no dia 07/06/2021 foi',tempoTotal,'Minutos')    

elif pomar == 2:
    tempoTotal = tempoTotal + 20
    trajeto = tempoTotal / distancia 
    print('\nUm Percuso de 7.25 Km')
    print('\n Tinha um belo Pomar no caminho! ')
    print(f'Em uma Caminhada Chigo faz: {trajeto:,.2f} Metros por minuto')
    print('O Tempo gasto por Chico para chegar à escola no dia 07/06/2021 foi',tempoTotal,'Minutos')

elif rosinha == 3:
    namorando = randint(0,10)
    tempoTotal = (namorando * 10) + tempoTotal
    trajeto = tempoTotal / distancia 
    print('\nUm Percuso de 7.25 Km')
    print('\n Chico encotro a Namorada Rosinha! ')
    print(f'Em uma Caminhada Chigo faz: {trajeto:,.2f} Metros por minuto')
    print('O Tempo gasto por Chico para chegar à escola no dia 07/06/2021 foi',tempoTotal,'Minutos')
else:
    trajeto = tempoTotal / distancia 
    print('\nUm Percuso de 7.25 Km')
    print(f'Em uma Caminhada Chigo faz: {trajeto:,.2f} Metros por minuto')
    print('O Tempo gasto por Chico para chegar à escola no dia 07/06/2021 foi',tempoTotal,'Minutos')
