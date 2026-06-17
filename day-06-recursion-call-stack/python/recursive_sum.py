def sum(arr):
    if not arr:                     # base case: empty list
        return 0
    return arr[0] + sum(arr[1:])    # recursive case

my_arr = [5, 10, 15]
print(sum(my_arr))  # 30

# Trace of sum([5, 10, 15]):
# sum([5, 10, 15]) -> 5 + sum([10, 15])
#   sum([10, 15]) -> 10 + sum([15])
#     sum([15]) -> 15 + sum([])
#       sum([]) -> returns 0
#     sum([15]) -> returns 15 + 0 = 15
#   sum([10, 15]) -> returns 10 + 15 = 25
# sum([5, 10, 15]) -> returns 5 + 25 = 30