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
while jogadores>0 and x==True: 
    #Verifica que todos os jogadores estão acima de 0 fichas
    for i in jogadores:
        if jogadores[i]==0:
            print('O jogador {0} não possui mais fichas'.format(jogadores[i]))
            del jogadores[i]
    
    baralhos = input('Quantos baralhos serão utilizados entre 1, 6 ou 8? ')
    #cartas do baralho
    cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]*baralhos
    
    perg = input('Deseja apostar?(s)(n) ')
    if perg == 's':
        for n in jogadores:
            print('Jogador {0} possui {1} fichas'.format(n ,jogador[n]))
            aposta = int(input('Quanto deseja apostar? '))
        while aposta > jogador or aposta < 0:
            print('Valor não acessivel, tente novamente')
            aposta = int(input('Quanto deseja apostar? '))
        quem = input('Em quem deseja apostar? banco(b),jogador(j) ou empate(e) ')
        
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
        print(cartas)
        
        #Se soma do jogador der 8 ou 9 
        if soma_jog==8 or soma_jog==9:
            if quem == 'j':
                print('Parabens você ganhou!!')
                jogador += aposta
                print('Você possui {0}'.format(jogador))
            else:
                print('Que pena você perdeu :(')
                jogador -= aposta
                print('Você possui {0}'.format(jogador))

        #Se soma do banco der 8 ou 9
        elif soma_ban == 8 or soma_ban == 9:
            if quem == 'b':
                print('Parabens você ganhou!!')
                jogador +=  0.95 * aposta
                print('Você possui {0}'.format(jogador))
            else:
                print('Que pena você perdeu :(')
                jogador -= aposta
                print('Você possui {0}'.format(jogador))

        #Se ocorrer um empate
        elif soma_jog == soma_ban:
            if quem == 'e':
                print('Parabens você ganhou!!')
                jogador += 8*aposta
                print('Você possui {0}'.format(jogador))
            else:
                print('Que pena você perdeu :(')
                jogador -= aposta
                print('Você possui {0}'.format(jogador))

        #Se ambos forem diferente de 8 ou 9
        elif (soma_jog!= 8 and 9) and (soma_ban != 8 and 9):
            #Cartas extras
            if soma_jog <= 5:
                carta_ex = random.choice(cartas)
                cartas.remove(carta_ex) 
                soma_jog += carta_ex
                print(carta_ex)
            elif soma_ban <= 5:
                carta_ex2 = random.choice(cartas)
                soma_ban += carta_ex2
                print(carta_ex2)
            
            elif soma_jog>=10:
                soma_jog = soma_jog[1]
                print(soma_jog)
            elif soma_ban>=10:
                soma_ban = soma_ban[1]
                print(soma_ban)

    else:
        print('Volte sempre!')
        x=False