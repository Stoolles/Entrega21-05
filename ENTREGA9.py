import random

import string
alfabeto = list(string.ascii_lowercase)
random.shuffle(alfabeto)

letra = input("Adivinhe a posição da letra 'e' (0 a 25): ")
if alfabeto[int(letra)] == 'e':
    print("Acertou!")
else:
    print("Errou. A letra 'e' está na posição:", alfabeto.index('e'))
