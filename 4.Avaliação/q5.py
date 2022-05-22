print('\nAvaliação - Erimilson Silva')
print('\nQ5 - Ler a Idade do Aluno e apresenta a sequência Lógica, Verdade ou Falso...')

A = True
B = True
C = False
D = False
idade = int(input('\nDigite sua idade: '))
if idade % 2 == 0:
    if((A and not (B or not A)) ^ B and C ^ (A or not D) and (A and B)):
        print('Verdade')
    else:
        print('Falso')
    A = False
    B = True
    C = False
    D = True
    if((C or not A and not (B and not A)) ^ B or C ^ (A ^ (not D)) and (A or C)):
        print('Verdade')
    else:
        print('Falso')
    A = True
    B = False
    C = False
    D = True
    if((C ^ (not A) and (B and not A)) ^ B and C ^ (A ^ (not D)) and (A or C)):
        print('Verdade')
    else:
        print('Falso')

else:
    if((A and not (B and D)) ^ B and C ^ (C or not D) and (A and B)):
        print('Verdade')
    else:
        print('Falso')
    A = False
    B = True
    C = False
    D = True
    if((C or not A and not (B and not A)) ^ B or C ^ (A ^ (not D)) and (A or C)):
        print('Verdade')
    else:
        print('Falso')
    A = True
    B = False
    C = False
    D = True
    if((C ^ (not A) and (B and not A)) ^ B and C ^ (A ^ (not D)) and (A or C)):
        print('Verdade')
    else:
        print('Falso')