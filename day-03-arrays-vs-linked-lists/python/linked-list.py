def create_node(value): 
    return { "value": value, "next": None }

def prepend(head, value):
    new_node = create_node(value)
    new_node["next"] = head
    return new_node

def traverse(head):
    current = head
    while current is not None:
        print(current["value"])
        current = current["next"]

def find(head, value):
    current = head
    while current is not None:
        if current["value"] == value:
            return current
        current = current["next"]
    return None

def insert_after(node, value):
    new_node = create_node(value)
    new_node["next"] = node["next"]
    node["next"] = new_node

# Test
head = create_node(10)
print(head)
print("\n===================\n")

head = prepend(head, 5)
print(head)
print("\n===================\n")

head = prepend(head, 3)
print(head)
print("\n===================\n")

traverse(head)
print("\n===================\n")

found = find(head, 5)
if found:
    insert_after(found, 7)
print(head)
print("\n===================\n")

traverse(head)