print('Exercicio 02/05 Erimilson Silva')
print('Q10 - Sistema de pesagem da BR232.')

print('\n Tabela de Preço para Caminhões ')

semCarga = float(input('\nPeso do Caminhão sem Carga: '))
comCarga = float(input('Caminhão com Carga: '))

cargaPesada1 = (10/100) * semCarga
cargaPesada2 = (20/100) * semCarga

if cargaPesada1 > cargaPesada2:
    print('\nTaxa de Carga Pesada 10%, Acima do Ideal, valor R$: 10,00 ')
elif cargaPesada2 > cargaPesada1:
    print('\nTaxa de Carga Pesada 20%, Acima do Ideal, valor R$: 20,00 ')
else:
     print('\nCarga Ideal, sem Taxas ')