# Day 11 – Hash Table Collisions & Load Factor

## 1. What is a collision in a hash table, and how does separate chaining solve it?

Collision occurs when two different keys hash to the same index. Separate chaining solves it by making each array slot a bucket (like a list) that can hold multiple key‑value pairs. When a collision happens, we simply add the new pair to the bucket.

## 2. Why is the load factor important? What is a typical threshold for resizing?

The load factor measures how full the hash table is. If it gets too high, collisions become frequent and performance drops to O(n). A typical threshold is 0.7 – when the load factor exceeds 0.7, we resize the array to keep lookups O(1) on average.

## 3. How does resizing keep the average time O(1)?

Resizing is an O(n) operation, but it only happens occasionally – after many insertions. The cost of resizing is amortised over the insertions, so each insertion still takes O(1) on average.
