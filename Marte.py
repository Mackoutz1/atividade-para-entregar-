# atividade-para-entregar 
distanciaSpace = int(input()) #distancia da terra pra marte no lançamento da spacex
velocidadeSpace = int(input()) #Velocidade da espaçonave da SpaceX em quilômetros por hora (km/h).
T = int(input()) #Tempo passado, em dias, entre o lançamento da SpaceX e Blue Origin.
distanciaBlue = int(input())  #Distância da trajetória, em quilômetros (km), entre a Terra e Marte no lançamento da Blue Origin.
velocidadeBlue = int(input()) #Velocidade da espaçonave da Blue Origin em quilômetros por hora (km/h).


total = distanciaSpace * velocidadeSpace
total2 = distanciaBlue * velocidadeBlue

dias1 = total / 24 
dias2 = total2 / 24 - T


if  dias1 < dias2:
    print("True")
else: 
    print("False")
