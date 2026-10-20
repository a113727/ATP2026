
def criarTurma():
    turma = []
    print("Turma criada com sucesso")
    return turma

def inserirAluno(turma):
    nome_aluno = input("Introduza o nome do aluno:")
    id_aluno = int(input("Introduza o ID do aluno:"))
    nota_tpc = float(input("Nota TPC:"))
    nota_proj = float(input("Nota Projeto:"))
    nota_teste = float(input("Nota Teste:"))

    aluno = (nome_aluno, id_aluno, nota_tpc, nota_proj, nota_teste)
    turma.append(aluno)
    print(f"Aluno {nome_aluno} inserido com sucesso")

    return turma

def listarTurma(turma):
    print("\n--- Lista da Turma ---")
    if len(turma) == 0:
        print("A turma está vazia.")
    else:
       for aluno in turma:
            nome_aluno, id_aluno, nota_tpc, nota_proj, nota_teste = aluno
            print(f"ID: {id_aluno} | Nome: {nome_aluno} | TPC: {nota_tpc} | Projeto: {nota_proj} | Teste: {nota_teste}")

def consultarAluno(turma):

    if len(turma) == 0:
        print("A turma está vazia.")
    else:
        id_procurado = int(input("Introduza o ID do aluno que pretende consultar: "))
        encontrado = False
        
        for aluno in turma:
            nome_aluno, id_aluno, nota_tpc, nota_proj, nota_teste = aluno
            if id_aluno == id_procurado:
                print(f"\n--- Aluno Encontrado ---")
                print(f"Nome  : {nome_aluno}")
                print(f"ID    : {id_aluno}")
                print(f"Notas : TPC = {nota_tpc}, Projeto = {nota_proj}, Teste = {nota_teste}")
                encontrado = True
                
        if not encontrado:
            print(f"Não existe nenhum aluno com o ID '{id_procurado}'.")

def guardarTurma(turma,fnome):
    file = open(fnome, "w")
    for aluno in turma:
        nome_aluno, id_aluno, nota_tpc, nota_proj, nota_teste = aluno
        file.write(f"{nome_aluno}::{id_aluno}::{nota_tpc}::{nota_proj}::{nota_teste}\n")
    file.close()
    print(f"Turma guardada com sucesso em '{fnome}'!")

def carregarTurma(fnome):
    turma = []
    file = open(fnome, "r")
    for linha in file:
        if linha != "\n":
            linha_sem_n = linha[:-1]

            partes = linha_sem_n.split("::")
            nome_aluno = partes[0]
            id_aluno = partes[1]
            nota_tpc = float(partes[2])
            nota_proj = float(partes[3])
            nota_teste = float(partes[4])

            aluno = (nome_aluno, id_aluno, nota_tpc, nota_proj, nota_teste)
            turma.append(aluno)
    file.close()
    print(f"Turma carregada com sucesso de '{fnome}'!")
    return turma


turma = []
opcao = ""

while opcao != "0":
    print("\n--- MENU DE GESTÃO DE TURMA ---")
    print("1: Criar uma turma")
    print("2: Inserir um aluno na turma")
    print("3: Listar a turma")
    print("4: Consultar um aluno por id")
    print("8: Guardar a turma em ficheiro")
    print("9: Carregar uma turma dum ficheiro")
    print("0: Sair da aplicação")

    opcao = input("\nSelecione uma opção: ")

    if opcao == "1":
        turma = criarTurma()
    elif opcao == "2":
        inserirAluno(turma)
    elif opcao == "3":
        listarTurma(turma)
    elif opcao == "4":
        consultarAluno(turma)
    elif opcao == "8":
        fnome = input("Nome do ficheiro para guardar (ex: turma.txt): ")
        guardarTurma(turma, fnome)
    elif opcao == "9":
        fnome = input("Nome do ficheiro para carregar (ex: turma.txt): ")
        turma = carregarTurma(fnome)
    elif opcao == "0":
        print("A sair da aplicação. Até breve!")
    else:
        print("Opção inválida! Tente novamente.")
    



