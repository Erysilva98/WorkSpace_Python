import random

print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ6 - O programa que gera Palpites para apostar na mega-sena')

num = int (input('\nInforme o número de Palpites: '))

for i in range(num):

    n1 = random.randint(1,60)
    n2 = random.randint(1,60)

    while n2 == n1:
        n2 = random.randint(1,60)
    
    n3 = random.randint(1,60)      
    while n3 == n1 or n3 == n2:
        n3 = random.randint(1,60)
    
    n4 = random.randint(1,60)       
    while n4 == n1 or n4 == n2 or n4 == n3:
        n4 = random.randint(1,60)

    n5 = random.randint(1,60)
    while n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
        n5 = random.randint(1,60)
    
    n6 = random.randint(1,60)
    while n6 == n1 or n6 == n2 or n6 == n3 or n6 == n4 or n6 == n5:
        n6 = random.randint(1,60)

    if n1 < 10:  n1 = '0'+str(n1)
    if n2 < 10:  n2 = '0'+str(n2)
    if n3 < 10:  n3 = '0'+str(n3)
    if n4 < 10:  n4 = '0'+str(n4)
    if n5 < 10:  n5 = '0'+str(n5)
    if n6 < 10:  n6 = '0'+str(n6)    

    print('Palpite da Mega Sena',i+1,'°',n1,'|',n2,'|',n3,'|',n4,'|',n5,'|',n6)




            


