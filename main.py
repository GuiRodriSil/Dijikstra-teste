import networkx as nx
import matplotlib.pyplot as plt

def exibir_grafo(grafo):



  options = {
      'node_color': 'darkblue',
      'edge_color': '#808080',
      'node_size': 600,
      'width': 2,
      'font_color': 'white',
      'font_weight': 'bold',
      'font_size': 10

  }
  plt.figure(1)

  nx.draw_networkx(
      grafo,
      pos=nx.spring_layout(grafo),
      with_labels=True,
      **options
  )

  labels = nx.get_edge_attributes(grafo,'valor')

  nx.draw_networkx_edge_labels(grafo, pos=nx.spring_layout(grafo), edge_labels=labels)


  plt.show()




G1 = nx.Graph()

G1.add_nodes_from(['A','B','C','D','E','F','G','H'])

G1.add_edge("A","B", valor = 5)
G1.add_edge("A","H", valor = 20)
G1.add_edge("B","C", valor = 5)
G1.add_edge("B","D", valor = 4)
G1.add_edge("C","E", valor = 2)
G1.add_edge("C","F", valor = 3)
G1.add_edge("D","E", valor = 6)
G1.add_edge("D","H", valor = 5)
G1.add_edge("E","G", valor = 5)
G1.add_edge("E","H", valor = 10)
G1.add_edge("F","G", valor = 7)
G1.add_edge("G","H", valor = 8)

exibir_grafo(G1)

def get_less_table(table):

  selected = {k: v for k, v in table.items() if v['is_less'] == False}
  sorted_ = sorted(selected.items(), key=lambda kv: kv[1]['distance'])

  return sorted_[0][0]

# Algoritmo de Dijikstra
def less_path(graph, v,destino):

  table_ = {v: {'is_less': True, 'distance': 0, 'path': ''}}
  found_ = [v]
  actual_node = v


  while set(found_) != set(list(graph.nodes())):

    all_neighbors = [x for x in list(nx.neighbors(graph, actual_node)) if x not in found_]
    for neigh in all_neighbors:
      new_distance = table_[actual_node]['distance'] + graph.get_edge_data(actual_node, neigh, 'valor')['valor']
      if neigh in table_.keys():
        if new_distance < table_[neigh]['distance']:
          table_[neigh]['distance'] = new_distance
          table_[neigh]['path'] = actual_node
      else:
        table_[neigh] = {'is_less': False, 'distance': new_distance, 'path': actual_node}


    actual_node = get_less_table(table_)
    table_[actual_node]['is_less'] = True
    found_.append(actual_node)

    if actual_node == destino:
      break

    caminho_final = retorna_caminho(table_, v, destino)

  return  caminho_final

def retorna_caminho(table, origem, destino):

  custo = table[destino]['distance']

  caminho = [destino]

  anterior = table[destino]['path']
  caminho.insert(0,anterior)

  while(anterior != origem):
    anterior = table[anterior]['path']
    caminho.insert(0,anterior)

  return{'caminho': caminho,'custo': custo}

less_path(G1,'A','H')
