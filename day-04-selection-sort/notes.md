# Day 4 – Selection Sort

---

## 1. Why is selection sort O(n²)?

Selection sort repeatedly scans the unsorted portion to find the smallest element. The first scan compares n elements, the next n‑1, then n‑2, and so on. The total comparisons are n + (n‑1) + … + 1 = n(n‑1)/2, which is O(n²). Big O ignores the ½ and lower‑order terms, leaving O(n²).

## 2. If you have a 1,000,000‑element list, roughly how many comparisons will selection sort do?

1,000,000(999,999)/2 ~ 500 bilion

## 3. Name one real‑life situation where selection sort might be acceptable despite O(n²).

Sorting our playlist by most played artist
