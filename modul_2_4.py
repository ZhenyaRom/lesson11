numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.remove(1)
primes = []
not_primes = []
for i in numbers:
    k = True
    for j in primes:
        if i % j == 0:
            not_primes.append(i)
            k = False
            break
    if k:
        primes.append(i)
print(primes)
print(not_primes)


