from time import sleep

def print_item(arr):
    for item in arr:
        print(item)

def print_item2(arr):
    for item in arr:
        sleep(1)
        print(item)

my_arr = [1, 2, 3, 4, 5, 6, "Bingo!"]
print_item(my_arr)
print_item2(my_arr)
