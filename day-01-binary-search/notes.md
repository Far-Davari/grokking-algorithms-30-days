# Day 1 – Binary Search & Big O Notes

---

## You should always validate the algorithm, not just the output.

- Binary search input must always be sorted.
- For any list of size `n`, binary search takes at most `⌈log₂ n⌉` steps.
  - 1024 elements → worst-case: 10 steps.

---

## 1. Explain binary search to a 10-year-old

_Use the phone book analogy. How do you find a name without flipping every page?_

You open the book to the middle and look at the name. If the name you want comes earlier in the alphabet, you throw away the second half of the book. If it comes later, you throw away the first half. Then you do the same thing again with the half you kept. You keep halving the book until you find the name. This is much faster than starting from page one and turning every page.

---

## 2. Big O classification (based on pages 1–10)

_The book introduced these runtimes: O(1), O(log n), O(n), O(n²), O(n!). Classify each operation below._

a) **Looking up the value at a specific index in an array (e.g., `arr[42]`).**  
**Answer: O(1)** – constant time. The computer jumps directly to the memory address. It doesn’t matter if the array has 10 or 10 million elements.

b) **Finding a name in a phone book by flipping to the middle, then the middle of the remainder, etc.**  
**Answer: O(log n)** – the classic binary search. Each step halves the remaining pages.

c) **Finding a name by starting at page 1 and turning one page at a time.**  
**Answer: O(n)** – linear time. In the worst case, you check every page.

d) **Printing every element of a 2D matrix (n rows, n columns).**  
**Answer: O(n²)** – you must visit n × n = n² elements. Example: a chessboard has 8 rows and 8 columns, 64 squares total, not 8.

e) **Checking if a sorted list contains any duplicate by comparing every possible pair of elements.**  
**Answer: O(n²)** – there are about n×(n-1)/2 pairs, which grows proportionally to n².

---

## 3. Why must binary search input be sorted?

_What would happen if the list were unsorted? Give an example where binary search would fail._

The algorithm works by discarding half the list based on the middle value. If the list isn't sorted, looking at the middle tells you nothing about which half to throw away. Example: `[5, 1, 9, 3]` sorted is `[1, 3, 5, 9]`. If you search for `3` in the unsorted version, the middle is 1. Since 1 < 3, binary search would discard the first half and never find 3 (which is in that discarded half). You would get a wrong result.

---

## 4. The buggy `mid = low + high` code

_I wrote code where `mid = (low + high)` without division, and it still found the element in a small sorted list. Why did it appear to work? What kind of search was it really performing? Under what conditions would it break?_

It appeared to work because `low` stayed 0 in my tests, so `mid` always equaled `high`. The code checked the last element, then the second-last, then the third-last, etc. It was performing a **reverse linear search** – O(n), not O(log n). On a tiny list the speed difference is invisible. It will break (produce an index out of bounds error) if `low` ever becomes non-zero during the search, because `low + high` could then exceed the last valid index. Even if it never crashes, on a large list the performance is terrible. I learned that getting the right index does not mean the algorithm is correct.

---

## 5. Test results with a 1024-element list

- **Correct binary search:** worst-case steps for finding `1024` = **10 steps**
- **Correct binary search:** steps for an element not present (e.g., `-1`) = **10 steps**
- **Buggy code (without division):** steps to find the first element (`1`) = **1024 steps** (it walked backward through the entire array)
- **Theoretical maximum from `maxGuesses(1024)`** = **10 steps**

This confirms that the buggy code is O(n) and the correct code is O(log n).

---

## 6. What did I learn about validating algorithms, not just output?

_Why is counting steps more important than just getting the right index?_

A wrong algorithm can still return the correct answer for some inputs (especially small ones). If I only check the final output, I might ship slow or broken code. By counting the number of steps and comparing it to the theoretical O(log n) value, I verify that the algorithm actually behaves like binary search. This protects me from performance bugs that would only show up with large data. From now on, I will test not just correctness but also complexity.
