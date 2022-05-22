print('Avaliação - Erimilson Silva')
print('Q1 - O sistema de compra e forma de pagamento.')

valor = float(input('Informe o Valor da Compra ex(0.00): '))
print('Forma de Pagamento:\n'
'    1- A vista\n'
'    2- Em 30 Dias\n'
'    3- Em 60 Dias')
opc = int(input('Digite: '))

if opc == 1:
    desc = (5/100) * valor
    pagar = valor - desc
    print('\n   Parabéns Você Recebeu 5%'' de Desconto')
    print('   Valor a Pagar R$:',pagar)
elif opc == 2:
    pagar = valor
    print('\n   Valor a Pagar R$:',pagar)
elif opc == 3:
    acrs = (15/100) * valor
    pagar = valor + acrs
    print('\n   Valor a Pagar R$:',pagar)
else:
    print('\n   Opção Invalida')