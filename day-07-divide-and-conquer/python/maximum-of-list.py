# Using a loop:
def max_loop(arr):
    if not arr:
        return None
    max_val = arr[0]
    for val in arr[1:]:
        if val > max_val:
            max_val = val
    return max_val


# Using recursion:
def max(arr):
    if not arr:
        return 0
    if (len(arr)) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

my_arr = [1, 5, 95, 226, -20, 78, 63]
print(max(my_arr))
print(max_loop(my_arr))