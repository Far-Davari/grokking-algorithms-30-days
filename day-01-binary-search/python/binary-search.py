def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    test = 0
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        test += 1

        if guess == item:
            return mid, test
        if guess > item:
            high = mid - 1
        else: 
            low = mid + 1

    return None, test

my_list = list(range(1, 1025))  

index, tries = binary_search(my_list, 512)
if index is not None:
    print(f"Found at index {index} in {tries} tries")
else:
    print(f"Not found after {tries} tries")