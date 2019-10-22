def sum(a, b):
    return a + b


def print_odd(n):
    a = 1
    while a < n:
        print(a)
        a = a + 2


if __name__ == '__main__':
    print(sum(1, 2))
    print(sum(3, 5))

    print_odd(100)
