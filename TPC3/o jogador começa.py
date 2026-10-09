import random

def jogo_do_100():
    soma = 0
    print("Vamos jogar Corrida ao 100!")
    print("REGRAS:Quem somar até atingir 100 ganha. Em cada turno, pode-se somar de 1 a 10.")
    print("Jogador comeca.")

    while soma < 100:
        jogador = int(input("Introduza um número de 1 a 10:"))
        if soma + jogador > 100:
            print(f"Jogada muito alta! Faltam apenas {100-soma} para atingir 100.")
        else:
            soma += jogador
            print(f"O jogador jogou {jogador}. Soma total: {soma}")
            
            if soma == 100:
                print("Parabéns! O jogador ganhou o jogo.")

            else:
                limite_comp = min (10, 100 - soma)
                computador = random.randint(1,limite_comp)
                soma += computador
                print(f"O computador jogou {computador}. Soma total: {soma}")
                
                if soma == 100:
                    print("Parabéns! O computador ganhou o jogo.")
            
jogo_do_100()