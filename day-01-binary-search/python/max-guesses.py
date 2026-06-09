import math

def max_guesses(n):
    if n < 0:
        raise ValueError("List size cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return math.ceil(math.log2(n))

print(max_guesses(1024))
print(max_guesses(100))
print(max_guesses(104545))
print(max_guesses(1))
print(max_guesses(0))
# print(max_guesses(-1)) raise ValueError