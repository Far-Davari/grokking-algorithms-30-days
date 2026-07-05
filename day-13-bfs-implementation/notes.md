# Day 13 – BFS Implementation, Run Time, and Graphs

## 1. What is the run time of BFS? Explain O(V + E).

BFS checks every **vertex** (V) and follows every **edge** (E) exactly once.  
Each vertex is enqueued and dequeued once, costing O(1) per vertex → O(V).  
When processing a vertex, its edges are examined, and over all vertices this totals O(E).  
Thus, the overall run time is O(V + E).

## 2. What is the difference between a directed graph and an undirected graph? Give an example of each.

- **Directed graph:** edges have a direction (arrows). Example: Twitter follows – Alice follows Bob, but Bob might not follow Alice.
- **Undirected graph:** edges are mutual (no arrows). Example: Facebook friends – if Alice is friends with Bob, then Bob is also friends with Alice.

## 3. What is a tree, in graph terms? Why is it a special graph?

A **tree** is a connected graph with **no cycles** – there is exactly one path between any two nodes.  
It is a special case of a graph: every tree is a graph, but not every graph is a tree.  
A tree cannot have edges that point back (no loops). Trees represent hierarchical structures like file systems or company org charts.
