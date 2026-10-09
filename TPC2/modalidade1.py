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