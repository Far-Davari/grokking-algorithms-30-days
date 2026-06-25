# Using loop:
def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

# Using recursion
def sum_arr(arr):
    if not arr:
        return 0
    return arr[0] + sum_arr(arr[1:])

my_arr = [1, 2, 3, 4]

print(sum(my_arr))
print(sum_arr(my_arr))