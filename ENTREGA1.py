#Escreva um programa que crie uma lista com números aleatórios e a imprima na
#tela


import random

lista = [random.randint(1, 100) for _ in range(10)]
print("Lista aleatória:", lista)

#Uso basico da lista com o uso do import random
