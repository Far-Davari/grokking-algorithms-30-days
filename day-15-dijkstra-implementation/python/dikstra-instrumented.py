# ---------- 1. The weighted graph (directed, with a negative edge) ----------
# Each node has a dictionary of {neighbor: cost}
graph = {
  "S": {"A": 1, "B": 3},
  "A": {"C": 1},
  "B": {"C": -2},         # negative edge – will cause Dijkstra to fail
  "C": {}
}

def dijkstra(graph, start):
  # ---------- 2. Initialise costs ----------
  # costs[node] = currently known cheapest cost from start to node
  costs = {node: float("inf") for node in graph}
  costs[start] = 0
  print(f"Initial costs: {costs}")

  # ---------- 3. Initialise parents ----------
  # parents[node] = the node that gave us the cheapest path to node
  parents = {start: None}
  print(f"Initial parents: {parents}")

  # ---------- 4. Processed set ----------
  processed = set()
  print(f"Processed: {processed}\n")

  # ---------- 5. Helper – find unprocessed node with smallest cost ----------
  def find_lowest_cost_node():
      lowest_cost = float("inf")
      lowest_node = None
      for node in costs:
          if node not in processed and costs[node] < lowest_cost:
              lowest_cost = costs[node]
              lowest_node = node
      return lowest_node

  # ---------- 6. Main loop ----------
  step = 1
  node = find_lowest_cost_node()
  while node is not None:
      cost_so_far = costs[node]
      print(f"--- Step {step}: processing '{node}' (current cost {cost_so_far}) ---")
      print(f"  Costs before: {costs}")
      print(f"  Parents before: {parents}")

      # Look at every neighbor of the current node
      for neighbor, weight in graph[node].items():
          # STANDARD DIJKSTRA: only update neighbors that have NOT been processed
          if neighbor not in processed:
              new_cost = cost_so_far + weight
              print(f"    Checking neighbor '{neighbor}' via '{node}': "
                    f"old cost {costs[neighbor]}, new cost {new_cost}")
              if new_cost < costs[neighbor]:
                  print(f"      -> UPDATING: cost of '{neighbor}' to {new_cost}, "
                        f"parent to '{node}'")
                  costs[neighbor] = new_cost
                  parents[neighbor] = node

      # Mark current node as processed (its cost is now final)
      processed.add(node)
      print(f"  Processed set after: {processed}")
      print(f"  Costs after: {costs}")
      print(f"  Parents after: {parents}\n")

      # Find next node to process
      node = find_lowest_cost_node()
      step += 1

  print(f"Final costs: {costs}")
  print(f"Final parents: {parents}")
  return costs, parents


# ---------- 7. Path reconstruction ----------
def get_path(parents, target):
  if target not in parents:      # unreachable
      return None
  path = []
  while target is not None:
      path.append(target)
      target = parents[target]
  return path[::-1]               # reverse


# ---------- 8. Run and test ----------
if __name__ == "__main__":
  costs, parents = dijkstra(graph, "S")
  print("\nCheapest cost from S to C:", costs["C"])
  print("Shortest path:", get_path(parents, "C"))