from random import randint
from os import system
import time

ARQUIVO_RECORDE = "recorde.txt"

# Cores ANSI
class Cor:
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    RESET = '\033[0m'

def limpar_tela():
    system('cls||clear')

# ---------------- RECORDES ---------------- #

def carregar_recordes():
    try:
        with open(ARQUIVO_RECORDE, "r") as f:
            linhas = f.readlines()
            return sorted([int(x.strip()) for x in linhas if x.strip().isdigit()], reverse=True)[:5]
    except:
        return []

def salvar_recorde(pontos):
    recordes = carregar_recordes()
    recordes.append(pontos)
    recordes = sorted(recordes, reverse=True)[:5]

    with open(ARQUIVO_RECORDE, "w") as f:
        for r in recordes:
            f.write(f"{r}\n")

def mostrar_recordes():
    limpar_tela()
    recordes = carregar_recordes()

    print("🏆 TOP 5 RECORDES\n")

    if not recordes:
        print("Nenhum recorde ainda.")
    else:
        for i, r in enumerate(recordes, 1):
            print(f"{i}º - {Cor.VERDE}{r} pontos{Cor.RESET}")

    input("\nPressione ENTER para voltar...")

# ---------------- DIFICULDADE ---------------- #

def escolher_dificuldade():
    opcoes = {
        "1": ("Fácil", 10),
        "2": ("Normal", 7),
        "3": ("Difícil", 5)
    }

    print(f"\n{Cor.AMARELO}Escolha a dificuldade:{Cor.RESET}")

    for k, v in opcoes.items():
        print(f"{k} - {v[0]} ({v[1]} tentativas)")

    while True:
        escolha = input("Opção: ").strip()

        if escolha in opcoes:
            return opcoes[escolha][1]

        print(f"{Cor.VERMELHO}Escolha inválida.{Cor.RESET}")

# ---------------- DICAS ---------------- #

def mostrar_dica(palpite, numero):
    distancia = abs(palpite - numero)

    if distancia <= 5:
        print(f"{Cor.VERMELHO}🔥 Muito quente!{Cor.RESET}")
    elif distancia <= 10:
        print(f"{Cor.AMARELO}🌡️ Quente!{Cor.RESET}")
    else:
        print("❄️ Frio...")

# ---------------- JOGO ---------------- #

def jogar():

    max_tentativas = escolher_dificuldade()
    tentativas = max_tentativas

    numero_magico = randint(1, 100)

    palpites = []

    min_num = 1
    max_num = 100

    limpar_tela()

    print("🎯 NÚMERO MÁGICO\n")
    print("Pensei em um número entre 1 e 100!")

    while tentativas > 0:

        print(f"\nIntervalo possível: {min_num} - {max_num}")
        print(f"Tentativas: {Cor.VERMELHO}{'❤️ ' * tentativas}{Cor.RESET}")

        if palpites:
            print("Palpites:", palpites)

        entrada = input("Seu palpite: ")

        if not entrada.isdigit():
            print("Digite um número válido.")
            continue

        palpite = int(entrada)

        if palpite in palpites:
            print("⚠️ Você já tentou esse número!")
            continue

        if not (1 <= palpite <= 100):
            print("Digite um número entre 1 e 100.")
            continue

        palpites.append(palpite)

        if palpite == numero_magico:

            pontos = tentativas * 15

            print(f"\n{Cor.VERDE}🎉 ACERTOU!{Cor.RESET}")
            print(f"Pontuação: {pontos}")

            salvar_recorde(pontos)

            return

        if palpite < numero_magico:
            print("🔼 Maior!")
            min_num = max(min_num, palpite + 1)

        else:
            print("🔽 Menor!")
            max_num = min(max_num, palpite - 1)

        mostrar_dica(palpite, numero_magico)

        tentativas -= 1

    print("\n💀 Fim de jogo!")

    print("Revelando número", end="")

    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")

    print(numero_magico)

# ---------------- MENU ---------------- #

def menu():

    while True:

        limpar_tela()

        print("================================")
        print("        🎯 NÚMERO MÁGICO")
        print("================================\n")

        print("1 - Jogar")
        print("2 - Ver Recordes")
        print("3 - Sair")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            jogar()
            input("\nPressione ENTER...")

        elif escolha == "2":
            mostrar_recordes()

        elif escolha == "3":
            break

        else:
            print("Opção inválida.")
            time.sleep(1)

# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    menu()