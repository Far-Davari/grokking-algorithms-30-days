# Day 14 – Dijkstra's Algorithm (Intro)

## 1. How does Dijkstra differ from BFS?
BFS finds the **shortest path** in unweighted graphs (fewest edges).  
Dijkstra finds the **fastest path** in weighted graphs (least total cost), as long as edge weights are non‑negative.

## 2. Explain the four steps of Dijkstra in your own words.
1. Find the unprocessed node with the lowest current cost.  
2. For each of its neighbors, check if going through this node gives a cheaper path. If yes, update the neighbor's cost and parent.  
3. Mark the node as processed (you won’t check it again).  
4. Repeat until all nodes are processed (or the target node is processed).

## 3. Why can’t Dijkstra handle negative weights?
Once a node is processed, Dijkstra assumes its cost is final. With negative weights, a later path could offer a lower cost through a node that was already processed, but Dijkstra would miss it. The algorithm requires non‑negative weights.

## 4. In the piano example, what was the cheapest path and its cost?
- Path: Book → LP → Drums → Piano  
- Total cost: 5 + 20 + 10 = 35