from random import randint

print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ7 - De 20 Alunos, quantos foram aprovados. A nota mínima para aprovação é 7.')

aprovados = 0

for i in range(0,3):
    
    media = int(input('\nInforme a Média do Aluno: '))

    if media >= 7:
        aprovados = aprovados + 1


print('\nO número de Alunos Aprovados =',aprovados)