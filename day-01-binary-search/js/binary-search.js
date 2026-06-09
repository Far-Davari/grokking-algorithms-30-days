function binarySearch(arr, item) {
  let low = 0;
  let high = arr.length - 1;
  let steps = 0;

  while (low <= high) {
    steps++;
    let mid = Math.floor((low + high) / 2),
      guess = arr[mid];

    if (guess === item) {
      return { index: mid, steps };
    } else if (guess > item) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return { index: null, steps };
}

const myArr = Array.from({ length: 1024 }, (_, i) => i + 1);

console.log(binarySearch(myArr, 512));
