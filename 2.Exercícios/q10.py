print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ10 - 50 primeiros termos do somatório: S = - 1 - 2 + 3 + 4 - 5 - 6 + 7 + 8 ...')

num = 0
s = 0
cont = 0
troca = True

print('\nS =', end ='')
for i in range(50):
    if troca :
        cont += + 1
        num += + 1
        print(' -',num, end= '')
        if cont == 2:
            troca = False
            cont = 0

    else:
        cont += + 1
        num += + 1
        print(' +',num, end= '')
        if cont == 2:
            troca = True
            cont = 0

print('\n')