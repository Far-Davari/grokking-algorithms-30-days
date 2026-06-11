// Create node
function createNode(value) {
  return { value: value, next: null };
}

// Add a value to the front, return the new head
function prepend(head, value) {
  let newNode = createNode(value);
  newNode.next = head;
  return newNode;
}

// Prints all values from head to end
function traverse(head) {
  let current = head;
  while (current !== null) {
    console.log(current.value);
    current = current.next;
  }
}

// Find node with given value, return node or null
function find(head, value) {
  let current = head;
  while (current !== null) {
    if (current.value === value) {
      return current;
    }
    current = current.next;
  }
  return null;
}

// Insert a new value after the given node
function insertAfter(node, value) {
  let newNode = createNode(value);
  newNode.next = node.next;
  node.next = newNode;
}

// Test
let head = createNode(10);
console.log(head);
console.log("\n===================\n");

head = prepend(head, 5);
console.log(head);
console.log("\n===================\n");

head = prepend(head, 3);
console.log(head);
console.log("\n===================\n");

traverse(head);
console.log("\n===================\n");

let found = find(head, 5);

if (found) {
  insertAfter(found, 7);
}
traverse(head);
