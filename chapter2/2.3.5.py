import numpy as np


def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    b = -theta

    output = np.sum(w*x)+b
    if (output <= 0):
        return 0
    else:
        return 1


def test():
    for i in range(0, 2):
        for j in range(0, 2):
            print(f'OR({i},{j})={OR(i,j)}')


test()
