# States we need to cover
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# Radio station and the states they cover
stations = {
  "kone": {"id", "nv", "ut"},
  "ktwo": {"wa", "id", "mt"},
  "kthree": {"or", "nv", "ca"},
  "kfour": {"nv", "ut"},
  "kfive": {"ca", "az"}
}

final_stations = set()

fruits = set(["avocado", "tomato", "banana"])
vegtables = set(["beets", "carrots", "tomato"])
print("Union:", fruits | vegtables)
print("Intersection:", fruits & vegtables)
print("Subtract:", fruits - vegtables)
print("Subtract:", vegtables - fruits)

while states_needed:
  best_station = None
  states_covered = set()
  for station, states in stations.items():
    covered = states_needed & states
    if len(covered) > len(states_covered):
      best_station = station
      states_covered = covered

  states_needed -= states_covered
  final_stations.add(best_station)

print(final_stations)