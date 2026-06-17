# Day 6 – The Call Stack with Recursion

---

## 1. Explain what happens to the call stack when `greet("farshad")` runs. Use push/pop terms.

When `greet("farshad")` is called, a frame is pushed onto the call stack. Inside it, `greet2("farshad")` is called, so another frame is pushed. `greet2` finishes and is popped, returning control to `greet`. Then `bye()` is called, pushing a new frame. When `bye` finishes, it is popped. Finally, `greet` ends and its frame is popped, leaving the stack empty.

## 2. Why does recursion use more memory than a loop? Give an example from today's reading.

Each recursive call adds a new frame to the call stack, keeping all variables and return addresses until that call returns. A loop reuses the same variables and doesn't add new frames. In the grandmother's suitcase example, if the boxes were deeply nested, the stack would grow with every opened box, eventually using a lot of memory and possibly causing a stack overflow. A loop would just keep one box in hand at a time.

## 3. Write a recursive function `sum(arr)` that returns the sum of numbers. Then manually trace `sum([5, 10, 15])` showing each call and return value.

**JavaScript implementation:**

```javascript
function sum(arr) {
  if (arr.length === 0) {
    return 0;
  }
  return arr[0] + sum(arr.slice(1));
}
```

sum([5, 10, 15]) -> 5 + sum([10, 15])
sum([10, 15]) -> 10 + sum([15])
sum([15]) -> 15 + sum([])
sum([]) -> returns 0
sum([15]) -> returns 15 + 0 = 15
sum([10, 15]) -> returns 10 + 15 = 25
sum([5, 10, 15]) -> returns 5 + 25 = 30
