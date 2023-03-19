def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = w1*x1+w2*x2
    if (temp <= theta):
        return 0
    else:
        return 1


def test():
    for i in range(0, 2):
        for j in range(0, 2):
            print(f'AND({i},{j})={AND(i,j)}')


test()
