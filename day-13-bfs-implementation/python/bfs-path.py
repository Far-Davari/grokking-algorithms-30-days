from collections import deque

graph = {
  "you": ["alice", "bob", "claire"],
  "alice": ["peggy"],
  "bob": ["anuj", "peggy"],
  "claire": ["thom", "jonny"],
  "anuj": [],
  "peggy": [],
  "thom": [],
  "jonny": []
}

def is_mango_seller(name):
  return name[-1] == "m"

def bfs_path(graph, start):
  queue = deque([start])
  visited = set()
  parent = {start: None} # Who discovered each node

  while queue:
    current = queue.popleft()
    if current not in visited:
      visited.add(current)
      if is_mango_seller(current):
        # Reconstruct path
        path = []
        while current is not None:
          path.append(current)
          current = parent[current]
        return path[::-1] # Reverse to get start->target
      for neighbour in graph[current]:
        if neighbour not in visited:
          parent.setdefault(neighbour, current)
          queue.append(neighbour)

  return None

print(bfs_path(graph, "you"))
