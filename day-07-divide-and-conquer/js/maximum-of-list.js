// Using a loop
function maxLoop(arr) {
  if (arr.length === 0) return null;
  let maxVal = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > maxVal) {
      maxVal = arr[i];
    }
  }
  return maxVal;
}

// Using Recursion
function max(arr) {
  if (arr.length === 0) return null;
  if (arr.length === 1) return arr[0];
  if (arr.length === 2) {
    return arr[0] > arr[1] ? arr[0] : arr[1];
  }
  const subMax = max(arr.slice(1));
  return arr[0] > subMax ? arr[0] : subMax;
}

const myArr = [1, 5, 95, 226, -20, 78, 63, 2525];
console.log(maxLoop(myArr));
console.log(max(myArr));
