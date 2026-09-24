TPC2

Inês Martins Azevedo, a113727

<img width="1660" height="2048" alt="foto readme" src="https://github.com/user-attachments/assets/0ec1a5d6-69e2-4db5-bb30-f7a83f349237" />

Resumo: Criar um programa em Python para jogar o jogo "Adivinha o número": O jogo pode ter 2 modalidades: computador pensa num número (entre 0 e 100), utilizador tenta adivinhar; ou, o utilizador pensa num número (entre 0 e 100) e o computador tenta adivinhar;


Lista de resultados:

[modalidade1.py](https://github.com/user-attachments/files/32629057/modalidade1.py)
import random
def utilizador_adivinha():
    print("Modalidade 1: Tenta adivinhar o número do computador!")
    número_secreto = random.randint(0, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = int(input("Introduza o seu palpite (0 a 100) :"))
        tentativas += 1

        if palpite == número_secreto:
            print("Acertou!")
            acertou = True
        elif palpite < número_secreto:
            print("O número que pensei é maior!")
        else:
            print("O número que pensei é menor!")
    print(f"Parabéns! Descubriu o número em {tentativas} tentativa(s)!")    

utilizador_adivinha()  

[modalidade2.py](https://github.com/user-attachments/files/32629060/modalidade2.py)
def computador_adivinha():
    print("Modalidade 2: Pensa num número entre 0 e 100!")
    input("Pensa num número e pressiona ENTER quando estiveres pronto...")

    limite_inferior = 0
    limite_superior = 100
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = (limite_inferior + limite_superior) // 2
        tentativas += 1

        print(f"O computador acha que é: {palpite}")
        print("Responda com:")
        print(" 1 -  Acertou")
        print(" 2 - O número que pensei é maior.")
        print(" 3 - O número que pensei é menor.")

        resposta = input("A sua resposta (1, 2 ou 3):")

        if resposta == "1":
            print("Acertou!")
            acertou = True
        elif resposta == "2":
            limite_inferior = palpite + 1
        elif resposta == "3":
            limite_superior = palpite - 1
        else:
            print("Opção inválida! Tente novamente.")
            tentativas -= 1

    print(f"O computador descubriu o número em {tentativas} tentativa(s)!")        

computador_adivinha()    
