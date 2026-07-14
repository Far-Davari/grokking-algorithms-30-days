// ---------- 1. The weighted graph (directed, with a negative edge) ----------
// Each node has an object of { neighbor: cost }
const graph = {
  S: { A: 1, B: 3 },
  A: { C: 1 },
  B: { C: -2 }, // negative edge – will cause Dijkstra to fail
  C: {},
};

function dijkstra(graph, start) {
  // ---------- 2. Initialise costs ----------
  // costs[node] = currently known cheapest cost from start to node
  const costs = {};
  for (let node in graph) {
    costs[node] = Infinity;
  }
  costs[start] = 0;
  console.log("Initial costs:", costs);

  // ---------- 3. Initialise parents ----------
  // parents[node] = the node that gave us the cheapest path to node
  const parents = { [start]: null };
  console.log("Initial parents:", parents);

  // ---------- 4. Processed set ----------
  const processed = new Set();
  console.log("Processed:", processed, "\n");

  // ---------- 5. Helper – find unprocessed node with smallest cost ----------
  function findLowestCostNode() {
    let lowestCost = Infinity;
    let lowestNode = null;
    for (let node in costs) {
      if (!processed.has(node) && costs[node] < lowestCost) {
        lowestCost = costs[node];
        lowestNode = node;
      }
    }
    return lowestNode; // returns the node name (string) or null
  }

  // ---------- 6. Main loop ----------
  let step = 1;
  let node = findLowestCostNode();
  while (node !== null) {
    const costSoFar = costs[node];
    console.log(
      `--- Step ${step}: processing '${node}' (current cost ${costSoFar}) ---`,
    );
    console.log("  Costs before:", costs);
    console.log("  Parents before:", parents);

    // Look at every neighbor of the current node
    for (let neighbor in graph[node]) {
      // STANDARD DIJKSTRA: only update neighbors that have NOT been processed
      if (!processed.has(neighbor)) {
        const weight = graph[node][neighbor];
        const newCost = costSoFar + weight;
        console.log(
          `    Checking neighbor '${neighbor}' via '${node}': old cost ${costs[neighbor]}, new cost ${newCost}`,
        );
        if (newCost < costs[neighbor]) {
          console.log(
            `      -> UPDATING: cost of '${neighbor}' to ${newCost}, parent to '${node}'`,
          );
          costs[neighbor] = newCost;
          parents[neighbor] = node;
        }
      }
    }

    // Mark current node as processed – its cost is now final
    processed.add(node);
    console.log("  Processed set after:", [...processed]);
    console.log("  Costs after:", costs);
    console.log("  Parents after:", parents, "\n");

    // Find next node to process
    node = findLowestCostNode();
    step++;
  }

  console.log("Final costs:", costs);
  console.log("Final parents:", parents);
  return { costs, parents };
}

// ---------- 7. Path reconstruction ----------
function getPath(parents, target) {
  if (!(target in parents)) return null; // unreachable
  const path = [];
  while (target) {
    path.push(target);
    target = parents[target];
  }
  return path.reverse(); // reverse to get start → target
}

// ---------- 8. Run and test ----------
const { costs, parents } = dijkstra(graph, "S");
console.log("\nCheapest cost from S to C:", costs["C"]);
console.log("Shortest path:", getPath(parents, "C"));
