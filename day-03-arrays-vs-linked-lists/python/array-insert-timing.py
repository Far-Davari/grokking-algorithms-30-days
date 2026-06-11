import time

def time_insert_front(n, repetitions=100):
    total = 0.0
    for _ in range(repetitions):
        test_list = list(range(n))
        start = time.perf_counter()
        test_list.insert(0, 999)
        end = time.perf_counter()
        total += (end - start)
    return total / repetitions

print("n, average_seconds")
for size in [1000, 10000, 50000, 100000]:
    t = time_insert_front(size)
    print(f"{size}, {t:.10f}")