import random

def quicksort_random(arr):
    if len(arr) < 2:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    print(pivot)

    less = [arr[i] for i in range(len(arr)) if i != pivot_index and arr[i] <= pivot]
    greater = [arr[i] for i in range(len(arr)) if i != pivot_index and arr[i] > pivot]
    return quicksort_random(less) + [pivot] + quicksort_random(greater)

print(quicksort_random([1, 2, 3, 4, 5]))
