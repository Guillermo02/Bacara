# EP - Design de Software
# Equipe: Guillermo Kuznietz
# Data: 5/10/2020

#importa a função aleatório
import random

#cartas do baralho
cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0, 0]*4
#dinheiro do jogador
jogador = 100


carta_jog1 = random(cartas)
carta_jog2 = random(0, len(cartas)-carta_jog1)
soma_jog = carta_jog1 + carta_jog2
carta_ban1 = random.randint(0, len(cartas)-carta_jog1-carta_jog2)
carta_ban2 = random.randint(0, len(cartas)-carta_jog1-carta_jog2-carta_ban1)
soma_ban = carta_ban1 + carta_ban2

carta_ex = random.randint(0, len(cartas)-carta_jog1-carta_jog2-carta_ban1-carta_ban2)
carta_ex2 = random.randint(0, len(cartas)-carta_jog1-carta_jog2-carta_ban1-carta_ban2-carta_ex)



if (soma_jog!= 8 and 9) and (soma_ban != 8 and 9):
    if soma_jog <= 5:
        soma_jog += carta_ex
    elif soma_ban <= 5:
        soma_ban += carta_ex2

x = True
while jogador>0 and x==True: 
    #pontos de inicio do jogador
    jogador = 100

    perg = input('Deseja apostar?(s)(n) ')
    if perg == 's':
        aposta = int(input('Quanto deseja apostar? '))
        while aposta > jogador or aposta < 0:
            print('Valor acima do que possui, tente novamente')
            aposta = int(input('Quanto deseja apostar? '))
        quem = input('Em quem deseja apostar? banco(b),jogador(j) ou empate(e) ')

        #Se soma do jogador der 8 ou 9 
        if soma_jog==8 or soma_jog==9:
            if quem == 'j':
                jogador += aposta
            else:
                jogador -= 0.05 * aposta

        #Se soma do banco der 8 ou 9
        elif soma_ban == 8 or soma_ban == 9:
            if quem == 'b':
                jogador += aposta
            else:
                jogador -= 0.05 * aposta

        #Se ocorrer um empate
        elif soma_jog == soma_ban:
            if quem == 'e':
                jogador += 8*aposta
            else:
                jogador -= 0.05 * aposta

    else:
        x=False