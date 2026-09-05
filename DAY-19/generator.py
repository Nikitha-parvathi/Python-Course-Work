def retrivedata():
    data = ['1..100', '101..200', '201..300', '301..400', '401..500']
    for i in data:
        yield i

def even():
    i = 0
    while True:
        i += 2
        yield i

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

def isprime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1): # optimized
        if n % j == 0:
            return False
    return True

def primes(n):
    for i in range(2, n + 1):
        if isprime(i):
            yield i

def count(n):
    for i in range(n, 0, -1):
        yield i

# --- Testing ---
print("1. Reels scroll simulator")
reels = retrivedata()
while True:
    status = input('[s]croll or [q]uit: ')
    if status == 's':
        try:
            print(next(reels))
        except StopIteration:
            print("No more data")
            break
    else:
        break

print("\n2. First 50 even numbers")
res = even()
for _ in range(50):
    print(next(res), end=" ")

print("\n\n3. Factors of 50")
for f in factors(50):
    print(f, end=" ")

print("\n\n4. Primes up to 50")
for p in primes(50):
    print(p, end=" ")

print("\n\n5. Countdown from 10")
for c in count(10):
    print(c, end=" ")