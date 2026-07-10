# Review Day – Core Algorithms & Big O Synthesis

## Self‑quiz answers

1. **Binary search works on unsorted arrays.** – False (it requires a sorted array).
2. **A linked list always gives O(1) insertion, no matter where.** – False (insertion at the head is O(1); at the end without a tail pointer is O(n)).
3. **Quicksort is always O(n log n).** – False (worst case is O(n²) when the pivot is unlucky).
4. **BFS can find the shortest path in a weighted graph.** – False (BFS works for unweighted graphs; weighted graphs need Dijkstra).
5. **A hash table with a high load factor is faster.** – False (high load factor → more collisions → slower performance).

## Big O / Algorithm Cheat Sheet

| Big O      | Name         | Example Algorithm(s) from this course                          |
| ---------- | ------------ | -------------------------------------------------------------- |
| O(1)       | Constant     | Array access by index, hash table lookup (average)             |
| O(log n)   | Logarithmic  | Binary search                                                  |
| O(n)       | Linear       | Simple search, linked list traversal, BFS (visiting all nodes) |
| O(n log n) | Linearithmic | Quicksort (average), merge sort                                |
| O(n²)      | Quadratic    | Selection sort, Quicksort (worst case)                         |
| O(n!)      | Factorial    | Traveling salesperson (brute force)                            |

**Why hash tables are O(1) average but can degrade to O(n):**  
A good hash function distributes keys evenly, making lookups instant. But if many keys collide (e.g., due to a bad hash function or a high load factor), all keys at that index form a linked list, and lookup becomes a linear scan of that list – O(n). Resizing and a low load factor keep the average time O(1).

## Algorithms I re‑implemented today

- **Linked List** (prepend, traverse, find, insertAfter) – both JS and Python.
- **Selection Sort** (find smallest + sort) – both JS and Python.

## Reflection

The linked list implementation felt smooth; I’m comfortable with pointer manipulation.  
Selection sort was also easy, though I remember the O(n²) cost is why we later learned Quicksort.  
I missed the comparison counter – a reminder that Big O isn’t about seconds, it’s about the number of operations.  
Overall, I feel confident in these fundamentals and ready to move on to Dijkstra’s algorithm.
