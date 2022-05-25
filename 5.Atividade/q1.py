print('Exercicio 02/05 Erimilson Silva')
print('Q1 - Desenvolvido um sistema de seleção de alunos.')

print ('\n1° Etapa. Prova de Português:')
nota1 = int(input('\nInforma a Nota da Avaliação de Portguês: '))

if nota1 >= 8: 
       
    print ('\n 2° Etapa. Prova de Matemática')
    nota2 = int(input('\nInforma a Nota da Avaliação de Matemática: '))

    if nota2 > 7:
            
        print ('\n 3° Etapa. Avaliação de Poder (0 a 10 ) ')
        poder = int(input('\nInforma a Nota da Avaliação de Poder: ')) 

        if poder == 10:
            print(' Ômega ')

        elif poder < 10 and poder >=8:
            media = (nota1 * 2) + (nota2 * 2) / 2
            print('\nNível alto de Poder')
            print('\nVoçê foi Classificado. Sua média é: ',media,' Parabéns')
        elif poder < 8 and poder > 6:
            media = (nota1 + nota2) / 2
            print('\nNível Médio de Poder')
            print('\nVoçê foi Classificado. Sua média é: ',media,)
        else:
            media = (nota1 + nota2) / 2
            print('\nNível Baixo de Poder')
            print('\nVoçê foi Classificado. Sua média é: ',media)
    else:
        print('\nDesclassificado na 2° Etapa ')
   
else:
    print('\n Desclassificado na 1° Etapa ')