from random import randint

print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ1 - O vencedor da Corrida Contra o FLASH.')

vLuz = 300 #Km/s
vSom = 34 #Km/s

#Personagens
jesseQuick = randint(1,10)
barryAllen = randint(1,10)
wallyWest = randint(1,10)
drWells = randint(1,10)
jayGarrick = randint(1,10)
maxMercury = randint(1,10)

# Aferição de Velocidade 
vl1 = jesseQuick * vSom
vl2 = barryAllen * vSom
vl3 = wallyWest * vSom
vl4 = drWells * vSom
vl5 = jayGarrick * vSom
vl6 = maxMercury * vSom

if vl1 < vl2 and vl1 < vl3 and vl1 < vl4 and vl1 < vl5 and vl1 < vl6:
    print('\nA Jesse Quick é a Vencedora, com Velocidade da Luz =',vl1,'Km/s')

elif vl2 < vl1 and vl2 < vl3 and vl2 < vl4 and vl2 < vl5 and vl2 < vl6:
    print('\nA Barry Allen é o Vencedor, com Velocidade da Luz =',vl2,'Km/s')

elif vl3 < vl1 and vl3 < vl2 and vl3 < vl4 and vl3 < vl5 and vl3 < vl6:
    print('\nA Wally West é o Vencedor, com Velocidade da Luz =',vl3,'Km/s')

elif vl4 < vl1 and vl4 < vl2 and vl4 < vl3 and vl4 < vl5 and vl4 < vl6:
    print('\nA Dr. Wells é o Vencedor, com Velocidade da Luz =',vl4,'Km/s')

elif vl5 < vl1 and vl5 < vl2 and vl5 < vl3 and vl5 < vl4 and vl5 < vl6:
    print('\nA Jay Garrick é o Vencedor, com Velocidade da Luz =',vl5,'Km/s')

elif vl6 < vl1 and vl6 < vl2 and vl6 < vl3 and vl6 < vl4 and vl6 < vl5:
    print('\nA Max Mercury é o Vencedor, com Velocidade da Luz =',vl6,'Km/s')

else: 
    print('\nErro! Perdemos algumas Aferiçõs de Velocidade... \n Tente Novamente ')