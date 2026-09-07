// States we need to cover (using Set)
const statesNeeded = new Set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]);

// Radio stations and the states they cover (object with Sets)
const stations = {
  kone: new Set(["id", "nv", "ut"]),
  ktwo: new Set(["wa", "id", "mt"]),
  kthree: new Set(["or", "nv", "ca"]),
  kfour: new Set(["nv", "ut"]),
  kfive: new Set(["ca", "az"]),
};

// Final set of stations
const finalStations = new Set();

function setIntersection(setA, setB) {
  const intersection = new Set();
  for (const item of setA) {
    if (setB.has(item)) {
      intersection.add(item);
    }
  }
  return intersection;
}

function setDifference(setA, setB) {
  const difference = new Set(setA);
  for (const item of setB) {
    difference.delete(item);
  }
  return difference;
}

while (statesNeeded.size > 0) {
  let bestStation = null;
  let statesCovered = new Set(); // States covered by best station
  for (const [station, states] of Object.entries(stations)) {
    const covered = setIntersection(statesNeeded, states);
    if (covered.size > statesCovered.size) {
      bestStation = station;
      statesCovered = covered;
    }
  }
  // Remove covered states from statesNeeded
  for (const state of statesCovered) {
    statesNeeded.delete(state);
  }
  finalStations.add(bestStation);
}

console.log(finalStations);
