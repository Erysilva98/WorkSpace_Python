import random

print('\nSimulado - Erimilon Silva ')
print('\nQ1 - Gera 50 números e Imprimir os N. Pares e Impares')

print('\nGere 50 números inteiros entre 0 e 100'
'\nInforme os dois maiores pares números gerados'
'\nInforme os dois menores números ímpares que foram gerados') 

maiorPar = maiorPar2 = - 1
menorImpar = menorImpar2 = 1000

for i in range(0,50):
    num = random.randint(1,100)
    if num % 2 == 0:
        if maiorPar < num:
            maiorPar2 = maiorPar
            maiorPar = num
        if maiorPar > num and maiorPar2 < num:
            maiorPar = num
    else:
        if menorImpar > num:
            menorImpar2 = menorImpar
            menorImpar = num
        if menorImpar < num and menorImpar2 > num:
            menorImpar2 = num

print('\n Dados Coletados')
print('\n 1° Maior numero Par = ',maiorPar)
print('\n 2° Maior numero Par =',maiorPar2)
print('\n 1° Menor numero Impar = ',menorImpar)
print('\n 2° Menor numero Impar =',menorImpar2)
