import random
from math import gcd
from collections import defaultdict

n = 31
h = 2
p = (1 << n) - 1  # 2^n - 1
iterations = 55000000

def random_from_Z_star(modulus):
    while True:
        x = random.randint(1, modulus - 1)
        if gcd(x, modulus) == 1:
            return x

def random_hamming_weight_vector(n, h):
    indices = random.sample(range(n), h)
    value = 0
    for i in indices:
        value |= (1 << i)
    return value

counter = defaultdict(int)

for _ in range(iterations):
    R = random.randint(0, p - 1)
    F = random.randint(0, p - 1)
    G = random_hamming_weight_vector(n, h)
    X1 = random_from_Z_star(p)
    X2 = random.randint(0, p - 1)
    X3 = random_from_Z_star(p)
    X4 = random.randint(0, p - 1)
    T = (R * (X1 * F + X2) + (X3 * G) + X4) % p

    counter[T] += 1

unique_count = len(counter)
total_count = iterations
duplicates = total_count - unique_count
max_repeats = max(counter.values())

print(f"\nУнікальних значень T: {unique_count}")
print(f"Кількість повторень (усі, що не унікальні): {duplicates}")
print(f"Максимальна кількість повторень для одного T: {max_repeats}")


