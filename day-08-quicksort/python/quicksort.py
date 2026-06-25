def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
my_arr = [-1, 25, 65, 45, 98, 23, -56, -644, 35, 70, 226, 26, 27, 20, -55]
print(quicksort(my_arr))