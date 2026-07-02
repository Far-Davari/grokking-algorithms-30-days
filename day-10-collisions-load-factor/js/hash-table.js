// Simple hash function: sum char codes modulo size
function hash(key, size) {
  let total = 0;
  for (let i = 0; i < key.length; i++) {
    total += key.charCodeAt(i);
  }
  return total % size;
}

class simpleHashTable {
  constructor(size = 10) {
    this.table = new Array(size);
    for (let i = 0; i < size; i++) {
      this.table[i] = []; // Each slot is an array (bucket)
    }
  }

  put(key, value) {
    const index = hash(key, this.table.length);
    const bucket = this.table[index];
    for (let pair of bucket) {
      if (pair[0] === key) {
        pair[1] = value;
        return;
      }
    }
    // Not found, push new pair
    bucket.push([key, value]);
  }

  get(key) {
    const index = hash(key, this.table.length);
    const bucket = this.table[index];
    for (let pair of bucket) {
      if (pair[0] === key) {
        return pair[1];
      }
    }
    return undefined;
  }
  //   Helper to see the interval state
  display() {
    for (let i = 0; i < this.table.length; i++) {
      console.log(`Slot ${i}: ${JSON.stringify(this.table[i])}`);
    }
  }
}

const ht = new simpleHashTable(5);
ht.put("cat", "meow");
ht.put("dog", "woof");
ht.put("act", "meow again!");
console.log(ht.get("cat"));
console.log(ht.get("act"));

ht.display();
