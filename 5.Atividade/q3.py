import random

print('Exercicio 02/05 Erimilson Silva')
print('Q3 - O Jogo da Vida, um Jogo de Tabuleiro...')

print(
' 1 - Médico\n'
' 2 - Jornalista\n'
' 3 - Advogado \n'
' 4 - Professor \n'
' 5 - Físico \n'
' 6 - Comerciante\n'
' 7 - Estudante \n'
)
opc = int(input('Escolha Sua Profissão : '))

if opc < 7:
    print('Escolher um dos dois caminhos possíveis para concluir a partida \n')
    plano = int(input('Digite (1) Plano A ou (2) Plano B : '))

    if plano == 1 or plano == 2:
        cont = 0
        valor = 0
        busca = 4
        medico = 50
        jornalista = 24
        advogado = 50
        professor = 24
        fisico = 30
        comerciante = 12
        estudante = 16

        if opc <= busca:
            if opc == 1:
                if plano == 1:
                    for i in range(1,30):
                        cont =+ 1 
                        for y in range(1,10):
                            pag = random.randint(1,10)
                            if cont == pag:
                                valor = valor + (medico/2)
                            else:
                                valor =+ medico
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)

                else: 
                    valor = valor + (medico/2)    
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
            
            elif opc == 2:
                if plano == 1:
                    for i in range(1,30):
                        cont =+ 1 
                        for y in range(1,10):
                            pag = random.randint(1,10)
                            if cont == pag:
                                valor = valor + (jornalista/2)
                            else:
                                valor =+ jornalista
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)

                else: 
                    valor = valor + (jornalista/2)    
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
            
            elif opc == 3:
                if plano == 1:
                    for i in range(1,30):
                        cont =+ 1 
                        for y in range(1,10):
                            pag = random.randint(1,10)
                            if cont == pag:
                                valor = valor + (advogado/2)
                            else:
                                valor =+ advogado
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
                else: 
                    valor = valor + (advogado/2)    
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
            
            elif opc == 4:
                if plano == 1:
                    for i in range(1,30):
                        cont =+ 1 
                        for y in range(1,10):
                            pag = random.randint(1,10)
                            if cont == pag:
                                valor = valor + (professor/2)
                            else:
                                valor =+ professor
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
                else: 
                    valor = valor + (professor/2)    
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)

        elif opc > 4 and opc < 8:
            if opc == 5:
                if plano == 1:
                    for i in range(1,30):
                        cont =+ 1 
                        for y in range(1,10):
                            pag = random.randint(1,10)
                            if cont == pag:
                                valor = valor + (fisico/2)
                            else:
                                valor =+ fisico
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
                else: 
                    valor = valor + (fisico/2)    
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
            
            elif opc == 6:
                if plano == 1:
                    for i in range(1,30):
                        cont =+ 1 
                        for y in range(1,10):
                            pag = random.randint(1,10)
                            if cont == pag:
                                valor = valor + (comerciante/2)
                            else:
                                valor =+ comerciante
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
                else: 
                    valor = valor + (comerciante/2)    
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
            
            elif opc == 7:
                if plano == 1:
                    for i in range(1,30):
                        cont =+ 1 
                        for y in range(1,10):
                            pag = random.randint(1,10)
                            if cont == pag:
                                valor = valor + (estudante/2)
                            else:
                                valor =+ estudante
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
                else: 
                    valor = valor + (estudante/2)    
                    print('Dia Do Pagamento \n')
                    print('Sálario é: ',valor)
            else:
                print()
        
    # Teste de Plano
    else:
        print('\n Opção Invalída! \n')

# Teste de Opção
else:
    print('\n Opção Invalída! \n')

    
    
