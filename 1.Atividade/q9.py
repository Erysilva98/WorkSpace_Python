print ('\nAtividade 14/03 - Erimilson Silva')
print('\nQ9 - O programa ler a temperatura da água e informa seu estado.')

tempAgua = int(input('\nInforme a Temperatura da Água em grau Celsius: '))

if tempAgua < 0:
    print('\nTemperatura da Água em',tempAgua,'°C, seu estado é Solido (Gelo)')

elif tempAgua > 0 and tempAgua < 100:
    print('\nTemperatura da Água em',tempAgua,'°C, seu estado é Liquído (Estával')

else:
    print('\nTemperatura da Água em',tempAgua,'°C, seu estado é Gasoso (Gás)')

