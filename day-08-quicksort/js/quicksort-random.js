function quicksortRandom(arr) {
  if (arr.length < 2) return arr;
  const pivotIndex = Math.floor(Math.random() * arr.length);
  const pivot = arr[pivotIndex];

  const less = [];
  const greater = [];

  for (let i = 0; i < arr.length; i++) {
    if (i === pivotIndex) continue;

    if (arr[i] <= pivot) {
      less.push(arr[i]);
    } else {
      greater.push(arr[i]);
    }
  }
  return [...quicksortRandom(less), pivot, ...quicksortRandom(greater)];
}

const myArr = [
  40, 162, 282, 410, 460, 482, 552, 565, 742, 756, 1046, 1196, 1267, 1292, 1295,
];

console.log(quicksortRandom(myArr));
