from random import randint

print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ8 - A Batalha pelo trono de Asgard')
#Personagens
#Loky
#Lady Sif, 
#alquíria, 
#Fandral, 
#Volstagg
#Hogun.

print('\nOs 5 Desafios de Loky, precisa de 3 Para Ser o Escolhido')

vitoria = 0 # *Loky é o Deus da Trapaça
result1 = ' '

print('\n1 - Desafio da Comida: Loky vs Volstagg ')

loky1 = randint(1,100)
volstagg = randint(1,100)

if loky1 < volstagg:
    vitoria = vitoria + 1
    result1 = '\n   Loky Venceu o 1° Desafio '
else:
    vitoria = vitoria + 1  # Trapaça. O Loky é Magrinho não consegue Comer muito
    result1 = '\n   Loky Venceu o 1° Desafio '

print(result1)

print('\n2 - Desafio de Arco e Flechas: Loky vs Frandral ')

for i in range(0,11):

    loky2 = randint(0,61)
    frandral = randint(0,61)

    # Alvo = 0
    sLoky = 0
    sFrandral = 0
    vencedor = False
    result2 = ' '

    if loky2 == 0 and  frandral != 0:
        vencedor = True
        result2 = '\n   Loky Venceu o 2° Desafio '

    else:
        sLoky = sLoky + loky2
        sFrandral = sFrandral + frandral
    
    if vencedor == False:

        if sLoky > sFrandral:
            vencedor = True
            result2 = '\n   Loky Venceu o 2° Desafio '
        elif sLoky == sFrandral:
            result2 = '\n   Desafio do Arco e Flecha, terminou em Empate '
        else:
            result2 = '\n   Loky Perdeu está Rodada'

if vencedor == True:
    vitoria = vitoria + 1

print(result2)

print('\n3 - Uma batalha de polegar: Loky vs Hogun ')
# Gerando um nível de Habilidade

lokyQI = randint(1,1000)
hogunQI = randint(1,1000)

if lokyQI > hogunQI:
    vitoria = vitoria + 1
    result3 = '\n   Loky Venceu o 3° Desafio '

elif lokyQI == hogunQI:
    result3 = '\n   Após Varias Horas foi Declarado Empate! '
else:
    result3 = '\n   Loky Perdeu está Rodada'

print(result3)

if vitoria == 3:
    print('\nLoky é o escolhido para Defender Asgard. ')

else:
    print('\n4 - Desafio da Batalha até a Rendição: Loky vs Valquíria ')

    repita = True
    result4 = ' '

    while repita:

        n1Loky = randint(1,10)
        n2Loky = randint(1,10)

        n1Val  = randint(1,10)
        n2Val  = randint(1,10)

        if n1Loky == n2Loky and n1Val != n2Val:
            vitoria = vitoria + 1
            result4 = '\n   Loky Venceu o 4° Desafio '
            repita = False
        elif n1Loky == n2Loky and n1Val == n2Val:
            repita = True
        else:
            result4 = '\n   Loky Perdeu está Rodada'
            repita = False

        print(result4)
        
    if vitoria == 3:
        print('\nLoky é o escolhido para Defender Asgard. ')

    else:
        print('\n5 - Desafio Luta de Espadas: Loky vs Lady Sif ')
        #Ex: Atacante gerou um número par e o defensor um número ímpar. O atacante conseguiu atingir o defensor.
        #Ex2: Atacante gerou um número par e o defensor um número par. O defensor desviou o ataque.

        a1Loky = randint(0,10)
        a2Loky = randint(0,10)
        a3Loky = randint(0,10)

        d1Lady = randint(0,10)
        d2Lady = randint(0,10)
        d3Lady = randint(0,10)

        lokyAtaque = 0
        ladyDefesa = 0
        result5 = ' '

        if a1Loky % 2 == 0 and d1Lady % 2 == 1:
            lokyAtaque =+ 1
        else:
            ladyDefesa =+ 1

        if a2Loky % 2 == 0 and d2Lady % 2 == 1:
            lokyAtaque =+ 1
        else:
            ladyDefesa =+ 1

        if a3Loky % 2 == 0 and d3Lady % 2 == 1:
            lokyAtaque =+ 1
        else:
            ladyDefesa =+ 1
        
        if lokyAtaque > ladyDefesa:
            vitoria = vitoria + 1
            result5 = '\n   Loky Venceu o 3° Desafio '

        elif lokyAtaque == ladyDefesa:
            result5 = '\n   A Batalha de Espada Término em Empate! '
        else:
            result5 = '\n   Loky Perdeu está Rodada'

        print(result5)
                
        if vitoria == 3:
            print('\nLoky é o escolhido para Defender Asgard. ')

        else:
            print('\nLoky não foi escolhido para Defender Asgard  ')












































