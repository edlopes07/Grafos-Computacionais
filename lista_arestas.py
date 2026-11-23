arestas = []
vertices = []

def exibir():
  for aresta in arestas:
    print(aresta)


def manipularVertice(v, tipo):
    global arestas
    if tipo == 1:
        if v in vertices:
            print(f"{v} já existe!")
            return

        vertices.append(v)
        return vertices

    if tipo == 2:
      if v not in vertices:
            print(f"{v} não existe!")
            return

      vertices.remove(v)
      atualizar = []
      for aresta in arestas:
        if v not in aresta:
          atualizar.append(aresta)
      arestas = atualizar

      return arestas, vertices


def manipularAresta(v1, v2, tipo, isDirecionado):
  if v1 not in vertices or v2 not in vertices:
    print(f"Não é possivel relacionar [{v1}][{v2}]!\nVerifique se os vértices existem.")
    return

  if tipo == 1:
    aresta = (v1, v2)
    aresta2 = (v2, v1)
    if aresta not in arestas:
      arestas.append(aresta)
      if not isDirecionado:
        arestas.append(aresta2)
    else:
      print(f"{aresta} já existe!")
      return

    return arestas

  if tipo == 2:
    aresta = (v1, v2)
    aresta2 = (v2, v1)
    if aresta not in arestas:
      print(f"{aresta} não existe!")
      return
    arestas.remove(aresta)
    if not isDirecionado:
      arestas.remove(aresta2)

    return arestas


def verificaExistencia(v1, v2):
  if v1 not in vertices or v2 not in vertices:
    print(f"Não é possivel relacionar [{v1}][{v2}]!\nVerifique se os vértices existem.")
    return

  aresta = (v1, v2)
  if aresta not in arestas:
    print("A aresta não existe!")
  else:
    print("A aresta existe!")


def calcularGrau(isDirecionado):
  if not vertices:
    print("Não existem vértices.")

  if not isDirecionado:
    for v in vertices:
      grau = 0
      for aresta in arestas:
          if v in aresta:
            grau += 1
      print(f"Vértice {v}: {grau}")
  else:
    for v in vertices:
      grauEnt = 0
      grauSai = 0
      for aresta in arestas:
        if aresta[0] == v:
          grauSai += 1
        if aresta[1] == v:
          grauEnt += 1
      print(f"Vértice {v} --> Entrada: {grauEnt}, Saída: {grauSai}")


def listarvizinho(v):
  if v not in vertices:
    print("Vértice não existente!")
  else:
    vizinhos = []

    for aresta in arestas:
      if aresta[0] == v:
        vizinhos.append(aresta[1])
      if aresta[1] == v:
        vizinhos.append(aresta[0])
    print(f"Vértice {v} --> vizinhos: {vizinhos}")


def pathFind(v1, v2):
  if v1 not in vertices or v2 not in vertices:
    return f"Não é possivel relacionar [{v1}][{v2}]!\nVerifique se os vértices existem."

  visitados = [v1]
  fila = [v1]
  possivel = False

  while len(fila) > 0:
    atual = fila.pop(0)
    if atual == v2:
      possivel = True
      break

    for aresta in arestas:
      if aresta[0] == atual:
        vizinho = aresta[1]
        if vizinho not in visitados:
          visitados.append(vizinho)
          fila.append(vizinho)

  if possivel:
    return f'Um percurso do vértice {v1} até o vértice {v2} é possível!'
  else:
    return 'O percurso determinado é impossível.'


def bfs(v):
  if not arestas:
    return "Não foi possível realizar uma busca.\nO grafo não possui arestas!"
  visitados = []
  fila = [v]

  while len(fila) > 0:
    print(f"Visitados: {visitados}")
    print(f"Fila: {fila}")
    atual = fila.pop(0)
    if atual not in visitados:
      visitados.append(atual)

    for aresta in arestas:
      if aresta[0] == atual:
        vizinho = aresta[1]
        if vizinho not in visitados and vizinho not in fila:
          fila.append(vizinho)
  return f'{visitados}'


def menor(inicio, destino):
    if not arestas:
        return "Não foi possível realizar a busca. \nO grafo não possui arestas!"

    visitados = []

    fila = [{
        'vertice': inicio,
        'caminho': [inicio]
    }]

    while len(fila) > 0:
        print(f"Visitados: {visitados}")
        print(f"Fila: {fila}")

        atual = fila.pop(0)
        vertice_atual = atual['vertice']
        caminho_atual = atual['caminho']

        if vertice_atual not in visitados:
            visitados.append(vertice_atual)

        if vertice_atual == destino:
            return caminho_atual

        for aresta in arestas:
            if aresta[0] == vertice_atual:
                vizinho = aresta[1]

                if vizinho not in [item['vertice'] for item in fila] and vizinho not in visitados:
                    fila.append({
                        'vertice': vizinho,
                        'caminho': caminho_atual + [vizinho]
                    })

    return "Não existe caminho entre esses vértices!"


