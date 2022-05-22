print('\nSimulado - Erimilon Silva ')
print('\nQ3 - Exibe 30 termos do Somátorio: S = 2/3 + 6/4 + 3/1 + 2/6 + (-1)/3 + 2/6...')

num = 2
div = 3
s = 0
sinal = True

print('\nS = (',num,'/',div,') ', end = '')

for i in range(0,8):
    if sinal:

        s = s + num/div
        temp = num
        num = num * 2
        div = temp * 2
        print('+ (',num,'/',div,')', end = '')
        sinal = False
    
    else:

        s = s + num/div
        num = num - 3
        div = div - 3
        print(' + (',num,'/',div,')', end = '')
        sinal = True

print('\n\nObs: Inconclusivo, Erro na sequência de termos no Somátorio ')