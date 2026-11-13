from collections import deque


class Graph:

  def __init__(self, directed: bool = False):
    self.directed = directed
    self.adj = {}
    self.vertices = set()

  def add_edge(self, u: str, v: str, weight: float = 1.0):
    self.vertices.add(u)
    self.vertices.add(v)
    if u not in self.adj:
      self.adj[u] = []
    if v not in self.adj:
      self.adj[v] = []

    self.adj[u].append((v, weight))
    if not self.directed:
      self.adj[v].append((u, weight))


def load_graph_from_file(file_path: str, directed: bool = False) -> Graph:
  graph = Graph(directed=directed)
  with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.strip()
      if not line or line.startswith('source'):
        continue
      parts = line.split(',')
      u, v = parts[0].strip(), parts[1].strip()
      w = float(parts[2].strip()) if len(parts) > 2 else 1.0
      graph.add_edge(u, v, w)
  return graph


def is_connected(graph: Graph) -> bool:
  if not graph.vertices:
    result = True
  else:
    start_node = next(iter(graph.vertices))
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
      curr = queue.popleft()
      for neighbor, _ in graph.adj.get(curr, []):
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append(neighbor)

    result = len(visited) == len(graph.vertices)

  print(f'is_connected: {result}')
  return result


def has_cycle(graph: Graph) -> bool:
  visited = set()

  def dfs(v, parent):
    visited.add(v)
    for neighbor, _ in graph.adj.get(v, []):
      if neighbor not in visited:
        if dfs(neighbor, v):
          return True
      elif neighbor != parent:
        return True
    return False

  result = False
  for node in graph.vertices:
    if node not in visited:
      if dfs(node, None):
        result = True
        break

  print(f'has_cycle: {result}')
  return result


def is_tree(graph: Graph) -> bool:
  connected = is_connected(graph)
  cycle = has_cycle(graph)
  result = connected and not cycle
  print(f'is_tree: {result}')
  return result


def is_forest(graph: Graph) -> bool:
  cycle = has_cycle(graph)
  result = not cycle
  print(f'is_forest: {result}')
  return result