# Day 10 – Hash Tables (Intro)

## 1. What is a hash table, in your own words? (Mention keys, values, and the hash function.)

A hash table is a data structure that combines an **array** with a **hash function**.  
You give a **key** (like a name) to the hash function. The hash function turns that key into a number – an **index** in the array.  
At that index, you store the **value** associated with the key.  
So the hash table **maps keys to values** by using the hash function to decide where each value lives.

## 2. Describe two real‑world uses of hash tables you learned today.

- **Phone books / contact lists:** you map a name (key) to a phone number (value).  
- **Duplicate prevention (voting booth):** you store each voter’s name in a hash table. When someone tries to vote again, an instant lookup tells you they’ve already voted.  
- **Caching / DNS resolution:** you map a website domain (key) to its IP address (value) so your browser doesn’t have to look it up every time.

## 3. Why is checking for duplicates with a hash table O(1) while using a list is O(n)?

In a hash table, you use the key to directly calculate the index where its value is stored. This **direct access** takes constant time – O(1) – regardless of how many items are in the table.  
With a plain list, to check if an element already exists you normally have to **scan the whole list** from beginning to end. In the worst case, you examine every element, so it’s O(n).  
(Binary search can be O(log n) for a sorted list, but keeping the list sorted while inserting new items also adds extra cost, and the book’s point is that a hash table gives O(1) lookups without any sorting.)