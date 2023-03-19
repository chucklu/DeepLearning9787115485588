import numpy as np
x = np.array([0, 1])  # input
w = np.array([0.5, 0.5])  # weight
theta = 0.7
b = -theta  # bias
print(f"input = {x}, weight = {w}, bias = {b}")

temp = w*x
print(f'w*x = {temp}')
weightedSum = np.sum(temp)
print(f"weightedSum = {weightedSum}")
output = weightedSum+b
print(f"output = {output}")
