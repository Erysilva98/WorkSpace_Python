print('Exercicio 02/05 Erimilson Silva')
print('Q14 - Ler o nome completo de uma pessoa. Exiba o primeiro e o último nome lido.')

velho = 0
jovem = 150
homemJovem = ' '
homemVelho = ' '
media = 0
cont = 0

continua = True

while continua:  
    nome = (input('\nDigite seu Nome: '))
    sexo = int(input('Qual seu sexo, ( 1 ) - Masculino ( 2 ) - Feminino: '))
    idade = int(input('Informe sua Idade: '))

    if sexo == 1:
        if idade > velho:
            velho = idade
            homemVelho = nome 
        else:
            jovem = idade
            homemJovem = nome

    elif sexo == 2:
        if idade >= 18:
            cont = cont + 1
            media = idade
    else:
        print('\nOpção de Sexo Incorreta! ')
    opc = int(input('\nDeseja Registrar uma Nova Pessoa: SIM (1) ou NÃO (2): '))
    if opc == 1:
       continua = True
    else:
        continua = False

media = media / cont

print('\nO',homemJovem,'é o Homem mais Jovem, Idade',jovem,'Anos')
print('\nO',homemVelho,'é o Homem mais Velho, Idade',velho,'Anos')
print('\nA média das Mulher com Maior é',media)
