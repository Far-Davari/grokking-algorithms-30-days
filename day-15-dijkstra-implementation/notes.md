# Day 15 – Dijkstra Instrumented & Deep Understanding

## 1. Why is node C processed before node B in the S‑A‑B‑C graph?
After processing S, the costs are: A=1, B=3, C=∞.  
Then we process A (the cheapest unprocessed node), which updates C to 2.  
Now the unprocessed nodes are B (cost 3) and C (cost 2).  
Because 2 < 3, C is the lowest-cost unprocessed node, so it gets processed before B.

## 2. When B is finally processed, why doesn’t it update C’s cost?
When B is processed, its cost is 3. The edge B→C has weight 1, so the new cost via B would be 4.  
C already has cost 2, which is cheaper, so no update occurs.  
The algorithm correctly keeps the best known path.

## 3. How does the `processed` set guarantee we don’t waste time re‑checking nodes that are already final?
Once a node is marked processed, its current cost is the absolute cheapest possible (because all edge weights are non‑negative).  
Any alternative path to that node would have to go through another unprocessed node whose cost is already higher (or equal), and adding a non‑negative edge can only increase the total.  
Thus, we never need to look at a processed node again – the `processed` set allows the algorithm to skip them and avoid unnecessary work.

## 4. (Bonus) What happened with the negative edge B→C = -2?
If the graph has a negative edge (B→C = -2), Dijkstra fails.  
Your trace would show:
- After processing S: A=1, B=3.
- Process A (cost 1), update C to 2.
- Now C (cost 2) is cheaper than B (3), so C gets processed **and locked**.
- When B is finally processed, it offers a path to C with cost 3 + (-2) = 1, which **is** cheaper than 2.
- But C is already in the `processed` set, so Dijkstra ignores the update.
- The algorithm ends with C’s cost = 2 (via S→A→C), while the true shortest path is S→B→C with cost 1.
That’s why Dijkstra requires non‑negative weights – the greedy assumption breaks when a negative edge could later reduce a locked node’s cost.