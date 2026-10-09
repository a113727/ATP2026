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