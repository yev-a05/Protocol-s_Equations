import random
from math import gcd
from collections import defaultdict

n = 31
h = 2
m = 3
gm = (1 << n) - (1 << m) - 1  # gm = 2^n - 2^m - 1

def random_from_Z_star(modulus):
    while True:
        x = random.randint(1, modulus - 1)
        if gcd(x, modulus) == 1:
            return x

def random_hamming_weight_vector_modulo(n, h, modulus):
    while True:
        indices = random.sample(range(n), h)
        value = 0
        for i in indices:
            value |= (1 << i)
        if value < modulus:
            return value

def generate_T_stats(modulus, count=10):
    counter = defaultdict(int)
    max_repeat = 0

    for _ in range(count):
        R = random.randint(0, modulus - 1)
        F = random.randint(0, modulus - 1)
        G = random_hamming_weight_vector_modulo(n, h, modulus)
        X1 = random_from_Z_star(modulus)
        X2 = random.randint(0, modulus - 1)
        X3 = random_from_Z_star(modulus)
        X4 = random.randint(0, modulus - 1)

        T = (R * (X1 * F + X2) + (X3 * G) + X4) % modulus
        counter[T] += 1
        if counter[T] > max_repeat:
            max_repeat = counter[T]

    total_count = count
    unique_count = len(counter)
    duplicates = total_count - unique_count

    return unique_count, duplicates, max_repeat

unique, duplicates, max_count = generate_T_stats(gm, count=55000000)

print(f"\nУнікальних значень T: {unique}")
print(f"Кількість повторень (усі, що не унікальні): {duplicates}")
print(f"Максимальна кількість повторень для одного T: {max_count}")

