from random import randint

print('\nSimulado - Erimilon Silva ')
print('\nQ4 - Jogo de Corrida e Informa o Vencedor (???)')

print('\nInformações: ')
print('\nTermos  2 Players com um Modelo de Carro cada')
print('\n5 Corridas e informe quem venceu o campeonato') 
print('\n   Red Bull vs Ferrari')
# Modificações com Base na Correção
# 1 - Carro Azul é a Red Bull
# 2 - Carro Branco é a Ferrari
# 3 - Circuitos com Km Reais 
# 4 - Velocidade Máxima Alterada
# Obs: Lógica de Cálculos segue o Padrão

#Circuitos
gp1 = 5412 #GP do Bahrein
gp2 = 5303 #GP da Austrália
gp3 = 5412 #GP de Miami
gp4 = 4675 #GP da Espanha 
gp5 = 3337 #GP de Mônaco
gp6 = 5842 #GP da França
gp7 = 5793 #GP da Itália
gp8 = 4361 #GP do Canadá 
gp9 = 4309 #GP do Brasil
gp10 = 4700 #GP de ABU Dhabi

#Vitória de Pilotos
mVerstappen = 0
cLeclerc = 0

for i in range(0,5):

    pista = randint(1,10)

    if pista == 1:
        pista = gp1
        print('\n   GP do Bahrein ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    elif pista == 2:
        pista = gp2
        print('\n   GP da Austrália ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    elif pista == 3:
        pista = gp3
        print('\n   GP de Miami ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    elif pista == 4:
        pista = gp4
        print('\n   GP da Espanha ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    elif pista == 5:
        pista = gp5
        print('\n   GP de Mônaco ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    elif pista == 6:
        pista = gp6
        print('\n   GP da França ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    elif pista == 7:
        pista = gp7
        print('\n   GP da Itália ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    elif pista == 8:
        pista = gp8
        print('\n   GP do Canadá ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    elif pista == 9:
        pista = gp9
        print('\n   GP do Brasil ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

    else:
        pista = gp10
        print('\n   GP do Abu Dhabi ')

        #Formula 1 Red Bull
        # * Alteração na Velocidade Máxima
        velMax1 = randint(210,240)
        temp1 = int (pista/velMax1)

        troca1 = randint(30,60)
        pitStop1 = int (pista/troca1)
        
        # Tempo de Volta
        redBull = temp1 + pitStop1
        
        #Formula 1 Ferrari 
        # * Alteração na Velocidade Máxima
        velMax2 = randint(206,240)
        temp2 = int (pista/velMax2)

        troca2 = randint(30,60)  
        pitStop2 = int (pista/troca2)
        
        # Tempo de Volta
        ferrari = temp2 + pitStop2 

        if redBull > ferrari:
            mVerstappen = mVerstappen + 1
            print('     1 - Verstappen Venceu')
        else:
            cLeclerc = cLeclerc + 1
            print('     2 - Leclerc Venceu')

if mVerstappen > cLeclerc:
    print('\n   Verstappen é o Campeão Mundial pela 2° Vez',mVerstappen,'pontos')
    print('   Red Bull Vence o Campeonato 2022 ')
elif cLeclerc > mVerstappen:
    print('\n   Leclerc é o Campeão Mundial pela 1° Vez, com',cLeclerc,'pontos')
    print('   Ferrari Vence o Campeonato 2022 ')
else:
    print('Inacreditável! Ferrrari e Red Bull terminarão empatadas')

