import random
import os

def limpar_tela():
    os.system("clear")

def exibir_tabuleiro(tabuleiro):
    limpar_tela()
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def verificar_empate(tabuleiro):
    return all(all(c != " " for c in linha) for linha in tabuleiro)

def fazer_jogada_jogador(tabuleiro):
    while True:
        try:
            linha, coluna = map(int, input("Informe a linha e coluna para a sua jogada (exemplo: 1 2): ").split())
            if linha < 1 or linha > 3 or coluna < 1 or coluna > 3:
                print("Por favor, insira valores de linha e coluna entre 1 e 3.")
                continue
            if tabuleiro[linha - 1][coluna - 1] == " ":
                tabuleiro[linha - 1][coluna - 1] = "X"
                return True
            else:
                print("Essa posição já está ocupada. Tente novamente.")
                continue
        except ValueError:
            print("Por favor, insira valores inteiros para linha e coluna.")
            continue

def fazer_jogada_computador(tabuleiro):
    while True:
        linha = random.randint(1, 3)
        coluna = random.randint(1, 3)
        if tabuleiro[linha - 1][coluna - 1] == " ":
            tabuleiro[linha - 1][coluna - 1] = "O"
            return

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    jogador_atual = random.choice(jogadores)
    print("Bem-vindo ao Jogo da Velha!")

    while True:
        exibir_tabuleiro(tabuleiro)
        if jogador_atual == "X":
            if fazer_jogada_jogador(tabuleiro):
                if verificar_vitoria(tabuleiro, "X"):
                    exibir_tabuleiro(tabuleiro)
                    print("Você venceu! Parabéns!")
                    break
                elif verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break
                jogador_atual = "O"
        else:
            fazer_jogada_computador(tabuleiro)
            if verificar_vitoria(tabuleiro, "O"):
                exibir_tabuleiro(tabuleiro)
                print("O computador venceu. Tente novamente.")
                break
            elif verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador_atual = "X"

if __name__ == "__main__":
    jogar_jogo_da_velha()
