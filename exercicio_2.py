import random

def escolha_com():
    return random.choice(escolhas)

def escolha_player():
    choice = str.lower(input("Escolha pedra, papel ou tesoura. \n"))
    if choice not in escolhas:
        choice = str.lower(input("Essa não [e uma opção. Escolha entre pedra, papel ou tesoura. \n"))
        return choice
    else:
        return choice

def derrota():
    return print("Ponto pra máquina!")

def vitoria():
    return print("Ponto pra você!")

def empate():
    return print("Empate!")

while True:
    escolhas = ["pedra" , "papel" , "tesoura"]
    rounds = 0
    pontos_com = 0
    pontos_player = 0
    while rounds < 4:
        com = escolha_com()
        player = escolha_player()
        if player == com:
            empate()
            rounds = rounds - 1
        elif player == "pedra":
            if com == "papel":
                derrota()
                pontos_com = pontos_com + 1
            elif com == "tesoura":
                vitoria()
                pontos_player = pontos_player + 1
        elif player == "tesoura":
            if com == "papel":
                vitoria()
                pontos_player = pontos_player + 1
            elif com == "pedra":
                derrota()
                pontos_com = pontos_com + 1
        elif player == "papel":
            if com == "pedra":
                vitoria()
                pontos_player = pontos_player + 1
            elif com == "tesoura":
                derrota()
                pontos_com = pontos_com + 1
        rounds = rounds + 1
        if pontos_com == 3:
            print("Você foi derrotado!")
            break
        elif pontos_player == 3:
            print("A vitória é sua!")
            break