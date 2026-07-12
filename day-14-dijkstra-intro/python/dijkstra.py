# Graph representation: each node has a dictionary of {neighbor: cost}
graph = {
  "book": {"lp": 5, "poster": 0},
  "lp": {"drums": 20, "guitar": 15},
  "poster": {"drums": 35, "guitar": 30},
  "drums": {"piano": 10},
  "guitar": {"piano": 20},
  "piano": {}   # the target node has no neighbors
}

def dijkstra(graph, start):
  #Costs from start to each node
  costs = {node: float("inf") for node in graph}
  costs[start] = 0
  parents = {start: None} # Parents dictionary to reconstruct the path later
  processed = set() # Set of nodes already precessed

  # Helper to find the lowest-cost unprocessed node
  def find_lowest_cost_node():
    lowest_cost = float("inf")
    lowest_node = None
    for node in costs:
      if node not in processed and costs[node] < lowest_cost:
        lowest_cost = costs[node]
        lowest_node = node
    return lowest_node
  
  node = find_lowest_cost_node()
  while node is not None:
    cost_so_far = costs[node] # the cheapest cost to reach this node
    # Look at all neighbors of the current node
    for neighbor, weight in graph[node].items():
      new_cost = cost_so_far + weight
      # If we found a cheaper path to the neighnor, update  it
      if new_cost < costs[neighbor]:
        costs[neighbor] = new_cost
        parents[neighbor] = node
    # Mark this node as processed
    processed.add(node)
    # Find the next cheapest unprocessed node
    node = find_lowest_cost_node()
  
  return costs, parents

def get_path(parents, target):
  path = []
  while target is not None:
    path.append(target)
    target = parents[target]
  return path[::-1] # reverse to get start -> target


costs, parents = dijkstra(graph, "book")
print("Costs:", costs["piano"])   # 35
print("Path:", get_path(parents, "piano"))  # ['book', 'lp', 'drums', 'piano']
