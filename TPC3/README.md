TPC3

Inês Martins Azevedo; a113727

<img width="1660" height="2048" alt="foto readme" src="https://github.com/user-attachments/assets/44fdbc63-df0d-4a5a-b942-ddeb21b29e19" />

Resumo: Criar um código capaz de jogar o jogo "Corrida ao 100", com as seguintes condições: Se for o computador a começar o computador tem de ganhar. Se for o jogador a começar tanto o jogador como o computador pode ganhar.

Lista de resultados:

[O computador começa.py](https://github.com/user-attachments/files/32922466/O.computador.comeca.py)

import random

def jodo_do_100():

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

jodo_do_100()


[o jogador começa.py](https://github.com/user-attachments/files/33168039/o.jogador.comeca.py)


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
