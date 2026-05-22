#Busca em largura(BFS)
#  explora sistemanticamente as arestas do grafo para descobrir 
# Todos os vértices alcançaveis a partir do vétice origem Scada vértice 
# Calcula a menor distância  de S até cada vértice que pode ser alcançado.

#Classe responsável pelo o Grafo
#Usando matriz de adjânceia
class Graph:
    def __init__(self, n):
        # é a quantidade de vertice do grafo
        self.n = n
        #Criação da matriz de adjacência com 0
        self.adj = [[0] * n for _ in range(n)]


#Insere uma aresta do vértice v para o vértice w
def GraphInsertARC(G, v, w):
    #se o vertice "v" está ligado com outro vertice "w" coloca 1
    if G.adj[v][w] == 0:
        G.adj[v][w] = 1

#remova a ligação de um V com o outro W
def GraphRemoveArc(G, v, w):
    #se a uma ligação 1 remova colocando 0
    if G.adj[v][w] == 1:
        G.adj[v][w] = 0

#exibe a matriz de adjâcencia do grafico
def GraphMatriz(G):
    for v in range(G.n):
        for w in range(G.n):
            print(G.adj[v][w],end=' ')
        print("\n")

#Exibe os vértices do grafo e suas ligações
def Graphshow(G):
    for v in range(G.n):
        print(v, end= " ")
        for w in range(G.n):
            if G.adj[v][w] == 1:
                print(w, end= " ")    
        print("\n")

def BFS(G, s):
    #quantidade de vertice do Grago "G"
    n = G.n
    #vetor que armzena o pai de cada vértice, inicialemnte -1
    pai = [-1]*n
    #vetor de distância da origem até cada vértice
    dist = [-1]*n
    #vetor de cores, se não passou pelo vértice 'B' se passou e a caminho 'C' e passou e não tem caminho 'p'
    cor = ['B']*n

    #Estrutura de fila utilizando BFS
    fila = [0]*n
    primeiro = 0
    ultimo = 0

    #Insere vertice de origem na fila
    fila[ultimo] = s
    ultimo+=1
    #A distancia 0, pois é origem
    dist[s] = 0
    #cor 'c' pq estamos nele e pode ter outros vertice ligados
    cor[s] = 'c'

    #Enquando a fila não tiver nula
    while primeiro < ultimo:
        #O vertice da fila
        u = fila[primeiro]
        #Percorre todos os vértices adjacentes a u
        for v in range(n):
            #Verifica se existe aresta e se não foi visitado
            if G.adj[u][v] == 1 and cor[v] == 'B':
                #insere o vertice na fila
                fila[ultimo] = v
                #Coloca o vertice como descoberto
                cor[v] = 'c'
                #Colocando a distancia
                dist[v] = dist[u] + 1
                #definindo o pai do vértice
                pai[v] = u
                ultimo+=1
        #Depois o vértice completamente explorado p
        cor[u] = 'p'
        primeiro+=1
    print(f"Distancia: {dist}")
    print(f"pais: {pai}")
    print(f"Fila: {fila}")

G = Graph(8)
GraphInsertARC(G,0,7)
GraphInsertARC(G,0,1)
GraphInsertARC(G,1,0)
GraphInsertARC(G,1,6)
GraphInsertARC(G,2,6)
GraphInsertARC(G,2,5)
GraphInsertARC(G,2,3)
GraphInsertARC(G,3,2)
GraphInsertARC(G,3,4)
GraphInsertARC(G,3,5)
GraphInsertARC(G,4,3)
GraphInsertARC(G,4,5)
GraphInsertARC(G,5,2)
GraphInsertARC(G,5,3)
GraphInsertARC(G,5,4)
GraphInsertARC(G,5,6)
GraphInsertARC(G,6,1)
GraphInsertARC(G,6,2)
GraphInsertARC(G,6,5)
GraphInsertARC(G,7,0)

GraphMatriz(G)
BFS(G,1)

Graphshow(G)