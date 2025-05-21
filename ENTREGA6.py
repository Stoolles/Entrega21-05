pares = [x for x in range(1, 11) if x % 2 == 0]
impares = [x for x in range(1, 11) if x % 2 != 0]
junta = pares + impares
print("Lista unida:", junta)
