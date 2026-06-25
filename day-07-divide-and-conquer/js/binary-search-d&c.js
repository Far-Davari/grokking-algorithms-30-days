function recursiveBinarySearch(arr, target, low = 0, high = arr.length - 1) {
  if (low > high) return null;
  let mid = Math.floor((low + high) / 2);
  if (arr[mid] === target) return mid;
  if (arr[mid] > target) {
    return recursiveBinarySearch(arr, target, low, mid - 1);
  } else {
    return recursiveBinarySearch(arr, target, mid + 1, high);
  }
}

const myList = [1,3,5,7,9];
console.log(recursiveBinarySearch(myList, 56));
