import random
from tabulate import tabulate
from collections import defaultdict

n = 31
h = 2
p = (1 << n) - 1  # 2^n - 1

def random_hamming_weight_vector(n, h):
    indices = random.sample(range(n), h)
    value = 0
    for i in indices:
        value |= (1 << i)
    return value

def generate_T_values(modulus, count=10):
    results = []
    for _ in range(count):
        R = random.randint(0, modulus - 1)
        F = random.randint(0, modulus - 1)
        G = random_hamming_weight_vector(n, h)
        T = (F * R + G) % modulus
        results.append(T)
    return results

T_values_p = generate_T_values(p, count=55000000)

counter = defaultdict(int)
for T in T_values_p:
    counter[T] += 1

repeats = [{'T': T, 'count': c} for T, c in counter.items() if c > 1]

max_repeats = max(counter.values())

print(tabulate(repeats[:20], headers='keys', tablefmt='grid'))

unique_count = len(counter)
total_count = len(T_values_p)
duplicates = total_count - unique_count
print(f"\nУнікальних значень T: {unique_count}")
print(f"Кількість повторень (усі, що не унікальні): {duplicates}")
print(f"Максимальна кількість повторень для одного T: {max_repeats}")




