def factorial(i):
    if i == 1: 
        return 1
    return i * factorial(i - 1)

print(factorial(2))
# factorial(4) -> waits for factorial(3)
# factorial(3) -> waits for factorial(2)
# factorial(2) -> waits for factorial(1)
# factorial(1) -> returns 1
# factorial(2) -> returns 2 * 1 = 2
# factorial(3) -> returns 3 * 2 = 6
# factorial(4) -> returns 4 * 6 = 24
