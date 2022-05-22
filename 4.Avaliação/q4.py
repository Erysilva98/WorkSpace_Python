print('\nAvaliação - Erimilson Silva')
print('\nQ4 - Somatório: S= 2/3 + 4/5 + 6/7 - 8/9 - 10/11 - 12/13 - 14/15 + 16/17...')


termo = int (input('Digite o número de Termos para S: '))

num = 2
div = 3
sinal = 2

print('S = ',num,'/',div, end= '')

s = num/div

for i in range(1,termo):
    if sinal < 4:
        sinal = sinal + 1
        num = num + 2
        div = div +2
        s = s + num /div
        print(' + ',num,'/',div, end='')
    elif sinal < 7:
        sinal = sinal + 1
        num = num + 2
        div = div + 2
        s = s - num /div
        print(' - ',num,'/',div, end='')
    else:
        sinal = 1
        num = num + 2
        div = div + 2
        s = s - num /div
        print(' -',num,'/',div, end='')
    
print(' = ',s)



print(' ')