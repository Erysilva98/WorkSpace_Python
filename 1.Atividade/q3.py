print ('\nAtividade 14/03 - Erimilson Silva')
print('\nQ3 - Ajudar o Senhor Wayne a Alugar um Carro.\n')

motor1   = int (295)
motor2   = float (147.5)
consumo1 = int (16)
consumo2 = int (11)
carro1   = int (300)
carro2   = int (500)
aluguel1 = int (300)
aluguel2 = int (500)
gasolina = float (0.75)

print("1 - Modelo Morcego Preto, Wayne vai gasta $:",consumo1 % gasolina, "em gasolina a cada 16Km")

custo1 = ((consumo1 % gasolina) * motor1 )

print("- A viajem á Gotham City, custará $:", custo1,"em gasolina")
print("- Com o aluguel do carro por $:300,00")
print("- Sr. Wayne vai gastar $:", aluguel1 + custo1, "para chegar ao destino com o Modelo 1 \n")


print("2 - Modelo Vampiro Voador, Wayne vai gasta $:",consumo2 % gasolina, "em gasolina a cada 11Km")

custo2 = ((consumo1 % gasolina) * motor2 )

print("- A viajem á Gotham City, custará $:",custo2,"em gasolina")
print("- Com o aluguel do carro por $:500,00")
print("- Sr. Wayne vai gastar $:", aluguel2 + custo2, "para chegar ao destino com o Modelo 2\n")


