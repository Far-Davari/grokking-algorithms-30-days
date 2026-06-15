# Day 5 – Recursion and the Call Stack

## 1. In your own words, explain what the call stack is and how recursion uses it.

The call stack is a data structure that keeps track of active function calls. It follows LIFO (Last‑In, First‑Out). When a function is called, a frame containing its parameters, local variables, and the return address is pushed onto the stack. When the function finishes, its frame is popped.
Recursion uses the call stack to handle multiple calls of the same function. Each recursive call pushes a new frame on the stack, waiting for the base case. Once the base case returns, the frames pop off one by one, each returning its result to the caller above it. This is why the deepest call finishes first.

## 2. Trace `fact(4)` step by step, showing the call stack at each phase.

factorial(4) -> waits for factorial(3)
factorial(3) -> waits for factorial(2)
factorial(2) -> waits for factorial(1)
factorial(1) -> returns 1
factorial(2) -> returns 2 X 1 = 2
factorial(3) -> returns 3 X 2 = 6
factorial(4) -> returns 4 X 6 = 24

## 3. What would happen if you called `fact(-1)`? Why?

When you call fact(-1), the base case i == 1 is never reached because the input gets more and more negative. The function keeps calling itself with -2, -3, -4, ... endlessly, adding a new frame to the call stack each time. Eventually the call stack exceeds its maximum size, and the program crashes with a stack overflow error (in Python, a RecursionError).
