comparisons = 0

def find_smallest(arr):
    global comparisons
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        comparisons += 1
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
def selection_sort(arr):
    global comparisons
    comparisons = 0
    new_arr = []
    working = arr[:]
    while working:
        smallest = find_smallest(working)
        new_arr.append(working.pop(smallest))
    return new_arr
    
arr = [2, 9, 8, 7, 99, 25, 60, 1]
print(selection_sort(arr))
print(comparisons)