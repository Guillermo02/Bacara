# EP - Design de Software
# Equipe: Guillermo Kuznietz
# Data: 5/10/2020

#importa a função aleatório
from random import randint

#cartas do baralho
A=1
J=0
Q=0
K=0
cartas = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]*4
jogador = 100
perg = input('Deseja apostar?(s)(n) ')

while jogador>0 and perg=='s': 
    #pontos de inicio do jogador
    jogador = 100
    if perg == 's':
        aposta = int(input('Quanto deseja apostar? '))
        if aposta > jogador:
            print('Valor acima do que possui, tente novamente')
            aposta = int(input('Quanto deseja apostar? '))
        quem = input('Em quem deseja apostar? banco(b),jogador(j) ou empate(e) ')
    
    #carta1_jog = random.randint(cartas)
    #carta2_jog = random.randint(cartas)