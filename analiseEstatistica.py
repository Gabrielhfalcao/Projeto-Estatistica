
import statistics
import sys
import os

listaDeDados = []

os.system('cls')
def povoarLista(lista):
    os.system('cls')
    x = int(input("Digite o tamanho da lista de dados a ser analisáda: "))
    print("")

    indice = 0
    while (indice < x):
        lista.append(int(input("Digite o " + str(indice + 1) + "º elemento: "))) 
        indice += 1

    listaDeDados.sort()
    os.system('cls')
    menuPrincipal()

def menuPrincipal():
    os.system('cls')  
    print()
    print("---------Menu Principal---------")
    print("Lista de dados: " + str(listaDeDados))
    print("Digite o número relativo a operação que deseja realizar: ")
    print("1 --> Média Aritmética")
    print("2 --> Média Ponderada")
    print("3 --> Moda")
    print("4 --> Mediana")
    print("5 --> Digitar lista de dados novamente")
    print("6 --> Sair do Programa")

    x = int(input())
    if x == 1:
        print()
        print("Lista de dados: " + str(listaDeDados)) 
        print("A Média Aritmética da lista de dados é: " + str(mediaAritmetica(listaDeDados)))
        opcaoVoltarAoMenuOuSair()
    
    elif x == 2:
        print()
        print("Lista de dados: " + str(listaDeDados)) 
        print("A Média Ponderada da lista de dados é: " + str(mediaPoderada(listaDeDados)))
        opcaoVoltarAoMenuOuSair()

    elif x == 3:
        print()
        print("A Moda da lista de dados é: " + str(moda(listaDeDados)))
        print()
        opcaoVoltarAoMenuOuSair()

    elif x == 4: 
        print()
        print("A Mediana da lista de dados é: " + str(mediana(listaDeDados)))
        print()
        opcaoVoltarAoMenuOuSair()

    elif x == 5:
        listaDeDados.clear()
        print()
        povoarLista(listaDeDados)
    elif x == 6:
        sairDoPrograma()
    else:
        print()
        ("Digite uma opção válida!")
        menuPrincipal()

def mediaAritmetica(lista):
    os.system('cls')
    print("Lista de dados: " + str(listaDeDados)) 
    return statistics.mean(lista)  

def moda(lista):
    os.system('cls')
    print("Lista de dados: " + str(listaDeDados)) 
    x = statistics.multimode(lista)
    if len(x) == len(lista):
        return("A lista não possui moda")
    elif len(x) == 1:
        return(str(statistics.multimode(lista)) + " (MODAL)")
    elif len(x) == 2:
        return(str(statistics.multimode(lista)) + " (BIMODAL)")        
    elif len(x) == 3:
        return(str(statistics.multimode(lista)) + " (TRIMODAL)")
    else:
        return(str(statistics.multimode(lista)) + " (MULTIMODAL)")

def mediaPoderada(lista):
    os.system('cls')
    print("Lista de dados: " + str(listaDeDados)) 
    indice = 0
    somaNumerador = 0
    somaDenominador = 0
    while (indice < len(lista)):
        x = int(input("Digite o peso referente ao " + str(indice + 1) + ("º dado: ")))
        somaNumerador += lista[indice] * x
        somaDenominador += x 
        indice += 1
    return (somaNumerador/somaDenominador)    

def mediana(lista):
    os.system('cls')
    print("Lista de dados: " + str(listaDeDados)) 
    return statistics.median(lista)

def opcaoVoltarAoMenuOuSair():
    x = int(input("-----Para sair do Programa digite [0] ou para voltar ao menu digite [1]----"))
    if x == 0:
        sairDoPrograma()
    elif x == 1:
        menuPrincipal()
    else:
        ("Digite uma opção válida:")
        opcaoVoltarAoMenuOuSair()    

def sairDoPrograma():    
    sys.exit()

povoarLista(listaDeDados)