# "contagem regressiva"
# import time
#
# for c in range(10, 0, -1):
#     time.sleep(1)
#     print(c)
# print("feliz 2020!! : D")
##############################################


# "aparecer apenas os pares desse intervalo"
# for c in range(2, 51, 2):
#     print(c)
###############################################


# "aparecer apenas os ímpares e depois somar apenas os que dividem por 3"
# list = []
# for c in range(1, 501, 2):
#     if c % 3 == 0:
#         list.append(c)
# print(list)
# print(sum(list))

##################################################################

#"tabuada usando o for"
# n = int(input("Escolha um numero para a tabuada: "))
#
# for c in range (1, 10):
#     tabuada = n * c
#     print(tabuada)
####################################################################
#separar apenas os numeros pares gigitados. mostar a soma deles
# list = []
# for c in range(0,3):
#    n = int(input("Digite um número:"))
#    if n % 2 == 0:
#         list.append(n)
# print("aqui apenas os numeros pares:", list)
# print("aqui a soma deles:")
# print(sum(list))
######################################################################

#desenvolva um programa que leia o primeiro termo e a razao de uma PA
#No final mostre os 10 primeiros termos dessa progressao.

# list =[]
# i = int(input("Digite o primeiro numero:"))
#
# r = int(input("Digite o intervalo(razao):"))

# for c  in range(10):
#     i += r
#     list.append(i)
# print(list)
###usando while#########
# list =[]
# i = int(input("Digite o primeiro numero:"))
#
# r = int(input("Digite o intervalo(razao):"))
# contador = 10
#
# while contador != 0:
#     i += r
#     list.append(i)
#     contador -= 1
# print(list)
##########################################################################
#ler um numero e verificar se ele é primo
# num = int(input("digite um numero:"))
# tot = 0
#
# for c in range(1, num +1):
#     if num % c == 0:
#       print('\033[33m', end='')
#       tot += 1
#     else:
#       print('\033[31m', end='')
#     print('{}'.format(c), end='')
# print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
# if tot == 2:
#    print('E por isso ele é primo!')
# else:
#    print('E por isso ele nao é primo!')
#########################################################
#verificando polimodros
# while True:
#     word = input("Digite uma palavra/frase: ")
#     word = word.split()
#     if word[::-1] == word:
#         print("isso é o mesmo detrasprafrente pequeno gafanhoto")
#     else:
#         print("error")

###########################################################
#        estrultura de repeticao while
###########################################################
#Definindo um sexo
# i = ["M", "F"]
# c = []
# while c != i[0] and c != i[1]:
#     c = input("digite seu sexo[M|F]: ").upper()
#     if c != i[0] and c != i[1] :
#         print("digite uma opcao valida!")
#     if c == "M":
#         print("masculino")
#     if c == "F":
#         print("feminino")
# else:
#     print("sexo definido!")
#

###############################################################################
# adivinhar um numero de 0 a 10 e mostrar o numero de tentativas ate o acerto.
# from random import shuffle
# list = []
# contagem = 0
# for x in range(0, 11):
#  list.append(x)
#  shuffle(list)
# n = list[5]
# i = []
# while i != n:
#     i = int(input("tente adivinhar um número de 0 a 10:"))
#     contagem = contagem + 1
#     if i == n:
#         print(i,"   Acertou miseravi!")
#         print("número de tentativas:", contagem)
##########################################################################
#MENU DE OPCOES DE CÁLCULOS E OUTROS

# def inputs():
#     x = int(input("digite um valor: "))
#     y = int(input("digite outro valor: "))
#     return [x, y]
#
# def soma():
#     num = inputs()
#     print(num[0] + num[1])
#     print("="*100)
#
# def multiplicar():
#     num = inputs()
#     print(num[0] * num[1])
#     print("=" * 100)
#
# def maior():
#     num = inputs()
#     x = num[0]
#     y = num[1]
#     if x > y:
#         print(x)
#         print("=" * 100)
#     else:
#         print(y)
#         print("=" * 100)
# def novos_numeros():
#     pass
#
#
#
# while True:
#     print("MENU:\n1-somar \n2-multiplicar \n3-maior(mostrar o maior numero) \n4-novos números \n5-sair do programa\n")
#     escolha = int(input("escolha uma opcao acima:"))
#
#     if escolha == 1:
#        soma()
#     if escolha == 2:
#        multiplicar()
#     if escolha == 3:
#         maior()
#     if escolha == 4:
#         print("=" * 100)
#         novos_numeros()
#     elif escolha == 5:
#         break
############################################################################
# mostrando o fatorial de um número
# x = int(input("digite um número para mostrar o seu fatorial:"))
# total = x
# for c in range(x-1, 0, -1):
#     total = total * c
# print(total)
##     mesma coisa usando while
# x = int(input("digite um numero :"))
# contador = x-1
# total = x
# while contador != 0:
#     total = total * contador
#     contador -= 1
# print(total)

#############################################################################
# Vou tentar explicar.
#Analisando o ciclo
# list = []
# a = 0
# b = 1
# while (b < 100):
#
#     list.append(b)
#
#     a,b=b,a+b
# print(list)
# a=b ("a" passa valer 1),
# mas b = a+b (nesse ponto "a" ainda vale ZERO porque a atribuição é feita na mesma linha)
# então
# b = a + b ou seja b(vale 1) = a(vale 0) + b(vale 1), o resultado é um.

# Quando a atribuição é sequente:
# a = b (a já vale 1)
# b = a(vale 1) + b(vale 1) Resultado é 2.
###############################################################################


