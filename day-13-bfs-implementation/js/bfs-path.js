graph = {
  you: ["alice", "bob", "claire"],
  alice: ["peggy"],
  bob: ["anuj", "peggy"],
  claire: ["thom", "jonny"],
  anuj: [],
  peggy: [],
  thom: [],
  jonny: [],
};

function isMangoSeller(name) {
  return name[name.length - 1] === "m";
}

function bfsPath(graph, start) {
  const queue = [start];
  const visited = new Set();
  const parent = { [start]: null };

  while (queue.length > 0) {
    const current = queue.shift();
    if (!visited.has(current)) {
      visited.add(current);
      if (isMangoSeller(current)) {
        const path = [];
        let node = current;
        while (node !== null) {
          path.push(node);
          node = parent[node];
        }
        return path.reverse();
      }
      for (const neighbour of graph[current]) {
        if (!visited.has(neighbour)) {
          if (!(neighbour in parent)) {
            parent[neighbour] = current;
          }
          queue.push(neighbour);
        }
      }
    }
  }
  return null;
}

console.log(bfsPath(graph, "you"));
