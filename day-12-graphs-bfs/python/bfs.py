from collections import deque

# Graph
graph = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def is_mango_seller(name):
    return name[-1] == "m" # Silly rule!

def bfs(graph, start):
    queue = deque(graph[start]) # start with the frist-degree friends
    visited = set()

    while queue:
        person = queue.popleft() # dequeue from the left. using pop(0) is O(n), so we avoid that
        if person not in visited:
            visited.add(person)
            if is_mango_seller(person):
                return person # Found!
            queue.extend(graph[person])
        
    return None

print(bfs(graph, "you"))