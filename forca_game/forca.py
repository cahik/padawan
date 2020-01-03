from random import shuffle, random



# O jogo deverá sortear uma fruta conforme a lista abaixo:
# - banana
# - jabuticaba
# - pitanga
# - mirtilo
# - morango
# - abacaxi
# - cereja
#
# O objetivo é acertar o nome da fruta. O jogador informa uma letra e o jogo verifica se a fruta tem essa letra.

frutas = ["banana", "jabuticaba", "pitanga", "mirtilo", "morango", "abacaxi", "cereja"]
shuffle(frutas)

palavra = frutas[2]
print("==================== A pista é:  ==========================\n\n Uma fruta com",(len(frutas[2])),"letras")

for x in range(5):
     print()
digitadas = []
acertos = []
erros = 0
while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else "."
     print(senha)
     if senha == palavra:
         print("acertou miseravi! ")
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print("Você já tentou esta letra!")
         continue

     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print("burro!")
     print("X==:==\nX  :   ")
     print("X  O   " if erros >= 1 else "X")
     linha2 = ""
     if erros == 2:
         linha2 = "  |   "
     elif erros == 3:
         linha2 = " \|   "
     elif erros >= 4:
         linha2 = " \|/ "
     print("X%s" % linha2)
     linha3 = ""
     if erros == 5:
         linha3 += " /     "
     elif erros >= 6:
         linha3 += " / \ "
     print("X%s" % linha3)
     print("X\n===========")
     if erros == 6:
         print("Enforcado!kkkkkkk")
         break


