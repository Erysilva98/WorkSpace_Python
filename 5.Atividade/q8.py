print('Exercicio 02/05 Erimilson Silva')
print('Q8 - O Sistema exibe os primeiros 30 termos da sequência: S: 1/2 + 2/4 + 3/6 + 4/8...')

numerador = 1
denominador = 2

s = 0 

print('\nS=',numerador,'/',denominador, end='')

for i in range(1,30):
    s = s+numerador/denominador
    temp = numerador
    numerador = temp + 1
    denominador = denominador + 2
    print(' +',numerador,'/',denominador, end ='')
    
print('')