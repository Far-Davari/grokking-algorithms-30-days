# Day 7 – Divide & Conquer

## 1. Explain Divide & Conquer using the farm‑plot example. What are the two steps?

Divide & Conquer is a recursive strategy. To find the largest square that can evenly divide a rectangular farm:
- **Base case:** If length equals width, that’s the square size.
- **Recursive step:** Cut off the largest possible square from the rectangle, then repeat the process on the remaining smaller rectangle.
The two general steps are:
1. Figure out the simplest possible case (base case).
2. Divide the problem into smaller subproblems until you hit the base case.

## 2. How does the recursive `count` function follow the D&C pattern? (Identify base case and recursive case.)

The function `count(arr)`:
- **Base case:** empty array → return 0.
- **Recursive case:** `1 + count(arr[1:])`. We count 1 for the current element and recursively count the rest of the array.
Each call reduces the array by one element until it’s empty, then the results are combined by addition.

## 3. Why is binary search a D&C algorithm? Name the base case and the division step.

Binary search uses D&C because each step reduces the search space by half.
- **Base cases:**
  - When `low > high` (the target is not in the array) → return `null`.
  - When `arr[mid] == target` → return `mid`.
- **Division step:** Compare the target with the middle element. If the target is smaller, search the left half; otherwise, search the right half. The problem size halves at each call.