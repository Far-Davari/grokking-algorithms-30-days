const graph = {
  book: { lp: 5, poster: 0 },
  lp: { drums: 20, guitar: 15 },
  poster: { drums: 35, guitar: 30 },
  drums: { piano: 10 },
  guitar: { piano: 20 },
  piano: {},
};

function dijkstra(graph, start) {
  // Initialise costs
  const costs = {};
  for (let node in graph) {
    costs[node] = Infinity;
  }
  costs[start] = 0;

  // Parents and processed set
  const parents = { [start]: null };
  const processed = new Set();

  // Helper to find lowest-cost
  function findLowestCostNode() {
    let lowestCost = Infinity;
    let lowestNode = null;
    for (let node in costs) {
      if (!processed.has(node) && costs[node] < lowestCost) {
        lowestCost = costs[node];
        lowestNode = node;
      }
    }
    return lowestNode;
  }

  let node = findLowestCostNode();
  while (node !== null) {
    const costSoFar = costs[node];
    // Check neighbors
    for (let neighbors in graph[node]) {
      const weight = graph[node][neighbors];
      const newCost = costSoFar + weight;
      if (newCost < costs[neighbors]) {
        costs[neighbors] = newCost;
        parents[neighbors] = node;
      }
    }
    processed.add(node);
    node = findLowestCostNode();
  }
  return { costs, parents };
}

function getPath(parents, target) {
  const path = [];
  while (target) {
    path.push(target);
    target = parents[target];
  }
  return path.reverse();
}

const { costs, parents } = dijkstra(graph, "book");
console.log("Cost to piano:", costs["piano"]);   // 35
console.log("Path:", getPath(parents, "piano")); // ['book', 'lp', 'drums', 'piano']
