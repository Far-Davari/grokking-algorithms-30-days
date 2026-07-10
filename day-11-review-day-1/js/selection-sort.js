function findSmallest(arr) {
  let smallest = arr[0];
  let smallestIndex = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < smallest) {
      smallest = arr[i];
      smallestIndex = i;
    }
  }
  return smallestIndex;
}

function selectionSort(arr) {
  let workingArr = [...arr];
  let sortedArr = [];

  while (workingArr.length > 0) {
    let index = findSmallest(workingArr);
    sortedArr.push(workingArr[index]);
    workingArr.splice(index, 1);
  }
  return sortedArr;
}

const myArr = [20, 50, 10, 2, 3, 99, 56, 7, 33, 53, 35, 0, -56];

console.log(findSmallest(myArr));
console.log(selectionSort(myArr));
