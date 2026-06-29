What is a hash table, in your own words? (Mention keys, values, and the hash function.)
hash function maps keys to values, and it's created from puting an array and hash funtion together.
you give a string to hash function and it will return an index, u loop up that index in array.

Describe two real‑world uses of hash tables you learned today.
DNS resolotion, caching, lookup

Why is checking for duplicates with a hash table O(1) while using a list is O(n)?
because in hash table u instantly access to the item u want, but in array when u want to look up, u should check every single element in worst case, and in best case use binary search!