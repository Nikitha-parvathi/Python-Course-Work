def display(n):
    if n > 10:
        return
    display(n + 1)
    print(n)

display(1)


def displaysum(n):
    if n == 0:
        return 0
    return n + displaysum(n - 1)

print(displaysum(8))


def displayprod(n):
    if n == 1:
        return 1
    return n * displayprod(n - 1)

print(displayprod(4))


def display(ind):
    if ind == len(s):
        return
    print(s[ind], end='')
    display(ind + 1)


s = 'Python Programming'
display(0)


def display(ind):
    if ind == len(s):
        return
    display(ind + 1)
    print(s[ind], end='')


s = 'Python Programming'
display(0)


def display(n):
    if n == len(s) + 1:
        return
    print(s[:n])
    display(n + 1)


s = 'Python'
display(1)


def displaydigits(n):
    if n == 0:
        return 0

def display(ind):
    if ind == len(s):
        return
    print(s[ind], end='')
    display(ind + 1)


s = 'Python Programming'
display(0)


def display(ind):
    if ind == len(s):
        return
    display(ind + 1)
    print(s[ind], end='')


s = 'Python Programming'
display(0)


def display(n):
    if n == len(s) + 1:
        return
    print(s[:n])
    display(n + 1)


s = 'Python'
display(1)
def display(ind):
    if ind == len(s):
        return
    display(ind + 1)
    print(s[ind], end='')


s = 'Python Programming'
display(0)


def display(n):
    if n == len(s) + 1:
        return
    print(s[:n])
    display(n + 1)


s = 'Python'
display(1)


def display(char):
    if char > len(s) - 1:
        return
    print(s[char], end='')
    display(char + 1)
def displaydigits(n):
    if n == 0:
        return 0
    return n % 10 + displaydigits(n // 10)

n = 987654
print(displaydigits(n))
n = 987654
print(displaydigits(n))



n = 10

def displaydigits(n):
    for i in range(n - 1):
        return (n - i) % 10
    print(i)


n = 10

def displaydigits(n):
    for i in range(n - 1):
        return (n - i) % 10
    print(i)




