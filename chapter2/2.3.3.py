import numpy as np


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
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
            print(f'AND({i},{j})={AND(i,j)}')


test()
