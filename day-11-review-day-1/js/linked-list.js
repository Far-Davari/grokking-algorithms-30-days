// Create node
function createNode(value) {
  return { value: value, next: null };
}

// Pre append an head to the beggining
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

// Find node with given value,  return node or null
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

let head = createNode(5);

head = prepend(head, 15);

// console.log(find(head, 5));
insertAfter(head, 10)
let found = find(head, 10)
console.log("--->", found);
if (found) {
  insertAfter(found, 4)
}
console.log(head);
