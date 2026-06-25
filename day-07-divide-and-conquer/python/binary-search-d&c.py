def recursive_binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return None
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    else:
        return recursive_binary_search(arr, target, mid + 1, high)
    
my_list = [1,3,5,7,9]
print(recursive_binary_search(my_list, 9))