def dfs(v):
  if not arestas:
    return "Não foi possível realizar uma busca.\nO grafo não possui arestas!"
  visitados = []
  pilha = [v]

  while len(pilha) > 0:
    print(f"Visitados: {visitados}")
    print(f"Pilha: {pilha}")
    atual = pilha.pop()
    if atual not in visitados:
      visitados.append(atual)

    for aresta in arestas:
      if aresta[0] == atual:
        vizinho = aresta[1]
        if vizinho not in visitados and vizinho not in pilha:
          pilha.append(vizinho)
  return f'{visitados}'

def ciclos(inicio):
  if not arestas:
    return "Não foi possível realizar uma busca. \nO grafo não possui arestas!"
  visitados = []
  pilha = [{
          'vertice': inicio,
          'pai': None
      }]
  while len(pilha) > 0:
      print(f"Visitados: {visitados}")
      print(f"Pilha: {pilha}")
      atual = pilha.pop()
      vertice_atual = atual['vertice']
      pai_atual = atual['pai']
      if vertice_atual not in visitados:
        visitados.append(vertice_atual)
      vizinho = []
      for aresta in arestas:
        if aresta[0] == vertice_atual:
          vizinho.append(aresta[1])
      for vizinhos in vizinho:
        if vizinhos not in visitados and vizinhos not in [item['vertice'] for item in pilha]:
          pilha.append({
          'vertice': vizinhos,
          'pai': vertice_atual})
        else:
          if vizinhos != pai_atual:
            return 'Ciclo detectado!'
  return f'Nenhum ciclo detectado!'

while True:
  dir = input(f"Seu grafo é direcionado? [S] ou [N]\n--> ")
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

opcaoAdicional = "[10] Detectar ciclos (DFS)\n" if not direcionado else ""

while True:
  x = input(f"""
LISTA DE ARESTAS
[1] Manipular vértices
[2] Manipular arestas
[3] Exibir grau de cada vértice
[4] Verificar possível aresta (de x para y)
[5] Listar vizinhos de um vértice
[6] Verificar se um determinado percurso é possível (de x para y)
[7] Busca em largura (BFS)
[8] Buscar menor caminho (BFS)
[9] Busca em profundidade (DFS)
{opcaoAdicional}[0] Sair\n
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
          print(f"Vértices: {vertices}")

        case 2:
          try:
            print(f"\nEscolha um vértice para remover {vertices}")
            vertice = int(input("--> "))
          except:
            print("O vértice deve ser um número inteiro.")
            continue
          manipularVertice(vertice, 2)
          print(f"Vértices: {vertices}\nArestas:")
          exibir()

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
            if direcionado:
              vertice1 = int(input("Origem --> "))
              vertice2 = int(input("Destino --> "))
            else:
              vertice1 = int(input("--> "))
              vertice2 = int(input("--> "))
          except:
            print("Os vértices devem ser um número inteiro.")
            continue
          manipularAresta(vertice1, vertice2, 1, direcionado)
          exibir()

        case 2:
          try:
            print(f"\nEscolha os vértices que compõem a aresta ({vertices})")
            if direcionado:
              vertice1 = int(input("Origem --> "))
              vertice2 = int(input("Destino --> "))
            else:
              vertice1 = int(input("--> "))
              vertice2 = int(input("--> "))
          except:
            print("Os vértices devem ser um número inteiro.")
            continue
          manipularAresta(vertice1, vertice2, 2, direcionado)
          exibir()

        case 0:
          continue

    case 3:
      calcularGrau(direcionado)

    case 4:
       try:
         print(f"\nEscolha os vértices da aresta que deseja checar ({vertices})")
         if direcionado:
          vertice1 = int(input("Origem --> "))
          vertice2 = int(input("Destino --> "))
         else:
          vertice1 = int(input("--> "))
          vertice2 = int(input("--> "))
       except:
         print("Os vértices devem ser números inteiros e estarem na lista")
         continue
       verificaExistencia(vertice1, vertice2)
       exibir()

    case 5:
      try:
            print(f"\nEscolha um vértice {vertices}")
            vertice = int(input("--> "))
      except:
        print("O vértice deve ser um número inteiro.")
        continue
      listarvizinho(vertice)

    case 6:
       try:
         print(f"\nEscolha o vértice Origem e Destino desejados ({vertices})")
         vertice1 = int(input("Origem --> "))
         vertice2 = int(input("Destino --> "))
       except:
         print("Os vértices devem ser números inteiros e estarem na lista")
         continue
       print(pathFind(vertice1, vertice2))

    case 7:
      try:
        v = vertices[0]
      except:
        print("Não há vértices disponíveis!")
        continue
      print(bfs(v))

    case 8:
      try:
        print(f"\n Escolha o vértice de Início e de Destino desejados ({vertices})")
        inicio = int(input("Início --> "))
        destino = int(input("Destino --> "))
      except:
        print("Os vértices devem ser inteiros e estarem na lista")
        continue
      print(menor(inicio, destino))
    
    case 9:
      try:
        v = vertices[0]
      except:
        print("Não há vértices disponíveis!")
        continue
      print(dfs(v))

    case 10:
        try:
          print(f"\n Escolha o vértice de Início da detecção de ciclos ({vertices})")
          inicio = int(input("--> "))
        except:
          print("Os vértices devem ser inteiros e estarem na lista")
          continue
        print(ciclos(inicio))

    case 0:
      break

    case default:
      print("Opção desconhecida.")
      continue
