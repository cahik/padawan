from random import shuffle, random
# from blackjack.servicos import *

baralho = [{"Nome":2, "Valor":2},{"Nome":3, "Valor":3},{"Nome":4, "Valor":4},{"Nome":5, "Valor":5},{"Nome":6, "Valor":6},
            {"Nome":7, "Valor":7},{"Nome":8, "Valor":8},{"Nome":9, "Valor":9}, {"Nome":10, "Valor":10},
            {"Nome":"J", "Valor":10},{"Nome":"Q", "Valor":10},{"Nome":"K", "Valor":10}, {"Nome":"A", "Valor":1}]


def player():
    print( "Are you ready? so")
    nome = input("type your name here: ")
    return nome



def embaralhar():
    nome = player()
    print("\n------------------------------------------------------\n")
    shuffle(baralho)
    if baralho[0]["Nome"] != "A":
        card1 = baralho[0]["Valor"]
        print("That's your first card:", card1)
    else:
        card1 = 11
        print("That's your first card:", card1)

    card2 = baralho[5]["Valor"]
    print("That's your second card:", card2)


    card3 = baralho[4]["Valor"]
    print("That's your third card:", card3)

    result = (card1 + card2 + card3)


    if result < 21:
        card4 = baralho[2]["Valor"]
        print("That's your last card:",card4)

    print("\n------------------------------------------------------\n")

    if result != 21:
        print(f'{nome} u r a loser')
    else:
        print(f'{nome},  u r a winner')

embaralhar()

