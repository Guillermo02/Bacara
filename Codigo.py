# EP - Design de Software
# Equipe: Guillermo Kuznietz
# Data: 5/10/2020

#importa a função aleatório
import random

#número de jogadores
n_jogadores = int(input('Quantos jogadores há? '))

x = True
while x==True: 
    #dinheiro dos jogadores
    jogadores = [100]*n_jogadores
    #Verifica que todos os jogadores estão acima de 0 fichas
    for i in range(0,len(jogadores)):
        if jogadores[i]==0:
            print('O jogador {0} não possui mais fichas'.format(jogadores[i]))
            del jogadores[i]
    
    baralhos = int(input('Quantos baralhos serão utilizados entre 1, 6 ou 8? '))
    #cartas do baralho
    cartas = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]*4)*baralhos
    
    perg = input('Deseja apostar?(s)(n) ')
    if perg == 's':
        aposta = [0]*n_jogadores
        quem = [0]*n_jogadores
        for n in range(0, n_jogadores):
            print('Jogador {0} possui {1} fichas'.format(n+1 ,jogadores[n]))
            #Cria uma lista comas diferentes apostas
            aposta[n] = int(input('Quanto deseja apostar? '))
            
            #Verifica que o valor da aposta esteja condizente
            while aposta[n] > jogadores[n] or aposta[n] < 0:
                print('Valor não acessivel, tente novamente')
                aposta[n] = int(input('Quanto deseja apostar? '))
            
            #Cria uma lista com as diferentes escolhas de quem apostar
            quem[n] = input('Em quem deseja apostar? banco(b),jogador(j) ou empate(e) ')

        print(aposta)
        print(quem)
        #Cartas do jogador
        carta_jog1 = random.choice(cartas)
        cartas.remove(carta_jog1) 
        carta_jog2 = random.choice(cartas)
        cartas.remove(carta_jog2)
        #Soma jogador
        soma_jog = carta_jog1 + carta_jog2
        #Cartas do banco
        carta_ban1 = random.choice(cartas)
        cartas.remove(carta_ban1) 
        carta_ban2 = random.choice(cartas)
        cartas.remove(carta_ban2) 
        #Soma banco
        soma_ban = carta_ban1 + carta_ban2
        

        print(carta_jog1, carta_jog2, carta_ban1, carta_ban2)
        print(soma_jog, soma_ban)
        
        #Se soma do jogador der 8 ou 9 
        for k in range(0, n_jogadores):
            if soma_jog==8 or soma_jog==9:
                if quem[k] == 'j':
                    print('Parabens jogador {0} ganhou!!'.format(k+1)
                    novo_valor = jogadores[k] + aposta [k]
                    print('Jogador {0} possui {1} fichas'.format(k+1, jogadores[k]))
                else:
                    print('Que pena jogador {0} perdeu :('.format(k+1))
                    jogadores[k] -= aposta[k]
                    print('Jogador {0} possui {1} fichas'.format(k+1, jogadores[k]))

            #Se soma do banco der 8 ou 9
            elif soma_ban == 8 or soma_ban == 9:
                if quem[k] == 'b':
                    print('Parabens jogador {0} ganhou!!'.format(k+1)
                    jogadores[k] +=  0.95 * aposta[k]
                    print('Jogador {0} possui {1} fichas'.format(k+1, jogadores[k]))
                else:
                    print('Que pena jogador {0} perdeu :('.format(k+1))
                    jogadores[k] -= aposta[k]
                    print('Jogador {0} possui {1} fichas'.format(k+1, jogadores[k]))

            #Se ocorrer um empate
            elif soma_jog == soma_ban:
                if quem[k] == 'e':
                    print('Parabens jogador {0} ganhou!!'.format(k+1))
                    jogadores[k] += 8*aposta[k]
                    print('Jogador {0} possui {1} fichas'.format(k+1, jogadores[k]))
                else:
                    print('Que pena jogador {0} perdeu :('.format(k+1))
                    jogadores[k] -= aposta[k]
                    print('Jogador {0} possui {1}'.format(k+1, jogadores[k]))

        #Se ambos forem diferente de 8 ou 9
        elif (soma_jog!= 8 and 9) and (soma_ban != 8 and 9):
            
            #Se soma de um for menor ou igual a 5
            if soma_jog <= 5:
                #Carta extras
                carta_ex = random.choice(cartas)
                cartas.remove(carta_ex) 
                soma_jog += carta_ex
            elif soma_ban <= 5:
                #Cartas extra 2
                carta_ex2 = random.choice(cartas)
                soma_ban += carta_ex2
            
            #Se soma de um for maior ou igual a 10
            elif soma_jog>=10:
                soma_jog = soma_jog[1]
            elif soma_ban>=10:
                soma_ban = soma_ban[1]

            for m in range(0, n_jogadores):
                #Verifica quem é o maior, resultando na vitória deste, ou, empate
                elif soma_jog > soma_ban:
                    if quem[m] == 'j':
                        jogadores[m] += aposta[m]
                    else:
                        jogadores[m] -= aposta[m]
                
                elif soma_ban > soma_jog:
                    if quem[m] == 'b':
                        jogadores[m] += 0.95*aposta[m]
                    else:
                        jogadores[m] -= aposta[m]
                
                elif soma_jog == soma_ban:
                    if quem[m] == 'e':
                        jogadores[m] += 8*aposta[m]
                    else:
                        jogadores[m] -= aposta[m]
    else:
        print('Volte sempre!')
        x=False