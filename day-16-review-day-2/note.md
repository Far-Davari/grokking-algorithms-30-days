# Day 16 – Greedy Algorithms: Set Covering

## 1. Why does the greedy algorithm for set covering run in O(n²) time?

The outer `while` loop runs once for each station we pick, and in the worst case we might pick all n stations.  
Inside that loop, the `for` loop scans all n stations to find the best one.  
So we have n passes, each doing n checks → n × n = O(n²).

## 2. What is a "power set" and why is finding the exact solution O(2ⁿ)?

A power set is the set of all possible subsets of a set.  
For n stations, each station can either be included or not included, giving 2 choices per station.  
Thus there are 2ⁿ possible subsets.  
To find the exact minimum set of stations, we must check every subset, which takes O(2ⁿ) time – impractical for large n.  
The greedy algorithm avoids this by choosing the best station at each step, giving an approximate solution in polynomial time.

## 3. Give one example of a problem where greedy is optimal, and one where it is not.

- Optimal: Classroom scheduling – always pick the class that ends earliest; this greedy choice yields the globally optimal schedule.
- Not optimal: The knapsack problem – picking the highest value item first may not give the best overall value because it might leave too little capacity.

## 4. In the set-covering greedy algorithm, why do we use intersection (`states_needed & states_for_station`) instead of just using `states_for_station` directly?

We use intersection to find only the states that are **still needed** and covered by this station.  
If we used `states_for_station` directly, we might count states already covered by previous stations.  
The intersection gives the number of **new** states this station can cover, which is what the greedy algorithm tries to maximize.

---

## NP‑Completeness Quiz

**Which of these is NP‑complete?**
a) Binary search -> **No**  
b) Finding the shortest path from A to B in a weighted graph (Dijkstra) -> **No**  
c) The traveling salesperson problem (decision version) -> **Yes**  
d) Sorting a list of numbers -> **No**

**Why is the set‑covering problem NP‑complete?**
To find the exact minimum set of stations, we must examine **every possible subset** of the stations (the power set). There are 2ⁿ subsets, so the brute‑force exact algorithm takes O(2ⁿ) time, which is exponential. The problem is in NP because if someone hands us a candidate set, we can quickly verify that it covers all states (polynomial time). But no polynomial‑time algorithm is known to find the best set from scratch. This combination makes it NP‑complete.

**If a problem is NP‑complete, what should you do instead of trying to find an exact solution?**
Use an approximation algorithm (like the greedy set‑covering algorithm) to get a good enough solution quickly, or use heuristics. For small inputs, brute force may be acceptable.

**True or False: Greedy algorithms always produce the optimal solution for NP‑complete problems.**
**False** – greedy algorithms often give a good approximation, but not necessarily the optimal solution.
