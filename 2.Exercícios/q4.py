print ('\nExercícios 08/06 - Erimilson Silva')
print('\nQ4 - Ler, Nome, Idade e Sexo. Informa a Mulher Mais Velha e Idade do Homem mais Novo.')

nomeHomem = ' '
nomeMulher = ' '
maiorIdade = 150
menorIdade = -1
continua = True

while continua:  
    nome = (input('\nDigite seu Nome: '))
    sexo = int(input('Qual seu sexo, ( 1 ) - Masculino ( 2 ) - Feminino: '))
    idade = int(input('Informe sua Idade: '))

    if sexo == 1:
       if idade < maiorIdade:
           maiorIdade = idade
           nomeHomem = nome

    elif sexo == 2:
        if idade > menorIdade:
            menorIdade = idade
            nomeMulher = nome
    else:
        print('\nOpção de Sexo Incorreta! ')
    opc = int(input('\nDeseja Registrar uma Nova Pessoa: SIM (1) ou NÃO (2): '))
    if opc == 1:
       continua = True
    else:
        continua = False

print('\nO',nomeHomem,'é o Homem mais Jovem, Idade',maiorIdade,'Anos')
print('\nA',nomeMulher,'é a Mulher com Maior, Idade',menorIdade,'Anos')