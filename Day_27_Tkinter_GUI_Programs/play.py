def add(*args):
    sum = 0
    for n in args:
        sum += n

    print(sum)
    return  sum

add(2, 1, 7)

def calculate(**kwargs):
    print(kwargs)

calculate(add=2, multiply=5)