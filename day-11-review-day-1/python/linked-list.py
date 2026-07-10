# Create node
def create_node(value):
  return { "value": value, "next": None }

# Pre append an head to the beggining
def prepend(head, value):
  new_node = create_node(value)
  new_node["next"] = head
  return new_node

# Prints all values from head to end
def traverse(head):
  current = head
  while current is not None:
    print(current["value"])
    current = current["next"]

# Find node with given value, return node or null 
def find(head, value):
  current = head
  while current is not None:
    if current["value"] == value:
      return current
    current = current["next"]
  return None

#  Insert a new value after the given node
def insert_after(node, value):
  new_node = create_node(value)
  new_node["next"] = node["next"]
  node["next"] = new_node

# Test
head = create_node(10)
print(head)
print("\n create node ===================\n")

head = prepend(head, 5)
print(head)
print("\n prepend 5 ===================\n")

head = prepend(head, 3)
print(head)
print("\n prepend 3 ===================\n")

traverse(head)
print("\n traverse ===================\n")

found = find(head, 5)
if found:
    insert_after(found, 7)
print(head)
print("\n find and insert after ===========\n")

traverse(head)