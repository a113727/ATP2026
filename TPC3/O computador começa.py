import random

def jogo_do_100():
    soma = 0
    print("Vamos jogar Corrida ao 100!")
    print("REGRAS:Quem somar até atingir 100 ganha. Em cada turno, pode-se somar de 1 a 10.")


    computador = 1
    soma += computador
    print(f"O computador começa e escolhe {computador}")
    print(f"Total atual:{soma}")

    while soma < 100:
        jogador = int(input("Sua vez escolha um número (1 a 10):"))
        if jogador < 1 or jogador > 10:
            print("Número inválido. Tente novamente.")
        else:
            soma += jogador
            print(f"O jogador escolheu {jogador}. Soma total:{soma}")

            if soma < 100:
                computador = 11 - jogador
                soma += computador
            print(f"O computador escolheu {computador}. Soma total:{soma}")

    if computador == (11 - jogador):
        print("O computador atingiu 100. O computador venceu!")   

jogo_do_100()