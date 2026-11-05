matriz = []
vertices = []

def exibirMatriz():
  print(vertices)
  for linha in matriz:
    print(linha)


def manipularVertice(v, tipo):
    if tipo == 1:
        if v in vertices:
            print(f"{v} já existe!")
            return

        vertices.append(v)

        for linha in matriz:
            linha.append(0)

        matriz.append([0] * len(vertices))
        return matriz

    if tipo == 2:
      if v not in vertices:
        print(f"{v} não existe!")
        return

      indice = vertices.index(v)
      vertices.remove(v)
      matriz.pop(indice)

      for linha in matriz:
        del linha[indice]
      return matriz


def manipularAresta(v1, v2, tipo, isDirecionado):
  if v1 not in vertices or v2 not in vertices:
    print(f"Não é possivel relacionar [{v1}][{v2}]!\nVerifique se os vértices existem.")
    return

  if not isDirecionado:
    if tipo == 1:
      indice1 = vertices.index(v1)
      indice2 = vertices.index(v2)

      matriz[indice1][indice2] = 1
      matriz[indice2][indice1] = 1
      return matriz

    if tipo == 2:
      indice1 = vertices.index(v1)
      indice2 = vertices.index(v2)

      matriz[indice1][indice2] = 0
      matriz[indice2][indice1] = 0
      return matriz

  if isDirecionado:
    if tipo == 1:
      indice1 = vertices.index(v1)
      indice2 = vertices.index(v2)

      matriz[indice1][indice2] = 1
    if tipo == 2:
      indice1 = vertices.index(v1)
      indice2 = vertices.index(v2)

      matriz[indice1][indice2] = 0


def calcularGrau(isDirecionado):
  if not matriz:
    print("A Matriz Adjacência está vazia.")
    return

  if not isDirecionado:
    calculados = {}
    for v in vertices:
      indice = vertices.index(v)
      grau = 0
      for i in matriz[indice]:
        if i == 1:
          grau += 1
      calculados[v] = [grau]
    print(calculados)
  else:
    for v in vertices:
      indice = vertices.index(v)
      grauSai = 0
      grauEnt = 0
      for i in matriz[indice]:
        if i == 1:
          grauSai += 1
      for linha in matriz:
        if linha[indice] == 1:
          grauEnt += 1
      print(f"Vértice {v} --> Entrada: {grauEnt}, Saída: {grauSai}")


def listarVizinhos(v):
  if v not in vertices:
    return f"{v} não existe!"

  coluna = -1
  vizinhos = []
  indice = vertices.index(v)

  for i in matriz[indice]:
    coluna += 1
    if i == 1:
      vizinhos.append(vertices[coluna])
  print(f"Vizinhos de {v}:")
  return vizinhos


def verificaExistencia(v1, v2):
  if v1 not in vertices or v2 not in vertices:
    print(f"Não é possivel relacionar [{v1}][{v2}]!\nVerifique se os vértices existem.")
    return
  indice1 = vertices.index(v1)
  indice2 = vertices.index(v2)
  if matriz[indice1][indice2] == 1:
    print("Aresta Existe!")
  else:
    print("Aresta não existe")


def pathFind(v1, v2):
  if v1 not in vertices or v2 not in vertices:
    print("Um ou mais vértices não existem na matriz.")
  else:
    visitados = [v1]
    possivel = False
    fila = [v1]
    while len(fila) > 0:
      coluna = -1
      atual = fila.pop(0)
      if atual == v2:
        possivel = True
        break

      indice = vertices.index(atual)
      for possui_aresta in (matriz[indice]):
        coluna += 1
        if possui_aresta == 1:
          vizinho = vertices[coluna]
          if vizinho not in visitados:
            visitados.append(vizinho)
            fila.append(vizinho)

    if possivel:
      print(f"Existe percurso entre {v1} e {v2}!")
    else:
      print(f"Não existe percurso entre {v1} e {v2}.")


while True:
  dir = input(f"""Seu grafo é direcionado? [S] ou [N]\n
  --> """)
  dir = dir.upper()

  match(dir):
    case 'S':
      print("Grafo Direcionado selecionado!")
      direcionado = True
      break
    case 'N':
      print("Grafo Não Direcionado selecionado!")
      direcionado = False
      break
    case default:
      print("Direção inválida!")

while True:
  x = input("""
MATRIZ DE ADJACÊNCIA
[1] Manipular vértices
[2] Manipular arestas
[3] Exibir grau de cada vértice
[4] Verificar possível aresta (de x para y)
[5] Listar vizinhos de um vértice
[6] Verificar se um determinado percurso é possível (de x para y)
[0] Sair\n
--> """)

  match(int(x)):
    case 1:
      y = input("""
  MANIPULAÇÃO DE VÉRTICES
  [1] Adicionar vértice
  [2] Remover vértice
  [0] Voltar\n
  --> """)

      match(int(y)):
        case 1:
          try:
            vertice = int(input("\nInsira um vértice: "))
          except:
            print("O vértice deve ser um número inteiro.")
            continue
          manipularVertice(vertice, 1)
          exibirMatriz()

        case 2:
          try:
            print(f"\nEscolha um vértice para remover {vertices}")
            vertice = int(input("--> "))
          except:
            print("O vértice deve ser um número inteiro.")
            continue
          manipularVertice(vertice, 2)
          exibirMatriz()

        case 0:
          continue

    case 2:
      y = input("""
  MANIPULAÇÃO DE ARESTAS
  [1] Adicionar aresta
  [2] Remover aresta
  [0] Voltar\n
  --> """)
      match(int(y)):
        case 1:
          try:
            print(f"\nEscolha os vértices que irão compor a aresta ({vertices})")
            vertice1 = int(input("--> "))
            vertice2 = int(input("--> "))
          except:
            print("Os vértices devem ser um número inteiro.")
            continue
          manipularAresta(vertice1, vertice2, 1, direcionado)
          exibirMatriz()

        case 2:
          try:
            print(f"\nEscolha os vértices que compõem a aresta ({vertices})")
            vertice1 = int(input("--> "))
            vertice2 = int(input("--> "))
          except:
            print("Os vértices devem ser um número inteiro.")
            continue
          manipularAresta(vertice1, vertice2, 2, direcionado)
          exibirMatriz()

        case 0:
          continue

    case 3:
      calcularGrau(direcionado)

    case 4:
      try:
        print(f"\nEscolha os vértices da aresta que deseja checar ({vertices})")
        vertice1 = int(input("--> "))
        vertice2 = int(input("--> "))
      except:
        print("Os vértices devem ser números inteiros e estarem na lista")
        continue
      verificaExistencia(vertice1, vertice2)

    case 5:
      try:
            print(f"\nEscolha um vértice {vertices}")
            vertice = int(input("--> "))
      except:
        print("O vértice deve ser um número inteiro.")
        continue
      print(listarVizinhos(vertice))

    case 6:
      try:
        print(f"\nEscolha os vértices da aresta que deseja checar ({vertices})")
        vertice1 = int(input("--> "))
        vertice2 = int(input("--> "))
      except:
        print("Os vértices devem ser números inteiros e estarem na lista")
        continue
      pathFind(vertice1, vertice2)

    case 0:
      break
