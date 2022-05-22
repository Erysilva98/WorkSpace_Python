from random import randint

print('\nAvaliação - Erimilson Silva')
print('\nQ2 - Sistema para Calcula a situação de Alunos de T.I\n')

aprovado  = 0
recup     = 0
reprovado = 0
mediaTurma = 0
frequencia = 70
maiorNota  = -1
menorNota  = 11
media = 0
cont = 0


for i in range(0,40):
    cont = cont + 1

    nota = randint(0,10)
    faltas = randint(0,100)

    #Calcular Frequência
    chGeral = ((200-faltas)/200)*100

    if nota >= 7:
        if chGeral >= frequencia:
            aprovado = aprovado + 1
            media = media +1
            if nota > maiorNota:
                maiorNota = nota   
        else:
            reprovado = reprovado +1

    elif nota < 4:
        reprovado = reprovado +1
        media = media +1
        if nota < menorNota:
            menorNota = nota

    elif nota >= 4 and nota < 7:
        recup = recup + 1
        media = media +1
        if chGeral < frequencia:
            reprovado = reprovado +1

medTurma = media / cont   

print('Alunos foram Aprovados por média:',aprovado)
print('Alunos foram para recuperação:',recup)
print('Alunos foram Reprovados:',reprovado)
print('A Maior Nota da Turma:',maiorNota)
print('A Menor Nota da Turma:',menorNota)
print('A Média da Turma:',medTurma)