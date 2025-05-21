tabuleiro = [" "]*9

def mostrar_tabuleiro():
    for i in range(0, 9, 3):
        print(tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])
        if i < 6:
            print("--+---+--")

def jogar(jogador):
    pos = int(input(f"Jogador {jogador}, escolha uma posição (0-8): "))
    if tabuleiro[pos] == " ":
        tabuleiro[pos] = jogador
    else:
        print("Posição ocupada. Tente de novo.")
        jogar(jogador)

def verificar_vencedor():
    combinacoes = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for x, y, z in combinacoes:
        if tabuleiro[x] == tabuleiro[y] == tabuleiro[z] != " ":
            return True
    return False

for rodada in range(9):
    mostrar_tabuleiro()
    jogador = "X" if rodada % 2 == 0 else "O"
    jogar(jogador)
    if verificar_vencedor():
        mostrar_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break
else:
    mostrar_tabuleiro()
    print("Empate!")
