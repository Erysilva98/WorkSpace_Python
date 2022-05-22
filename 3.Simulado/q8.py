print('\nSimulado - Erimilon Silva ')
print('\nQ8 - Ler 3 Números e Informe o M.M.C dos Números')

print('\nLeia três números inteiros'
'\nInforme o M.M.C dos números lidos\n')

n1 = int (input('1° Número: '))
n2 = int (input('2° Número: '))
n3 = int (input('3° Número: '))

if n1 > n2 and n1 > n3:
    maior = n1
    num2 = n2
    num3 = n3
elif n2 > n1 and n2 > n3:
    maior = n2
    num2 = n1
    num3 = n3
else:
    maior = n3
    num2 = n1
    num3 = n2

mmc = 1
print('\nMMC de ',maior,'.',num2,'.',num3,'/',2)
for i in range(2,maior+1):
    
    while maior % i == 0 or num2 % i == 0 or num3 % i == 0:
        mmc = mmc * i        

        if maior % i == 0: 
            maior = int (maior/i)
        
        if num2 % i == 0:
            num2 = int (num2/i)

        if num3 % i == 0:
            num3 = int (num3/i)

        print('\n       ',maior,'.',num2,'.',num3,'/',i)
        
print('\nMMC =',mmc)
