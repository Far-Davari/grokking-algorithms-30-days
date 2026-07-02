def simple_hash(key, size):
    total = sum(ord(ch) for ch in key)
    return total % size

class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)] # List of buckets

    def put(self, key, value):
        idx = simple_hash(key, self.size)
        bucket = self.table[idx]
        # update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,  value)
                return
        bucket.append((key, value))

    def get(self, key):
        idx = simple_hash(key, self.size)
        bucket = self.table[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Slot {i}: {bucket}")

ht = SimpleHashTable(5)
ht.put("cat", "meow")
ht.put("dog", "woof")
ht.put("act", "meow again")
print(ht.get("cat"))
print(ht.get("act"))
ht.display()