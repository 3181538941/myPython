class Fibs:
    '''end : max FibNumber'''

    def __init__(self, end=1e100):
        self.first = 0
        self.second = 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.first, self.second = self.second, self.first + self.second
        if self.first > self.end:
            raise StopIteration
        return self.first


def Gen():
    '''end : max FibNumber'''
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a

#迭代器
fib = Fibs(1000)
for i in fib:
    print(i)

# 生成器1
for i in Gen():
    if i > 10000:
        break
    print(i, end=' ')

# 生成器2
s = Gen()
for i in range(10):
    s1 = next(s)
    print(s1)



