import random


def criaLista(N):
    lista = []
    i = 0
    while i < N:
        n = random.randint(1, 100)
        lista.append(n)
        i = i + 1
    return lista


def LeLista(L):
    lista = []
    for i in range(1, L + 1):
        num = int(input("Introduza um número: "))
        lista.append(num)
    return lista


def somaLista(lista):
    soma = 0
    for e in lista:
        soma = soma + e
    return soma


def mediaLista(lista):
    soma = 0
    i = 0
    if len(lista) == 0:
        media = 0
    else:
        for e in lista:
            soma = soma + e
            i = i + 1
        media = soma / i
    return media


def maiorLista(lista):
    maior = lista[0]
    for e in lista:
        if e > maior:
            maior = e
    return maior


def menorLista(lista):
    menor = lista[0]
    for e in lista:
        if e < menor:
            menor = e
    return menor


def crescente(lista):
    i = 0
    res = "Sim!"
    while i < (len(lista) - 1) and res:
        if lista[i] > lista[i + 1]:
            res = "Não!"
        i = i + 1
    return res


def decrescente(lista):
    i = 0
    res = "Sim!"
    while i < (len(lista) - 1) and res:
        if lista[i] < lista[i + 1]:
            res = "Não!"
        i = i + 1
    return res


def posicao(lista, elem):
    encontrei = False
    i = 0
    res = -1
    while i < len(lista) and not encontrei:
        if lista[i] == elem:
            encontrei = True
            res = i
        i = i + 1
    return res


menu_msg = """Escolha um número e será direcionado para essa operação:
(1) Criar Lista
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) estaOrdenada por ordem crescente
(8) estaOrdenada por ordem decrescente
(9) Procura um elemento
(0) Sair
Opção: """

lista = []

n = int(input(menu_msg))

while n != 0:
    if n == 1:
        N = int(input("Por quantos números deseja que a sua lista seja composta? "))
        lista = criaLista(N)
        print(lista)
    elif n == 2:
        L = int(input("Por quantos números deseja que a sua lista seja composta? "))
        lista = LeLista(L)
        print(lista)
    elif n == 3:
        print(somaLista(lista))
    elif n == 4:
        print(mediaLista(lista))
    elif n == 5:
        print(maiorLista(lista))
    elif n == 6:
        print(menorLista(lista))
    elif n == 7:
        print(crescente(lista))
    elif n == 8:
        print(decrescente(lista))
    elif n == 9:
        elem = int(input("Qual elemento deseja procurar na lista? "))
        print(posicao(lista, elem))
    else:
        print("ERRO! Número inválido")

    n = int(input(menu_msg))

print(f"A aplicação terminou, a sua lista é: {lista}")