# using loop
def count_loop(arr):
    total = 0
    if not arr:
        return 0
    for i in arr:
        total += 1
    return total
    
# using recursion
def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

my_arr = [1, 2, 3, 4, 5]
print(count(my_arr))
print(count_loop(my_arr))

