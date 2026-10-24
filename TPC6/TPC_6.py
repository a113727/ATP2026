# TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]
    # Data = (Int,Int,Int)
    # TempMin = Float
    # TempMax = Float
    # Precipitacao = Float

#Calcula a temperatura média de cada dia, dando como resultado uma lista de pares: [(data, temperaturaMédia)]:

def medias(tabMeteo):
    res = []
    for x in tabMeteo:
        Data, TempMin,TempMax,*_ = x
        media = (TempMax + TempMin) / 2
        #tem de ter o append se nao  so vai ler o ultimo
        res.append((Data, media))
    return res

#Define uma função para guardar uma tabela meteorológica num ficheiro de texto.

def guardaTabMeteo(t, fnome):
    file = open(fnome,"w")
    for data, tmin, tmax, p in t:
    #for(ano,mes,dia),tmin,tmax,p int:
        ano, mes, dia = data
        file.write(f"{ano}--{mes}--{dia}|{tmin}|{tmax}|{p}\n")    
    file.close()
    return

#Define uma função para carregar uma tabela meteorológica de um ficheiro de texto.

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome,"r")
    for linha in file:
        campos = linha.split("|") #data,tmin,tmax,p=line.split("|")
        d = campos[0].split("--")#ano,mes,dia = data.split("-")
        data = (int(d[0]), int(d[1]), int(d[2]))    
        res.append((data,float(campos[1]),float(campos[2]),float(campos[3])))
        #res.append((int(ano),int(mes),int(dia)),float(tmin),float(tmax),float(p))
    file.close()
    return res

#Calcula a temperatura mínima mais baixa registada na tabela, dando como resultado esse valor:

def minMin(tabMeteo):
    minima = tabMeteo [0][1]
    for x in tabMeteo:
        Data,TempMin,*_ = x
        if TempMin < minima: #posso usar x[1] em vez de TempMin
            minima = TempMin
    return minima

#Calcula a amplitude térmica (diferença entre a temperatura máxima e a temperatura mínima) de cada dia, dando como resultado uma lista de pares: [(data, amplitude)]

def amplTerm(tabMeteo):
    res = []
    for x in tabMeteo:
        Data,TempMin,TempMax,*_ = x
        amplitude = (TempMax - TempMin)
        res.append((Data,amplitude))
    return res 

#Calcula o dia em que a precipitação registada teve o seu valor máximo e indica esse valor, dando como resultado o par (data, valor):

def maxChuva(tabMeteo):
    max_prec = tabMeteo [0][3]
    max_data = tabMeteo [0][0]
    for x in tabMeteo:
        data,TempMin,TempMax,p =x
        if p > max_prec:
            max_prec = p
            max_data = data

    return (max_data, max_prec)

#Define uma função que recebe uma tabela meteorológica e um limite `p` e retorna uma lista de pares [(data, precipitação)] correspondente aos dias em que a precipitação foi superior a `p`.

def diasChuvosos(tabMeteo, p):
    lista =[]
    
    for x in tabMeteo:
        data,TempMin,TempMax,prec =x
        if prec > p:
            lista.append((data,prec))

    return lista

#Define uma função que recebe uma tabela meteorológica e um limite `p` e retorna o maior número consecutivo de dias com precipitação abaixo desse limite.

def maxPeriodoCalor(tabMeteo, p):
    res = 0
    i = 0 #contador
    for x in tabMeteo:
        data,TempMin,TempMax,prec = x
        if prec < p:
            i = i + 1
            if i > res:
                res = i
        else:
            i = 0
    return res

#Define uma função que recebe uma tabela meteorológica e desenha os gráficos da temperatura mínima, máxima e de pluviosidade.

import matplotlib.pyplot as plt
def grafTabMeteo(t):
    y_min = [tmin for data, tmin, *_ in t]
    y_max = [tmax for data, tmin, tmax, *_ in t]
    y_prec = [p for data,tmin,tmax,p in t]
    x =[f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]


    plt.plot(x,y_min, color="red", marker = "o",label = "Temperatura Mínima ºC")
    plt.plot(x,y_max, color="green", marker = "o",label = "Temperatura Máxima ºC")
    plt.title("Tabela Meteorológica")
    plt.xticks(rotation = 45)
    plt.legend()   
    plt.grid()
    plt.show() 

    plt.bar(x,y_prec,color = "c",label = "Precipitação (mm)")
    plt.xticks(rotation = 45)
    plt.grid()
    plt.legend()
    plt.show()
    return

menu = """1) Calcular a temperatura média de cada dia;
2) Guardar tabela meteorológica num ficheiro de texto;
3) Carregar tabela meteorológica de um ficheiro de texto;
4) Calcular a temperatura mínima mais baixa registada na tabela;
5) Calcular a amplitude térmica de cada dia;
6) Calcular o dia em que a precipitação registada teve o seu valor máximo e indicar esse valor;
7) Dias com precipitação superior a um limite escolhido;
8) Maior número de dias consecutivos com precipitação abaixo do limite escolhido;
9) Gráficos da temperatura mínima, máxima e de pluviosidade;
0) Sair da aplicação."""

tabMeteo = []
N = int(input("Quantos dias tem a sua Tabela Meteorológica?"))
while N > 0:
    dia = int(input("Introduza o dia:"))
    mes = int(input("Introduza o mês:"))
    ano = int(input("Introduza o ano:"))
    data = (dia,mes,ano)

    tmin = float(input("Introduza a Temperatura Mínima em ºC:"))
    tmax = float(input("Introduza a Temperatura Máxima em ºC:"))
    prec = float(input("Introduza a Precipitação em mm:"))
    tabMeteo.append((data,tmin,tmax,prec))
    N = N - 1

operacao = -1
while operacao != 0:
    print(menu)
    operacao = int(input("Qual é a operação que deseja realizar? "))
    if operacao == 1:
        print("Temperatura média:", medias(tabMeteo))
    elif operacao == 2:
        fnome = input("Nome do ficheiro para guardar (ex: meteo.txt): ")
        guardaTabMeteo(tabMeteo, fnome)
        print("Tabela guardada com sucesso!")
    elif operacao == 3:
        fnome = input("Nome do ficheiro para carregar: ")
        tabMeteo = carregaTabMeteo(fnome)
        print("Tabela carregada:", tabMeteo)
    elif operacao == 4:
        print("Temperatura mínima mais baixa:", minMin(tabMeteo))
    elif operacao == 5:
        print("Amplitude térmica:", amplTerm(tabMeteo))
    elif operacao == 6:
        print(maxChuva(tabMeteo))
    elif operacao == 7:
        p = float(input("Introduza o limite de precipitação (p): "))
        print("Dias chuvosos:", diasChuvosos(tabMeteo,p))
    elif operacao == 8:
        p = float(input("Introduza o limite de precipitação (p): "))
        print("Maior período de calor consecutivo:", maxPeriodoCalor(tabMeteo,p))
    elif operacao == 9:
        print(grafTabMeteo(tabMeteo))
    elif operacao == 0:
        print("A sair da aplicação. Até breve!")
    else:
        print("Opção inválida. Tente novamente.")


