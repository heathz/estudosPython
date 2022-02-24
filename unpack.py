# unpack

expl = [1, 23, 236363, 2727]
print(expl)  # [1, 23, 236363, 2727]
print(*expl)  # unpack -> 1 23 236363 2727


def func(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4)]

for pair in pairs:
    func(*pair)


# *args / **kwargs (argumentos com key)
def func2(*args, **kwargs):
    print(args, kwargs)


func2(1, 2, 3, 4, 5, one=0, two=1)
