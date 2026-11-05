grafo = {}

while True:
  dir_lst = input("Seu grafo é direcionado? [S] ou [N]\n--> ")
  dir_lst = dir_lst.upper()
  if dir_lst == 'S':
    print("Grafo Direcionado selecionado!")
    direcionado = True
    break
  elif dir_lst == 'N':
    print("Grafo Não Direcionado selecionado!")
    direcionado = False
    break
  else:
    print("Opção inválida!")

while True:
  x = input("""
LISTA DE ADJACÊNCIA\n
[1] Inserir vértice
[2] Remover vértice
[3] Inserir aresta
[4] Remover aresta
[5] Calcular grau
[6] Verificar possível aresta (de x para y)
[7] Listar vizinhos de um vértice
[8] Verificar se um determinado percurso é possível (de x para y)
[9] Exibir grafo
[0] Sair\n
--> """)

  match(int(x)):
    case 1:
      vertice = int(input(f"\nInsira um vértice: "))
      if vertice not in grafo:
        grafo[vertice] = []
      else:
        print(f"O vértice {vertice} já existe!")
      print(grafo)

    case 2:
      vertice = int(input(f"\nInsira o vértice a ser removido: "))
      if vertice in grafo:
        for v in grafo:
          if vertice in grafo[v]:
            grafo[v].remove(vertice)
        del grafo[vertice]
      else:
        print("O vértice não existe.")
      print(grafo)

    case 3:
      try:
        vertice1 = int(input(f"\nEscolha o vértice nº1 (origem): "))
        vertice2 = int(input(f"\nEscolha o vértice nº2 (destino): "))
      except:
        print("Os vértices devem ser números inteiros.")
        continue

      if vertice1 not in grafo or vertice2 not in grafo:
        print("Um ou mais vértices não existem.")
      else:
          if vertice2 not in grafo[vertice1]:
              grafo[vertice1].append(vertice2)
          if not direcionado and vertice1 not in grafo[vertice2]:
              grafo[vertice2].append(vertice1)
      print(grafo)

    case 4:
      try:
        vertice1 = int(input(f"\nEscolha o vértice nº1: "))
        vertice2 = int(input(f"\nEscolha o vértice nº2: "))
      except:
        print("Os vértices devem ser números inteiros.")
        continue

      if vertice1 not in grafo or vertice2 not in grafo:
        print("Um ou mais vértices não existem.")
      else:
          if vertice2 in grafo[vertice1]:
              grafo[vertice1].remove(vertice2)
          if not direcionado and vertice1 in grafo[vertice2]:
              grafo[vertice2].remove(vertice1)
      print(grafo)

    case 5:
      if grafo:
        if not direcionado:
          for v in grafo:
            print(f"O grau do vértice {v} é {len(grafo[v])}")
        else:
          for v in grafo:
            grauSai = len(grafo[v])
            grauEnt = 0
            for v2 in grafo:
              if v in grafo[v2]:
                grauEnt += 1
            print(f"Vértice {v} --> Entrada: {grauEnt}, Saída: {grauSai}")
      else:
        print("Não há vértices disponíveis.")

    case 6:
      try:
        vertice1 = int(input(f"\nEscolha o vértice nº1: "))
        vertice2 = int(input(f"\nEscolha o vértice nº2: "))
      except:
        print("Os vértices devem ser números inteiros.")
        continue

      if vertice1 not in grafo or vertice2 not in grafo:
        print("Um ou mais vértices selecionados não existem.")
      elif vertice2 in grafo[vertice1]:
        print("A aresta existe.")
      else:
        print("A aresta não existe.")

    case 7:
      try:
        vertice = int(input(f"\nEscolha o vértice: "))
      except:
        print("O vértice deve ser um número inteiro.")
        continue

      if vertice in grafo:
        print(f"Os vizinhos do vértice {vertice} são: {grafo[vertice]}")
      else:
        print("O vértice não existe.")

    case 8:
      try:
        vertice1 = int(input(f"\nEscolha o vértice inicial: "))
        vertice2 = int(input(f"\nEscolha o vértice final: "))
      except:
        print("Os vértices devem ser números inteiros.")
        continue

      if vertice1 not in grafo or vertice2 not in grafo:
        print("Um ou mais vértices não existem.")
      else:
        visitados = [vertice1]
        fila = [vertice1]
        possivel = False

        while len(fila) > 0:
          atual = fila.pop(0)

          if atual == vertice2:
            possivel = True
            break

          for vizinho in grafo[atual]:
            if vizinho not in visitados:
              visitados.append(vizinho)
              fila.append(vizinho)

        if possivel:
          print(f"Existe um percurso entre '{vertice1}' e '{vertice2}'.")
        else:
          print(f"Não existe percurso entre '{vertice1}' e '{vertice2}'.")

    case 9:
      print(grafo)

    case 0:
      break
