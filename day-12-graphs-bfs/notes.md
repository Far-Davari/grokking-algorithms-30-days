# Day 12 – Graphs and Breadth‑First Search

## 1. What is a graph, and how does it represent a network? (Mention nodes, edges, and give a real‑world example.)

A graph is a set of **nodes** (also called vertices) connected by **edges**.  
It models relationships between objects: each edge represents a direct connection between two nodes.  
A real‑world example: a road network where cities are nodes and roads are edges. Another: a social network where people are nodes and friendships are edges.

## 2. Explain the two types of questions BFS can answer. (Path existence and shortest path.)

1. **Is there a path from node A to node B?** (connectivity check)  
2. **What is the shortest path from node A to node B?** (shortest‑path problem)  

BFS can answer both because it explores nodes level by level – the first time you reach a node, you've found the shortest path (in terms of number of edges).

## 3. Why does BFS use a queue, not a stack? (Hint: what would happen if you used a stack – think LIFO vs. FIFO?)

A queue is **FIFO** (First‑In, First‑Out). This means you explore nodes in the order you discover them – first‑degree connections are checked before second‑degree, and so on.  
If you used a **stack** (LIFO), you would immediately dive into the most recently added node, going deep into a branch before checking other nearby nodes. This would become a **depth‑first search** and would not guarantee finding the shortest path.  
The queue ensures BFS stays broad and finds the closest node first.