def find_smallest(arr):
  smallest = arr[0]
  smallest_index = 0;
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  
  return smallest_index

def selection_sort(arr):
  new_arr = []
  working_arr = arr[:]

  while working_arr:
    smallest = find_smallest(working_arr)
    new_arr.append(working_arr.pop(smallest))
  return new_arr

my_arr = [20, 50, -566, 10, 2, 3, 99, 56, 7, 33, 53, 35, 0, -56];

print(find_smallest(my_arr))
print(selection_sort(my_arr))