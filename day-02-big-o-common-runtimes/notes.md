# Day 2 – Common Big O Runtimes & Traveling Salesperson

---

## What is Big O notation really about?
Big O describes how the number of operations (or "time") of an algorithm grows as the input size grows. It focuses on the **worst case** and ignores constants and small details. It's not about seconds; it's about the shape of the growth curve.

## Big O runtimes with real-world analogies and examples

### O(1) – Constant time
- **Analogy:** Looking up a word in a dictionary's index. The index tells you the exact page; the time doesn't depend on the dictionary's size.
- **Example:** Accessing an array element by index (`arr[5]`).

### O(log n) – Logarithmic time
- **Analogy:** Searching for a name in a phone book by flipping to the middle, discarding half each time.
- **Example:** Binary search. For 1,000,000 elements, it takes ~20 steps.

### O(n) – Linear time
- **Analogy:** Reading every page of a book from start to finish. Double the pages, double the time.
- **Example:** Simple search (linear scan) through an unsorted list.

### O(n log n) – Linearithmic time
- **Analogy:** Sorting a huge pile of papers by repeatedly dividing them into smaller groups, sorting each group, then merging them back together.
- **Example:** Efficient sorting algorithms like merge sort, quicksort (average case).

### O(n²) – Quadratic time
- **Analogy:** In a classroom of n students, every student shakes hands with every other student. There are about n×(n-1)/2 handshakes, which grows like n².
- **Example:** Simple sorting algorithms (selection sort, bubble sort). Also, comparing every pair in a list.

### O(n!) – Factorial time
- **Analogy:** Trying every possible order in which to visit cities to find the shortest route. The number of possibilities explodes astronomically.
- **Example:** The traveling salesperson problem solved by brute force. For 20 cities, there are ~1.2×10^17 routes – impossible to compute.

## Why is the traveling salesperson problem O(n!)?
If a salesperson must visit n cities and return home, the number of possible routes is the number of ways to arrange n cities (permutations). For n cities, the routes are `(n-1)!` if the start city is fixed, or `n!` if not. For n=4, the routes are (4-1)! = 6:

1. City A → B → C → D → A
2. A → B → D → C → A
3. A → C → B → D → A
4. A → C → D → B → A
5. A → D → B → C → A
6. A → D → C → B → A

For n=5, it's 24. For n=6, 120. For n=10, 362,880. For n=20, it's beyond astronomical. That's why O(n!) is a disaster for even moderate n.

## If an algorithm is O(n² + n), what is its overall Big O? Why?
O(n² + n) simplifies to **O(n²)**. Because as n grows very large, the n² term dominates completely. The n term becomes insignificant, so we drop it.

## Which is faster for large n: O(100n) or O(n log n)? Explain.
**O(100n) is O(n)** because we drop constants. O(n) is faster than O(n log n) for sufficiently large n. Even though the constant 100 makes it seem slower initially, eventually the log n factor makes O(n log n) grow faster. For example, when n = 1,000,000:
- O(n) ≈ 100,000,000 operations
- O(n log n) ≈ 20,000,000 operations (since log2(1e6) ≈ 20, total 20e6)
Wait, that seems O(n log n) is smaller? Actually 100n = 100,000,000 vs n log2 n = 20,000,000. So O(n log n) is faster than O(100n) in that specific n? That contradicts my claim. Let's recalc: 100n vs n log n. For large n, n log n will eventually surpass 100n? No, n log n grows faster than n, so if we ignore constants, O(n) is better. But here we have constant 100. The crossing point: n log n > 100n when log n > 100, i.e., n > 2^100, which is a number with 30 digits. So for all practical n, the constant 100 is huge, and O(100n) might actually be slower than O(n log n) for realistic input sizes. The key is Big O ignores constants, so we still call them O(n) and O(n log n), and O(n) is the "faster" complexity class. In a real-world choice, constants matter, but Big O says O(n) is the faster growth rate. I'll clarify: Big O tells us that for extremely large n, O(n) will eventually be faster than O(n log n). But because of the 100 constant, the crossover might be beyond practical limits. So when comparing algorithms, we must consider both the Big O class and any hidden constants.

(A more nuanced answer: Big O says O(n) is asymptotically better than O(n log n). However, the constant factor 100 could make O(100n) slower for all feasible n. For a complete analysis, we'd need empirical testing, but the Big O notation still correctly indicates that O(n) scales better.)

## How does Big O help you decide which algorithm to choose before writing code?
Big O lets you predict performance without running the code. If you know your input will be large, you can avoid algorithms with poor growth rates (like O(n²) or O(n!)) and select one that scales well (like O(n log n) or O(log n)). For example, for searching in a sorted database, you'd choose binary search (O(log n)) over linear search (O(n)) because it will remain fast even as the data grows to millions of records.

## Day 1 Review – Binary search and Big O
On Day 1, I learned binary search, which is O(log n). Now I see where O(log n) fits in the Big O family. It's the "fast growth" end of the spectrum, right next to O(1). Binary search halves the input each step, so its runtime only grows logarithmically. My test with 1024 elements proved it: exactly 10 steps, matching log₂(1024). This understanding connects to today's lesson: O(log n) is extremely efficient, and recognizing it helps me choose the right algorithm.
