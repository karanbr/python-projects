def add(n1, n2, n3=0, n4=0):
    return n1 + n2 + n3 + n4


# If I want to use any number of arguments:
def add_n(*args):
    # result = 0
    # for n in args:
    #     result += n
    # return result
    return sum(args)


print(add_n(1, 1, 1, 1, 2, 1))
