import numpy as np


def Perceptron(inputs, weights, bias):
    output = np.sum(weights*inputs)+bias
    if (output <= 0):
        return 0
    else:
        return 1


def AND(inputs):
    weights = np.array([0.5, 0.5])
    bias = -0.7
    return Perceptron(inputs, weights, bias)


def NAND(inputs):
    weights = np.array([-0.5, -0.5])
    bias = 0.7
    return Perceptron(inputs, weights, bias)


def OR(inputs):
    weights = np.array([0.5, 0.5])
    bias = -0.2
    return Perceptron(inputs, weights, bias)


def testWithFunctionName(function_name):
    for i in range(0, 2):
        for j in range(0, 2):
            inputs = np.array([i, j])
            output = callFunction(function_name, inputs)
            print(f'{function_name}({i},{j}) = {output}')


def callFunction(function_name, inputs):
    if function_name in globals() and callable(globals()[function_name]):
        function = globals()[function_name]
        return function(inputs)


def test():
    for function_name in ['AND', 'NAND', 'OR']:
        testWithFunctionName(function_name)
        print()


test()
