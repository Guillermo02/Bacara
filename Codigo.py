# EP - Design de Software
# Equipe: Guillermo Kuznietz
# Data: 5/10/2020

#importa a função aleatório
import random

#número de jogadores
n_jogadores = int(input('Quantos jogadores há? '))

#dinheiro dos jogadores
jogadores = [100]*n_jogadores
x = True
#INICIO DO LOOP
while x==True: 
    #Verifica que todos os jogadores estão acima de 0 fichas
    for i in range(0,len(jogadores)):
        if jogadores[i]==0:
            print('O jogador {0} não possui mais fichas'.format(jogadores[i]))
            del jogadores[i]
    
    perg = input('Deseja apostar?(s)(n) ')
    
    if perg == 's':
        #Quantos baralhos sernao utilizados
        baralhos = int(input('Quantos baralhos serão utilizados entre 1, 6 ou 8? '))
        while baralhos != 1 and baralhos != 6 and baralhos != 8:
            baralhos = int(input('Tente novamente, quantos baralhos? 1, 6 ou 8? '))
        
        #cartas do baralho
        cartas = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]*4)*baralhos

        #Aposta e em quem apostou pra cada jogador
        aposta = [0]*n_jogadores
        quem = [0]*n_jogadores
        for n in range(0, n_jogadores):
            print('Jogador {0} possui {1} fichas'.format(n ,jogadores[n]))
            #Cria uma lista comas diferentes apostas
            aposta[n] = int(input('Quanto deseja apostar? '))
            
            #Verifica que o valor da aposta esteja condizente
            while aposta[n] > jogadores[n] or aposta[n] <= 0:
                print('Valor não acessivel, tente novamente')
                aposta[n] = int(input('Quanto deseja apostar? '))
            
            #Cria uma lista com as diferentes escolhas de quem apostar
            quem[n] = input('Em quem deseja apostar? banco(b),jogador(j) ou empate(e) ')

        #Cartas do jogador
        carta_jog1 = random.choice(cartas)
        cartas.remove(carta_jog1) 
        carta_jog2 = random.choice(cartas)
        cartas.remove(carta_jog2)
        #Soma do jogador
        soma_jog = carta_jog1 + carta_jog2
        #Cartas do banco
        carta_ban1 = random.choice(cartas)
        cartas.remove(carta_ban1) 
        carta_ban2 = random.choice(cartas)
        cartas.remove(carta_ban2) 
        #Soma do banco
        soma_ban = carta_ban1 + carta_ban2
        
        #INICIO DO JOGO
        for k in range(0, len(jogadores)):
            #Se soma do jogador der 8 ou 9 
            if soma_jog==8 or soma_jog==9:
                if quem[k] == 'j':
                    jogadores[k] = int(jogadores[k] + aposta[k])
                    print('Parabens jogador {0} você ganhou!!Você possui {1} fichas'.format(k, jogadores[k]))
                else:
                    jogadores[k] = int(jogadores[k] - aposta[k])
                    print('Que pena jogador {0} você perdeu, você possui {1} fichas'.format(k, jogadores[k]))

            #Se soma do banco der 8 ou 9
            elif soma_ban == 8 or soma_ban == 9:
                if quem[k] == 'b':
                    jogadores[k] = int(jogadores[k] + aposta[k])
                    print('Parabens jogador {0} você ganhou!!Você possui {1} fichas'.format(k, jogadores[k]))
                else:
                    jogadores[k] = int(jogadores[k] - aposta[k])
                    print('Que pena jogador {0} você perdeu, você possui {1} fichas'.format(k, jogadores[k]))

            #Se ocorrer um empate
            elif soma_jog == soma_ban:
                if quem[k] == 'e':
                    jogadores[k] = int(jogadores[k] - 8*aposta[k])
                    print('Parabens jogador {0} você ganhou!!Você possui {1} fichas'.format(k, jogadores[k]))
                else:
                    jogadores[k] = int(jogadores[k] - aposta[k])
                    print('Que pena jogador {0} você perdeu, você possui {1} fichas'.format(k, jogadores[k]))

            #Se ambos forem diferente de 8, 9, 18 e a soma do banco ser diferente da soma do jogador
            elif soma_jog!= 8 and soma_jog!= 9 and soma_ban != 8 and soma_ban != 9 and soma_ban!=18 and soma_jog!=18 and soma_ban!=soma_jog:
            
                #Se soma de um for menor ou igual a 5
                if soma_jog <= 5:
                    #Carta extra
                    carta_ex = random.choice(cartas)
                    cartas.remove(carta_ex) 
                    soma_jog += carta_ex
                elif soma_ban <= 5:
                    #Cartas extra 2
                    carta_ex2 = random.choice(cartas)
                    soma_ban += carta_ex2
                
                #Se soma de um for maior ou igual a 10
                #Conta apenas o segundo digito
                elif soma_jog>=10:
                    soma_jog = str(soma_jog)
                    soma_jog = int(soma_jog[1])
                elif soma_ban>=10:
                    soma_ban = str(soma_ban)
                    soma_ban = int(soma_ban[1])

                #Verifica quem é o maior? Resultando na vitória de um, ou, empate
                #Se soma do jogador for maior que do banco
                if soma_jog > soma_ban:
                    if quem[k] == 'j':
                        jogadores[k] = int(jogadores[k] + aposta[k])
                        print('Parabens jogador {0} você ganhou!! Você possui {1} fichas'.format(k, jogadores[k]))
                    else:
                        jogadores[k] = int(jogadores[k] - aposta[k])
                        print('Que pena jogador {0} você perdeu, você possui {1} fichas'.format(k, jogadores[k]))
                            
                #Se soma do banco for maior que do jogador  
                elif soma_jog < soma_ban:
                    if quem[k] == 'b':
                        jogadores[k] = int(jogadores[k] + 0.95*aposta[k])
                        print('Parabens jogador {0} você ganhou!! Você possui {1} fichas'.format(k, jogadores[k]))
                    else:
                        jogadores[k] = int(jogadores[k] - aposta[k])
                        print('Que pena jogador {0} você perdeu, você possui {1} fichas'.format(k, jogadores[k]))
                
                #Se ocorreu um empate  
                elif soma_jog == soma_ban:
                    if quem[k] == 'e':
                        jogadores[k] = int(jogadores[k] + 8*aposta[k])
                        print('Parabens jogador {0} você ganhou!! Você possui {1} fichas'.format(k, jogadores[k]))
                    else:
                        jogadores[k] = int(jogadores[k] - aposta[k])
                        print('Que pena jogador {0} você perdeu, você possui {1} fichas'.format(k, jogadores[k]))
    #Se resposta de 'Deseja apostar' foi não
    else:
        print('Volte sempre!')
        x=False