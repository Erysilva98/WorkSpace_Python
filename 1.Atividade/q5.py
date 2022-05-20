print ('\nAtividade 14/03 - Erimilson Silva')
print('\nQ5 - Programa para informa o Vencedor da Eleição...')

print("Aldeia de 50 Membros realizou uma eleição. Escolher seu Sexto Hokage \n")
cad1 = int(input (" Quantos votos o Naruto Uzumaki obteve: "))
cad2 = int(input (" Quantos votos o Sakura Haruno obteve: "))
cad3 = int(input (" Quantos votos o Shin Aburame obteve: "))

invalido = int (input ("\nO Número de Brancos ou Nulos: "))

votos = int (cad1+ cad2 + cad3)

if votos <= 50:
    if invalido < votos:
        if cad1 > cad2 and cad1 > cad3:
            print("\n O Novo Hokage é Naruto Uzumaki")
        elif cad2 > cad1 and cad2 > cad3:
            print("\n O Novo Hokage é Sakura Haruno")
        elif cad3 > cad1 and cad3 > cad2:
            print("\n O Novo Hokage é Shin Aburame")
    else:
        print("\nA aldéia está confusa, não decidiu qual será seu novo Hokage")
else:
    print("\nOcorreu uma Fraude na eleição !\n")