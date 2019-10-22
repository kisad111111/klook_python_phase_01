# 1. 定义一个函数sum，求两个整数之和。
def sum(a, b):
    return a + b


# 2. 定义一个函数odd，输出小于100的所有奇数。
# 这里可以简单变通一下：输出小于n的所有奇数。调用函数的时候，传入参数100
def print_odd(n):
    a = 1
    while a < n:
        print(a)
        a = a + 2


if __name__ == '__main__':
    print(sum(1, 2))
    print(sum(3, 5))

    print_odd(100)
