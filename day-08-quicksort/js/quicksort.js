function quicksort(arr) {
  if (arr.length < 2) return arr;
  const pivot = arr[0];
  const less = [];
  const greater = [];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] <= pivot) {
      less.push(arr[i]);
    } else {
      greater.push(arr[i]);
    }
  }
  return [...quicksort(less), pivot, ...quicksort(greater)];
}

const myArr = [-1, 25, 65, 45, 98, 23, -56, -644, 35, 70, 226, 26, 27, 20, -55];

console.log(quicksort(myArr));

console.log(quicksort([3, 1, 4, 2]));
// pivot = 3
// less = [1,2]  (since 1<=3, 2<=3)
// greater = [4] (4>3)
// left = quicksort([1,2])
//    pivot=1, less=[], greater=[2]
//    left = [] + [1] + [2] = [1,2]
// right = quicksort([4]) -> [4]
// return [1,2] + [3] + [4] = [1,2,3,4]
