// The graph
const graph = {
  you: ["alice", "bob", "claire"],
  alice: ["peggy"],
  bob: ["anuj", "peggy"],
  claire: ["thom", "jonny"],
  anuj: [],
  peggy: [],
  thom: [],
  jonny: [],
};

// Person we look for
function isMangoSeller(name) {
  return name[name.length - 1] === "m"; // Silly rule!
}

function bfs(graph, start) {
  const queue = [...graph[start]];
  const visited = new Set();

  while (queue.length > 0) {
    const person = queue.shift();
    if (!visited.has(person)) {
      visited.add(person);
      if (isMangoSeller(person)) {
        return person; // Found!
      }
      // Add their friends to the queue
      queue.push(...graph[person]);
    }
  }
  return null; // No seller!
}

console.log(bfs(graph, "you"));
