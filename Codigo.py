# EP - Design de Software
# Equipe: Guillermo Kuznietz
# Data: 5/10/2020

#importa a função aleatório
import random


#dinheiro do jogador
jogador = 100




x = True
while jogador>0 and x==True: 
    #cartas do baralho
    cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
    
    perg = input('Deseja apostar?(s)(n) ')
    if perg == 's':
        print('Você possui {0}'.format(jogador))
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
        print(carta_ex, carta_ex2)
        print(soma_jog, soma_ban)
        print(cartas)
        
        #Se soma do jogador der 8 ou 9 
        if soma_jog==8 or soma_jog==9:
            if quem == 'j':
                print('Parabens você ganhou!!')
                jogador += aposta
            else:
                print('Que pena você perdeu :(')
                jogador -= aposta

        #Se soma do banco der 8 ou 9
        elif soma_ban == 8 or soma_ban == 9:
            if quem == 'b':
                print('Parabens você ganhou!!')
                jogador +=  0.95 * aposta
                print('Você possui {0}'.format(jogador))
            else:
                print('Que pena você perdeu :(')
                jogador -= aposta

        #Se ocorrer um empate
        elif soma_jog == soma_ban:
            if quem == 'e':
                print('Parabens você ganhou!!')
                jogador += 8*aposta
                print('Você possui {0}'.format(jogador))
            else:
                print('Que pena você perdeu :(')
                jogador -= aposta

        #Se ambos forem diferente de 8 ou 9
        elif (soma_jog!= 8 and 9) and (soma_ban != 8 and 9):
            #Cartas extras
            carta_ex = random.choice(cartas)
            cartas.remove(carta_ex) 
            carta_ex2 = random.choice(cartas)
            if soma_jog <= 5:
                soma_jog += carta_ex
            elif soma_ban <= 5:
                soma_ban += carta_ex2
    else:
        print('Volte sempre!')
        x=False