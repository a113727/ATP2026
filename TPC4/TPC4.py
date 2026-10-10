import random

def mostrarMenu():
    print("\n--- MENU ---")
    print("(1) Criar Lista (Aleatória)")
    print("(2) Ler Lista (Manual)")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

def principal():
    lista = []
    continuar = True
    while continuar:
        mostrarMenu()
        opcao = input("Escolha uma opção:")

        if opcao == '1':
            n = int(input("Quantos elementos quer que a lista tenha?"))
            min_val = int(input("Valor mínimo:"))
            max_val = int(input("Valor máximo:"))
            lista = [random.randint(min_val, max_val) for _ in  range(n)]
            print(f"Lista criada com sucesso: {lista}")

        elif opcao == '2':
            entrada = input("Introduza os números inteiros separados por espaços:")
            lista = [int(x) for x in entrada.split()]
            print(f"Lista guardada com sucesso: {lista}")

        elif opcao in ['3','4','5','6','7','8','9']:
            if not lista:
                print("Aviso: A lista está vazia. Crie ou introduza uma lista (Opção 1 ou 2).")

        if opcao == '3':
            soma = sum(lista)    
            print(f"A soma dos elementos da lista é: {soma}")

        elif opcao == '4':
            media = sum(lista) / len(lista)
            print(f"A média dos elementos da lista é: {media:.2f}")

        elif opcao == '5':
            maior = max(lista)
            print(f"O maior elemento da lista é: {maior}")

        elif opcao == '6':
            menor = min(lista)
            print(f"O menor elemento da lista é: {menor}")

        elif opcao == '7':
            crescente = all(lista[i] <= lista[i+1] for i in range(len(lista) - 1))
            resultado = "Sim" if crescente else "Não"
            print(f"A lista está ordenada por ordem crescente? {resultado}")

        elif opcao == '8':
            decrescente = all(lista[i] >= lista[i+1] for i in range(len(lista) - 1))
            resultado = "Sim" if decrescente else "Não"
            print(f"A lista está ordenada por ordem decrescente? {resultado}")

        elif opcao == '9':
            elem = int(input("Qual é o elemento que deseja procurar?"))
            if elem in lista:
                pos = lista.index(elem)
                print(f"O elemento {elem} foi encontrado na posição {pos}")
            else:
                print("-1 (O elemento não se encontra na lista)")
    
        elif opcao == '0':
            print(f"\nA terminar a aplicação. A lista final guardada é: {lista}")
            continuar = False

    

if __name__ == "__main__":
    principal()