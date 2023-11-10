import random

escolhas = ("pedra", "papel", "tesoura")
escolha_com = random.choice(escolhas)
escolha_player = str.lower(input("Escolha pedra, papel ou tesoura. \n"))
pontos_player = 0
pontos_com = 0
rounds = 0

while rounds <= 4:
    if escolha_player == "pedra" and escolha_com == "tesoura":
        pontos_player = pontos_player + 1
        print("Você venceu!")
    elif escolha_player == "tesoura" and escolha_com == "papel":
        pontos_player = pontos_player + 1
        print("Você venceu!")
    elif escolha_player == "papel" and escolha_com == "pedra":
        pontos_player = pontos_player + 1
        print("Você venceu!")
    elif escolha_player == escolha_com:
        print("Empate!")
        rounds = rounds - 1
    else:
        pontos_com = pontos_com + 1
        print ("Você perdeu!")

    rounds = rounds + 1
    if pontos_player == 3:
        print("As máquinas não chegam aos seus pés.")
        break
    elif pontos_com == 3:
        print("As máquinas venceram, a humanidade perdeu e a culpa é sua. Fracote!")
        break
    else:
        escolha_player = str.lower(input("Escolha novamente. \n"))
        escolha_com = random.choice(escolhas)