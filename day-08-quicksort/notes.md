# Day 8 – Quicksort

## 1. Explain how Quicksort uses Divide & Conquer.

Quicksort is a Divide & Conquer algorithm.

- **Divide:** Pick a pivot element (here, the first element). Partition the array into two sub‑arrays: `less` (all elements ≤ pivot) and `greater` (all elements > pivot).
- **Conquer:** Recursively apply Quicksort to `less` and `greater`. The base case is an array of size 0 or 1 (it is already sorted).
- **Combine:** `sorted_less + [pivot] + sorted_greater`.  
  Because the sub‑arrays become smaller at each step, the recursion eventually stops at the base case, and the whole array becomes sorted.

## 2. Why is Quicksort O(n log n) on average?

If the pivot splits the array roughly in half, the recursion tree is balanced with about log₂(n) levels.  
At each level, we do O(n) work (partitioning the array and concatenating).  
Thus, the total work is O(n) × O(log n) = O(n log n) on average.

## 3. What happens if the array is already sorted? Why is that a problem?

If we always take the first element as the pivot and the array is already sorted (ascending), then:

- `less` will be empty, and `greater` will contain all remaining elements.
- The recursion depth becomes n (instead of log n).
- At each level we still do O(n) work, so total work becomes O(n²).  
  This is the worst case. Choosing a better pivot (e.g., median or random) avoids this.

## 4. Why does Quicksort have a smaller constant than merge sort, making it often faster in practice?

Quicksort usually has a smaller constant factor than Merge sort because it can be implemented **in-place** (no extra array copies) and has a simpler inner loop that only swaps elements. Merge sort, on the other hand, needs to copy the whole array during the merging step, which adds overhead. This makes Quicksort faster in practice, even though both are O(n log n) on average.

## 5. Explain how choosing a random pivot changes the worst-case behaviour from O(n²) to O(n log n) on average.

The stack size equals the maximum depth of recursion. If you pick a random pivot, the probability of repeatedly hitting the worst case (where the pivot is always the smallest or largest element) becomes extremely small. The expected depth of the recursion tree is O(log n), so the total work remains O(n) × O(log n) = O(n log n) on average, even if the array is already sorted.
