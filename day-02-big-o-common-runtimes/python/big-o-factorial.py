import math

def routs(n):
    if n < 1:
        return
    return math.factorial(n - 1);

for i in range(1, 21):
    print(f"{i} cites -> {routs(i)} routs")